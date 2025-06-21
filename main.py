from kivymd.app import MDApp
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window

Window.size = (500, 650)

from screens.screens import *

class WindowManager(ScreenManager):
	pass

class LapakNgoding(MDApp):
	def build(self):
		self.logged_user = None
		
		self.wm = WindowManager()
		screens =[
			Hallog(name="hallog"),
			Daftar(name="daftar"),
			Hallogadmin(name="hallogadmin"),
			Beranda(name='beranda'),
		]
		for screen in screens:
			self.wm.add_widget(screen)
		return self.wm
	
	def logout(self):
		self.wm.current = "hallog"

if __name__ == '__main__':
	LabelBase.register(name="Atma", fn_regular="kv/assets/fonts/Atma-Bold.ttf")
	LabelBase.register(name="Tagline", fn_regular="kv/assets/fonts/Ubuntu-LI.ttf")
	LabelBase.register(name="Line", fn_regular="kv/assets/fonts/Ubuntu-M.ttf")
	LapakNgoding().run()
