class Robot:
    def __init__(self):
        self.frame = None # ChassisBuilder
        self.wheels = None# ChassisBuilder
        self.joints = None # ChassisBuilder

        self.sensors = None #ControlBuilder
        self.processors = None#ControlBuilder
        self.ai_modules  = None#ControlBuilder

        self.battery = None#PowerBuilder
        self.energy_efficiency = None # PowerBuilder
        self.charging_system = None # PowerBuilder
    
    def __str__(self):
        return f"{self.frame}\n{self.wheels}\n{self.ai_modules}\n{self.energy_efficiency}\n{self.charging_system}"


class RobotBuilder:
    def __init__(self, robot=Robot()):
        self.robot = robot
    
    def chassis(self):
        return ChassisBuilder(self.robot)
    
    def control(self):
        return ControlBuilder(self.robot)
    
    def power(self):
        return PowerBuilder(self.robot)
    
    def build(self):
        return self.robot
    

class ChassisBuilder(RobotBuilder):    
    def set_frame(self, frame):
        self.robot.frame = frame
        return self

    
    def set_wheels(self, wheels):
        self.robot.wheels = wheels
        return self

    
    def set_joints(self, joints):
        self.robot.joints = joints
        return self


class ControlBuilder(RobotBuilder):
    
    def set_sensors(self, sensors):
        self.robot.sensors = sensors
        return self

    def set_processors(self, processors):
        self.robot.processors = processors
        return self

    def set_ai_modules(self, ai_modules):
        self.robot.ai_modules = ai_modules
        return self


class PowerBuilder(RobotBuilder):
    
    def set_battery(self, battery):
        self.robot.battery = battery
        return self
    
    def set_energy_efficiency(self, energy_efficiency):
        self.robot.energy_efficiency = energy_efficiency
        return self
    
    def set_charging_system(self, charging_system):
        self.robot.charging_system = charging_system
        return self


builder = RobotBuilder()
robot = (
    builder
    .chassis()
    .set_frame(10)
    .set_wheels(4)
    .set_joints(1)
    .control()
    .set_ai_modules("AI Powered")
    .set_processors("M4 Pro")
    .set_sensors("Latest Sensor")
    .power().set_battery("100%")
    .set_charging_system("HP")
    .set_energy_efficiency("A+")
    .build())
print(robot)
print(isinstance(robot,Robot))







class Car:
    def __init__(self):
        self.engine = None
        self.color = None
        self.model = None
        self.gps = None
        self.fuel_type = None
    
    def __str__(self):
        return f"{self.engine}\n{self.color}\n{self.model}\n{self.gps}\n{self.fuel_type}"
    

class CarBuilder:
    def __init__(self, car=Car()):
        self.car = car
    
    def design(self):
        return DesignBuilder(self.car)
    
    def engine(self):
        return EngineBuilder(self.car)
    
    def features(self):
        return FeatureBuilder(self.car)
    
    def build(self):
        return self.car
    

class DesignBuilder(CarBuilder):
    def set_color(self, color):
        self.car.color = color
        return self
    
    def set_model(self, model):
        self.car.model = model
        return self
    

class EngineBuilder(CarBuilder):
    def set_engine(self, engine):
        self.car.engine = engine
        return self
    

class FeatureBuilder(CarBuilder):
    def set_gps(self, gps):
        self.car.gps = gps
        return self
    
    def set_fuel_type(self, fuel_type):
        self.car.fuel_type = fuel_type
        return self
    
car_builder = CarBuilder()
car = (
    car_builder
    .design()
    .set_color("Red")
    .set_model("Sedan")
    .engine()
    .set_engine("V8")
    .features()
    .set_gps("Advanced GPS")
    .set_fuel_type("Diesel")
    .build())
print(car)
print(isinstance(car,Car))