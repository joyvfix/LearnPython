# import pyautogui
# import time


# def send_whatsapp_message(Juhadi, message):
#     # Buka WhatsApp Web di browserJuhadi

#     pyautogui.hotkey('ctrl', 't')
#     pyautogui.typewrite('https://web.whatsapp.com\n')
#     time.sleep(10)  # Tunggu beberapa detik untuk memuat halaman WhatsApp Web

#     # Cari kontak berdasarkan nama
#     pyautogui.typewrite(Juhadi)
#     time.sleep(0.5)
#     pyautogui.press('enter')
#     time.sleep(0.5)

#     # Ketik pesan
#     pyautogui.typewrite(message)
#     pyautogui.press('enter')


# # Contoh penggunaan
# send_whatsapp_message('Juhadi', 'Halo, ini adalah pesan dariku.')
##########################################################################################################################################
import pyautogui
import time


def send_whatsapp_message(Ade, message, max_messages=10):
    # Buka WhatsApp Web di browser
    pyautogui.hotkey('ctrl', 't')
    pyautogui.typewrite('https://web.whatsapp.com\n')
    time.sleep(10)  # Tunggu beberapa detik untuk memuat halaman WhatsApp Web

    # Cari kontak berdasarkan nama
    pyautogui.typewrite(Ade)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)

    # Batasi jumlah pesan yang akan dikirim
    for _ in range(max_messages):
        # Ketik pesan
        pyautogui.typewrite(message)
        pyautogui.press('enter')
        time.sleep(0.5)  # Tunggu sejenak sebelum mengirim pesan berikutnya


# Contoh penggunaanHalo, ini adalah pesan otomatis.

send_whatsapp_message(
    'hallo', 'Halo, ini adalah pesan otomatis.', max_messages=10)
