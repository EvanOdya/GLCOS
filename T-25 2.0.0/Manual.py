
from estop import top, estoping, shortclock
from Errors import E300, E550, E400
import ridemusic
from Shutdown import shutdown
import winsound
import constants
import time

def resetride():
  print("")
  ##Reset all looping values to defalt

def printsongs():
  top()
  print(ridemusic.song1n)
  print(ridemusic.song2n)
  print(ridemusic.song3n)
  print(ridemusic.song5n)
  print(ridemusic.song6n)

def manualmodeen():

    ##Starting values
    totalrideload = 0
    gyro = True
    ridetimer = 5

    riderunning = True
    restraintcheck = True
    musicq = input("Would you like onboard music (y/n): ")
    if(musicq == "y"):
        music = True
    elif(musicq == "n"):
        music = False
    elif(musicq == "4"):
        estoping()
        quit()
    else:
        E300()
        quit()
    top()
    riderunning = True
    while(riderunning == True):
        resetride()
        while(restraintcheck == True):
            if(music == True):
                printsongs()
                musicc = input('Please select music choice (1-2-3-5-6):')
                top()
                if(musicc == "1"):
                    ridemusic.song1()
                elif(musicc == "2"):
                    ridemusic.song2()
                elif(musicc == "3"):
                    ridemusic.song3()
                elif(musicc == "5"):
                    ridemusic.song5()
                elif(musicc == "6"):
                    ridemusic.song6()
                elif(musicc == "4"):
                    estoping()
                    break
            riderweight = input("Input rider weight:")
            top()
            restraints = input("Verify Restraints: Press to continue")
            top()
            if(restraints == "5"):
                top()
                print("Restraints Locked: GREEN to Dispatch")
                restraintcheck = False
            elif(restraints == "4"):
                estoping()
                break
            elif(restraints =="take5"):
                shutdown()
                quit()
            else:
                E300()
                break
        dispatch1 = input("")
        top()
        if(dispatch1 == "31"):
            riderweightint = int(riderweight)
            if(constants.maxriderweight >= riderweightint):
                print
            else:
                E550()
                estoping()
                quit()
            if(totalrideload >= constants.allowrideload):
                E400()
                estoping()
                quit()
            print("## Ride Running")
            restraintcheck = True
            while(gyro == True ) and (ridetimer > 0):
                print("DATA GO")
                time.sleep(1)
                ridetimer -= 1




            print("##Ride over")
            totalrideload += riderweightint
            shortclock()
            winsound.PlaySound(None, winsound.SND_PURGE)
            top()
        elif(dispatch1 == "4"):
            estoping()
            break
        elif(dispatch1 == "y"):
            top()
            riderunning = False
        else: 
            E300()
            break