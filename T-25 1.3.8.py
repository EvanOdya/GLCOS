import os
import time
import datetime

##Errors below
##100: Op mode not avaible
##200: E-STOP Engaged
##300: Unknown Command

passwordtimes = 5
running = True
opmode = "Manual" 
topcode = "*** PLEASE READ OPERATION MANUAL BEFORE USE ***"

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

# Ride position is based off of the feet traveled there is no negitive only goes up
rideposition = 0
#Ride posititon is the percentage of track traveled
ridepositionp = 0

def top():
  clear()
  print(topcode)

def shortclock():
  time.sleep(3)

def clear():
  os.system('cls' if os.name == 'nt' else "printf '\033c'")

def estopeng():
  motorspeed = 0
  clear()
  print(topcode)
  fh = open('estoplog.txt', 'a')
  current_date = datetime.datetime.now()
  fh.write("\n" + "RIDE E-STOPED: " + str(current_date) + "\n")
  fh.close()
  print("Error 200: E-STOP Engaged")
  esrpress = input("RIDE E-STOPED - PRESS ESR RESET TO CONTINUE")
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
  returnestop = input("PRESS RIGHT DISPATCH TO RETURN TO MANUAL OPS")
  if(esrpress == "2") and (scanplatestop == "1") and (matpass == "scancomplete") and (returnestop == "1"):
    top()
  else:
    running = False
    top()
    print("HARD RESTART IS REQUIRD TO CONTIUNE OPERATIONS")
    time.sleep(999)
def ifestopeng():
  if(input("") == "4"):
    estopeng()
  else:
    print("")
def resetride():
  prox1 = 0
  prox2 = 0
  prox3 = 0
  prox4 = 0
  motorspeed = 0
  rideposition = 0
  ridepositionp = 0

top()
print("GLCOS Version: 1.3.8")
print("GLC: Saftey by Design")
time.sleep(5)
top()

print("Operations Mode: " + opmode)
while(running == True):
  if(opmode == "Manual"):
    opname = input("Operator Name: ")
    runningpassword = input("Password:")
    if(runningpassword == "take5"):
      top()
      print("T-25 In Startup...")
      shortclock()
      ridecheck1 = input("T-25 been inspected following standared precerdures:")
      ridecheck2 = input("Seatbelts and saftey systems have been tested:")
      ridecheck3 = input("Weather is inside operation minimums and maximuns:")
      ridecheck4 = input("Ride area is clear of all foregin objects:")
      ridecheck5 = input("IA All guests have been instructed in proper rider form:")
      ridecheck6 = input("All operators are licenced and aware:")
      if(ridecheck1 == "y") and (ridecheck2 == "y") and (ridecheck3 == "y") and(ridecheck4 == "y") and (ridecheck5 == "y") and (ridecheck6 == "y"):
        clear()
        print(topcode)
        print("T-25 is Ready for Testing")
        fh = open('ridestartlog.txt', 'a')
        current_date = datetime.datetime.now()
        fh.write("\n" + 'T-25 Started: ' + str(current_date) + "\n" + "Inspection Status: " + ridecheck1 + ridecheck2 + ridecheck3 + ridecheck4 + ridecheck5 + ridecheck6 + "\n" + "Operator Name: " + opname + "\n")
        fh.close()
        if(input("E-STOP Test - Press E-STOP to Continue") == "4"):
           top()
           if(input("RIDE E-STOPED - PRESS ESR RESET TO CONTINUE") == "2"):
             top()
             print("E-STOP is Operational")
             shortclock()
             clear()
           else:
             print("Error 300: Unknown Command")
             shortclock()
             break  
        else: 
          print("Error 300: Unknown Command")
          shortclock()
          break
        print(topcode)
        print("Dispatch Test - Press Both Dispatch to Continue")
        dispatchtest1 = input("")
        top()
        dispatchtest2 = input("")
        if(dispatchtest1 == "1") or (dispatchtest1 == "3"):
           top()
           if(dispatchtest2 == "3") or (dispatchtest2 == "1"):
             top()
             print("Dispatch Buttons are Operational")
             shortclock()
             top()
           else:
             print("Error 300: Unknown Command")
             shortclock()
             break
        elif(dispatchtest1 == "4"):
          estopeng()
        else: 
          print("Error 300: Unknown Command")
          shortclock()
          break
        pickstartmode = input("Press ESR Reset for MANUAL, Press Right Dispatch for AUTO")
        top()
        if(pickstartmode == "2"):
          #THIS IS NORMAL MANUAL OPERATING MODE (CODE HERE LOLOLOL)
          opmode = "Manual"
          print("MODE SWITCH: MANUAL")
          riderunning = True
          while(riderunning == True):
            resetride()
            restraints = input("Verify Restraints: Press to continue")
            if(restraints == "5"):
             top()
             print("Restraints Locked: GREEN to Dispatch")
            elif(restraints == "4"):
             estopeng()
            else:
             print("Error 300: Unknown Command")
             shortclock()
             break

            dispatch1 = input(" ")
            top()
            dispatch2 = input(" ")
            if(dispatch1 == "1") or (dispatch1 == "3"):
             top()
             if(dispatch2 == "3") or (dispatch2 == "1"):
               top()
               print("## RIDE RUNNING")
               shortclock()
               top()
             elif(dispatch2 == "4"):
                estopeng()
             else:
               print("Error 300: Unknown Command")
               shortclock()
               break
            elif(dispatch1 == "4"):
             estopeng()
            else: 
             print("Error 300: Unknown Command")
             shortclock()
             break

             
            



















        elif(pickstartmode == "1"):
          #THIS IS NORMAL AUTO OPERATING MODE (CODE HERE LOLOLOL)
          print("MODE SWITCH: AUTO")
          print("Error 100: Op mode not avalible")














        elif(pickstartmode == "4"):
          estopeng()
        else:
          print("Error 300: Unknown Command")
          shortclock()
          running = False
          break
      elif(ridecheck1 == "4") and (ridecheck2 == "4") and (ridecheck3 == "4") and(ridecheck4 == "4") and (ridecheck5 == "4") and (ridecheck6 == "4"):
        estopeng()
      else:
        print("Error 300: Unknown Command")
        print("SHUTTING DOWN")
        fh = open('ridestartlog.txt', 'a')
        current_date = datetime.datetime.now()
        fh.write("\n" + 'T-25 Start Failed: ' + str(current_date) + "\n" + "Inspection Status: " + ridecheck1 + ridecheck2 + ridecheck3 + ridecheck4 + ridecheck5 + ridecheck6 + "\n" + "Operator Name: " + opname + "\n")
        fh.close()
        shortclock()
        running = False
    elif(runningpassword == "4"):
      estopeng()
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
          opmode = "MAT"
        elif(matpass == "4"):
          estopeng()
        else:
          print("SHUTING DOWN")
          running = False
  else:
    top()
    print("Error 100: Op mode not avalible")
    print("AUTO MODE SWITCH: Manual")
    opmode = "Manual"
    passwordtimes += 5
  