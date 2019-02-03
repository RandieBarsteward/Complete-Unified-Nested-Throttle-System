"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
                                 
              (Joystick Gremlin Profile/Scripts for Star Citizen)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import gremlin
import math
import hotas
import scmap



joystick = gremlin.input_devices.JoystickDecorator(hotas.JOY_Name,
                                                   hotas.JOY_Id,
                                                   "Default")

radians = math.radians(hotas.JOY_Rotation)
cosX = math.cos(radians)
sinX = math.sin(radians)
cosY = math.cos(radians)
sinY = -math.sin(radians)

actualX = 0
actualY = 0

# Thank you to @WhiteMagic for figuring out the required math formulas
def setAxes(vjoy):
    global actualX
    global actualY
    def maxVectorLength(angle):
        angle = abs(angle)
        if 0 <= angle < math.pi/4:
            return math.sqrt(1 + math.tan(angle)**2)
        elif math.pi/4 <= angle < 0.75*math.pi:
            return math.sqrt(1 + (1.0/math.tan(angle)) ** 2)
        else:
            return math.sqrt(1 + math.tan(angle) ** 2)
    # Obtain angles of the current input, physical as well as virtual
    physical_angle = math.atan2(actualY, actualX)
    virtual_angle = radians + physical_angle
    # Scale factor between virtual and physical vector
    scale = maxVectorLength(virtual_angle) / maxVectorLength(physical_angle)
    vjoy[1].axis(scmap.Yaw).value = (cosX*actualX + sinY*actualY) * scale
    vjoy[1].axis(scmap.Pitch).value = (sinX*actualX + cosY*actualY) * scale

@joystick.axis(hotas.JOYAXIS_Yaw)
def onJoystickAxis_X(event, vjoy):
    global actualX
    actualX = event.value
    setAxes(vjoy)

@joystick.axis(hotas.JOYAXIS_Pitch)
def onJoystickAxis_Y(event, vjoy):
    global actualY
    actualY = event.value
    setAxes(vjoy)

