import sys
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QMessageBox,

)
from PyQt5.QtCore import Qt


class PomodoroApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # 1. Önce Değişkenler
        self.kalan_saniye = 25 * 60 
        self.tur_sayisi = 0

        # 2. Arayüz ve Pencereler
        self.pencere_ayarlari()
        self.arayuz_olustur()
        self.layout_kurulumu()

        # 3. Timer ve Buton Bağlantıları
        self.timer = QTimer()
        self.timer.timeout.connect(self.sayac_guncelle)
        self.buton_baglantilari()
        self.stil_uygula()

    def pencere_ayarlari(self):
        self.setWindowTitle("Pomodoro uygulaması")
        self.resize(650,450)
        self.setMinimumSize(450,350)

    def arayuz_olustur(self):
        self.btn_pomodoro  = QPushButton(("🍅 Pomodoro (25 dk)"))
        self.btn_kisa_mola = QPushButton(("🌿 Kısa Mola (5 dk)"))
        self.btn_uzun_mola = QPushButton(("📚 Uzun Mola (15 dk)"))

        self.lbl_sayac = QLabel("25:00")
        self.lbl_sayac.setObjectName("lbl_sayac")
        self.lbl_sayac.setAlignment(Qt.AlignCenter)
        
        self.lbl_tur_sayisi = QLabel("tamamlanan pomodoro : 0 🍅")
        self.lbl_tur_sayisi.setAlignment(Qt.AlignCenter)

        self.btn_baslat = QPushButton("▶  başla")
        self.btn_durdur = QPushButton("⏸  durdur")
        self.btn_sifirla = QPushButton("🔄 sıfırla")


        self.btn_pomodoro.setObjectName("btn_pomodoro")
        self.btn_kisa_mola.setObjectName("btn_kisa_mola")
        self.btn_uzun_mola.setObjectName("btn_uzun_mola")
        self.btn_baslat.setObjectName("btn_baslat")
        self.btn_durdur.setObjectName("btn_durdur")
        self.btn_sifirla.setObjectName("btn_sifirla")
        self.lbl_tur_sayisi.setObjectName("lbl_tur_sayisi")




    
    def layout_kurulumu(self):
        ust_layout = QHBoxLayout()
        ust_layout.addWidget(self.btn_pomodoro)
        ust_layout.addWidget(self.btn_kisa_mola)
        ust_layout.addWidget(self.btn_uzun_mola)

        alt_layout = QHBoxLayout()
        alt_layout.addWidget(self.btn_baslat)
        alt_layout.addWidget(self.btn_durdur)
        alt_layout.addWidget(self.btn_sifirla)

        ana_layout = QVBoxLayout()
        ana_layout.addLayout(ust_layout)
        ana_layout.addWidget(self.lbl_sayac)
        ana_layout.addWidget(self.lbl_tur_sayisi)
        ana_layout.addSpacing(15)
        ana_layout.addLayout(alt_layout)

        merkez = QWidget()
        merkez.setLayout(ana_layout)
        self.setCentralWidget(merkez)

        # 1. Her saniye çalışacak sayaç
    def sayac_guncelle(self):
        if self.kalan_saniye > 0:
            self.kalan_saniye -= 1
            dakika = self.kalan_saniye // 60
            saniye = self.kalan_saniye % 60
            self.lbl_sayac.setText(f"{dakika:02d}:{saniye:02d}")
        else:
            self.timer.stop()
            self.tur_sayisi += 1
            self.lbl_tur_sayisi.setText(f"Tamamlanan Pomodoro: {self.tur_sayisi} 🍅")
            QMessageBox.information(self, "Tebrikler!", "Süre doldu, mola zamanı!")

    # 2. Butonların Fonksiyonları
    def baslat(self):
        self.timer.start(1000) # 1000 ms = 1 saniye

    def durdur(self):
        self.timer.stop()

    def sifirla(self):
        self.timer.stop()
        self.kalan_saniye = 25 * 60
        self.lbl_sayac.setText("25:00")

    def modu_degistir(self, saniye):
        self.timer.stop()
        self.kalan_saniye = saniye
        dakika = saniye // 60
        self.lbl_sayac.setText(f"{dakika:02d}:00")

    # 3. Butonları Bağlama (Tek seferlik)
    def buton_baglantilari(self):
        self.btn_baslat.clicked.connect(self.baslat)
        self.btn_durdur.clicked.connect(self.durdur)
        self.btn_sifirla.clicked.connect(self.sifirla)

        self.btn_pomodoro.clicked.connect(lambda: self.modu_degistir(25 * 60))
        self.btn_kisa_mola.clicked.connect(lambda: self.modu_degistir(5 * 60))
        self.btn_uzun_mola.clicked.connect(lambda: self.modu_degistir(15 * 60))

    def stil_uygula(self):
        self.setStyleSheet("""
            QMainWindow{
            background-color : #F9F6EE;
            }
            #lbl_sayac{
                font-size:100px;
                color: #000000;
                font-weight: bold;
            }
            QPushButton{
                font-size : 15px;
                border-radius : 12px;
                padding : 8px;
                font-weight: bold;
                
            }
            QPushButton#btn_pomodoro{
                background-color: #F28C28;
            }        
            QPushButton#btn_kisa_mola{
                background-color: #2E7D32;
            }
            QPushButton#btn_uzun_mola{
                background-color: #1565C0;
            }
            QPushButton#btn_baslat{
                background-color: #E2C13C;
            }
            QPushButton#btn_durdur{
                background-color: #F2332C;
            }
            QPushButton#btn_sifirla{
                background-color: #D3D3D3;
            }
            QLabel#lbl_tur_sayisi{
                font-size: 15px;
                font-weight: bold;
                border-radius: 10px;         
                padding: 6px 14px; 
            }
            QPushButton#btn_pomodoro:pressed{
                background-color: #FFEA00;

            }        
            QPushButton#btn_kisa_mola:pressed{
                background-color: #7CFC00;

            }
            QPushButton#btn_uzun_mola:pressed{
                background-color: #7DF9FF;
            }
            QPushButton#btn_baslat:pressed{
                background-color:#7DF9FF;
            }
            QPushButton#btn_durdur:pressed{
                background-color: #A6100D;
            }
            QPushButton#btn_sifirla:pressed{
                background-color: #FFFFFF;
            }

        """)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pomodoro = PomodoroApp()
    pomodoro.show()
    sys.exit(app.exec_())
