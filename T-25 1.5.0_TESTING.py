glcos = "1.5.0"

#NOTES
#1) USE METRIC DUMBASSES

import os
import time
import datetime
import winsound
import keyboard
import multiprocessing
from playsound import playsound
from inputimeout import inputimeout, TimeoutOccurred
from threading import Thread
os.chdir('C:\Evans_Stuff\Python\T-25_Ops\RideLogs')

##Errors below
##100: Op mode not avaible
##200: E-STOP Engaged
##300: Unknown Command
##400: Hard reset requird to return to operations

passwordtimes = 5
running = True
opmode = "manual" 
topcode = "*** PLEASE READ OPERATION MANUAL BEFORE USE ***"
restraintcheck = True

#prox data True if train is present
prox1 = False
prox2 = False
prox3 = False
prox4 = False

#if Ultrasonic sensors are used
ultras1 = 0
ultras2 = 0
ultras3 = 0
ultras4 = 0

#motor once it exists
motorspeed = 0

# Ride position is based off of the meters traveled there is no negitive only goes up
rideposition = 0
#Ride posititon is the percentage of track traveled
ridepositionp = 0

##music variables
stop_thread1 = False
stop_thread2 = False
stop_thread3 = False
stop_thread4 = False

#On ride music library
def song1():
  winsound.PlaySound('C:\Evans_Stuff\Python\T-25_Ops\zide_music\Cold.wav', winsound.SND_ASYNC)
song1n = "1- Cold"
def song2():
  winsound.PlaySound('C:\Evans_Stuff\Python\T-25_Ops\zide_music\Heroes_Tonight.wav', winsound.SND_ASYNC)
song2n = "2- Heros Tonight"
def song3():
  winsound.PlaySound('C:\Evans_Stuff\Python\T-25_Ops\zide_music\Light_It_Up.wav', winsound.SND_ASYNC)
song3n = '3- Light It Up'
def song5():
  winsound.PlaySound('C:\Evans_Stuff\Python\T-25_Ops\zide_music\Lost_Sky.wav', winsound.SND_ASYNC)
song5n = '5- Lost Sky'
def song6():
  winsound.PlaySound('C:\Evans_Stuff\Python\T-25_Ops\zide_music\sop_gun_Anthem.wav', winsound.SND_ASYNC)
song6n = '6- Top Gun Anthem'
def printsongs():
  top()
  print(song1n)
  print(song2n)
  print(song3n)
  print(song5n)
  print(song6n)


##Put this to clear screen and print warning message
def top():
  clear()
  print(topcode)

##3 second timer, no code runs
def shortclock():
  time.sleep(3)

#Clears screen (no use)
def clear():
  os.system('cls' if os.name == 'nt' else "printf '\033c'")

##Runs e-stop protocall
def estopeng():
  motorspeed = 0
  clear()
  print(topcode)
  fh = open('estoplog.txt', 'a')
  current_date = datetime.datetime.now()
  fh.write("\n" + "RIDE E-STOPED: " + str(current_date) + "\n")
  fh.close()
  winsound.PlaySound(None, winsound.SND_PURGE)
  print("Error 200: E-STOP Engaged")
  errorsound()
  print("RIDE E-STOPED - PRESS ESR RESET TO CONTINUE")
  esrpressloop = True
  while(esrpressloop == True):
    estopingsound = Thread(target=estopsound)
    estopingsound.start()
    top()
    print("Error 200: E-STOP Engaged")
    print("RIDE E-STOPED - PRESS ESR RESET TO CONTINUE")
    try:
      esrpress = inputimeout(prompt='>>', timeout=1)
    except TimeoutOccurred:
      esrpress = ''
    if(esrpress == '2'):
      break
  top()
  print("Scan Platform and ride area, if any injurys are seen call 911,")
  scanplatestop = input("If problem is resolved press the right DISPATCH button to continue")
  top()
  print("Maintenance is required to reset operation system")
  matpass = input("MAINTENANCE PASSWORD: ")
  top()
  estopcause = input("Write a short discription of the issue: ")
  fh = open('estoplog.txt', 'a')
  fh.write("Cause of E-STOP: " + estopcause + "\n")
  fh.close()
  top()
  returnestop = input("PRESS RIGHT DISPATCH TO RETURN TO MANUAL OR CLOSE OPS")
  if(esrpress == "2") and (scanplatestop == "1") and (matpass == "scancomplete") and (returnestop == "1"):
    top()
  else:
    running = False
    top()
    print("Error 400: Hard Restart is Required")
    errorsound()
    print("HARD RESTART IS REQUIRD TO CONTIUNE OPERATIONS")
    time.sleep(999)

##trys to find if the e-stop is pressed
def ifestopeng():
  if(input("") == "4"):
    estopeng()
  else:
    print("")

##sets all values to zero
def resetride():
  prox1 = False
  prox2 = False
  prox3 = False
  prox4 = False
  motorspeed = 0
  rideposition = 0
  ridepositionp = 0
  ultras1 = 0
  ultras2 = 0
  ultras3 = 0
  ultras4 = 0

##logs all mode switches
def modeswitchlog():
  if(opmode == "manual") or (opmode == "auto") or (opmode == "mat"):
    fh = open('modeswitchlog.txt', 'a')
    current_date = datetime.datetime.now()
    fh.write("Mode switched to " + opmode + " at " + str(current_date) + "\n" + "\n")
    fh.close()
  else:
    print("Error 101: Op mode Unknown")
    shortclock()

##Plays E-stop warning sound
def estopsound():
  playsound('C:\Evans_Stuff\Python\T-25_Ops\zirbus_autopilot.wav')

##Plays error sound
def errorsound():
    playsound('C:\Evans_Stuff\Python\T-25_Ops\error_sound.mp3')
    time.sleep(1)

##Checks for E-stop
def checking_interrupt():
    global buttons
    if keyboard.is_pressed("4"):
       top()
       print(i)
       time.sleep(5)
       estopeng()
       top()
       print("Error 400: Hard reset requird to return to operations")
       time.sleep(4)
       quit()
    else:
      time.sleep(0.001)
      quit()

## chech for estop engage
def esck():
  global estopengage
  if(estopengage == True):
    time.sleep(10000)


top()
print("GLCOS Version: " + glcos)
print("GLC: Saftey by Design")
time.sleep(5)
top()


def main():

  #Define variables in the method because im dumb
  passwordtimes = 5
  running = True
  opmode = "manual" 
  topcode = "*** PLEASE READ OPERATION MANUAL BEFORE USE ***"
  restraintcheck = True
  
  print("Operations Mode: " + opmode)
  while(running == True):
    if(opmode == "manual"):
      modeswitchlog()
      opname = input("Operator Name: ")
      ##if(opname == "4"):
       ## estopeng()
       ## break
      runningpassword = input("Password:")
      if(runningpassword == "take5"):
        top()
        print("T-25 In Startup...")
        shortclock()
        ridecheck1 = input("T-25 been inspected following standared precerdures:")
        ridecheck2 = input("Seatbelts and saftey systems have been tested:")
        ridecheck3 = input("Weather is inside operation minimums and maximuns:")
        ridecheck4 = input("Ride area is clear of all foregin objects:")
        ridecheck5 = input("(IA) All guests have been instructed in proper rider form:")
        ridecheck6 = input("All operators are licenced and aware:")
        if(ridecheck1 == "y") and (ridecheck2 == "y") and (ridecheck3 == "y") and(ridecheck4 == "y") and (ridecheck5 == "y") and (ridecheck6 == "y"):
          clear()
          top()
          print("T-25 is Ready for Testing")
          fh = open('ridestartlog.txt', 'a')
          current_date = datetime.datetime.now()
          fh.write("\n" + 'T-25 Started: ' + str(current_date) + "\n" + "Inspection Status: " + ridecheck1 + ridecheck2 + ridecheck3 + ridecheck4 + ridecheck5 + ridecheck6 + "\n" + "Operator Name: " + opname + "\n")
          fh.close()
          top()
          print("Dispatch Test - Press Both Dispatch to Continue")
          dispatchtest1 = input("")
          top()
          if(dispatchtest1 == "31"):
             top()
             print("Dispatch Buttons are Operational")
             shortclock()
          elif(dispatchtest1 == "4"):
            estopeng()
            break
          else: 
            print("Error 300: Unknown Command")
            errorsound()
            shortclock()
            break
          pickstartmode = input("Press ESR Reset for MANUAL, Press Right Dispatch for AUTO")
          top()
          if(pickstartmode == "2"):
            #THIS IS NORMAL MANUAL OPERATING MODE (CODE HERE LOLOLOL)
            opmode = "manual"
            modeswitchlog()
            print("MODE SWITCH: MANUAL")
            riderunning = True
            musicq = input("Would you like onboard music (y/n): ")
            if(musicq == "y"):
              music = True
            elif(musicq == "n"):
              music = False
            elif(musicq == "4"):
              estopeng()
              break
            else:
              print("Error 300: Unknown Command")
              errorsound()
              shortclock()
              break
            top()
            while(riderunning == True):
              resetride()
              while(restraintcheck == True):
                if(music == True):
                  printsongs()
                  musicc = input('Please select music choice (1-2-3-5-6):')
                  top()
                  if(musicc == "1"):
                    song1()
                  elif(musicc == "2"):
                    song2()
                  elif(musicc == "3"):
                    song3()
                  elif(musicc == "5"):
                    song5()
                  elif(musicc == "6"):
                    song6()
                  elif(musicc == "4"):
                    estopeng()
                    break
                restraints = input("Verify Restraints: Press to continue")
                top()
                if(restraints == "5"):
                   top()
                   print("Restraints Locked: GREEN to Dispatch")
                   restraintcheck = False
                elif(restraints == "4"):
                   estopeng()
                   break
                elif(restraints =="take5"):
                  top()
                  shutdown = input(" Contiune to ride shutdown: Right DISPATCH to continue")
                  if(shutdown == "1"):
                    top()
                    finalshutdown = input("Complete paper check list to continue with shutdown: Right DISPATCH to continue")
                    if (finalshutdown == "1"):
                      top()
                      print("T-25 is currently in shut down...")
                      print
                      fh = open('rideshutdownlog.txt', 'a')
                      current_date = datetime.datetime.now()
                      fh.write("\n" + 'T-25 Shutdown: ' + str(current_date) + "\n")
                      fh.close()
                      shortclock()
                      top()
                      print("GLCOS Version: " + glcos)
                      print("GLC: Saftey by Design")
                      print("From all of us at Great Lakes Coasters thank you for operating with us :)")
                      shortclock()
                      quit()
                    elif(finalshutdown == "4"):
                      estopeng()
                      break
                  elif(shutdown == "4"):
                    estopeng()
                    break
                else:
                   print("Error 300: Unknown Command")
                   errorsound()
                   shortclock()
                   break
              dispatch1 = input("")
              top()
              if(dispatch1 == "31"):
                print("## Ride Running")
                restraintcheck = True
                shortclock()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
                print("##Ride over")
                shortclock()
                winsound.PlaySound(None, winsound.SND_PURGE)
                top()
              elif(dispatch1 == "4"):
               estopeng()
               break
              else: 
               print("Error 300: Unknown Command")
               errorsound()
               shortclock()
               break
          elif(pickstartmode == "1"):
            #THIS IS NORMAL AUTO OPERATING MODE (CODE HERE LOLOLOL)
            print("MODE SWITCH: AUTO")
            opmode = "auto"
            modeswitchlog()
            print("Error 100: Op mode not avalible")
            errorsound()
  
  
  
  
  
  
  
  
  
  
  
  
  
  
          elif(pickstartmode == "4"):
            estopeng()
            break
          else:
            print("Error 300: Unknown Command")
            errorsound()
            shortclock()
            running = False
            break
        elif(ridecheck1 == "4") or (ridecheck2 == "4") or (ridecheck3 == "4") or (ridecheck4 == "4") or (ridecheck5 == "4") or (ridecheck6 == "4"):
          estopeng()
          break
        else:
          print("Error 300: Unknown Command")
          errorsound()
          print("SHUTTING DOWN")
          fh = open('ridestartlog.txt', 'a')
          current_date = datetime.datetime.now()
          fh.write("\n" + 'T-25 Start Failed: ' + str(current_date) + "\n" + "Inspection Status: " + ridecheck1 + ridecheck2 + ridecheck3 + ridecheck4 + ridecheck5 + ridecheck6 + "\n" + "Operator Name: " + opname + "\n")
          fh.close()
          shortclock()
          running = False
      elif(runningpassword == "4"):
        estopeng()
        break
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
            estopeng()
            break
          else:
            print("SHUTING DOWN")
            running = False
    else:
      top()
      print("Error 100: Op mode not avalible")
      errorsound()
      print("AUTO MODE SWITCH: Manual")
      opmode = "manual"
      modeswitchlog()
      passwordtimes += 5

t1 = Thread(target= main)

t1.start()

##continously checks for estop
for i in range(1000000000):
  t2 = Thread(target= checking_interrupt, args= i)
  t2.start()
  t2.join()