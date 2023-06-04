##This file is going to read data and print from a report file

from estop import top, shortclock
import time

def errorReport():
    top()
    print("PRINTING ERROR LOG...")
    shortclock()
    file = open('C:\Evans_Stuff\Python\T-25_Ops\T-25 2.0.0\Logs\errorLogs.txt', 'r')

    for line in file:
        if line.startswith('Error'):
            error = line
            print(error)
            time.sleep(0.2)


def estopReport():
    top()
    print("PRINTING ESTOP LOG...")
    shortclock()
    file = open('C:\Evans_Stuff\Python\T-25_Ops\T-25 2.0.0\Logs\estopLog.txt', 'r')

    for line in file:
        if line.startswith('RIDE'):
            error = line
            print(error)
            time.sleep(0.2)

def modeSwitchReport():
    top()
    print("PRINTING MODE SWITCH LOG...")
    shortclock()
    file = open('C:\Evans_Stuff\Python\T-25_Ops\T-25 2.0.0\Logs\modeSwitchLog.txt', 'r')

    for line in file:
        if line.startswith('Mode'):
            error = line
            print(error)
            time.sleep(0.2)

def shutDownReport():
    top()
    print("PRINTING SHUT DOWN LOG...")
    shortclock()
    file = open('C:\Evans_Stuff\Python\T-25_Ops\T-25 2.0.0\Logs\shutDownlog.txt', 'r')

    for line in file:
        if line.startswith('T-25'):
            error = line
            print(error)
            time.sleep(0.2)

def startReport():
    top()
    print("PRINTING RIDE START LOG...")
    shortclock()
    file = open('C:\Evans_Stuff\Python\T-25_Ops\T-25 2.0.0\Logs\startLog.txt', 'r')

    for line in file:
        if line.startswith('T-25'):
            error = line
            print(error)
            time.sleep(0.2)
        if line.startswith('Inspection'):
            error = line
            print(error)
            time.sleep(0.2)
        if line.startswith('Operator'):
            error = line
            print(error)
            time.sleep(0.2)


