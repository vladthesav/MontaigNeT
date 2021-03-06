import torch
import torch.nn as nn
import torch.nn.functional as F

from text_processing import *
import numpy as np
import json
import os



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


#load data needed to prepeocess text and initialize model
with open('preprocessing_meta.json', 'r') as fp: preprocessing_meta = json.load(fp)

n_vocab = preprocessing_meta['n_vocab']
vocab_to_int = preprocessing_meta['vocab_to_int']
#int_to_vocab = preprocessing_meta['int_to_vocab']
int_to_vocab = {i:c for c,i in vocab_to_int.items()}

#params needed to initialize model
seq_size = preprocessing_meta['seq_size']
embedding_size = preprocessing_meta['embedding_size']
lstm_size = preprocessing_meta['lstm_size']

#create model instance and load state dict
net = RNNModule(n_vocab, seq_size,embedding_size,lstm_size )
net.load_state_dict(torch.load('lstm_state_dict.pt'))
net.eval()

def predict(text,device=device, net=net, n_vocab=n_vocab, vocab_to_int=vocab_to_int, int_to_vocab=int_to_vocab, top_k=5):
    """predict sequence of words following text"""
    print(text)
    text = pad_chars(text)
    words = text.split()

    state_h, state_c = net.zero_state(1)
    state_h = state_h.to(device)
    state_c = state_c.to(device)
    for w in words:

        #if a word is not in our vocabulary return 
        #a propper error message to the user
        if w not in vocab_to_int:
            err_msg = "Error: \"{}\" is not recognized by the model, please use another word".format(w)
            return err_msg
        ix = torch.tensor([[vocab_to_int[w]]]).to(device)
        output, (state_h, state_c) = net(ix, (state_h, state_c))

    _, top_ix = torch.topk(output[0], k=top_k)
    choices = top_ix.tolist()
    choice = np.random.choice(choices[0])

    words.append(int_to_vocab[choice])

    for _ in range(100):
        ix = torch.tensor([[choice]]).to(device)
        output, (state_h, state_c) = net(ix, (state_h, state_c))

        _, top_ix = torch.topk(output[0], k=top_k)
        choices = top_ix.tolist()
        choice = np.random.choice(choices[0])
        words.append(int_to_vocab[choice])

    out =' '.join(words)
    out = remove_padding(out)
    return out

#print(predict("I am"))