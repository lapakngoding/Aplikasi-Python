from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import sqlite3
import bcrypt

class Beranda(MDScreen):
    pass

    def __init__(self, **kwargs):
        Builder.load_file("kv/hallog.kv")
        super().__init__(**kwargs)