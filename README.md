# MontaigNeT
MontaigNet (Montaigne - net) is a machine learning web app that generates text in the style of 1500' French essayist Michel de Montaigne.

![alt text](https://preview.redd.it/ixgebbvrklu61.png?width=728&format=png&auto=webp&s=f007191738a077de9cdf3b6e9ef22a45f28ef5d4)

This application is powered by a PyTorch LSTM model trained on The Essays of Michel de Montaigne (https://www.gutenberg.org/files/3600/3600-h/3600-h.htm), which runs in a python flask REST API.

This web application (with a react frontend) takes a prompt from the user, feeds it into the API, and then displayes the generated text.

In order to ensure that this application can be run on any machine with minimal hassle, each component (react frontend and flask backend) is dockerized. We use docker compose to ensure that these components play nicely.

## Usage

Running MontaigNet with docker-compose:

    git clone https://github.com/vladthesav/MontaigNeT.git
    cd MontaigNeT
    sudo docker-compose up --build
    
    
Connect to http://localhost:3000 and you're set!


Todo:
- [X] Get app working with docker compose.
- [ ] Add error handling to backend (deal with unknown tokens).
- [ ] Improve text generation model.
- [ ] Touch up frontend.
- [ ] Upload model training code. 
