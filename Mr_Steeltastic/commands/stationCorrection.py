import commands2
import wpilib
import ctre
from subsystems.drivetrain import Drivetrain
from subsystems.arm import Arm

class StationCorrection(commands2.CommandBase):

    def __init__(self, train: Drivetrain, arm: Arm):

        super().__init__()

        self.train = train
        self.arm = arm
        
        self.addRequirements([self.train, self.arm])

        self.startTime = wpilib.Timer.getFPGATimestamp()
        
        self.commandFinished = False

    def execute(self):

        if self.commandFinished:

            self.startTime = wpilib.Timer.getFPGATimestamp()
            self.commandFinished = False

        wpilib.SmartDashboard.putNumber("Angle", self.train.gyro.getAngle())

        if self.train.gyro.getAngle() <= 7.5 and not self.train.onChargeStation:

            self.train.arcadeDrive(-0.2, 0.0)

            wpilib.SmartDashboard.putString("Auto Status", "Driving to Station")

        else:

            self.train.onChargeStation = True
            
            power = (self.train.pidController.calculate(self.train.gyro.getAngle(), 0.0))

            wpilib.SmartDashboard.putNumber("Requested Power", power)
            wpilib.SmartDashboard.putString("Auto Status", "PID Control")

            if abs(power) <= 0.5:

                self.train.arcadeDrive(power, 0.0)

                wpilib.SmartDashboard.putBoolean("Power Accepted", True)

            else:

                wpilib.SmartDashboard.putBoolean("Power Accepted", False)
        
        self.arm.keepArmsAtZero()

        wpilib.SmartDashboard.putNumberArray("Time", [wpilib.Timer.getFPGATimestamp(), wpilib.Timer.getFPGATimestamp() - self.startTime])
        wpilib.SmartDashboard.putBoolean("Running", True)

        # wpilib.SmartDashboard.putNumberArray("Time", [self.startTime, wpilib.Timer.getFPGATimestamp(), wpilib.Timer.getFPGATimestamp - self.startTime])

    def end(self, interrupted: bool):
        
        self.train.arcadeDrive(0.0, 0.0)
        wpilib.SmartDashboard.putBoolean("Running", False)
        self.commandFinished = True
    
    def isFinished(self):
        
        return False