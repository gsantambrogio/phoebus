#!/usr/bin/python3
import epics
from tabulate import tabulate
import time

def switch_vars(choice):
    match choice:
        case 1:
            val = 1-int(epics.caget('PressureGauge:switch'))
            epics.caput('PressureGauge:switch',val)
            return "Switched CC1"
        case 2:
            val = 1-int(epics.caget('CC1:notify'))
            epics.caput('CC1:notify',val)
            return "Switched alarm on CC1"
        case 3:
            val = 1-int(epics.caget('ACP:switch'))
            epics.caput('ACP:switch',val)
            return "Switched scroll"
        case 4:
            val = 1-int(epics.caget('Valve1'))
            epics.caput('Valve1',val)
            return "Switched Valve"
        case 5:
            val = 1-int(epics.caget('Turbo:station'))
            epics.caput('Turbo:station',val)
            return "Switched Turbo" 
        case 6:
            val = 1-int(epics.caget('Turbo:venting'))
            epics.caput('Turbo:venting',val)
            return "Switched Venting"       
        case 7:
            val = 1-int(epics.caget('cryo:switch'))
            epics.caput('cryo:switch',val)
            return "Switched Cryo"
        case 0:
            return "Refreshing..."
        case _:
            return "Error"

def get_vals():
    vals=[['','Pirani','',epics.caget('pirani:PRESSURE')],
                [1,'Cold cathode',epics.caget('PressureGauge:switch'),epics.caget('CC1:PRESSURE')],
                [2,'Cold cathode Notification',epics.caget('CC1:notify'),''],
                [],
                [3,'Scroll',epics.caget('ACP:switch'),''],
                [4,'Valve',epics.caget('Valve1'),''],
                [5,'Turbo',epics.caget('Turbo:station'),epics.caget('Turbo:rotspeed')],
                [6,'Vent',epics.caget('Turbo:venting'),''],
                [7,'Cryo',epics.caget('cryo:switch'),''],
                ['','Temp 1','',epics.caget('CTC:Temp1')],
                ['','Temp 2','',epics.caget('CTC:Temp2')],
                ['','Temp 3','',epics.caget('CTC:Temp3')],
                ['','Temp 4','',epics.caget('CTC:Temp4')]]
    return vals


while True:
    print(tabulate(get_vals()))
    switch = int(input("Want to switch something? Enter switch #,  or 0 to refresh: "))
    print(switch_vars(switch))
    time.sleep(1)
