FROM ubuntu:20.04

#STEP ONE: SET UP AND RUN BACKEND
#================================
#install pip3
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./backend/requirements.txt  /app/requirements.txt

WORKDIR /app

#install python dependancies
RUN pip3 install -r requirements.txt

#copy files from backend directory into the container
COPY ./backend /app/backend

#do this so python knows where to find these files (I don't like this either)
RUN mv backend/preprocessing_meta.json preprocessing_meta.json && \
    mv backend/lstm_state_dict.pt lstm_state_dict.pt

#optional: expose port 3500 to test api
EXPOSE 3500

#WORKDIR /backend
#ENTRYPOINT [ "python3" ]

CMD [ "python3", "backend/server.py" ]



#now do the frontend
COPY ./frontend /app/frontend
