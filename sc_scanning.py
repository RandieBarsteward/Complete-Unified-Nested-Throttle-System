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

#Controls Joystick Alt switch and prevents duplicate input of controls
@joystick.button(hotas.SWITCH_JoystickAltMod)
def onJoystickSwitch_AltModScanning(event, vjoy):
    vjoy[1].button(scmap.TgtReticle).is_pressed = False
    vjoy[1].button(scmap.TgtCycleAll).is_pressed = False
    vjoy[1].button(scmap.TgtCyclePinned).is_pressed = False
    vjoy[1].button(scmap.TgtSetPin).is_pressed = False
    vjoy[1].button(scmap.TgtNearestHostile).is_pressed = False
    vjoy[1].button(scmap.TgtCycleAllBack).is_pressed = False
    vjoy[1].button(scmap.TgtCycleHostile).is_pressed = False
    vjoy[1].button(scmap.TgtCycleFriendly).is_pressed = False
    vjoy[1].button(scmap.TgtCycleHostileBck).is_pressed = False
    vjoy[1].button(scmap.TgtCycleFriendlyBck).is_pressed = False

@joystick.button(hotas.JOYBTN_TgtReticle_CycleAll)
def onJoystickBtn_TgtReticle_CycleAll(event, vjoy, joy):
    if not joy[hotas.JOY_Name].button(hotas.SWITCH_JoystickAltMod).is_pressed:
        vjoy[1].button(scmap.TgtReticle).is_pressed = event.is_pressed
    else:
        vjoy[1].button(scmap.TgtCycleAll).is_pressed = event.is_pressed

@joystick.button(hotas.JOYBTN_TgtCyclePin_SetPin)
def onJoystickBtn_TgtCyclePin_SetPin(event, vjoy, joy):
    if not joy[hotas.JOY_Name].button(hotas.SWITCH_JoystickAltMod).is_pressed:
        vjoy[1].button(scmap.TgtCyclePinned).is_pressed = event.is_pressed
    else:
        vjoy[1].button(scmap.TgtSetPin).is_pressed = event.is_pressed

@joystick.button(hotas.JOYBTN_TgtNearestEnemy_CycleAllBck)
def onJoystickBtn_TgtNearestEnemy_CycleAllBck(event, vjoy, joy):
    if not joy[hotas.JOY_Name].button(hotas.SWITCH_JoystickAltMod).is_pressed:
        vjoy[1].button(scmap.TgtNearestHostile).is_pressed = event.is_pressed
    else:
        vjoy[1].button(scmap.TgtCycleAllBack).is_pressed = event.is_pressed

@joystick.button(hotas.JOYBTN_TgtEnemyFwd_FriendlyFwd)
def onJoystickBtn_TgtEnemyFwd_FriendlyFwd(event, vjoy, joy):
    if not joy[hotas.JOY_Name].button(hotas.SWITCH_JoystickAltMod).is_pressed:
        vjoy[1].button(scmap.TgtCycleHostile).is_pressed = event.is_pressed
    else:
        vjoy[1].button(scmap.TgtCycleFriendly).is_pressed = event.is_pressed

@joystick.button(hotas.JOYBTN_TgtEnemyBck_FriendlyBck)
def onJoystickBtn_TgtEnemyBck_FriendlyBck(event, vjoy, joy):
    if not joy[hotas.JOY_Name].button(hotas.SWITCH_JoystickAltMod).is_pressed:
        vjoy[1].button(scmap.TgtCycleHostileBck).is_pressed = event.is_pressed
    else:
        vjoy[1].button(scmap.TgtCycleFriendlyBck).is_pressed= event.is_pressed
