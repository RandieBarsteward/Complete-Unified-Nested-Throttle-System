"""''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''  
              (Joystick Gremlin Profile/Scripts for Star Citizen)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

                          ###########################
                          # HOTAS PHYSICAL MAPPINGS #
                          ###########################

# The following variables are initialized to the physical axes and buttons on
# the HOTAS. The included scripts' logic utilize these values to know what
# inputs to "listen" for to do particular actions and maneuvers.

USING_RUDDER_PEDALS = True
RUDDER_PEDALS_INVERT = -1.0 # must be -1.0 or 1.0 (negative for invert)
##############################################################################
# Rudder Pedals Information
RUD_Name = "Saitek Pro Flight Combat Rudder Pedals"
RUD_Id = 111347556

# Set the following actions to the physical axes on your rudder (sc_throttle.py)
RUDAXIS_Reverse = 1  # Z Axis                   L PEDAL(sc_throttle.py)
RUDAXIS_Boost = 2    # WORKING   vJoy 8        R PEDAL(sc_throttle.py)
RUDAXIS_Roll = 3     # Rz Axis                  PIVOT     (sc_throttle.py)
RUDAXISBTN_Threshold = -0.5         # Less than = no press

##############################################################################
# Joystick Information
JOY_Name = "Joystick - HOTAS Warthog"
JOY_Id = 72287234

# Set desired offset rotation amount in degrees. This is useful for those who
# have a centered joystick that are mounted in this way for ergonomic reasons
JOY_Rotation = 85

# Set the following actions to the physical axes on the joystick
JOYAXIS_Yaw = 1
JOYAXIS_Pitch = 2

# Set the following actions to the physical buttons on the joystick
# Trigger
JOYBTN_FireWep = 1                     # ##WORKING  vJoy 1 / 2 ##   TG1 (Trigger stage 1) (sc_gunnery.py)
JOYBTN_FocusFireZoom = 6               # DISABLED TG2 (Trigger stage 2) (sc_gunnery.py)

#Weapon Release Button
JOYBTN_Missiles = 2                    # ##WORKING   vJoy 4   ##   S2 (red button) (sc_gunnery.py)

#Stick Pinky Button (sc_gunnery.py)
JOYBTN_CycleWepGrp = 3                 # ##WORKING   vJoy 46   ##S3 (pinky button)(sc_gunnery.py)

#Master Mode Control Button / Index Right
JOYBTN_CycleWeaponAmmo = 5             # ##WORKING vJoy 6 ##   S1 (index finger button) (sc_gunnery.py)

# (optional mod-lever held) (sc_scanning.py)/(sc_shields.py)
SWITCH_JoystickAltMod = 4              # ##WORKING No vJoy binding needed ##S4 (mod-lever in back) (sc_scanning.py)/(sc_shields.py)

#Target Managment Switch (sc_shields.py)
JOYBTN_ShieldFront_Top = 7             # ##WORKING vJoy 26 / 30 (alt handle)    H2U (sc_shields.py)
JOYBTN_ShieldBack_Bottom = 9           # ##WORKING vJoy 27 / 31 (alt handle)    H2D (sc_shields.py)
JOYBTN_ShieldLeft = 10                 # ##WORKING vJoy 28                      H2R (sc_shields.py)
JOYBTN_ShieldRight = 8                 # ##WORKING vJoy 29                      H2L (sc_shields.py)

#Data Management Switch (sc_power.py)
JOYBTN_ResetPowerDistribution = 11     # ##WORKING vJoy 32 ##                    H3U (sc_power.py)
JOYBTN_IncPower1 = 14                  # ##WORKING vJoy 33 ##                    H3L (sc_power.py)
JOYBTN_IncPower2 = 12                  # ##WORKING vJoy 34 ##                    H3R (sc_power.py)
JOYBTN_IncPower3 = 13                  # ##WORKING vJoy 35 ##                    H3D (sc_power.py)

#Countermeasures Management Switch (sc_scanning.py)
JOYBTN_TgtReticle_CycleAll = 15        # ##WORKING vJoy 16 / 17 (alt handle)     H4U (sc_scanning.py)
JOYBTN_TgtNearestEnemy_CycleAllBck = 17# ##WORKING vJoy 25 / 18 (alt handle)     H4D (sc_scanning.py)
JOYBTN_TgtEnemyFwd_FriendlyFwd = 16    # ##WORKING vJoy 23 / 19 (alt handle)     H4R (sc_scanning.py)
JOYBTN_TgtEnemyBck_FriendlyBck = 18    # ##WORKING vJoy 24 / 20 (alt handle)     H4L (sc_scanning.py)
JOYBTN_TgtCyclePin_SetPin = 19         # ##WORKING vJoy 22 / 21 (alt handle)     H4P (sc_scanning.py)

JOYHAT_Zoom = 1  #(sc_gunnery.py)

##############################################################################
# Throttle Information
THR_Name = "Throttle - HOTAS Warthog"
THR_Id = 72287236

THRAXIS_ThrottleAbs = 4                # Right throttle (sc_throttle.py)
THRAXIS_StrafeThrustAmt = 5            # An unused slider is a good choice. (sc_throttle.py)
THRAXIS_ThrusterPower = 128
# Set the following actions to the physical switches on the throttle. Switches
# are buttons in the virtual sense, but the logic that uses them assumes they
# can easily be held down indefinitely


#FUEL NORM SWITCHES
SWITCH_CycleFire = 17                  # ##WORKING No vJoy binding needed ##  EFRNORM (Right Fuel Norm Switch)
#SWITCH_XXX = 16                       # EFRNORM (Left Fuel Norm Switch)

#ENGINE OPERATE SWITCHES
#THRBTN_ShieldRaise = 31               #ENGINE OPERATE LEFT FORWARD (MOMENT)
#SWITCH_XXX = 18                       #ENGINE OPERATE LEFT BACK (SWITCH)
#SWITCH_XXX = 32                       #ENGINE OPERATE RIGHT FORWARD (MOMENT)
#SWITCH_XXX = 19                       #ENGINE OPERATE LEFT BACK (SWITCH)

#FLAPS (sc_throttle.py)
SWITCH_FlapsUp = 22                    # ##WORKING vJoy 10          FLAPU (flaps up Quantum) (sc_throttle.py)
SWITCH_FlapsDown = 23                  # ##WORKING No vJoy          FLAPD (flaps down Precision Thrusters) (sc_throttle.py)

#ENGINE IDLE
SWITCH_EngineOff = 29                 # ##WORKING vJoy 45           Engine Idle R (sc_throttle.py)
#SWITCH_EngineOff = 30                # 

#APU ON (sc_cockpit.py)
SWITCH_Power = 20                      # ##WORKING vJoy 44          APU ON (SWITCH)(sc_cockpit.py)

#THROTTLE FRICTION
#JOYAXIS_FRICTION =                    # THROTTLE FRICTION SLIDER

#L/G WRN SILENCE (sc_throttle.py)
THRBTN_LandingGear = 21                # ##WORKING vJoy 9           LDGH (Landing Gear button) (sc_throttle.py)

#EAC ON/OFF
SWITCH_PowerOn = 24                     # ##WORKING vJoy 38           EAC ON/OFF (SWITCH) (sc_throttle.py)
#SWITCH_FlightSystemsReady = 24         # ##WORKING vJoy 38           EAC ON/OFF (SWITCH) (sc_throttle.py)

#RDR ALTM
SWITCH_ShieldsOn = 25                   # ##WORKING vJoy 37           RDR ALTM (SWITCH) (sc_throttle.py)

#AUTOPILOT (sc_autopilot.py)
THRBTN_AutopilotEngage = 26            # ##WORKING vJoy 12 / 11 (APALT DOWN)             APENG (Autopilot engage) (sc_autopilot.py)
SWITCH_AutopilotUp = 27              #                                                APALT (Autopilot switch in "PATH") (sc_autopilot.py)
SWITCH_AutopilotDown = 28               # ##WORKING No vJoy                               APALT (Autopilot switch in "ALT") (sc_autopilot.py)

####################
####################
####################
# Set the following actions to the physical buttons on the throttle
#THROTTLE PINKY  ###CHANGE THIS. WASTE OF KEYS###
SWITCH_ModeOnFoot = 13                 # PSF (Pinky switch forward)
SWITCH_ModeVehicle = 14                # PSB (Pinky switch backward)

#THROTTLE RIGHT THUMB SWITCH (sc_throttle.py)
THRBTN_StrafeUp = 3                    # Y Axis                     MSU (thumb hat up) (sc_throttle.py)
THRBTN_StrafeDown = 5                  # Y Axis                     MSD (thumb hat down) (sc_throttle.py)
THRBTN_StrafeRight = 4                 # X Axis                     MSR (thumb hat right) (sc_throttle.py)
THRBTN_StrafeLeft = 6                  # X Axis                     MSL (thumb hat left) (sc_throttle.py)
THRBTN_ResetZoom = 2                   # ##NO vJoy BINDING          MSP (thumb hat press) (sc_throttle.py)

#RED THUMB SWITCH / CHINA HAT (sc_gunnery.py)
THRBTN_CycleCounterMeasure = 11        # ##WORKING vJoy 5          CHF (red two way forward) (sc_gunnery.py)
THRBTN_LaunchCounterMeasures = 12      # ##WORKING vJoy 3          CHB (red two way backward) (sc_gunnery.py)

#SPEED BRAKE
THRBTN_Afterburner = 7                 # ##WORKING vJoy 13         SPDF (Fat two way forward) (locks) (sc_throttle.py)
THRBTN_LookBehind = 8                  # ##WORKING vJoy 14         SPDB (Fat two way backward) (sc_camera.py)

#LEFT THROTTLE BUTTON (RED) (sc_throttle.py)
THRBTN_MatchTarget = 15                # ##WORKING vJoy 48                    LTB (red pinky button) (sc_throttle.py)


#RIGHT BOAT SWITCH
THRBTN_DecoupledModeToggle = 10        # ##WORKING vJoy 15          BOAT (Boat back) (sc_throttle.py)



#THRBTN_IncreaseCoolerRate
#THRBTN_DecreaseCoolerRate
#
#THRBTN_OpenAllDoors
#THRBTN_CloseAllDoors
#THRBTN_LockAllDoors
#THRBTN_UnlockAllDoors

THRHAT_StrafeUpDown = 1                # HAT 1 (up/down) (sc_throttle.py)
THRHAT_Roll = 1                        # HAT 1 (left/right) (sc_throttle.py)


##############################################################################
# Button Box Information
BUT_Name = "BU0836X Interface"
BUT_Id = 500305921

BUT_Key = 1
BUT_PowerOn = 2
BUT_EngineOn = 3
BUT_ShieldsOn = 4
BUT_ShipLights = 5
BUT_IFCS = 6
BUT_AutoLand = 7
BUT_VTOL = 8
BUT_ModeStealth = 9
BUT_ModeCombat = 10
BUT_ModePrecision = 11
BUT_ScanModeToggle = 12
BUT_Scan = 13
BUT_GunArm = 14
BUT_MissileArm = 15
BUT_ESPToggle = 16
BUT_LandGear = 17
BUT_ShipLock = 18
BUT_ShipDoors = 19
BUT_DestructArm = 20
BUT_SelfDestruct = 21

BUT_WpnGroupThreeSafe = 22
BUT_WpnGroupFourSafe = 23
BUT_LandGear = 24
BUT_ShipLock = 25
BUT_ShipDoors = 26
BUT_DestructArm = 27
BUT_SelfDestruct = 28
BUT_Pedal = 29
BUT_HeadTrack = 30






