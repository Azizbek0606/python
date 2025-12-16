class BallFlyweight:
    def __init__(self, radius, imageUrl, texture):
        self.radius = radius
        self.imageUrl = imageUrl
        self.texture = texture

    def draw(self, position, speed, color):
        return f"radius={self.radius}; imageUrl={self.imageUrl}; texture={self.texture}, |==||==| position={position}, speed={speed}, color={color}"


class Ball:
    def __init__(self, ballFlyweight, position, speed, color):
        self.ballFlyweight = ballFlyweight
        self.position = position
        self.speed = speed
        self.color = color

    def draw(self):
        return self.ballFlyweight.draw(self.position, self.speed, self.color)


class BallFlyWeightFactory:
    _cash = {}
    @classmethod
    def create(cls, radius, imageUrl, texture):
        key = (radius, imageUrl, texture)
        if key not in cls._cash:
            cls._cash[key] = BallFlyweight(radius, imageUrl, texture)
        return cls._cash[key]


class Game:
    def __init__(self):
        self.ball = []

    def add_ball(self,radius, imageUrl, texture, position, speed, color):
        ballflyweight = BallFlyWeightFactory.create(radius, imageUrl, texture)
        print(id(ballflyweight))
        ball = Ball(ballflyweight, position, speed, color)
        self.ball.append(ball)

    def draw_ball(self):
        for ball in self.ball:
            print(ball.draw())
game = Game()
game.add_ball(1.2,"https://img.png", "texture.png", 1.1,3,"red")
game.add_ball(1.2,"https://img.png", "texture.png", 1.1,3,"red")
game.add_ball(1.2,"https://img.png", "texture.png", 1.1,3,"red")
game.add_ball(1.2,"https://img.png", "texture.png", 1.1,3,"red")
game.add_ball(1.2,"https://img.png", "texture.png", 1.1,3,"red")
game.add_ball(1.2,"https://img.png", "texture.png", 1.1,3,"red")
game.draw_ball()