import cv2
import numpy as np
import math
from taichi.math import * 
import taichi as ti
from memory_profiler import profile
ti.init(arch=ti.gpu)    


image_resolution = (800, 600)
image_pixels = ti.Vector.field(3, float, image_resolution)
gui1 = ti.GUI("ChangeColor", image_resolution)

thisrun = True
nowimage = 1
while thisrun:
    path = "./image"+str(nowimage)+".jpg"
    img = ti.tools.imread(path).astype('float32')
    img = img / 255
    image_pixels.from_numpy(img)
    gui1.running = True
    while gui1.running:
        if gui1.get_event(ti.GUI.PRESS):
            if gui1.event.key == ti.GUI.RIGHT:
                nowimage+=1
                gui1.running = False
            if gui1.event.key == ti.GUI.LEFT:
                if nowimage > 1:
                    nowimage-=1
                gui1.running = False
        if gui1.is_pressed(ti.GUI.LMB): 
            mouse_x, mouse_y = gui1.get_cursor_pos()
            xi = int(mouse_x*800)
            yj = int(mouse_y*600)
            for x_size in range(10):
                for y_size in range(10):
                    image_pixels[xi+x_size, yj+y_size]=  (1,0,0)
            #print(xi, yj)
        gui1.set_image(image_pixels)  # 为画布设置图像
        if gui1.is_pressed("s"): 
            gui1.show("./image_"+str(nowimage)+".jpg")
        gui1.show() 
    if(nowimage>3):
        thisrun = False
        print("已结束") 
      # 显示窗口


