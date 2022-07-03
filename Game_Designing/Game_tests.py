from pyexpat import model
from turtle import position
from black import diff
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform


game_test = Ursina()



Sky()
# for z in range(20):
#     for x in range(20):
#         Entity(
#             model="cube", color=color.dark_gray, collider="box", ignore=True,
#             position = (x, 0, z),
#             parent=scene,
#             orgin_y = 0.5,
#             texture = "white_cube")



ground = Entity(model="plane", texture="grass", collider="mesh", scale=(200, 1, 200))
player = FirstPersonController(position=(0,2,-5))

robo_entity = Entity(model=r'Assets\finnaly_letri.obj', texture=r'Assets\DefaultMaterial_Base_Color.png', scale=5, y=3, x = 2, z=.11)



# weapon = Entity(model=r'Assets\improvedwireframe.obj', parent=camera.ui, scale=5,color=color.gold, texure="white_cube", position=(0.8, -0.6), rotation=(-10,-20,-10))

controller = FirstPersonController()
        

scifi_shotgun = Entity(parent=controller.camera_pivot, scale=4, position=Vec3(0.7,-1,1.5), model=r'Assets\scifi_shotty.obj', texture=r"Assets\shotgun_color.png.png")
controller.speed = 20






    














kongs = []
objects = []
# groups of donkey kongs
for i in range(4):
    
    enemy_kong_animation = FrameAnimation3d(r'monke_animation/dk', color = color.black, scale=4, fps=25, position=(uniform(-45,45), 1,uniform(33,45)))
    enemy_object = Entity(model=r"monke_animation/dk_1", scale=4, parent=enemy_kong_animation, position=(0,30,0))

    enemy_object.visible = False
    enemy_object.look_at(controller)
    enemy_object.rotation_x=270

    enemy_object.rotation_z = -50

    kongs.append(enemy_kong_animation)

    objects.append(enemy_object)









        

class Bullet(Entity):
    def __init__(self, speed=1000, lifetime=15, **kwargs):
        super().__init__(**kwargs)
        self.lifetime = lifetime
        self.speed = speed
        self.start = time.time()

    def update_rays(self):
        ray = raycast(self.world_position, self.forward, distance= self.speed * time.dt)
        if not ray.hit and time.time() - self.start < self.lifetime:
            self.world_position += self.forward * self.speed * time.dt
        else:
            destroy(self)



def update():
        if held_keys['left mouse']:
            Bullet(model=r"Assets\10176_Coconut_Whole_v01-it3.obj", texture=r"Assets\Coconut_01.jpg", scale=0.01, position=controller.camera_pivot.world_position, rotation=controller.camera_pivot.world_rotation)
        if controller.y <-5:
            controller.y = 2
        for enemy in kongs:
            if enemy.visible:
                enemy.lookAt(controller)
                enemy.rotation_x = 270
                enemy.rotation_z = -50
                dist = distance(enemy, controller)
                if dist > 5: # if enemy is distance is greater than 5
                    enemy.resume()
                    diff_x = controller.x - enemy.x
                    diff_z = controller.z - enemy.z
                    enemy.x += 4*time.dt*diff_x*abs(diff_x)
                    enemy.z += 4*time.dt*diff_z/abs(diff_z)
                else:
                    enemy.pause()
                    print("enemy is stopped")


 
game_test.run()