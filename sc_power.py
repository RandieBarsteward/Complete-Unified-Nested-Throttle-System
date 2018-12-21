"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                
              (Joystick Gremlin Profile/Scripts for Star Citizen)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

import gremlin
import hotas
import scmap

joystick = gremlin.input_devices.JoystickDecorator(hotas.JOY_Name,
                                                   hotas.JOY_Id,
                                                   "Default")

@joystick.button(hotas.JOYBTN_ResetPowerDistribution)
def onJoystickBtn_ResetPowerDistribution(event, vjoy, joy):
    vjoy[15].button(scmap.PowerResetDistribution).is_pressed = event.is_pressed

@joystick.button(hotas.JOYBTN_IncPower1)
def onJoystickBtn_IncPower1(event, vjoy):
    vjoy[15].button(scmap.PowerPresetInc1).is_pressed = event.is_pressed

@joystick.button(hotas.JOYBTN_IncPower2)
def onJoystickBtn_IncPower2(event, vjoy):
    vjoy[15].button(scmap.PowerPresetInc2).is_pressed = event.is_pressed

@joystick.button(hotas.JOYBTN_IncPower3)
def onJoystickBtn_IncPower3(event, vjoy):
    vjoy[15].button(scmap.PowerPresetInc3).is_pressed = event.is_pressed
