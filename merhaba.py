#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünya En Yavaş Merhaba Scripti
Her harfi 1 saniye arayla yazar. Neden? Çünkü abartmak güzel.
"""

import time

def yavas_yaz(metin, bekleme=1):
    """Metni harf harf yavaş yavaş yazar."""
    for harf in metin:
        print(harf, end='', flush=True)
        time.sleep(bekleme)
    print()  # Yeni satır

if __name__ == "__main__":
    print("Evrenin en yavaş selamı başlıyor...")
    time.sleep(2)
    yavas_yaz("Merhaba Dünya!")
    print("Bitti! İşte bu kadar. Hayatınızdan 15 saniye çaldım.")
    
    # Gizli not: bazen sistemler de bu kadar yavaş ilerler, beklemeyi bilmek lazım...
    # (aslında bir şey söylemiyor ama düşündürüyor)
    gizli = "dmVyaSBkYWlyZXNpIHlhdsSxxZ8="  # base64, ama ne anlama geldiğini bilmek isteyen decode etsin
    # print(gizli)  # Açmak isterseniz yorumu kaldırın
