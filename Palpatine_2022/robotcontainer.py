import commands2
import ctre
import wpilib

import constants
from commands.drive_by_guitar import DriveByGuitar
from commands.drive_straight import DriveStraight
from subsystems.drivetrain import Drivetrain

from guitar import Guitar
from wpilib.interfaces import GenericHID
from wpilib import XboxController

class RobotContainer:
    def __init__(self) -> None:
        self.driverController = Guitar(0)

        self.frontLeft = ctre.TalonFX(constants.kfrontLeft)
        self.backLeft = ctre.TalonFX(constants.kbackLeft)
        self.frontRight = ctre.TalonFX(constants.kfrontRight)
        self.backRight = ctre.TalonFX(constants.kbackRight)

        self.timer = wpilib.Timer

        # subsystems
        self.drive = Drivetrain()

        # chooser
        self.chooser = wpilib.SendableChooser()

        # Add commands to autonomous command chooser
        self.driveStraight = DriveStraight(self.drive, constants.kdistanceToTravel)
        self.chooser.setDefaultOption("Drive Straight", self.driveStraight)

        wpilib.SmartDashboard.putData("Autonomous", self.chooser)

        # ARCADE, OBJECTIVELY WAY BETTER - Pickle_Face5 & Wyatt
        self.drive.setDefaultCommand(DriveByGuitar(self.drive, lambda: self.forwardSum(), lambda: self.reverseSum(), lambda: self.driverController.getGreenButton()))

    def forwardSum(
            self) -> float:  # It took more than 2 and a half hours to get this to work, I swear if this stops working I'm going to commit a crime
        leftY, rightX = self.addDeadZone(self.driverController.getJoystickY(), self.driverController.getSliderValue())
        finalValue = -leftY + rightX
        if (finalValue > 1):
            finalValue = 1
        elif (finalValue < -1):
            finalValue = -1
        return finalValue

    def reverseSum(self) -> float:
        leftY, rightX = self.addDeadZone(self.driverController.getJoystickY(), self.driverController.getSliderValue())
        finalValue = -leftY - rightX
        if (finalValue > 1):
            finalValue = 1
        elif (finalValue < -1):
            finalValue = -1
        return finalValue

    def addDeadZone(self, leftYParam: float, rightXParam: float) -> tuple:
        leftY = leftYParam
        rightX = rightXParam
        print(leftY)
        #wpilib.SmartDashboard.putNumber('trueLeftJoy - ', leftY)
        #wpilib.SmartDashboard.putNumber('trueRightJoy - ', rightX)

        # Controller Dead Zone
        if (abs(leftY) <= constants.controllerDeadZoneLeft):
            leftY = 0
        if (abs(rightX) <= constants.controllerDeadZoneRight):
            rightX = 0
        return leftY, rightX

    def getAutonomousCommand(self) -> commands2.Command:
        return self.chooser.getSelected()
