from statistics import mean

hp_prices = [["iphone", 12000000], ["samsung", 8000000], ["vivo", 6000000], ["oppo", 4700000], ["xiaomi", 6600000], ["realme", 3600000]]



def display_menu():
    print("\n ======== Menu ======== ")
    print("1. Lihat seluruh data")
    print("2. Tambah data")
    print("3. Hapus data")
    print("4. Ubah harga")
    print("5. Hitung harga rata-rata")
    print("6. Keluar")
    print("\n ========================")


def lihat_data():
    print("\nData Harga HP :")

    #data ne kalo kosong
    if not hp_prices:
        print("Ga ada data.")
        return
    
    #Ni buat ngeliatin setiap merek dan harga
    for hp, harga in hp_prices:
        print(f"- {hp}: Rp{harga:,}")


def tambah_data():
    hp = input("Masukkan nama HP: ")
    try:
        harga = int(input("Masukkan harga HP: "))
        hp_prices.append([hp, harga])
        print(f"Data {hp} dengan harga Rp{harga:,} berhasil ditambahkan.")
    except ValueError:
        print("Harga harus berupa angka. Data tidak ditambahkan.")


def hapus_data():
    hp = input("Masukkan nama HP yang ingin dihapus: ")
    for i, (nama, harga) in enumerate(hp_prices):
        if nama.lower() == hp.lower():
            del hp_prices[i]
            print(f"Data {nama} berhasil dihapus.")
            return
    print(f"Data {hp} tidak ditemukan.")


def hitung_rata_rata():
    if not hp_prices:
        print("Tidak ada data untuk dihitung.")
        return
    harga_list = [harga for _, harga in hp_prices]
    rata_rata = mean(harga_list)
    print(f"Harga rata-rata HP: Rp{rata_rata:,.2f}")


def ubah_harga():
    hp = input("Masukkan nama HP yang ingin diubah harganya: ")
    for i, (nama, harga) in enumerate(hp_prices):
        if nama.lower() == hp.lower():
            try:
                new_price = int(input(f"Masukkan harga baru untuk {nama}: "))
                hp_prices[i][1] = new_price
                print(f"Harga {nama} berhasil diubah menjadi Rp{new_price:,}.")
            except ValueError:
                print("Harga harus angka, bukan yang laen")
            return
    print(f"Data {hp} tidak ditemukan.")



def main():
    while True:
        display_menu()
        choice = input("Pilih menu (1-6): ")

        if choice == "1":
            lihat_data()
        elif choice == "2":
            tambah_data()
        elif choice == "3":
            hapus_data()
        elif choice == "4":
            ubah_harga()
        elif choice == "5":
            hitung_rata_rata()
        elif choice == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":    
    main()