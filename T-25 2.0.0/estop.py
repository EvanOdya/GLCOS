import os
import time
import datetime
import winsound
from playsound import playsound
from inputimeout import inputimeout, TimeoutOccurred
from threading import Thread
from ridemusic import estopsound
from ridemusic import errorsound
os.chdir('C:\Evans_Stuff\Python\T-25_Ops\T-25 2.0.0\Logs')

topcode = "*** PLEASE READ OPERATION MANUAL BEFORE USE ***"

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

def estoping():
  top()
  fh = open('estopLog.txt', 'a')
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
  print("Report event into paper logs and report injuries to GLC.com/operations,")
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
    top()
    print("Error 400: Hard Restart is Required")
    errorsound()
    print("HARD RESTART IS REQUIRD TO CONTIUNE OPERATIONS")
    time.sleep(999)
