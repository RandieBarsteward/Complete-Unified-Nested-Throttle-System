"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                
              (Joystick Gremlin Profile/Scripts for Star Citizen)

Moduel intended to integrate a custom button box/controller into Joystick Gremlin.  

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import hotas
import scmap
import time

button = gremlin.input_devices.JoystickDecorator(hotas.BUT_Name,
                                                   hotas.BUT_Id,
                                                   "Default")


##############################################################################
#Power On section of Button Box

# Button Box Power On Key and Button
# Key on allows one button press to start power, key off will shut down power

PowerKey = False
PowerState = False
ScanMode = False
DestructArm = False

@button.button(hotas.BUT_Key)
def onThrottleBtn_BUT_Key(event, vjoy):
    global PowerKey
    global PowerState
    if event.is_pressed:
        PowerKey = True
    else:
        PowerKey = False
        PowerState = False
        vjoy[1].button(scmap.PowerOn).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.PowerOn).is_pressed = False
               
                    
     
@button.button(hotas.BUT_PowerOn)
def onThrottleBtn_BUT_PowerOn(event, vjoy):
    global PowerKey
    global PowerState
    if PowerKey == True and PowerState == False:
        PowerState = True
        vjoy[1].button(scmap.PowerOn).is_pressed = event.is_pressed
    else:
        vjoy[1].button(scmap.PowerOn).is_pressed = False

@button.button(hotas.BUT_EngineOn)
def onThrottleBtn_BUT_EngineOn(event, vjoy):
    if event.is_pressed:
        vjoy[1].button(scmap.EngineOff).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.EngineOff).is_pressed = False
    else:
        vjoy[1].button(scmap.EngineOff).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.EngineOff).is_pressed = False
                
@button.button(hotas.BUT_ShieldsOn)
def onThrottleBtn_BUT_ShieldsOn(event, vjoy):
    if event.is_pressed:
        vjoy[1].button(scmap.ShieldsOn).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.ShieldsOn).is_pressed = False
    else:
        vjoy[1].button(scmap.ShieldsOn).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.ShieldsOn).is_pressed = False
        
@button.button(hotas.BUT_ShipLights)
def onThrottleBtn_BUT_ShipLights(event, vjoy):
    if event.is_pressed:
        vjoy[1].button(scmap.ShipLights).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.ShipLights).is_pressed = False
    else:
        vjoy[1].button(scmap.ShipLights).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.ShipLights).is_pressed = False

##############################################################################
#IFCS Section

@button.button(hotas.BUT_DecoupleOff)
def onThrottleBtn_BUT_DecoupleOff(event, vjoy):
    if event.is_pressed:
        vjoy[1].button(scmap.DecoupledMode).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.DecoupledMode).is_pressed = False
    else:
        vjoy[1].button(scmap.DecoupledMode).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.DecoupledMode).is_pressed = False

@button.button(hotas.BUT_ComstabOff)
def onThrottleBtn_BUT_ComstabOff(event, vjoy):
    if event.is_pressed:
        vjoy[1].button(scmap.ComstabOff).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.ComstabOff).is_pressed = False
    else:
        vjoy[1].button(scmap.ComstabOff).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.ComstabOff).is_pressed = False


@button.button(hotas.BUT_GSAFE)
def onThrottleBtn_BUT_GSAFE(event, vjoy):
    if event.is_pressed:
        vjoy[1].button(scmap.GSAFE).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.GSAFE).is_pressed = False
    else:
        vjoy[1].button(scmap.GSAFE).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.GSAFE).is_pressed = False

##############################################################################
#FLIGHT MODE Section









##############################################################################
#SCANNING Section
#Sets toggle for scan mode and restricts button press.  Scan button bound to LockFireMissiles in scmap.py to save buttons

@button.button(hotas.BUT_ScanModeToggle)
def onThrottleBtn_BUT_ScanModeToggle(event, vjoy):
    global ScanMode
    if event.is_pressed:
        ScanMode = True
    else:
        ScanMode = False
                    
                    
     
@button.button(hotas.BUT_Scan)
def onThrottleBtn_BUT_Scan(event, vjoy):
    global ScanMode
    if ScanMode == True:
        vjoy[1].button(scmap.LockFireMissiles).is_pressed = event.is_pressed
    else:
        vjoy[1].button(scmap.LockFireMissiles).is_pressed = False


##############################################################################
#Comms Section


##############################################################################
#Weapons Section


##############################################################################
#Exterior Section

@button.button(hotas.BUT_LandGear)
def onThrottleBtn_BUT_LandGear(event, vjoy):
    if event.is_pressed:
        vjoy[1].button(scmap.LandingGear).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.LandingGear).is_pressed = False
    else:
        vjoy[1].button(scmap.LandingGear).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.LandingGear).is_pressed = False

@button.button(hotas.BUT_ShipLock)
def onThrottleBtn_BUT_ShipLock(event, vjoy):
    if event.is_pressed:
        vjoy[1].button(scmap.LockAllDoors).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.LockAllDoors).is_pressed = False
    else:
        vjoy[1].button(scmap.UnlockAllDoors).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.UnlockAllDoors).is_pressed = False

@button.button(hotas.BUT_ShipDoors)
def onThrottleBtn_BUT_ShipDoors(event, vjoy):
    if event.is_pressed:
        vjoy[1].button(scmap.OpenAllDoors).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.OpenAllDoors).is_pressed = False
    else:
        vjoy[1].button(scmap.CloseAllDoors).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.CloseAllDoors).is_pressed = False

##############################################################################
#Self Destruct Section


@button.button(hotas.BUT_DestructArm)
def onThrottleBtn_BUT_DestructArm(event, vjoy):
    global DestructArm
    if event.is_pressed:
        DestructArm = True
    else:
        DestructArm = False
                  
@button.button(hotas.BUT_SelfDestruct)
def onThrottleBtn_BUT_SelfDestruct(event, vjoy):
    global DestructArm
    if DestructArm == True:
        vjoy[1].button(scmap.SelfDestruct).is_pressed = event.is_pressed
    else:
        vjoy[1].button(scmap.SelfDestruct).is_pressed = False
















