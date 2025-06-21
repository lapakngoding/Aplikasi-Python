from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
import sqlite3
import bcrypt
import os

# Buat path database dinamis
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, '..', 'LapakNgoding.db')

from kivymd.app import MDApp  # ⬅ WAJIB agar MDApp bisa diakses

class Hallog(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file("kv/hallog.kv")
        super().__init__(**kwargs)

    def loginAcc(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        if not username or not password:
            self.dialog = MDDialog(
                text="Username dan Password tidak boleh kosong!",
                radius=[20, 7, 20, 7],
            )
            self.dialog.open()
            return

        try:
            # Ambil data dari database
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute("SELECT username, password FROM member")
            db = c.fetchall()
            conn.close()

            # Buat dict username -> password
            userdata = {uname: pwd for uname, pwd in db}

            if username in userdata:
                hashed_pw = userdata[username]

                # Konversi ke bytes jika perlu
                if isinstance(hashed_pw, str):
                    hashed_pw = hashed_pw.encode('utf-8')

                # Validasi password
                if bcrypt.checkpw(password.encode(), hashed_pw):
                    print(f"✅ Login berhasil untuk: {username}")
                    MDApp.get_running_app().logged_user = username
                    self.manager.current = 'beranda'
                else:
                    self.dialog = MDDialog(
                        text="❌ Password salah! Coba lagi.",
                        radius=[20, 7, 20, 7],
                    )
                    self.dialog.open()
            else:
                self.dialog = MDDialog(
                    text="❌ Username tidak ditemukan.",
                    radius=[20, 7, 20, 7],
                )
                self.dialog.open()
        except Exception as e:
            print("🔥 Error saat login:", e)
            self.dialog = MDDialog(
                text="Terjadi kesalahan saat login. Periksa koneksi atau database.",
                radius=[20, 7, 20, 7],
            )
            self.dialog.open()
