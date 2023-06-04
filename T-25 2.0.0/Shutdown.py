
from estop import top, shortclock, estoping
import datetime
import constants


def shutdown():
    top()
    shutdown = input(" Contiune to ride shutdown: Right DISPATCH to continue")
    if(shutdown == "1"):
        top()
        finalshutdown = input("Complete paper check list to continue with shutdown: Right DISPATCH to continue")
        if (finalshutdown == "1"):
            top()
            print("T-25 is currently in shut down...")
            print
            fh = open('shutDownlog.txt', 'a')
            current_date = datetime.datetime.now()
            fh.write("\n" + 'T-25 Shutdown: ' + str(current_date) + "\n")
            fh.close()
            shortclock()
            top()
            print("GLCOS Version: " + constants.glcos)
            print("GLC: Saftey by Design")
            print("From all of us at Great Lakes Coasters thank you for operating with us :)")
            shortclock()
            quit()
        elif(finalshutdown == "4"):
            estoping()
            quit()
    elif(shutdown == "4"):
      estoping()
      quit()
