"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                              
              (Joystick Gremlin Profile/Scripts for Star Citizen)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import hotas
import scmap

joystick = gremlin.input_devices.JoystickDecorator(hotas.JOY_Name,
                                                   hotas.JOY_Id,
                                                   "Default")

throttle = gremlin.input_devices.JoystickDecorator(hotas.THR_Name,
                                                   hotas.THR_Id,
                                                   "Default")

isAlphaFire = False
curWepGrp = 1

def setWeapons(vjoy, joy):
    global curWepGrp
    if joy[hotas.JOY_Name].button(hotas.JOYBTN_FireWep).is_pressed:
        if isAlphaFire == False and joy[hotas.THR_Name].button(hotas.SWITCH_CycleFire).is_pressed:
            if curWepGrp == 1:
                vjoy[1].button(scmap.FireWeaponGroup1).is_pressed = True
                vjoy[1].button(scmap.FireWeaponGroup2).is_pressed = False
            else:
                vjoy[1].button(scmap.FireWeaponGroup1).is_pressed = False
                vjoy[1].button(scmap.FireWeaponGroup2).is_pressed = True
        else:
            vjoy[1].button(scmap.FireWeaponGroup1).is_pressed = True
            vjoy[1].button(scmap.FireWeaponGroup2).is_pressed = True
    else:
        vjoy[1].button(scmap.FireWeaponGroup1).is_pressed = False
        vjoy[1].button(scmap.FireWeaponGroup2).is_pressed = False

@joystick.button(hotas.JOYBTN_FireWep)
def onJoystickBtn_FireWeapons(event, vjoy, joy):
    setWeapons(vjoy, joy)

@joystick.button(hotas.JOYBTN_CycleWepGrp)
def onJoystickBtn_CycleWeaponGroup(event, vjoy, joy):
    vjoy[1].button(scmap.CycleWeaponGroup).is_pressed = event.is_pressed
    
#@joystick.button(hotas.JOYBTN_CycleWepGrp)
#def onJoystickBtn_CycleWeaponGroup(event, vjoy, joy):
#    global isAlphaFire
#    global curWepGrp
#    if event.is_pressed:
#        isAlphaFire = True
#    else:
#        isAlphaFire = False
#        curWepGrp = 2 if (curWepGrp == 1) else 1
#    setWeapons(vjoy, joy)
    
@joystick.hat(hotas.JOYHAT_Zoom) #allows all direction on HAT 1
def onJoystickHat_Zoom(event, vjoy, joy):
    vjoy[1].hat(1).direction = (event.value)

#@joystick.hat(hotas.JOYHAT_Zoom) # Only UP DOWN on HAT 1
#def onJoystickHat_Zoom(event, vjoy, joy):
#    vjoy[1].hat(1).direction = (0, event.value[1])

# WAITING FOR DYNAMIC ZOOM SUPPORT IN GAME (CURRENTLY BROKEN IN 3.0.1)
#@joystick.button(hotas.JOYBTN_FocusFireZoom)
#def onJoystickBtn_FocusFireZoom
#    if event.is_pressed:

@throttle.button(hotas.SWITCH_CycleFire)
def onThrottleSwitch_AlphaFireWeaponGroups(event, vjoy, joy):
    setWeapons(vjoy, joy)

@joystick.button(hotas.JOYBTN_CycleWeaponAmmo)
def onJoystickBtn_CycleWeaponAmmo(event, vjoy):
    vjoy[1].button(scmap.CycleWeaponAmmo).is_pressed = event.is_pressed

@joystick.button(hotas.JOYBTN_Missiles)
def onJoystickBtn_LockOrFireMissiles(event, vjoy):
    vjoy[1].button(scmap.LockFireMissiles).is_pressed = event.is_pressed

@throttle.button(hotas.THRBTN_LaunchCounterMeasures)
def onThrottleBtn_LaunchCounterMeasures(event, vjoy):
    vjoy[1].button(scmap.CounterMeasures).is_pressed = event.is_pressed

@throttle.button(hotas.THRBTN_CycleCounterMeasure)
def onThrottleBtn_CycleCounterMeasures(event, vjoy):
    vjoy[1].button(scmap.CycleCounterMeasures).is_pressed = event.is_pressed
