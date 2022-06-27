from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

game_test = Ursina()


for z in range(20):
    for x in range(20):
        Entity(
            model="cube", color=color.dark_gray, collider="box", ignore=True,
            position = (x, 0, z),
            parent=scene,
            orgin_y = 0.5,
            texture = "white_cube")

robo_entity = Entity(model="D:\Summer_Programs_2021\Assets\deathbot.obj", scale=2, y=2, z=1)


player = FirstPersonController()
game_test.run()