import logging
import datetime
import string
from random import randint

from flask import Flask, render_template // importing working library

from flask_ask import Ask, statement, question, session // importing working library


app = Flask(__name__)

ask = Ask(app, "/")

log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

// Basic function which starts when skill is called. How to call skill -> see README
@ask.launch
def launch():
    return question("Hello. My name is Alexa. I'm your new friend. What is your name?")

// Name gettin function. To call you have to answer previous function.
@ask.intent("whatIsYourName")
def nameIdentify(nickname):
    with open("info.txt", "w") as myfile:
        myfile.truncate()
        myfile.write("Patient's name is {} \n".format(nickname))
    return question("It's nice to meet you {}. How are you today? From 1 - 10. 1 is very sad. 10 is very happy".format(nickname)).reprompt("I didn't hear you")

// Mood getting function. To call you have to answer previous question.
@ask.intent("MyMoodIntent")
def what_is_my_mood(mood):
    with open("info.txt", "a") as myfile:
        myfile.write("Patient's mood at {} is {} \n".format(datetime.datetime.now().time(),mood))
    if (mood >= 5):
        return question("I like your mood today, are you hungry?").reprompt("I didn't hear you")
    else:
        return question("You're a sad kitty today, are you hungry? ").reprompt("I didn't hear you")

// ifHungry getting function. To call you have to answer previous question.
@ask.intent("ifHungry")
def hungry(hunger):
    with open("info.txt", "a") as myfile:
        myfile.write("Patient's answer on question if he is hungry was {} at {} \n".format(hunger,datetime.datetime.now().time()))
    if (hunger == "yes"):
        return question("Nurse is on her way already. Can I ask you one more question? What is your body temperature?").reprompt("I didn't hear you")
    else:
        return question("Seems good. Can I ask you one more question? What is your body temperature?").reprompt("I didn't hear you")

// Temperature getting function. To call you have to answer previous question
@ask.intent("MyTempIntent")
def my_temp_is(newTemp, convert={'newTemp' : int}):
    #msg = "your temp is {}".format(newTemp)
    with open("info.txt", "a") as myfile:
        myfile.write("Patient's temperature at {} is {} \n \n".format(datetime.datetime.now().time(),newTemp))
    if (newTemp >= 37):
        return statement('Ohh, you seem  to be sick, doctor is on his way. Data is collected. Thank you!').reprompt("I didn't hear you")
    else:
        return statement("You're healthy and ready for it! Data is collected. Thank you!").reprompt("I didn't hear you")




// Stopping function. To call you have to say: "Shut up!"

@ask.intent("AMAZON.StopIntent")
def stop():
    return statement("I'm in tears!")


if __name__ == '__main__':

    app.run(debug=True)
