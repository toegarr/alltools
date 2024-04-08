import time
import os
import colorama
from colorama import Fore, Style, Back
os.system('clear')
print(Style.BRIGHT, Fore.CYAN)
os.system('figlet SCRIPT HACK WHATSAPP')
print(Style.BRIGHT, Fore.YELLOW)

while True:
    print(Style.BRIGHT, Back.RED, Fore.WHITE + "SCRIPT HACK WA USING OTP ((PREMIUM))" + Style.RESET_ALL)
    print()
    print(Style.BRIGHT, Fore.YELLOW + "1. HACK WHATSAPP OTP")
    print(Style.BRIGHT, Fore.RED + "0. BUY SC (50K)")
    print()
    prank_choice = int(input(Fore.YELLOW + "PILIH : "))
    
    if prank_choice == 3:
        os.system('clear')
        os.system('figlet Ngepet')
        print()
        input_nomor = input('Masukkan nomor target : ')
        input_jumlah = int(input('Mau ngepet berapa kali : '))

        for _ in range(input_jumlah):
            print(Fore.RED + f"Berhasil ngepet nomor {input_nomor} sebanyak {input_jumlah} Kali")
            time.sleep(0.03)
        
        break  # Berhenti setelah perintah pertama selesai
        
    elif prank_choice == 1:
        os.system('clear')
        os.system('figlet WHATSAPP')
        input_satelit = input('MASUKAN NOMOR TARGET : ')
        time.sleep(1)
        print(Fore.CYAN + "SEDANG MENDAPATKAN KODE......")
        time.sleep(5)
        time.sleep(3)
        print(Fore.GREEN + f"BERHASIL MENDAPATKAN OTP ⚠️⚠️")
        print(Fore.RED + f"DENGAN NOMOR {input_satelit} KODE OTP : ******")
        break  # kode berhenti setelah perintah pertama selesai
        
    elif prank_choice == 0:
        print("BUY SC ? CHAT WA : 0852-1535-1487 (ADMIN)")
        break
      #selamat tinggal maksudnya 🗿

    else:
        print(Fore.RED + "Pilihan tidak valid.")
