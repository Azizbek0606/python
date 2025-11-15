# from abc import ABC, abstractmethod
# class Computer:
#     def __init__(self):
#         self.cpu = None
#         self.ram = None
#         self.storage = None
#         self.gpu = None
#         self.os = None
#         self.wifi_enabled = None

#     def __str__(self):
#         return (f"Computer Specifications:\n"
#                 f"CPU: {self.cpu}\n"
#                 f"RAM: {self.ram}\n"
#                 f"Storage: {self.storage}\n"
#                 f"GPU: {self.gpu}\n"
#                 f"OS: {self.os}\n"
#                 f"WiFi Enabled: {self.wifi_enabled}")


# class ComputerBuilder(ABC):
#     @abstractmethod
#     def set_cpu(self, cpu):
#         pass

#     @abstractmethod
#     def set_ram(self, ram):
#         pass

#     @abstractmethod
#     def set_storage(self, storage):
#         pass

#     @abstractmethod
#     def set_gpu(self, gpu):
#         pass

#     @abstractmethod
#     def set_os(self, os):
#         pass

#     @abstractmethod
#     def set_wifi_enabled(self, wifi_enabled):
#         pass

#     @abstractmethod
#     def get_computer(self):
#         pass


# class GamingComputerBuilder(ComputerBuilder):
#     def __init__(self):
#         self.computer = Computer()

#     def set_cpu(self, cpu):
#         self.computer.cpu = cpu

#     def set_ram(self, ram):
#         self.computer.ram = ram

#     def set_storage(self, storage):
#         self.computer.storage = storage

#     def set_gpu(self, gpu):
#         self.computer.gpu = gpu

#     def set_os(self, os):
#         self.computer.os = os

#     def set_wifi_enabled(self, wifi_enabled):
#         self.computer.wifi_enabled = wifi_enabled

#     def get_computer(self):
#         return self.computer


# class ComputerDirector:
#     def __init__(self, builder: ComputerBuilder):
#         self.builder = builder

#     def construct_gaming_computer(self):
#         self.builder.set_cpu("Intel Core i9")
#         self.builder.set_ram("32GB")
#         self.builder.set_storage("1TB SSD")
#         self.builder.set_gpu("NVIDIA GeForce RTX 3080")
#         self.builder.set_os("Windows 11")
#         self.builder.set_wifi_enabled(True)
#         return self.builder.get_computer()
    

# builder = GamingComputerBuilder()
# director = ComputerDirector(builder)
# gaming_computer = director.construct_gaming_computer()
# print(gaming_computer)
# print(isinstance(gaming_computer, Computer))


# facade tasks:
'''
class UserProfile:
    def __init__(self, username, email, age, phone, address):
        self.username = username
        self.email = email
        self.age = age
        self.phone = phone
        self.address = address

    def __repr__(self):
        return (f"UserProfile(username={self.username}, email={self.email}, "
                f"age={self.age}, phone={self.phone}, address={self.address})")
Implement with Director
'''






# from abc import ABC, abstractmethod

# class UserProfile:
#     def __init__(self, username, email, age, phone, address):
#         self.username = username
#         self.email = email
#         self.age = age
#         self.phone = phone
#         self.address = address

#     def __repr__(self):
#         return (f"UserProfile(username={self.username}, email={self.email}, "
#                 f"age={self.age}, phone={self.phone}, address={self.address})")


# class UserProfileBuilder(ABC):
#     @abstractmethod
#     def set_username(self, username):
#         pass

#     @abstractmethod
#     def set_email(self, email):
#         pass

#     @abstractmethod
#     def set_age(self, age):
#         pass

#     @abstractmethod
#     def set_phone(self, phone):
#         pass

#     @abstractmethod
#     def set_address(self, address):
#         pass

#     @abstractmethod
#     def get_user_profile(self):
#         pass

# class ConcreteUserProfileBuilder(UserProfileBuilder):
#     def __init__(self):
#         self.user_profile = UserProfile(None, None, None, None, None)

#     def set_username(self, username):
#         self.user_profile.username = username

#     def set_email(self, email):
#         self.user_profile.email = email

#     def set_age(self, age):
#         self.user_profile.age = age

#     def set_phone(self, phone):
#         self.user_profile.phone = phone

#     def set_address(self, address):
#         self.user_profile.address = address

#     def get_user_profile(self):
#         return self.user_profile

# class UserProfileDirector:
#     def __init__(self, builder: UserProfileBuilder):
#         self.builder = builder

#     def construct_user_profile(self, username, email, age, phone, address):
#         self.builder.set_username(username)
#         self.builder.set_email(email)
#         self.builder.set_age(age)
#         self.builder.set_phone(phone)
#         self.builder.set_address(address)
#         return self.builder.get_user_profile()
    

# builder = ConcreteUserProfileBuilder()
# director = UserProfileDirector(builder)
# user_profile = director.construct_user_profile(
#     username="john_doe",
#     email="email@gmail.com",
#     age=30,
#     phone="123-456-7890",
#     address="123 Main St, Anytown, USA"
# )




# task 6

from abc import ABC, abstractmethod

class Robot:
    def __init__(self):
        self.frame = None
        self.wheels = None
        self.joints = None
        self.sensors = None
        self.processors = None
        self.ai_modules = None
        self.battery = None
        self.energy_efficiency = None
        self.charging_system = None

    def __str__(self):
        return (f"Robot Specifications:\n"
                f"Frame: {self.frame}\n"
                f"Wheels: {self.wheels}\n"
                f"Joints: {self.joints}\n"
                f"Sensors: {self.sensors}\n"
                f"Processors: {self.processors}\n"
                f"AI Modules: {self.ai_modules}\n"
                f"Battery: {self.battery}\n"
                f"Energy Efficiency: {self.energy_efficiency}\n"
                f"Charging System: {self.charging_system}")
    

class Builder:
    def __init__(self, robot=Robot()):
        self.robot = robot

    @property
    def chassie(self):
        return ChassisBuilder(self.robot)
    @property
    def control(self):
        return ControlBuilder(self.robot)
    @property
    def power(self):
        return PowerBuilder(self.robot)

    def get_chassis(self):
        return self.robot
    

class ChassisBuilder(Builder):
    
    def set_frame(self, frame):
        self.robot.frame = frame

    def set_wheels(self, wheels):
        self.robot.wheels = wheels

    def set_joints(self, joints):
        self.robot.joints = joints

class ControlBuilder(Builder):

    def set_sensors(self, sensors):
        self.robot.sensors = sensors

    def set_processors(self, processors):
        self.robot.processors = processors

    def set_ai_modules(self, ai_modules):
        self.robot.ai_modules = ai_modules
    

class PowerBuilder(Builder):

    def set_battery(self, battery):
        self.robot.battery = battery

    def set_energy_efficiency(self, energy_efficiency):
        self.robot.energy_efficiency = energy_efficiency

    def set_charging_system(self, charging_system):
        self.robot.charging_system = charging_system


    
class RobotBuilder:
    def __init__(self):
        self.chassis_builder = ChassisBuilder()
        self.control_builder = ControlBuilder()
        self.power_builder = PowerBuilder()

    def construct_robot(self):
        self.chassis_builder.set_frame("Aluminum Frame")
        self.chassis_builder.set_wheels("All-Terrain Wheels")
        self.chassis_builder.set_joints("Hydraulic Joints")

        self.control_builder.set_sensors("LIDAR, Camera")
        self.control_builder.set_processors("Quad-Core CPU")
        self.control_builder.set_ai_modules("Navigation AI")

        self.power_builder.set_battery("Lithium-Ion Battery")
        self.power_builder.set_energy_efficiency("High Efficiency")
        self.power_builder.set_charging_system("Fast Charging System")

        robot = Robot()
        chassis = self.chassis_builder.get_chassis()
        control = self.control_builder.get_control()
        power = self.power_builder.get_power()

        robot.frame = chassis.frame
        robot.wheels = chassis.wheels
        robot.joints = chassis.joints
        robot.sensors = control.sensors
        robot.processors = control.processors
        robot.ai_modules = control.ai_modules
        robot.battery = power.battery
        robot.energy_efficiency = power.energy_efficiency
        robot.charging_system = power.charging_system

        return robot
    

builder = RobotBuilder()
robot = builder.construct_robot()
print(robot)