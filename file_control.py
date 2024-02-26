# coding: utf-8
import os
import shutil
import time
from tqdm import tqdm  # tqdm kütüphanesini yükleyebilirsiniz


def kontrol_et_kopyala_sil(kaynak_dizin, hedef_dizin):
    while True:
        # Kaynak dizindeki dosyaları al
        kaynak_dosyalar = os.listdir(kaynak_dizin)
        kaynak_dosyalar = [dosya for dosya in kaynak_dosyalar if os.path.isfile(os.path.join(kaynak_dizin, dosya))]

        # En son eklenen dosyayı bul
        en_son_eklenen = max(kaynak_dosyalar, key=lambda x: os.path.getmtime(os.path.join(kaynak_dizin, x)))

        # Hedef dizindeki dosyaları al
        hedef_dosyalar = os.listdir(hedef_dizin)
        hedef_dosyalar = [dosya for dosya in hedef_dosyalar if os.path.isfile(os.path.join(hedef_dizin, dosya))]

        # En son eklenen dosyayı hariç al
        if en_son_eklenen in kaynak_dosyalar:
            kaynak_dosyalar.remove(en_son_eklenen)

        # Dosya adları ve yükleme zamanlarını içeren sözlük oluştur
        dosya_zaman_sozlugu = {dosya: os.path.getmtime(os.path.join(kaynak_dizin, dosya)) for dosya in kaynak_dosyalar}

        # Eksik olan dosyaları bul
        eksik_dosyalar = set(kaynak_dosyalar) - set(hedef_dosyalar)

        # Eksik dosyaları kopyala
        for dosya in tqdm(eksik_dosyalar, desc="Dosyalar kopyalanıyor"):
            kaynak_yol = os.path.join(kaynak_dizin, dosya)
            hedef_yol = os.path.join(hedef_dizin, dosya)

            try:
                shutil.copy2(kaynak_yol, hedef_yol)
                yukleme_zamani = dosya_zaman_sozlugu[dosya]
                print(f"{dosya} kopyalandı. Yükleme Zamanı: {time.ctime(yukleme_zamani)}")
            except Exception as e:
                print(f"Hata: {e}")

        # Kopyalanan dosyaları sil
        for dosya in tqdm(kaynak_dosyalar, desc="Kopyalanan dosyalar siliniyor"):
            try:
                os.remove(os.path.join(kaynak_dizin, dosya))
                print(f"{dosya} başarıyla silindi.")
            except Exception as e:
                print(f"Hata: {e}")

        time.sleep(3600)  # 1 saat bekleme süresi (saniye cinsinden)


if __name__ == "__main__":
    kaynak_dizin = "D:\\"  # Kaynak dizin
    hedef_dizin = "X:\\"  # Hedef dizin
    kontrol_et_kopyala_sil(kaynak_dizin, hedef_dizin)
