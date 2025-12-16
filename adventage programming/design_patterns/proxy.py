from abc import ABC, abstractmethod

class HeroImage(ABC):
    @abstractmethod
    def display(self):
        pass


class RealImage(HeroImage):
    def __init__(self, imageUrl):
        self.imageUrl = imageUrl
        print(self.load_image())

    def load_image(self):
        return f"{self.imageUrl} file loaded from disk"

    def display(self):
        print(f"Displaying {self.imageUrl}")



class ProxyImage(HeroImage):
    def __init__(self, imageUrl):
        self.imageUrl = imageUrl
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self.imageUrl)
        self._real_image.display()


image = ProxyImage("hero.png")
image.display()
image.display()


class DataService(ABC):
    @abstractmethod
    def read_data(self):
        pass

class RealData(DataService):
    def __init__(self, data):
        self._data = data

    def read_data(self):
        return f"Sensitive data: {self._data}"

class AuthProxy(DataService):
    def __init__(self, data, user_role):
        self.user_role = user_role
        self._real_data = RealData(data)

    def read_data(self):
        if self.user_role != "admin":
            raise PermissionError("Access denied: Unauthorized user")
        return self._real_data.read_data()


proxy = AuthProxy("Top Secret Info", "admin")
print(proxy.read_data())
