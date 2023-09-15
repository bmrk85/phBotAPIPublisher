from flask import Flask
from phBot import *
import QtBind
import json
from threading import Thread
import logging


gui = QtBind.init(__name__,'Flask phBot API publisher')


QtBind.createLabel(gui, 'phBot api endpoint publishing, clicking on the start button, \na server will start running at localhost:5000', 10, 80)
button1 = QtBind.createButton(gui, 'button_clicked', 'Start flask server', 10, 125)

log('[%s] Loaded' % __name__)


#flask

app = Flask(__name__)

#endpoints

@app.route('/client')
def getClientInfo(): 
    return get_client()

@app.route('/guild')
def getGuildInfo(): 
    return str(get_guild())

@app.route('/players')
def getPlayersNearby():
	return str(get_players())

@app.route('/character')
def getCharacterData():
	return get_character_data()

@app.route('/position')
def getPosition():
	return str(get_position())

@app.route('/mastery')
def getMasteries():
	return str(get_mastery())

@app.route('/inventory')
def getInventory():
	return str(get_inventory())

@app.route('/pouch')
def getJobPouch():
	return str(get_job_pouch())

@app.route('/pets')
def getSummonedPets():
	return str(get_pets())

@app.route('/mobs')
def getMobsNearby():
	return str(get_monsters())

@app.route('/training-area')
def getTrainingArea():
	return str(get_training_area())

@app.route('/quests')
def getQuests():
	return str(get_quests())


#run flask
def flask_thread():
	app.run(host='0.0.0.0')
	

def main():
	th = Thread(target=flask_thread)
	th.start()
	log("Server started at localhost:5000")
	
def button_clicked():
    main()
    logging.basicConfig(filename='flask_error.log',level=logging.DEBUG)
