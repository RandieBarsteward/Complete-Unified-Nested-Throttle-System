"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                
              (Joystick Gremlin Profile/Scripts for Star Citizen)

Moduel intended to integrate a custom button box/controller into Joystick Gremlin.  

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import hotas
import scmap
import time
import math



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
GunArmed = False
MissileArmed = False
ShieldOn = True




@button.button(hotas.BUT_Key)
def onThrottleBtn_BUT_Key(event, vjoy):
    global PowerKey
    global PowerState
    global ShieldOn
    if event.is_pressed:
        PowerKey = True
    elif event.is_pressed == False and PowerState == False:
        PowerKey = False
    elif event.is_pressed == False:
        PowerKey = False
        PowerState = False
        gremlin.macro.MacroManager().queue_macro(PowerOff_macro)


@button.button(hotas.BUT_PowerOn)
def onThrottleBtn_BUT_PowerOn(event, vjoy):
    global PowerKey
    global PowerState
    global ShieldOn
    if event.is_pressed and PowerKey == True and PowerState == False:
        PowerState = True
        ShieldOn = False
        gremlin.macro.MacroManager().queue_macro(PowerOn_macro)


# Create a macro that can be used repeatedly
PowerOn_macro = gremlin.macro.Macro()
PowerOn_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("5"), True)) #Turn on power
PowerOn_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("6"), True)) #Turn off shield
PowerOn_macro.add_action(gremlin.macro.PauseAction(0.1))
PowerOn_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("5"), False))
PowerOn_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("6"), False))

PowerOff_macro = gremlin.macro.Macro()
PowerOff_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("5"), True)) #Turn off power.  Double press 5 because of toggle issue with shields where if shields are down 5 toggles shield instead of Power Off
PowerOff_macro.add_action(gremlin.macro.PauseAction(0.1))
PowerOff_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("5"), False))
PowerOff_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("5"), True)) 
PowerOff_macro.add_action(gremlin.macro.PauseAction(0.1))
PowerOff_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("5"), False))

PowerAndShieldOff_macro = gremlin.macro.Macro()
PowerAndShieldOff_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("6"), True)) #Turn off shield
PowerAndShieldOff_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("5"), True)) #Turn off power
PowerAndShieldOff_macro.add_action(gremlin.macro.PauseAction(0.1))
PowerAndShieldOff_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("6"), False))
PowerAndShieldOff_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("5"), False))

@button.button(hotas.BUT_EngineOn)
def onThrottleBtn_BUT_EngineOn(event, vjoy):
    global PowerKey
    global PowerState
    if event.is_pressed and PowerKey == True and PowerState == True:
        gremlin.macro.MacroManager().queue_macro(EngineOn_macro)
        PowerState = True
    if event.is_pressed == False and PowerKey == True and PowerState == True:
        gremlin.macro.MacroManager().queue_macro(EngineOn_macro)
        PowerState = False        

# Create a macro that can be used repeatedly
EngineOn_macro = gremlin.macro.Macro()
EngineOn_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("4"), True))
EngineOn_macro.add_action(gremlin.macro.PauseAction(0.1))
EngineOn_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("4"), False))

@button.button(hotas.BUT_ShieldsOn)
def onThrottleBtn_BUT_ShieldsOn(event, vjoy):
    global PowerKey
    global PowerState
    global ShieldOn
    if event.is_pressed and PowerKey == True and PowerState == True:
        gremlin.macro.MacroManager().queue_macro(ShieldsOn_macro)
        ShieldOn = True        
    if event.is_pressed == False and PowerKey == True and PowerState == True:
        gremlin.macro.MacroManager().queue_macro(ShieldsOn_macro)
        ShieldOn = False
        
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

@button.button(hotas.BUT_IFCS)
def onThrottleBtn_BUT_IFCS(event, vjoy):
    if event.is_pressed:
        gremlin.macro.MacroManager().queue_macro(IFCS_macro)
    #else:
        #gremlin.macro.MacroManager().queue_macro(Decouple_macro)
        
# Create a macro that can be used repeatedly
IFCS_macro = gremlin.macro.Macro()
IFCS_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("2"), True))
IFCS_macro.add_action(gremlin.macro.PauseAction(0.1))
IFCS_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("2"), False))


@button.button(hotas.BUT_AutoLand)
def onThrottleBtn_BUT_AutoLand(event, vjoy):
    if event.is_pressed:
        gremlin.macro.MacroManager().queue_macro(AutoLand_macro)
        
        
# Create a macro that can be used repeatedly
AutoLand_macro = gremlin.macro.Macro()
AutoLand_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("N"), True))
AutoLand_macro.add_action(gremlin.macro.PauseAction(3))
AutoLand_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("N"), False))


@button.button(hotas.BUT_VTOL)
def onThrottleBtn_BUT_VTOL(event, vjoy):
    if event.is_pressed:
        gremlin.macro.MacroManager().queue_macro(VTOL_macro)
    else:
        gremlin.macro.MacroManager().queue_macro(VTOL_macro)

# Create a macro that can be used repeatedly
VTOL_macro = gremlin.macro.Macro()
VTOL_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("3"), True))
VTOL_macro.add_action(gremlin.macro.PauseAction(0.1))
VTOL_macro.add_action(gremlin.macro.KeyAction(gremlin.macro.key_from_name("3"), False))

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
#Weapons Section
'''
@button.button(hotas.BUT_GunArm)
def onThrottleBtn_BUT_GunArm(event, vjoy):
    global GunArmed
    if event.is_pressed:
        GunArmed == True
    else:
        GunArmed == False

@button.button(hotas.BUT_MissileArm)
def onThrottleBtn_BUT_MissileArm(event, vjoy):
    global MissileArmed
    if event.is_pressed:
        MissileArmed == True
    else:
        MissileArmed == False
'''                 
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
 
