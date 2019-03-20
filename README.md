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

4. Then you have to run ngrok: go to the repository where ngrok is and then run : ./ngrok http 5000

5. It will run a server and retranslate your localhost(python) to it. By this, your echo will be able to talk to the amazon server.

6. Then just simply turn on your echo and call the invocation name you put in the developer.amazon.com

Program will save all the information in the text file which path is included in main.py

That's it! Enjoy your speaking thing.
