import mainDAO
from datetime import datetime, time

dao = mainDAO.mainDAO()

def run():
	#Verification du temps  (18h- 22h) et les videos sont ready
	#if():
	now = datetime.now().time()
	if(time(18,00) <= now <= time(22,00) and dao.getData('isReady') == '1'):
		#HDMI --> On
		os.system("vlc --loop --fullscreen ~/videos/*")
run()
