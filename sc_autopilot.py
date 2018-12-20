"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 
              (Joystick Gremlin Profile/Scripts for Star Citizen)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import hotas
import scmap
import time

throttle = gremlin.input_devices.JoystickDecorator(hotas.THR_Name,
                                                   hotas.THR_Id,
                                                   "Default")


@throttle.button(hotas.SWITCH_AutopilotUp)
def onThrottleBtn_AutopilotUp(event, joy, vjoy):
    if event.is_pressed:
        vjoy[1].button(scmap.Autoland).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.Autoland).is_pressed = False
    else:
        vjoy[1].button(scmap.Autoland).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.Autoland).is_pressed = False

@throttle.button(hotas.SWITCH_AutopilotDown)
def onThrottleBtn_AutopilotDown(event, joy, vjoy):
    if event.is_pressed:
        vjoy[1].button(scmap.VTOL).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.VTOL).is_pressed = False
    else:
        vjoy[1].button(scmap.VTOL).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.VTOL).is_pressed = False

@throttle.button(hotas.THRBTN_AutopilotEngage)
def onThrottleBtn_AutopilotEngage(event, joy, vjoy):
    vjoy[1].button(scmap.LandingGear).is_pressed = event.is_pressed
       

        
'''
    if event.is_pressed:
            vjoy[1].button(scmap.Autoland).is_pressed = True
            time.sleep(.500)
            vjoy[1].button(scmap.Autoland).is_pressed = False
    else:
        vjoy[1].button(scmap.Autoland).is_pressed = True
        time.sleep(.500)
        vjoy[1].button(scmap.Autoland).is_pressed = False
  '''          



'''
def cancelAutopilot(vjoy):
    vjoy[1].button(scmap.Autoland).is_pressed = False
    vjoy[1].button(scmap.MatchVel).is_pressed = False

@throttle.button(hotas.THRBTN_AutopilotEngage) 
def onThrottleBtn_AutopilotEngage(event, vjoy, joy):
    if event.is_pressed:
        thr = joy[hotas.THR_Name]
        if not thr.button(hotas.SWITCH_AutopilotPath).is_pressed:
            if not thr.button(hotas.SWITCH_AutopilotAlt).is_pressed:
                vjoy[1].button(scmap.MatchVel).is_pressed = True
        if thr.button(hotas.SWITCH_AutopilotAlt).is_pressed:
            vjoy[1].button(scmap.Autoland).is_pressed = True
    else:
        vjoy[1].button(scmap.MatchVel).is_pressed = False
        vjoy[1].button(scmap.Autoland).is_pressed = False

@throttle.button(hotas.SWITCH_AutopilotPath)
def onThrottleSwitch_AutopilotPath(event, vjoy):
    cancelAutopilot(vjoy)

@throttle.button(hotas.SWITCH_AutopilotAlt)
def onThrottleSwitch_AutopilotAlt(event, vjoy):
    cancelAutopilot(vjoy)
'''
