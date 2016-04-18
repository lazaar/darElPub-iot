import os, urllib2, mainDAO, json
from datetime import datetime

# Ce script doit etre execute a chaque demarage
isFirstTime = not os.path.isfile('darelpub.db')
dao = mainDAO.mainDAO()
currentDate = datetime.now();

def sendData():
	print("Send Data")
	# Reinitialisation de la base

def getNewData():
	print("get New Data")
	# Reinitialisation de la base
	url = "http://10.42.6.190/siblu/videos.json"
	data = urllib2.urlopen(url)
	videos = json.loads(data.read())
	for video in videos['videos']: 
		dao.insertVideo((video['name'], video['qte'], 1))
		if(not os.path.isfile('videos/'+video['name']+'.mp4')):
			os.system("python youtube-dl --output ./videos/%s.mp4 %s"%(video['name'],'https://www.youtube.com/watch?v='+video['name']))
	dao.setData('isReady', '1')

# mettre HDMI du raspberry en mode off

# verifier est ce qu'il s'agit du premier demarrage du raspberry
if(isFirstTime):
	print('First Time')
	dao.initDB()
	dao.setData('lastDate', currentDate.strftime("%d/%m/%Y"))
else:
	# verifier est ce qu'il s'agit du premier demarrage du raspberry dans la journee
	lastDate = datetime.strptime(dao.getData('lastDate'), "%d/%m/%Y")
	if(lastDate < currentDate):
		# Envoi des donnees de la journee precedentes
		sendData()
		# L'Appel du WS pour recuperation des donnees
		getNewData()