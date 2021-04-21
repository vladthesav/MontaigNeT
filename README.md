# MontaigNeT
MontaigNet (montaigne - net) is a machine learning web app that generates text in the style of 1500' French essayist Michel de Montaigne.

This application is powered by a PyTorch LSTM model trained on The Essays of Michel de Montaigne, which runs in a python flask REST API.

This web application (with a react frontend) takes a prompt from the user, feeds it into the API, and then displayes the generated text.

In order to ensure that this application can be run on any machine with minimal hassle, each component (react frontend and flask backend) is dockerized. We use docker compose to ensure that these components play nicely.

## Usage

Runing MontaigNet with docker-compose:

    cd MontaigNet
    docker-compose up --build
    
    
Connect to http://localhost:3000 and you're set!
