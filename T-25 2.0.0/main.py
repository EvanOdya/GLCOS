
import os
import time
import datetime
import winsound
from playsound import playsound
from inputimeout import inputimeout, TimeoutOccurred
from threading import Thread

##Importing Internal DEFS
import ridemusic
from ridemusic import errorsound, estopsound, song1n, song2n, song3n, song5n, song6n
from estop import estoping, shortclock, top, clear
from Errors import E100, E101, E200, E300, E400, E500, E510, E520, E530, E540, E550, E560, E570
from Shutdown import shutdown
from matmode import matmodes
from Manual import manualmodeen
import constants
import fileReport
os.chdir('C:\Evans_Stuff\Python\T-25_Ops\T-25 2.0.0\Logs')

##Local starting Values
totalrideload = 0
passwordtimes = 5
running = True
restraintcheck = True
opmode = "manual" 

maxspeed = "5.74"
maxgforce = "2.341"
maxforceint = 2.341

##music variables, Defaulting all to stop
stop_thread1 = False
stop_thread2 = False
stop_thread3 = False
stop_thread4 = False

def resetride():
  print("")
  ##Reset all looping values to defalt

##logs all mode switches
def modeswitchlog():
  if(opmode == "manual") or (opmode == "auto") or (opmode == "mat"):
    fh = open('modeSwitchLog.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("Mode switched to " + opmode + " at " + str(current_date) + "\n" + "\n")
    fh.close()
  else:
    E101()
    shortclock()

    
##Start of ride code
top()
print("GLCOS Version: " + constants.glcos)
print("GLC: Saftey by Design")
time.sleep(5)
top()

print("Operations Mode: " + opmode)


while(running == True):
  if(opmode == "manual"):
    modeswitchlog()
    opname = input("Operator Name: ")
    if(opname == "4"):
      estoping()
    runningpassword = input("Password:")
    if(runningpassword == "take5"):
      top()
      pollStart = input("BEGIN GO/NO GO POLL, right Dispatch to Start Ride")
      if(pollStart == "1"):
        ##Put all the code for Gyro and ORC
        print("RIDE COMPUTER: GO")
        time.sleep(1)
        print("RIDE FILES: GO")
        time.sleep(1)
        print("GYRO: GO")
        time.sleep(1)
        print("ORC: GO")
        time.sleep(1)
        print("ESTOP: GO")
        shortclock()
      elif(pollStart == "4"):
        estoping()
        break
      else:
        E300()
        break
      top()
      print("T-25 In Startup...")
      ##make longer for real coaster
      alarmloop = 1
      while(alarmloop >= 0):
        estopsound()
        shortclock()
        alarmloop -= 1
      shortclock()
      ridecheck1 = input("T-25 been inspected following standared precerdures:")
      ridecheck2 = input("Seatbelts and saftey systems have been tested:")
      ridecheck3 = input("Weather is inside operation minimums and maximuns:")
      ridecheck4 = input("Ride area is clear of all foregin objects:")
      ridecheck5 = input("(IA) All guests have been instructed in proper rider form:")
      ridecheck6 = input("All operators are licenced and aware:")
      if(ridecheck1 == "y") and (ridecheck2 == "y") and (ridecheck3 == "y") and(ridecheck4 == "y") and (ridecheck5 == "y") and (ridecheck6 == "y"):
        clear()
        print(constants.topcode)
        print("T-25 is Ready for Testing")
        fh = open('startLog.txt', 'a')
        current_date = datetime.datetime.now()
        fh.write("\n" + 'T-25 Started: ' + str(current_date) + "\n" + "Inspection Status: " + ridecheck1 + ridecheck2 + ridecheck3 + ridecheck4 + ridecheck5 + ridecheck6 + "\n" + "Operator Name: " + opname + "\n")
        fh.close()
        if(input("E-STOP Test - Press E-STOP to Continue") == "4"):
            top()
            estopsound()
            if(input("RIDE E-STOPED - PRESS ESR RESET TO CONTINUE") == "2"):
              top()
              print("E-STOP is Operational")
              shortclock()
              clear()
            else:
              E300()
              quit()
        else: 
          E300()
          quit()
        print(constants.topcode)
        print("Dispatch Test - Press Both Dispatch to Contiune")
        dispatchtest1 = input("")
        top()
        if(dispatchtest1 == "31"):
            top()
            print("Dispatch Buttons are Operational")
            shortclock()
        elif(dispatchtest1 == "4"):
          estoping()
          quit()
        else: 
          E300()
          quit()
        top()
        modeswitch = True
        riderunning = True
        while(modeswitch == True):
          pickstartmode = input("ESR Reset for MANUAL, Right Dispatch for AUTO, Restraints for MAT")
          top()
          if(pickstartmode == "2"):
            #THIS IS NORMAL MANUAL OPERATING MODE (CODE HERE LOLOLOL)
            opmode = "manual"
            modeswitchlog()
            print("MODE SWITCH: MANUAL")
            manualmodeen()
          elif(pickstartmode == "1"):
            #THIS IS NORMAL AUTO OPERATING MODE (CODE HERE LOLOLOL)
            print("MODE SWITCH: AUTO")
            opmode = "auto"
            modeswitchlog()
            E100()
            shortclock()
          elif(pickstartmode == "5"):
            ##This is the MAT mode for lots of data
            opmode = "mat"
            modeswitchlog()
            print("MODE SWITCH: MAT")
            riderunning = True
            matmodepass = input("MAINTENANCE PASSWORD:")
            if(matmodepass == "scancomplete"):
              matmodes()
            elif(matmodepass == "4"):
              estoping()
              quit()
            else:
              E300()
              quit()




          elif(pickstartmode == "4"):
            estoping()
            quit()
          else:
            E300()
            running = False
            quit()
      elif(ridecheck1 == "4") or (ridecheck2 == "4") or (ridecheck3 == "4") or (ridecheck4 == "4") or (ridecheck5 == "4") or (ridecheck6 == "4"):
        estoping()
        quit()
      else:
        E300()
        print("SHUTTING DOWN")
        fh = open('startLog.txt', 'a')
        current_date = datetime.datetime.now()
        fh.write("\n" + 'T-25 Start Failed: ' + str(current_date) + "\n" + "Inspection Status: " + ridecheck1 + ridecheck2 + ridecheck3 + ridecheck4 + ridecheck5 + ridecheck6 + "\n" + "Operator Name: " + opname + "\n")
        fh.close()
        shortclock()
        running = False
    elif(runningpassword == "4"):
      estoping()
      quit()
    else:
      top()
      print("INCORRECT PASSWORD")
      passwordtimes -= 1
      if(passwordtimes <= 0):
        top()
        print("MAINTENANCE REQUIRED")
        matpass = input("MAINTENANCE PASSWORD:")
        if(matpass == "scancomplete"):
          top()
          print("MODE SWITCH: MAT")
          opmode = "mat"
        elif(matpass == "4"):
          estoping()
          quit()
        else:
          print("SHUTING DOWN")
          running = False
  else:
    top()
    E100()
    print("AUTO MODE SWITCH: Manual")
    opmode = "manual"
    modeswitchlog()
  passwordtimes += 5
