"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                              
              (Joystick Gremlin Profile/Scripts for Star Citizen)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import hotas
import scmap

joystick = gremlin.input_devices.JoystickDecorator(hotas.JOY_Name,
                                                   hotas.JOY_Id,
                                                   "Default")

@joystick.button(hotas.SWITCH_JoystickAltMod)
def onJoystickSwitch_AltModShields(event, vjoy, joy):
    if joy[hotas.JOY_Name].button(hotas.JOYBTN_ShieldFront_Top).is_pressed:
        if event.is_pressed:
            vjoy[15].button(scmap.ShieldFront).is_pressed = False
            vjoy[15].button(scmap.ShieldTop).is_pressed = True
        else:
            vjoy[15].button(scmap.ShieldFront).is_pressed = True
            vjoy[15].button(scmap.ShieldTop).is_pressed = False
    if joy[hotas.JOY_Name].button(hotas.JOYBTN_ShieldBack_Bottom).is_pressed:
        if event.is_pressed:
            vjoy[15].button(scmap.ShieldBack).is_pressed = False
            vjoy[15].button(scmap.ShieldBottom).is_pressed = True
        else:
            vjoy[15].button(scmap.ShieldBack).is_pressed = True
            vjoy[15].button(scmap.ShieldBottom).is_pressed = False

@joystick.button(hotas.JOYBTN_ShieldFront_Top)
def onJoystickBtn_ShieldFront_Top(event, vjoy, joy):
    if event.is_pressed:
        if joy[hotas.JOY_Name].button(hotas.SWITCH_JoystickAltMod).is_pressed:
            vjoy[15].button(scmap.ShieldFront).is_pressed = False
            vjoy[15].button(scmap.ShieldTop).is_pressed = True
        else:
            vjoy[15].button(scmap.ShieldFront).is_pressed = True
            vjoy[15].button(scmap.ShieldTop).is_pressed = False
    else:
        vjoy[15].button(scmap.ShieldFront).is_pressed = False
        vjoy[15].button(scmap.ShieldTop).is_pressed = False

@joystick.button(hotas.JOYBTN_ShieldBack_Bottom)
def onJoystickBtn_ShieldBack_Bottom(event, vjoy, joy):
    if event.is_pressed:
        if joy[hotas.JOY_Name].button(hotas.SWITCH_JoystickAltMod).is_pressed:
            vjoy[15].button(scmap.ShieldBack).is_pressed = False
            vjoy[15].button(scmap.ShieldBottom).is_pressed = True
        else:
            vjoy[15].button(scmap.ShieldBack).is_pressed = True
            vjoy[15].button(scmap.ShieldBottom).is_pressed = False
    else:
        vjoy[15].button(scmap.ShieldBack).is_pressed = False
        vjoy[15].button(scmap.ShieldBottom).is_pressed = False

@joystick.button(hotas.JOYBTN_ShieldLeft)
def onJoystickBtn_ShieldLeft(event, vjoy):
    vjoy[15].button(scmap.ShieldLeft).is_pressed = event.is_pressed

@joystick.button(hotas.JOYBTN_ShieldRight)
def onJoystickBtn_ShieldRight(event, vjoy):
    vjoy[15].button(scmap.ShieldRight).is_pressed = event.is_pressed
