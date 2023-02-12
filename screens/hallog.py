from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
import sqlite3
import bcrypt

class Hallog(MDScreen):
    pass

    def __init__(self, **kwargs):
        Builder.load_file("kv/hallog.kv")
        super().__init__(**kwargs)

    def loginAcc(self):
        username = self.ids.username.text
        password = self.ids.password.text

        if not len(username or password) < 1:
            if True:
                conn = sqlite3.connect('/home/zahir/LapakNgoding.db')
                c = conn.cursor()
                c.execute("SELECT * FROM MEMBER")

                db = c.fetchall()
                l = []
                n = []
                for user in db:
                    a = (user[1])
                    z = (user[6])
                    l.append(a)
                    n.append(z)
                    userdata = dict(zip(l, n))
                    #userdata = (l,n)
                try:
                    if username in userdata:
                        user = userdata[username]

                        try:
                            if  bcrypt.checkpw(password.encode(), user):
                                print("Berhasil login!")
                                print("Hi", username)
                                
                            else:
                                print()
                                self.dialog = MDDialog(
                                    text = "Password salah!.untuk mengulangi klik di luar box",
                                    radius=[20, 7, 20, 7],
                                    )
                                self.dialog.open()
                        except:
                            print()
                            self.dialog = MDDialog(
                                text = "Mohon password dan username periksa kembali!.untuk mengulangi klik di luar box",
                                radius=[20, 7, 20, 7],
                                )
                            self.dialog.open()
                    else:
                        print()
                        self.dialog = MDDialog(
                            text = "Maaf username tidak terdaftar!.untuk mengulangi klik di luar box",
                            radius=[20, 7, 20, 7],
                            )
                        self.dialog.open()
                except:
                    print()
                    self.dialog = MDDialog(
                        text = "Password atau username belum terdaftar!.untuk mengulangi klik di luar box",
                        radius=[20, 7, 20, 7],
                        )
                    self.dialog.open()
            else:
                print()
                self.dialog = MDDialog(
                    text = "Gagal login!.untuk mengulangi klik di luar box",
                    radius=[20, 7, 20, 7],
                    )
                self.dialog.open()
        else:
            print()
            self.dialog = MDDialog(
                text = "Password dan username tidak boleh kosong!.untuk mengulangi klik di luar box",
                radius=[20, 7, 20, 7],
                )
            self.dialog.open()