import wpilib

DRIVERCONTROLLERPORT = 0

FRONTLEFT = 0
BACKLEFT = 1
FRONTRIGHT = 2
BACKRIGHT = 3

ARMBASEPORT = 4
ARMMIDPORT = 5
ARMTOPPORT = 6
ARMGRABBERPORT = 7
ARMGRABBERWRISTPORT = 8 

# Arm Gear Ratios

BASERATIO = 48 * (74/18)
MIDDLERATIO = 48 * (50/18)
TOPRATIO = 48
GRABBERRATIO = 12
WRISTRATIO = 4

TIMEOUTMS = 10

CRUISEVELOCITY = 15000
CRUISEACCEL = 6000

# Motion Magic PIDF
MMP = 0.375
MMI = 0.0
MMD = 0.0
MMF = 0.0

DEADBAND = 0.15

# Normal P Control for Charge Station
P = 0.0125
I = 0.0
D = 0.0

ARMBASEP = 0
ARMBASED = 0
ARMBASEF = 0.225

ARMMIDP = 0
ARMMIDD = 0
ARMMIDF = 0.279

ARMTOPP = 0
ARMTOPD = 0
ARMTOPF = 0.197

ARMGRABBERP = 0.29
ARMGRABBERD = 0
ARMGRABBERF = 0.286

ARMWRISTP = 0
ARMWRISTD = 0
ARMWRISTF = 0

# Cruising Velocities
ARMBASECRUISEVEL = 10
ARMMIDCRUISEVEL = 10
ARMTOPCRUISEVEL = 10
ARMGRABBERCRUISEVEL = 750
ARMWRISTCRUISEVEL = 10


# Motion Acceleration
ARMBASEACCEL = 100
ARMMIDACCEL = 100
ARMTOPACCEL = 100
ARMGRABBERACCEL = 750
ARMWRISTACCEL = 100

# Solenoid on Grabber

SOLENOIDMODULE = 0
SOLENOIDMODULETYPE = wpilib.PneumaticsModuleType.CTREPCM
GRABBERSOLENOIDIN = 0
GRABBERSOLENOIDOUT = 1