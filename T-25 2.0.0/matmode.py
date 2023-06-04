
from estop import top, estoping, shortclock
import winsound
from Errors import E300
from Shutdown import shutdown
import constants
import main
import fileReport


def matmodes():

    riderunning1 = True

    while(riderunning1 == True):
        top()
        settingsq = input("ESR Reset to enter settings screen, Right DISPATCH to contiune")
        if(settingsq == "2"):
            print("maxspeed: " + main.maxspeed + " - 2")
            print("maxgforce: " + main.maxgforce + " - 3")
            print("Print Error Log - 5")
            print("Print Estop Log - 6")
            print("Print Mode Switch Log - 7")
            print("Print Ride Shutdown Log - 8")
            print("Print Ride Start Log - 9")
            shortclock()
            top()
            changeValueLoop = True
            while(changeValueLoop == True):
                changevalues =input("select number vlaue to change or print report, right DISPATCH to continue")

                if(changevalues == "1"):
                    top()
                elif(changevalues == "2"):
                    main.maxspeed = input("Input new max speed: ")
                    shortclock()
                    changeMoreSettings = input("Right DISPATCH to contiune, FE right DISPATCH to Exit")
                    top()
                    if(changeMoreSettings == "y"):
                        changeValueLoop = False
                    
                elif(changevalues == "3"):
                    main.maxgforce = input("Input new max GForce: ")
                    main.maxforceint = float(main.maxgforce)
                    shortclock()
                    changeMoreSettings = input("Right DISPATCH to contiune, FE right DISPATCH to Exit")
                    top()
                    if(changeMoreSettings == "y"):
                        changeValueLoop = False
                elif(changevalues == "5"):
                    fileReport.errorReport()
                    changeMoreSettings = input("Right DISPATCH to contiune, FE right DISPATCH to Exit")
                    top()
                    if(changeMoreSettings == "y"):
                        changeValueLoop = False
                elif(changevalues == "6"):
                    fileReport.estopReport()
                    changeMoreSettings = input("Right DISPATCH to contiune, FE right DISPATCH to Exit")
                    top()
                    if(changeMoreSettings == "y"):
                        changeValueLoop = False
                elif(changevalues == "7"):
                    fileReport.modeSwitchReport()
                    changeMoreSettings = input("Right DISPATCH to contiune, FE right DISPATCH to Exit")
                    top()
                    if(changeMoreSettings == "y"):
                        changeValueLoop = False
                elif(changevalues == "8"):
                    fileReport.shutDownReport()
                    changeMoreSettings = input("Right DISPATCH to contiune, FE right DISPATCH to Exit")
                    top()
                    if(changeMoreSettings == "y"):
                        changeValueLoop = False
                elif(changevalues == "9"):
                    fileReport.startReport()
                    changeMoreSettings = input("Right DISPATCH to contiune, FE right DISPATCH to Exit")
                    top()
                    if(changeMoreSettings == "y"):
                        changeValueLoop = False
                elif(changevalues == "4"):
                    estoping()
                    quit()
                else:
                    E300()
                    quit()
        elif(settingsq == "4"):
            estoping()
            quit()
        elif(settingsq == "1"):
            top()
        else:
            E300()
            quit()
        top()
        restraints = input("Verify Restraints: Press to contiune")
        top()
        if (restraints == "5"):
            top()
            riderweight =input("Input rider weight:")
            top()
            print("Rider Weight:" + riderweight)
            riderweightint = float(riderweight)
            pforce =riderweightint / 2.5
            force = 32.9476 * pforce
            aweight = riderweightint * main.maxforceint
            sforce = str(force)
            print("Max speed: " + main.maxspeed + " MPS")
            print("Max force on track: " + sforce + "N")
            print("Max G-Force: " + main.maxgforce + "Gs")
            saweight = str(aweight)
            print("Aparent Weight: " + saweight + "LBS")
            input("Right DISPATCH to contiune")
            top()
            dispatch1 =input("Restraints Locked: Green to Disptach")
        elif(restraints == "4"):
            estoping()
            quit()
        elif(restraints == "take5"):
            shutdown()
            quit()
            top()
        if(dispatch1 == "31"):
            print("## ride running")
            restraintcheck = True
            shortclock()
            print("##ride over")
            shortclock()
            winsound.PlaySound(None,winsound.SND_PURGE)
            top()
        elif(dispatch1 == "4"):
            estoping()
            quit()
        elif(dispatch1 == "y"):
            top()
            riderunning1 = False
        else:
            E300()
            quit()