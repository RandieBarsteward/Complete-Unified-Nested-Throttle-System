"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                
              (Joystick Gremlin Profile/Scripts for Star Citizen)

Moduel intended to integrate a custom button box/controller into Joystick Gremlin.  

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import hotas
import scmap
import time
import math
import threading


button = gremlin.input_devices.JoystickDecorator(hotas.BUT_Name,
                                                   hotas.BUT_Id,
                                                   "Default")


throttle = gremlin.input_devices.JoystickDecorator(hotas.THR_Name,
                                                   hotas.THR_Id,
                                                   "Default")


##############################################################################
#Power On section of Button Box

# Button Box Power On Key and Button
# Key on allows one button press to start power, key off will shut down power

PowerKey = False
PowerState = False
ScanMode = False
DestructArm = False
DestructCountdown = False
WheelsDown = False

@button.button(hotas.BUT_Key)
def onThrottleBtn_BUT_Key(event, vjoy):
    global PowerKey
    global PowerState
    if event.is_pressed:
        PowerKey = True
    else:
        PowerKey = False
        PowerState = False
        gremlin.macro.MacroManager().queue_macro(PowerOn_macro)
        


@button.button(hotas.BUT_PowerOn)
def onThrottleBtn_BUT_PowerOn(event, vjoy):
    global PowerKey
    global PowerState
    if PowerKey == True and PowerState == False:
        PowerState = True
        gremlin.macro.MacroManager().queue_macro(PowerOn_macro)

# Create a macro that can be used repeatedly
PowerOn_macro = gremlin.macro.Macro()
PowerOn_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("5"), True))
PowerOn_macro.add_action(gremlin.macro.PauseAction(0.1))
PowerOn_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("5"), False))

@button.button(hotas.BUT_EngineOn)
def onThrottleBtn_BUT_EngineOn(event, vjoy):
    if event.is_pressed:
        gremlin.macro.MacroManager().queue_macro(EngineOn_macro)
    else:
        gremlin.macro.MacroManager().queue_macro(EngineOn_macro)

# Create a macro that can be used repeatedly
EngineOn_macro = gremlin.macro.Macro()
EngineOn_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("4"), True))
EngineOn_macro.add_action(gremlin.macro.PauseAction(0.1))
EngineOn_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("4"), False))

@button.button(hotas.BUT_ShieldsOn)
def onThrottleBtn_BUT_ShieldsOn(event, vjoy):
    if event.is_pressed:
       gremlin.macro.MacroManager().queue_macro(ShieldsOn_macro)
    else:
        gremlin.macro.MacroManager().queue_macro(ShieldsOn_macro)

# Create a macro that can be used repeatedly
ShieldsOn_macro = gremlin.macro.Macro()
ShieldsOn_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("6"), True))
ShieldsOn_macro.add_action(gremlin.macro.PauseAction(0.1))
ShieldsOn_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("6"), False))
        
@button.button(hotas.BUT_ShipLights)
def onThrottleBtn_BUT_ShipLights(event, vjoy):
    if event.is_pressed:
        gremlin.macro.MacroManager().queue_macro(ShipLights_macro)
    else:
        gremlin.macro.MacroManager().queue_macro(ShipLights_macro)

# Create a macro that can be used repeatedly
ShipLights_macro = gremlin.macro.Macro()
ShipLights_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("3"), True))
ShipLights_macro.add_action(gremlin.macro.PauseAction(0.1))
ShipLights_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("3"), False))

##############################################################################
#IFCS Section

@button.button(hotas.BUT_DecoupleOff)
def onThrottleBtn_BUT_DecoupleOff(event, vjoy):
    if event.is_pressed:
        gremlin.macro.MacroManager().queue_macro(Decouple_macro)
    else:
        gremlin.macro.MacroManager().queue_macro(Decouple_macro)
        
# Create a macro that can be used repeatedly
Decouple_macro = gremlin.macro.Macro()
Decouple_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("V"), True))
Decouple_macro.add_action(gremlin.macro.PauseAction(0.1))
Decouple_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("V"), False))


@button.button(hotas.BUT_ComstabOff)
def onThrottleBtn_BUT_ComstabOff(event, vjoy):
    if event.is_pressed:
        gremlin.macro.MacroManager().queue_macro(IFCSToggle_macro)
    else:
        gremlin.macro.MacroManager().queue_macro(IFCSToggle_macro)
        
# Create a macro that can be used repeatedly
IFCSToggle_macro = gremlin.macro.Macro()
IFCSToggle_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("2"), True))
IFCSToggle_macro.add_action(gremlin.macro.PauseAction(0.1))
IFCSToggle_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("2"), False))


@throttle.button(hotas.SWITCH_AutopilotUp)
def onThrottleBtn_AutopilotUp(event, joy, vjoy):
    global WheelsDown
    if WheelsDown == True:
        if event.is_pressed:
            gremlin.macro.MacroManager().queue_macro(AutoLand_macro)
    
        
# Create a macro that can be used repeatedly
AutoLand_macro = gremlin.macro.Macro()
AutoLand_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("N"), True))
AutoLand_macro.add_action(gremlin.macro.PauseAction(3))
AutoLand_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("N"), False))

'''
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
'''
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
        gremlin.macro.MacroManager().queue_macro(ScanMode_macro)
    else:
        gremlin.macro.MacroManager().queue_macro(ScanMode_macro)
        
# Create a macro that can be used repeatedly
ScanMode_macro = gremlin.macro.Macro()
ScanMode_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("tab"), True))
ScanMode_macro.add_action(gremlin.macro.PauseAction(0.1))
ScanMode_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("tab"), False))
     
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
                   
@button.button(hotas.BUT_ESPToggle)
def onThrottleBtn_BUT_ESPToggle(event, vjoy):
    global ScanMode
    if event.is_pressed:
        ScanMode = True
        gremlin.macro.MacroManager().queue_macro(ESPToggle_macro)
    else:
        gremlin.macro.MacroManager().queue_macro(ESPToggle_macro)
        
# Create a macro that can be used repeatedly
ESPToggle_macro = gremlin.macro.Macro()

ESPToggle_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("leftalt"), True))
ESPToggle_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("O"), True))
ESPToggle_macro.add_action(gremlin.macro.PauseAction(0.1))
ESPToggle_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("leftalt"), False))
ESPToggle_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("O"), False))


##############################################################################
#Exterior Section

@button.button(hotas.BUT_LandGear)
def onThrottleBtn_BUT_LandGear(event, vjoy):
    global WheelsDown
    if event.is_pressed:
        gremlin.macro.MacroManager().queue_macro(LandGear_macro)
        WheelsDown = True
    else:
        gremlin.macro.MacroManager().queue_macro(LandGear_macro)
        WheelsDown = False
        
# Create a macro that can be used repeatedly
LandGear_macro = gremlin.macro.Macro()
LandGear_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("N"), True))
LandGear_macro.add_action(gremlin.macro.PauseAction(0.1))
LandGear_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("N"), False))

@button.button(hotas.BUT_ShipLock)
def onThrottleBtn_BUT_ShipLock(event, vjoy):
    if event.is_pressed:
        gremlin.macro.MacroManager().queue_macro(ShipLock_macro)
    else:
        gremlin.macro.MacroManager().queue_macro(ShipLock_macro)
        
# Create a macro that can be used repeatedly
ShipLock_macro = gremlin.macro.Macro()
ShipLock_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("0"), True))
ShipLock_macro.add_action(gremlin.macro.PauseAction(0.1))
ShipLock_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("0"), False))

@button.button(hotas.BUT_ShipDoors)
def onThrottleBtn_BUT_ShipDoors(event, vjoy):
    if event.is_pressed:
        gremlin.macro.MacroManager().queue_macro(ShipDoors_macro)
    else:
        gremlin.macro.MacroManager().queue_macro(ShipDoors_macro)
        
# Create a macro that can be used repeatedly
ShipDoors_macro = gremlin.macro.Macro()
ShipDoors_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("9"), True))
ShipDoors_macro.add_action(gremlin.macro.PauseAction(0.1))
ShipDoors_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("9"), False))

##############################################################################
#Self Destruct Section
# Arm switch with destruct button that issues default keyboard input to save vJoy keys

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
        if event.is_pressed:
            gremlin.macro.MacroManager().queue_macro(destruct_macro)
        
# Create a macro that can be used repeatedly
destruct_macro = gremlin.macro.Macro()
destruct_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("leftalt"), True))
destruct_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("backspace"), True))
destruct_macro.add_action(gremlin.macro.PauseAction(0.1))
destruct_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("leftalt"), False))
destruct_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("backspace"), False))



##############################
#Macro testing
 
