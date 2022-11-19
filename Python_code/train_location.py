#modules import
import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
from datetime import datetime

#Provide your IBM Watson Device Credentials
organization = "2ayt7j"
deviceType = "IoT"
deviceId = "95509404"
authMethod = "token"
authToken = "77087672"

#cheran exp 12673
def Cheran_express():
    if T in range(1290,1320):
        result="CURRENT RUNNING STATUS :  About to Start from  MGR Chennai Central " ;
    elif T==1320:
         result="CURRENT RUNNING STATUS : Started from  MGR Chennai Central";
    elif  T in range(1321,1380):
         result="CURRENT RUNNING STATUS : About to Reach Arakkonam Junction";
    elif T==1380:
         result="CURRENT RUNNING STATUS : Train reached Arakkonam Junction";
    elif T in range(1381,1439) or T in range(0,65):
         result="CURRENT RUNNING STATUS : Train crossed Arakkonam Junction and about to reach Jolarpettai Junction";
    elif T==65:
         result="CURRENT RUNNING STATUS :  Train reached Jolarpettai Junction";
    elif T in range(66,170):
        result="CURRENT RUNNING STATUS : Train crossed Jolarpettai Junction and about to reach Salem Junction";
    elif T==170:
        result="CURRENT RUNNING STATUS : Train reached Salem Junction";
    elif T in range(171,230):
        result="CURRENT RUNNING STATUS : Train crossed Salem Junction and about to reach Erode Junction";
    elif T==230:
        result="CURRENT RUNNING STATUS : Train reached Erode Junction ";
    elif T in range(231,275):
        result="CURRENT RUNNING STATUS : Train crossed Erode Junction and about to reach Tiruppur ";
    elif T==275:
        result="CURRENT RUNNING STATUS : Train reached Tiruppur Junction ";
    elif  T in range(276,330):
        result="CURRENT RUNNING STATUS : Train crossed Tiruppur Junction and about to reach Coimbature North";
    elif T==330:
        result="CURRENT RUNNING STATUS : Train reached Coimbature North ";
    elif  T in range(331,360):
        result="CURRENT RUNNING STATUS : Train crossed Coimbature North and about to reach Coimbature Junction";
    elif T==360:
        result="CURRENT RUNNING STATUS : Train reached Coimbature Junction";
    else :
        result="CURRENT RUNNING STATUS : Train reached Coimbatore Junction at 06:00 and Yet to start from MGR Chennai Central at 22:00 ";
    return result    

#Nilagiri express 12671
def Nilagiri_express():
    if T in range(1235,1265):
        result="CURRENT RUNNING STATUS :  About to Start from  MGR Chennai Central by 21:05 " ;
    elif T==1265:
         result="CURRENT RUNNING STATUS : Starts from  MGR Chennai Central";
    elif  T in range(1266,1325):
         result="CURRENT RUNNING STATUS : Started from MGR Chennai Central and About to Reach Arakkonam Junction";
    elif T==1325:
         result="CURRENT RUNNING STATUS : Train reached Arakkonam Junction";
    elif T in range(1326,1375):
         result="CURRENT RUNNING STATUS : Train crossed Arakkonam Junction and about to reach Katpadi Junction";
    elif T==1375:
         result="CURRENT RUNNING STATUS :  Train reached Katpadi Junction";
    elif T in range(1376,1440) or T in range(0,110) :
        result="CURRENT RUNNING STATUS : Train crossed Katpadi Junction and about to reach Salem Junction";
    elif T==110:
        result="CURRENT RUNNING STATUS : Train reached Salem Junction";
    elif T in range(111,180):
        result="CURRENT RUNNING STATUS : Train crossed Salem Junction and about to reach Erode Junction";
    elif T==180:
        result="CURRENT RUNNING STATUS : Train reached Erode Junction ";
    elif T in range(181,225):
        result="CURRENT RUNNING STATUS : Train crossed Erode Junction and about to reach Tiruppur ";
    elif T==225:
        result="CURRENT RUNNING STATUS : Train reached Tiruppur Junction ";
    elif  T in range(226,270):
        result="CURRENT RUNNING STATUS : Train crossed Tiruppur Junction and about to reach Coimbature North";
    elif T==270:
        result="CURRENT RUNNING STATUS : Train reached Coimbature North ";
    elif  T in range(271,320):
        result="CURRENT RUNNING STATUS : Train crossed Coimbature North and about to reach Coimbature Junction";
    elif T==320:
        result="CURRENT RUNNING STATUS : Train reached Coimbature Junction";
    elif T in range(321,375):
        result="CURRENT RUNNING STATUS : Train crossed Coimbature Junction and about to reach Mettupalayam ";
    elif T==375:
        result="CURRENT RUNNING STATUS : Train reached Mettupalayam";
    elif T in range(376,406):
        result="CURRENT RUNNING STATUS : Train reached Mettupalayam at 06:15";    
    else :
        result="CURRENT RUNNING STATUS : Train reached Mettupalayam at 06:15 and Yet to start from MGR Chennai Central at 21:05 ";
    return result
#Kovai express1 12675
def Kovai_express():
    if T in range(340,370):
        result="CURRENT RUNNING STATUS :  About to Start from  MGR Chennai Central by 06:10 " ;
    elif T==370:
         result="CURRENT RUNNING STATUS : Starts from  MGR Chennai Central";
    elif  T in range(371,430):
         result="CURRENT RUNNING STATUS : Started from MGR Chennai Central and About to Reach Arakkonam Junction";
    elif T==430:
         result="CURRENT RUNNING STATUS : Train reached Arakkonam Junction";
    elif T in range(431,460):
         result="CURRENT RUNNING STATUS : Train crossed Arakkonam Junction and about to reach Walaja Road Junction";
    elif T==460:
         result="CURRENT RUNNING STATUS :  Train reached Walaja Road Junction";
    elif T in range(461,485):
        result="CURRENT RUNNING STATUS : Train crossed Walaja Road Junction and about to reach Katpadi Junction";
    elif T==485:
        result="CURRENT RUNNING STATUS : Train reached Katpadi Junction";
    elif T in range(486,525):
        result="CURRENT RUNNING STATUS : Train crossed Katpadi Junction and about to reach Ambur";
    elif T==525:
        result="CURRENT RUNNING STATUS : Train reached Ambur ";
    elif T in range(526,560):
        result="CURRENT RUNNING STATUS : Train crossed Ambur and about to reach Jolarpettai Junction ";
    elif T==560:
        result="CURRENT RUNNING STATUS : Train reached Jolarpettai Junction ";
    elif  T in range(561,610):
        result="CURRENT RUNNING STATUS : Train crossed Jolarpettai Junction and about to reach Morappur";
    elif T==610:
        result="CURRENT RUNNING STATUS : Train reached Morappur ";
    elif  T in range(611,670):
        result="CURRENT RUNNING STATUS : Train crossed  Morappur and about to reach Salem Junction";
    elif T==670:
        result="CURRENT RUNNING STATUS : Train reached Salem Junction";
    elif T in range(671,730):
        result="CURRENT RUNNING STATUS : Train crossed Salem Junction and about to reach Erode Junction ";
    elif T==730:
        result="CURRENT RUNNING STATUS : Train reached Erode Junction";
    elif T in range(731,775):
        result="CURRENT RUNNING STATUS :Train crossed Erode Junction and about to reach Tiruppur";
    elif T==775:
        result="CURRENT RUNNING STATUS : Train reached Tiruppur";    
    elif T in range(776,845):
        result="CURRENT RUNNING STATUS :Train crossed Tiruppur and about to reach Coimbatore Juntion";
    elif T==845:
        result="CURRENT RUNNING STATUS : Train reached Coimbatore Junction";
    elif T in range(846,876):
        result="CURRENT RUNNING STATUS : Train reached Coimbator Junction at 14:05";
    else :
        result="CURRENT RUNNING STATUS : Train Coimbatore Junction at 14:05 and Yet to start from MGR Chennai Central at 06:10 ";
    return result

#Nagercoil Jn sf express 12689
def Nagercoil_JN_SF_Express():
    if T in range(1110,1140):
        result="CURRENT RUNNING STATUS :  About to Start from  MGR Chennai Central by 19:00 " ;
    elif T==1140:
         result="CURRENT RUNNING STATUS : Starts from  MGR Chennai Central";
    elif  T in range(1141,1200):
         result="CURRENT RUNNING STATUS : Started from MGR Chennai Central and About to Reach Arakkonam Junction";
    elif T==1200:
         result="CURRENT RUNNING STATUS : Train reached Arakkonam Junction";
    elif T in range(1200,1250):
         result="CURRENT RUNNING STATUS : Train crossed Arakkonam Junction and about to reach Katpadi Junction";
    elif T==1250:
         result="CURRENT RUNNING STATUS :  Train reached Katpadi Junction";
    elif T in range(1251,1330):
        result="CURRENT RUNNING STATUS : Train crossed Katpadi Junction and about to reach Jolarpettai Junction";
    elif T==1330:
        result="CURRENT RUNNING STATUS : Train reached Jolarpettai Junction";
    elif T in range(1331,1340):
        result="CURRENT RUNNING STATUS : Train crossed Jolarpettai Junction and about to reach Tirupattur";
    elif T==1340:
        result="CURRENT RUNNING STATUS : Train reached Tirupattur ";
    elif T in range(1341,1375):
        result="CURRENT RUNNING STATUS : Train crossed Tirupattur and about to reach Morappur";
    elif T==1375:
        result="CURRENT RUNNING STATUS : Train reached Morappur ";
    elif  T in range(1376,1435):
        result="CURRENT RUNNING STATUS : Train crossed Morappur and about to reach Salem Junction";
    elif T==1435:
        result="CURRENT RUNNING STATUS : Train reached Salem Junction";
    elif  T in range(1436,1440) or T in range(0,50):
        result="CURRENT RUNNING STATUS : Train crossed  Salem Junction and about to reach Namakkal";
    elif T==50:
        result="CURRENT RUNNING STATUS : Train reached Namakkal";
    elif T in range(51,95):
        result="CURRENT RUNNING STATUS : Train crossed Namakkal and about to reach Karur Junction ";
    elif T==95:
        result="CURRENT RUNNING STATUS : Train reached Karur Junction";
    elif T in range(96,190):
        result="CURRENT RUNNING STATUS :Train crossed Karur Junction and about to reach Tiruchchirappalli Junction";
    elif T==190:
        result="CURRENT RUNNING STATUS : Train reached Tiruchchirappalli Junction";    
    elif T in range(191,255):
        result="CURRENT RUNNING STATUS :Train crossed Tiruchchirappalli Junction and about to reach Dindigul Junction";
    elif T==255:
        result="CURRENT RUNNING STATUS : Train reached Dindigul Junction";
    elif T in range(256,275):
        result="CURRENT RUNNING STATUS : Train crossed Dindigul Junction and about to reach Kodaikanal Road";
    elif T==275:
        result="CURRENT RUNNING STATUS : Train reached Kodaikanal Road";
    elif T in range(276,340):
        result="CURRENT RUNNING STATUS : Train crossed Kodaikanal Road and about to reach Madurai Junction";
    elif T==340:
        result="CURRENT RUNNING STATUS : Train reached Madurai Junction";
    elif T in range(341,375):
        result="CURRENT RUNNING STATUS : Train crossed Madurai Junction and about to reach Virudunagar Junction";
    elif T==375:
        result="CURRENT RUNNING STATUS : Train reached Virudunagar Junction";
    elif T in range(376,400):
        result="CURRENT RUNNING STATUS : Train crossed Virudunagar Junction and about to reach Satur";
    elif T==400:
        result="CURRENT RUNNING STATUS : Train reached Satur";
    elif T in range(401,425):
        result="CURRENT RUNNING STATUS : Train crossed Satur and about to reach Kovilpatti";
    elif T==425:
        result="CURRENT RUNNING STATUS : Train reached Kovilpatti";
    elif T in range(426,540):
        result="CURRENT RUNNING STATUS : Train crossed Kovilpatti and about to reach Tirunelveli Junction";
    elif T==540:
        result="CURRENT RUNNING STATUS : Train reached Tirunelveli Junction";
    elif T in range(541,650):
        result="CURRENT RUNNING STATUS :  Train crossed Tirunelveli Junction and about to reach Nagercoil Junction";
    elif T==650:
        result="CURRENT RUNNING STATUS : Train reached Nagercoil Junction ";
    elif T in range(651,681):
        result="CURRENT RUNNING STATUS : Train reached Nagercoil Junction at 10:50";    
    else :
        result="CURRENT RUNNING STATUS : Train reached Nagercoil Junction at 10:50 and Yet to start from MGR Chennai Central at 19:00 ";
    return result



#Madurai SF Express 20601
def Madurai_SF_Express():
    if T in range(1320,1350):
        result="CURRENT RUNNING STATUS :  About to Start from  MGR Chennai Central by 22:30 " ;
    elif T==1350:
         result="CURRENT RUNNING STATUS : Starts from  MGR Chennai Central";
    elif T in range(1350,1400) or T in range(0,15):
         result="CURRENT RUNNING STATUS : Started from MGR Chennai Central and About to Reach Katpadi Junction";
    elif T==15:
         result="CURRENT RUNNING STATUS : Train reached Katpadi Junction";
    elif T in range(16,185):
         result="CURRENT RUNNING STATUS : Train crossed Katpadi Junction and about to reach Salem Junction";
    elif T==185:
         result="CURRENT RUNNING STATUS :  Train reached Salem Junction";
    elif T in range(186,280):
        result="CURRENT RUNNING STATUS : Train crossed Salem Junction and about to reach Karur Junction";
    elif T==280:
        result="CURRENT RUNNING STATUS : Train reached Karur Junction";
    elif T in range(281,360):
        result="CURRENT RUNNING STATUS : Train crossed Karur Junction and about to reach Dindigul Junction";
    elif T==360:
        result="CURRENT RUNNING STATUS : Train reached Dindigul Junction";
    elif T in range(361,440):
        result="CURRENT RUNNING STATUS : Train crossed Dindigul Junction and about to reach Madurai Junction";
    elif T==440:
        result="CURRENT RUNNING STATUS : Train reached Madurai Junction";
    elif T in range(441,471):
        result="CURRENT RUNNING STATUS : Train reached Madurai Junction at 07:20";    
    else :
        result="CURRENT RUNNING STATUS : Train reached Madurai Junction at 07:20 and Yet to start from MGR Chennai Central at 22:30 ";
    return result

#MYSURU VANDE BHARAT EXPRESS 20607
def MYSURU_Vande_Bharat_Express():
    if T in range(320,350):
        result="CURRENT RUNNING STATUS :  About to Start from  MGR Chennai Central by 05:50 " ;
    elif T==350:
         result="CURRENT RUNNING STATUS : Starts from  MGR Chennai Central";
    elif T in range(351,445):
         result="CURRENT RUNNING STATUS : Started from MGR Chennai Central and About to Reach Katpadi Junction";
    elif T==445:
         result="CURRENT RUNNING STATUS : Train reached Katpadi Junction";
    elif T in range(446,625):
         result="CURRENT RUNNING STATUS : Train crossed Katpadi Junction and about to reach KSR Bengaluru City Junction";
    elif T==625:
         result="CURRENT RUNNING STATUS :  Train reached KSR Bengaluru City Junction";
    elif T in range(626,740):
        result="CURRENT RUNNING STATUS : Train crossed KSR Bengaluru City Junction and about to reach Mysuru Junction";
    elif T==740:
        result="CURRENT RUNNING STATUS : Train reached Mysuru Junction";
    elif T in range(741,771):
        result="CURRENT RUNNING STATUS : Train reached Mysuru Junction at 12:20";    
    else :
        result="CURRENT RUNNING STATUS : Train reached Mysuru Junction at 12:20 and Yet to start from MGR Chennai Central at 05:50 ";
    return result

#Mysuru shatabdi express 12007
def MYSURU_Shatabdi_Express():
    if T in range(330,360):
        result="CURRENT RUNNING STATUS :  About to Start from  MGR Chennai Central by 06:00" ;
    elif T==360:
         result="CURRENT RUNNING STATUS : Starts from  MGR Chennai Central";
    elif T in range(361,460):
         result="CURRENT RUNNING STATUS : Started from MGR Chennai Central and About to Reach Katpadi Junction";
    elif T==460:
         result="CURRENT RUNNING STATUS : Train reached Katpadi Junction";
    elif T in range(466,650):
         result="CURRENT RUNNING STATUS : Train crossed Katpadi Junction and about to reach KSR Bengaluru City Junction";
    elif T==650:
         result="CURRENT RUNNING STATUS :  Train reached KSR Bengaluru City Junction";
    elif T in range(651,780):
        result="CURRENT RUNNING STATUS : Train crossed KSR Bengaluru City Junction and about to reach Mysuru Junction";
    elif T==780:
        result="CURRENT RUNNING STATUS : Train reached Mysuru Junction";
    elif T in range(781,811):
        result="CURRENT RUNNING STATUS : Train reached Mysuru Junction at 01:00";    
    else :
        result="CURRENT RUNNING STATUS : Train reached Mysuru Junction at 01:00 and Yet to start from MGR Chennai Central at 06:00 ";
    return result



# Initialize GPIO
# TO get information from cloud to python code

def myCommandCallback(cmd):
    print("Train no.: %s" % cmd.data['command'])
    status=cmd.data['command']
    if status=="12673":
        tr_name='CHERAN EXPRESS'
        result = Cheran_express()
        data = {'TRAIN_NO': status,'TRAIN_NAME': tr_name,'LOCATION' : result}
        
        def myOnPublishCallback():
            print ("Published location = %s " % result,"to IBM Watson")
        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        
        if not success:
            print("Not connected to IoTF")
    elif status=="12671":
        tr_name='NILAGIRI EXPRESS'
        result = Nilagiri_express()
        data = {'TRAIN_NO': status,'TRAIN_NAME': tr_name,'LOCATION' : result}
        
        def myOnPublishCallback():
            print ("Published location = %s " % result,"to IBM Watson")
        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        
        if not success:
            print("Not connected to IoTF")
    elif status=="12675":
        tr_name='KOVAI EXPRESS'
        result = Kovai_express()
        data = {'TRAIN_NO': status,'TRAIN_NAME': tr_name,'LOCATION' : result}
        
        def myOnPublishCallback():
            print ("Published location = %s " % result,"to IBM Watson")
        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
    elif status=="11679":
        tr_name='CBE INTERCITY'
        result = Cbe_intercity()
        data = {'TRAIN_NO': status,'Train_Name': tr_name,'LOCATION' : result}
        
        def myOnPublishCallback():
            print ("Published location = %s " % result,"to IBM Watson")
        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)    
        if not success:
            print("Not connected to IoTF")
    elif status=="12689":
        tr_name='NAGERCOIL JN SF EXPRESS'
        result = Nagercoil_JN_SF_Express()
        data = {'TRAIN_NO': status,'TRAIN_NAME': tr_name,'LOCATION' : result}
        
        def myOnPublishCallback():
            print ("Published location = %s " % result,"to IBM Watson")
        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        
        if not success:
            print("Not connected to IoTF")
    elif status=="20601":
        tr_name='MADURAI_SF_EXPRESS'
        result = Madurai_SF_Express()
        data = {'TRAIN_NO': status,'TRAIN_NAME': tr_name,'LOCATION' : result}
        
        def myOnPublishCallback():
            print ("Published location = %s " % result,"to IBM Watson")
        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        
        if not success:
            print("Not connected to IoTF")
    elif status=="20607":
        tr_name='MYSURU VANDHE BHARAT EXPRESS'
        result = Madurai_SF_Express()
        data = {'TRAIN_NO': status,'TRAIN_NAME': tr_name,'LOCATION' : result}
        
        def myOnPublishCallback():
            print ("Published location = %s " % result,"to IBM Watson")
        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        
        if not success:
            print("Not connected to IoTF")
    elif status=="12007":
        tr_name='MYSURU SHATABDI EXPRESS'
        result = MYSURU_Shatabdi_Express()
        data = {'TRAIN_NO': status,'TRAIN_NAME': tr_name,'LOCATION' : result}
        
        def myOnPublishCallback():
            print ("Published location = %s " % result,"to IBM Watson")
        success = deviceCli.publishEvent("IoTSensor", "json", data, qos=0, on_publish=myOnPublishCallback)
        
        if not success:
            print("Not connected to IoTF")        
            
    else :
        print ("please send proper command")
        
#pinging device
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()        

#to connect
deviceCli.connect()

#this code runs everytime
while True:
    cur=datetime.now()
    H=cur.hour
    M=cur.minute
    T=(60*H)+M;
    deviceCli.commandCallback = myCommandCallback
    time.sleep(2)
deviceCli.disconnect()    
    
    

	
