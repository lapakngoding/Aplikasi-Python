from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
import sqlite3
import bcrypt

class Daftar(MDScreen):
    pass

    def __init__(self, **kwargs):
        Builder.load_file("kv/daftar.kv")
        super().__init__(**kwargs)

    def submit(self):
        username = self.ids.username.text
        nama = self.ids.nama.text
        email = self.ids.email.text
        nohp = self.ids.nohp.text
        alamat = self.ids.alamat.text
        password = self.ids.password.text
        passconf = self.ids.passconf.text

        #koneksi ke data base
        conn = sqlite3.connect('/home/zahir/LapakNgoding.db')
        c = conn.cursor()
        c.execute("SELECT * FROM MEMBER")
        db = c.fetchall()
        z = []
        for user in db:
            a = (user[1])
            z.append(a)
        if not len (password)<=7:
            conn = sqlite3.connect('/home/zahir/LapakNgoding.db')
            if not username == None:
                if len(username)<3:
                    print ()
                    self.dialog = MDDialog(
                        text = "Username minimal 3 karakter!.untuk mengulangi klik di luar box",
                        radius=[20, 7, 20, 7],
                        )
                    self.dialog.open()
                elif username in z:
                    print()
                    self.dialog = MDDialog(
                        text="Username sudah terdaftar, untuk mengulangi klik di luar box",
                        radius=[20, 7, 20, 7],
                    )
                    self.dialog.open()
                else:
                    if  password == passconf:
                        password = password.encode('utf-8')
                        password = bcrypt.hashpw(password, bcrypt.gensalt())

                        conn = sqlite3.connect('/home/zahir/LapakNgoding.db')
                        c = conn.cursor()
        
                        c.execute("INSERT INTO member(nama, email, nohp, alamat, password, username)VALUES(:nama, :email, :nohp, :alamat, :password, :username)",
                        {
                            'username' : username,
                            'nama' : nama,
                            'email' : email,
                            'nohp' : nohp,
                            'alamat' : alamat,
                            'password' : password
                        })
                        conn.commit()
                        conn.close()
                        print()
                        self.dialog = MDDialog(
                            title="S E L A M A T",
                            text="Kamu telah terdaftar, Silahkan login di halaman utama",
                            radius=[20, 7, 20, 7],
                            )
                        self.dialog.open()

                    else:
                        print()
                        self.dialog = MDDialog(
                            text="Password harus sama dengan Konfirmasi Password, untuk mengulangi klik di luar box",
                            radius=[20, 7, 20, 7],
                            )
                        self.dialog.open()
        else:
            print()
            self.dialog = MDDialog(
                text="Password terlalu pendek minmal 8 karakter, untuk mengulangi klik di luar box",
                radius=[20, 7, 20, 7],
                )
            self.dialog.open()
            