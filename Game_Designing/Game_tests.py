from turtle import position
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import time

game_test = Ursina()


ground = Entity(model="plane", texture="grass", collider="mesh", scale=(200, 1, 200))
player = FirstPersonController(position=(0,2,-5))
Sky()
# for z in range(20):
#     for x in range(20):
#         Entity(
#             model="cube", color=color.dark_gray, collider="box", ignore=True,
#             position = (x, 0, z),
#             parent=scene,
#             orgin_y = 0.5,
#             texture = "white_cube")

robo_entity = Entity(model=r'Assets\finnaly_letri.obj', texture=r'Assets\DefaultMaterial_Base_Color.png', scale=5, y=3, x = 2, z=.11)



# weapon = Entity(model=r'Assets\improvedwireframe.obj', parent=camera.ui, scale=5,color=color.gold, texure="white_cube", position=(0.8, -0.6), rotation=(-10,-20,-10))


class Player(Entity):
    def __init__(self, **kwargs):
        self.controller = FirstPersonController(**kwargs)
        super().__init__(parent=self.controller)

        self.scifi_shotgun = Entity(parent=self.controller.camera_pivot, scale=4, position=Vec3(0.7,-1,1.5), model=r'Assets\scifi_shotty.obj', texture=r"Assets\shotgun_color.png.png")
        self.controller.speed = 20

    def input(self, key):
        if key == "left mouse down":
            Bullet(model="sphere", color=color.black, scale=0.3, position=self.controller.camera_pivot.world_position, rotation=self.controller.camera_pivot.world_ro)





class Bullet(Entity):
    def __init__(self, speed=50, lifetime=10, **kwargs):
        super().__init__(**kwargs)
        self.lifetime = lifetime
        self.speed = speed
        self.start = time.time()

    def update(self):
        ray = (self.world_position, self.forward, distance= self.speed * time.dt)
        if not ray.hit and time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
        else:
            destroy(self)


        
        
player1 = Player(position=(0,10,0))
game_test.run()