# amazon-echo

Amazon-echo project is an interactive voice UI application that asks and records information of the patients without the need of the third party.

# Installation

## Required libraries
To work with the project, you need to install flash-ask and ngrok.

User your package management system to install flask-ask. <br/>
```pip install flask-ask```

Install ngrok: <br/>
`https://ngrok.com/`

## How to use

1. Connect the local server to the internet.

2. Upload Scheme, Simple Utters and ngrok address from `developer.amazon.com` to the application.

3. Execute the Python file in the project.

4. Navigate to ngrok repository and run ```./ngrok http 5000```

5. ngrok server will translate the Python localhost. By running ngrok server, the application can interact with Amazon server.

6. Turn on your echo and call the invocation name that was added in the developer.amazon.com

Program will save all the information in the text file which path is included in main.py

Enjoy using the application.
