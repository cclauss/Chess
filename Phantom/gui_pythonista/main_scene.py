# -*- coding: utf-8 -*-

"""The main scene object for the GUI.  Allowes use of multiple scene classes with one GUI."""

from scene import *

class MultiScene (Scene):
    def __init__(self, start_scene):
        self.active_scene = start_scene
        self.tmp_t = 0
        self.invocations = 0
    def switch_scene(self, new_scene):
        self.active_scene = new_scene
    def setup(self):
        global screen_size
        screen_size = self.size
        self.tmp_t = self.t
        self.active_scene.setup()
    def draw(self):
        self.invocations += 1
        background(0, 0, 0)
        fill(1, 0, 0)
        self.active_scene.touches = self.touches
        self.active_scene.t = self.t - self.tmp_t
        self.active_scene.draw()
    def touch_began(self, touch):
        self.active_scene.touch_began(touch)
    def touch_moved(self, touch):
        self.active_scene.touch_moved(touch)
    def touch_ended(self, touch):
        self.active_scene.touch_ended(touch)
    
    def set_main_scene(self, s):
        self.main_scene = s
    
    def set_load_scene(self, s):
        self.load_scene = s
    
    def set_dbg_scene(self, s):
        self.dbg_scene = s
    
    def did_begin(self):
        self.switch_scene(self.main_scene)

