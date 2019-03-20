# amazon-echo

Amazon-echo project is an interactive voice UI application that asks and records information of the patients without the need of the third party.

# Installation

## Required libraries
To work with the project, you need to install flash-ask and ngrok.

User your package management system to install flask-ask.
```pip install flask-ask```

Install ngrok:
`https://ngrok.com/`

## How to use

You will also have to expand your local server to the internet for skill to work.

You will need to install ngrok: https://ngrok.com/

You will also have to upload Scheme and Simple Utters and ngrok adress on developer.amazon.com into your skill.

After that you can run python file.

Then you have to run ngrok: go to the repository where ngrok is and then run : ./ngrok http 5000

It will run a server and retranslate your localhost(python) to it. By this, your echo will be able to talk to the amazon server.

Then just simply turn on your echo and call the invocation name you put in the developer.amazon.com

Program will save all the information in the text file which path is included in main.py

That's it! Enjoy your speaking thing.
