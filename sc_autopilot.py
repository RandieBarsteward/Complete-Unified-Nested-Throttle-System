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

#Function to turn switch to a toggle.  Action issues on both switch on AND switch off, releasing after a short interval 


#Function to turn switch to a toggle.  Action issues on both switch on AND switch off, releasing after a short interval
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
       


