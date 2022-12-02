import os
import sys
import time
from datetime import date
from cplan_sock import send_command


def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def main(host, port):
    while True:
        clear()
        print("Halo Selamat Datang di CPlan ^_^")
        today = date.today()
        print("Tanggal hari ini:", today)
        print("-------------------------------------------------------------")
        print("List Agenda:\n ")
        current_list = send_command(host, port, 'list')
        print(current_list)
        print("[1] Tambah Agenda  [2] Hapus Agenda  [3] Refresh  [4] Keluar")
        print("-------------------------------------------------------------")
        choice = input("Pilih [1-3]: ")
        if not choice.isdigit():
            continue
        choice = int(choice)
        if choice == 1:
            menu_tambah(host, port)
        elif choice == 2:
            menu_hapus(host, port)
        elif choice == 3:
            continue
        elif choice == 4:
            break
        time.sleep(1)
        
        


def menu_tambah(host, port):
    date = input('Tanggal [YYYY-MM-DD]: ')
    desc = input('Deskripsi agenda    : ')
    res = send_command(host, port, f'add {date} {desc}')
    if res == 'OK':
        print('Data berhasil ditambahkan!')
    else:
        print('Error')


def menu_hapus(host, port):
    date = input('Tanggal [YYYY-MM-DD]: ')
    desc = input('Kata kunci deskripsi: ')
    delete = send_command(host, port, f'del {date} {desc}')
    if delete == 'OK':
        print('Data berhasil dihapus!')
    else:
        print('Error')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f'usage: {sys.argv[0]} <host> <port>')
        sys.exit(2)
    main(sys.argv[1], int(sys.argv[2]))
