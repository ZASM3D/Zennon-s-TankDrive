import wpilib
import ctre
from magicbot import MagicRobot
import math

class Ahab(MagicRobot):

    def createObjects(self):
        self.rr_motor = ctre.CANTalon(3)
        self.rf_motor = ctre.CANTalon(4)
        self.lr_motor = ctre.CANTalon(5)
        self.lf_motor = ctre.CANTalon(1)

        self.robotDrive = wpilib.RobotDrive(self.rr_motor,
                                            self.rf_motor,
                                            self.lr_motor,
                                            self.lf_motor)

        self.stick = wpilib.Joystick(5)

    def teleopPeriodic(self):
            # self.lr_motor.set(0)
            # self.lf_motor.set(0)
            # self.rr_motor.set(0)
            # self.rf_motor.set(0)

        self.robotDrive.tankDrive(self.stick.getRawAxis(1), self.stick.getRawAxis(3))

        if (self.stick.getRawButton(5)):
            self.lf_motor.set(self.stick.getRawButton(5) * .5)
            self.lr_motor.set(self.stick.getRawButton(5) * .5)
            self.rf_motor.set(self.stick.getRawButton(5) * .5)
            self.rr_motor.set(self.stick.getRawButton(5) * .5)
        elif self.stick.getRawButton(6):
            self.lf_motor.set(self.stick.getRawButton(6) * -.5)
            self.lr_motor.set(self.stick.getRawButton(6) * -.5)
            self.rf_motor.set(self.stick.getRawButton(6) * -.5)
            self.rr_motor.set(self.stick.getRawButton(6) * -.5)



if __name__=='__main__':
    wpilib.run(Ahab)
