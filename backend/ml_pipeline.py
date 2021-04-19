import torch
import torch.nn as nn
import torch.nn.functional as F

#select device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class RNNModule(nn.Module):
    def __init__(self, n_vocab, seq_size, embedding_size, lstm_size):
        super(RNNModule, self).__init__()
        self.seq_size = seq_size
        self.lstm_size = lstm_size
        self.embedding = nn.Embedding(n_vocab, embedding_size)
        self.lstm = nn.LSTM(embedding_size,
                            lstm_size,
                            batch_first=True)
        
        self.dense_1 = nn.Linear(lstm_size, lstm_size//2)
        self.tanh_1 = nn.Tanh()
        self.dense_2 = nn.Linear(lstm_size//2, n_vocab)
        
    def forward(self, x, prev_state):
        embed = self.embedding(x)
        output, state = self.lstm(embed, prev_state)
        logits = self.dense_2(self.tanh_1(self.dense_1((output))))

        return logits, state
      
    def zero_state(self, batch_size):
        return (torch.zeros(1, batch_size, self.lstm_size),
                torch.zeros(1, batch_size, self.lstm_size))

#load lstm
net = torch.load('lstm',map_location=device)

