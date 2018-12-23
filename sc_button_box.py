"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                
              (Joystick Gremlin Profile/Scripts for Star Citizen)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import hotas
import scmap
import time

button = gremlin.input_devices.JoystickDecorator(hotas.BUT_Name,
                                                   hotas.BUT_Id,
                                                   "Default")

                                                   
@button.button(hotas.BUT_Test)
def onThrottleBtn_BUT_Test(event, vjoy):
    vjoy[1].button(scmap.ButtonTest).is_pressed = event.is_pressed
