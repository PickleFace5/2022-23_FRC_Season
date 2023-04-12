import typing

import commands2
import wpilib
from subsystems.drivetrain import Drivetrain

class DriveByGuitar(commands2.CommandBase):
    """
    This allows us to drive the robot with a Wii Guitar Controller. Yep. This is what we're doing right now.
    """

    def __init__(self, drive: Drivetrain, left_axis: typing.Callable[[], float], right_axis: typing.Callable[[], float], test_button: typing.Callable[[], bool]) -> None:
        # def __init__(self, drive: Drivetrain, left_axis, right_axis) -> None:
        super().__init__()

        self.drive = drive
        self.left_axis = left_axis
        self.right_axis = right_axis
        self.test_button = test_button

        self.addRequirements([self.drive])

        


    def execute(self) -> None:
        self.drive.userDrive(self.left_axis(), self.right_axis(), 1)

        wpilib.SmartDashboard.putNumber('Joystick - ', self.left_axis())
        wpilib.SmartDashboard.putNumber('Slider - ', self.right_axis())
        wpilib.SmartDashboard.putNumber("Left Velocity - ", self.drive.frontLeft.getSelectedSensorVelocity())
        wpilib.SmartDashboard.putNumber("Right Velocity - ", self.drive.frontRight.getSelectedSensorVelocity())
        wpilib.SmartDashboard.putNumberArray("LR", [self.left_axis(), self.right_axis()])
        wpilib.SmartDashboard.putBoolean("Test Button - ", self.test_button())

    def end(self, interrupted: bool) -> None:
        #
        # Called once after isFinished returns True
        # Stop the drivetrain from moving any further
        self.drive.stopMotors()

    def isFinished(self) -> bool:
        # Make this return True when this command no longer needs to run execute()
        return False
