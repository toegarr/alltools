import time
import os
import colorama
from colorama import Fore, Style, Back
os.system('clear')
print(Style.BRIGHT, Fore.CYAN)
os.system('figlet SCRIPT FACEBOOK TARGET')
print(Style.BRIGHT, Fore.YELLOW)

while True:
    print(Style.BRIGHT, Back.RED, Fore.WHITE + "NOTE! : SCRIPT HACK FACEBOOK ((PREMIUM)) " + Style.RESET_ALL)
    print()
    print(Style.BRIGHT, Fore.YELLOW + "1. HACK FACEBOOK")
    print(Style.BRIGHT, Fore.RED + "0. BELI SC (50k)")
    print()
    prank_choice = int(input(Fore.YELLOW + "Pilih : "))
    
    if prank_choice == 2:
        os.system('clear')
        os.system('figlet Facebook')
        print()
        input_nomor = input('Masukkan nomor target : ')
        input_jumlah = int(input('Mau ngepet berapa kali : '))

        for _ in range(input_jumlah):
            print(Fore.RED + f"Berhasil ngepet nomor {input_nomor} sebanyak {input_jumlah} Kali")
            time.sleep(0.03)
        
        break  # Berhenti setelah perintah pertama selesai
        
    elif prank_choice == 1:
        os.system('clear')
        os.system('figlet Facebook')
        input_satelit = input('MASUKAN ID FACEBOOK : ')
        time.sleep(1)
        print(Fore.CYAN + "SEDANG MENDAPATKAN PASSWORD.....")
        time.sleep(5)
        time.sleep(3)
        print(Fore.GREEN + f"TERDETEKSI ⚠️ : ANDA BUKAN PENGGUNA PREMIUM")
        print(Fore.RED + f"PASSWORD DENGAN ID {input_satelit} ADALAH *********** ✔️")
        break  # kode berhenti setelah perintah pertama selesai
        
    elif prank_choice == 0:
        print("BUY SC? WA : 0852-1535-1487 (ADMIN)")
        break
      #selamat tinggal maksudnya 🗿

    else:
        print(Fore.RED + "PILIHAN TIDAK VALID.")
