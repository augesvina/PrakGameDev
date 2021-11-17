#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import pi, sin, cos  #untuk menghitung pergerakan kamera

from direct.showbase.ShowBase import ShowBase #untuk mengambil dan menampilkan image
from direct.task import Task #untuk manajemen fungsi
from direct.actor.Actor import Actor #meload kelas aktor yang digunakan.
from panda3d.core import ClockObject


keyMap = {
    "left": False,
    "right": False,
    "rotate": False
}



def updateKeyMap(key, state):
    keyMap[key] = state


class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)  

        # Nonaktifkan kontrol trackball kamera.
        self.disableMouse()

        # memuat environment model.
        self.scene = self.loader.loadModel("models/environment")
        # Atur ulang model yang akan dirender.
        self.scene.reparentTo(self.render)
         # Terapkan transformasi scale dan posisi pada model.
        self.scene.setScale(0.25, 0.25, 0.25)
        self.scene.setPos(-8, 42, 0)

        # Tambahkan prosedur spinCameraTask ke pengelola tugas.
        self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

        # Load dan ubah aktor panda.
        self.Panda = Actor("models/panda-model",
                           {"walk": "models/panda-walk4"})
        self.Panda.setScale(0.005, 0.005, 0.005)
        self.Panda.reparentTo(self.render)
        # Loop animasinya.
        self.Panda.loop("walk")

        self.accept("arrow_left", updateKeyMap, ["left", True])
        self.accept("arrow_left-up", updateKeyMap, ["left", False])

        self.accept("arrow_right", updateKeyMap, ["right", True])
        self.accept("arrow_right-up", updateKeyMap, ["right", False])

        self.accept("space", updateKeyMap, ["rotate", True])
        self.accept("space-up", updateKeyMap, ["rotate", False])

        self.speed=6
        self.angle=0 

        self.taskMgr.add(self.update, "update")

    # Tentukan prosedur untuk menggerakkan kamera.
    def spinCameraTask(self, task):
        angleDegrees=task.time * 6.0
        angleRadians=angleDegrees * (pi / 180.0)
        self.camera.setPos(20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr(angleDegrees, 0, 0)
        return Task.cont

    def update(self, task):

        globalClock = ClockObject.getGlobalClock()

        dt = globalClock.getDt()

        pos = self.Panda.getPos()

        if keyMap["left"]:
            pos.x -= self.speed * dt
        if keyMap["right"]:
            pos.x += self.speed * dt
        if keyMap["rotate"]:
            self.angle += 1 
            self.Panda.setH(self.angle)

        self.Panda.setPos(pos)

        return task.cont

#inisialisasi Function MyApp() ke variabel app
app=MyApp()
mySound=app.loader.loadSfx("haegeum.ogg")
mySound.play() #musik diputar
mySound.setLoop(True)#untuk mengulang musik
mySound.setVolume(13)#untuk mengulang musik
app.run()#untuk menjalankan aplikasi


# In[ ]:




