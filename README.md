# Flask_webhook

A simple python flask webhook server that can capture and display the body of any HTTP POST request made to the app.

##Prerequisites

Install Docker

##File Information

App.py: Flask application

  Connects to Couchdb database.
  Generates a unique URI endpoint and displays to the user.
  User can generate a GET or POST request.
  
Dockerfile : Containerize and build flask application.
  Installs python3 and pip3 and other dependencies
  Run the python application.
  
gunicorn_conf.py: Configuration file for the gunicorn server
  Communicates with multiple web servers.
  Reacting to multiple web requests at once and load balancing.
  Enable multiple processes of the flask application running.
  
requirements.txt:
  Served as input to install dependencies and libraries.
    flask
    couchdb
    requests
    urllib3
    gunicorn
    
##Build and run using docker

###Using Docker
    Docker build images
      ```docker build -t webhookapp:latest .```

    Docker run
      ```docker run -it webhookapp```
      
      
###Regular flask application run
    Install python3
    Install pip3
    Run ```pip3 install -r requirements.txt```
      Installs dependencies and libraries
      
    Run 'couchdb' to start the database
      
###Usage
    
    1: User navigates to app root where the server is listening to : 127.0.0.1:8000
    2: Application displays a unique URL endpoint.
    3: User can submit a GET or POST method to the URL.
      if request==POST
        curl --header "Content-Type: application/json" \ 
        --request POST \
        --data '{"highspot":"webhook","candidate":"abc"}' \
        http://127.0.0.1:8000/<guid>/
        
      if request == GET
        curl -x GET http://127.0.0.1:8000/<guid>/
        
     
    
    
    
      
      
    


      
