from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

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



weapon = Entity(model=r'Assets\improvedwireframe.obj', parent=camera.ui, scale=2.5,color=color.gold, texure="white_cube", position=(0.8, -0.6))

camera.z = -5
game_test.run()