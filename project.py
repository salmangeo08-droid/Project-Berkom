# ==========================================
# VENDING MACHINE KOPI JUMPSTART
# ==========================================

# 1. SUBPROGRAM: Menampilkan Menu Utama & Harga
def tampilkan_menu(daftar_menu, daftar_harga):
    print("\n" + "=" * 45)
    print("       SILAKAN PILIH MENU KOPI JUMPSTART")
    print("=" * 45)
    for i in range(len(daftar_menu)):
        print(f"[{i + 1}] {daftar_menu[i]:<25} : Rp {daftar_harga[i]:,}")
    print("=" * 45)

# 2. SUBPROGRAM: Mengatur Suhu Minuman (Ice/Hot)
def pilih_suhu():
    print("\nPilih Suhu Minuman:")
    print("[1] Hot (Panas)")
    print("[2] Ice (Dingin)")
    while True:
        pilihan = input("Masukkan pilihan suhu (1/2): ")
        if pilihan == '1':
            return "Hot"
        elif pilihan == '2':
            return "Ice"
        else:
            print("Pilihan tidak valid. Silakan masukkan 1 atau 2.")

# 3. SUBPROGRAM: Mengatur Tingkat Kemanisan
def pilih_kemanisan():
    print("\nPilih Tingkat Kemanisan (Sugar Level):")
    print("[1] Normal Sugar (100%)")
    print("[2] Less Sugar (50%)")
    print("[3] No Sugar (0%)")
    while True:
        pilihan = input("Masukkan pilihan kemanisan (1/3): ")
        if pilihan == '1':
            return "Normal Sugar"
        elif pilihan == '2':
            return "Less Sugar"
        elif pilihan == '3':
            return "No Sugar"
        else:
            print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.")

# 4. SUBPROGRAM: Proses Pembayaran QRIS (Tanpa Kembalian)
def proses_pembayaran_qris(harga_total):
    print("\n" + "=" * 40)
    print("         PEMBAYARAN VIA QRIS")
    print("=" * 40)
    print(f"Total Tagihan : Rp {harga_total:,}")
    print("\n[QR CODE DIPERLIHATKAN DI LAYAR]")
    print("[  [████████]  ]")
    print("[  [██  ██  ]  ]")
    print("[  [████████]  ]")
    print("Silakan scan QRIS dengan aplikasi pembayaran/m-banking Anda.")
    
    while True:
        konfirmasi = input("\nKetik 'BAYAR' jika Anda sudah menyelesaikan pembayaran via QRIS: ").strip().upper()
        if konfirmasi == "BAYAR":
            print("\n>> Memverifikasi Pembayaran...")
            print(">> Pembayaran QRIS Berhasil Diverifikasi! [Status: LUNAS]")
            return True
        else:
            print("Pembayaran belum terdeteksi. Silakan ketik 'BAYAR' untuk konfirmasi.")

# 5. SUBPROGRAM: Simulasi Alur Kerja Mesin di Dunia Nyata
def buat_minuman(nama_menu, suhu, kemanisan):
    print("\n" + "=" * 45)
    print("   MESIN SEDANG MEMPROSES MINUMAN ANDA...")
    print("=" * 45)
    
    # Alur umum: Ambil cup dan letakkan
    print("[1] Mengeluarkan 1 buah Cup dari dispenser otomatis...")
    print(f"[2] Meletakkan Cup di posisi dispenser untuk {suhu} {nama_menu}...")
    
    # Percabangan Alur Berdasarkan Resep Dunia Nyata
    if "Chocolate" in nama_menu or "Mocha" in nama_menu:
        print("[3] Menuangkan bubuk cokelat premium ke dalam cup...")
        print(f"[4] Menambahkan takaran gula/pemanis: {kemanisan}...")
        print("[5] Menuangkan espresso shot segar...")
        if suhu == "Ice":
            print("[6] Menambahkan es batu secukupnya...")
        else:
            print("[6] Menambahkan air panas...")
        print("[7] Melakukan proses mixing/pengadukan otomatis...")
        
    elif "Latte" in nama_menu or "Cappucino" in nama_menu:
        print(f"[3] Menambahkan takaran gula/pemanis: {kemanisan}...")
        print("[4] Menuangkan espresso shot...")
        if suhu == "Ice":
            print("[5] Menambahkan es batu ke dalam cup...")
            print("[6] Menuangkan fresh milk dingin di atasnya...")
        else:
            print("[5] Melakukan steaming susu cair hingga berbusa...")
            print("[6] Menuangkan susu panas...")
        print("[7] Mengaduk ringan agar larutan homogen...")
        
    elif "Espresso" in nama_menu:
        print("[3] Menyiapkan portafilter dan gilingan biji kopi...")
        print("[4] Mengekstrak espresso murni ke dalam cup...")
        print("[5] Menambahkan susu segar sesuai porsi...")
        if suhu == "Ice":
            print("[6] Menambahkan es batu...")
        else:
            print("[6] Menghangatkan minuman...")
        print("[7] Minuman siap disajikan...")
        
    else: # Contoh untuk Kopi Gula Aren, Americano, dll.
        print(f"[3] Menambahkan takaran gula: {kemanisan}...")
        if suhu == "Ice":
            print("[4] Menambahkan es batu...")
            print("[5] Menuangkan air/susu...")
            print("[6] Menuangkan espresso shot di lapisan atas...")
        else:
            print("[4] Menuangkan air panas...")
            print("[5] Menuangkan espresso shot...")
            print("[6] Mengaduk larutan kopi...")
        print("[7] Menutup cup rapat dengan mesin sealer...")

    print("=" * 45)
    print(">> SELESAI! Silakan ambil pesanan Anda di slot pengambilan.")
    print("=" * 45)

# --- PROGRAM UTAMA ---
def main():
    # Array Nama Menu
    menu_kopi = [
        "Kopi Gula Aren",
        "Cafe Latte",
        "Dark Chocolate",
        "Americano",
        "Cappucino",
        "Cafe Mocha",
        "Espresso Milk Chocolate"
    ]
    
    # Array Harga Menu (Dalam rentang 8k - 15k)
    harga_kopi = [12000, 14000, 13000, 8000, 14000, 15000, 15000]

    # Loop Utama Transaksi
    while True:
        tampilkan_menu(menu_kopi, harga_kopi)
        
        # Validasi Pilihan Menu
        try:
            pilihan = int(input("\nPilih nomor menu yang diinginkan (1-7): "))
            if pilihan < 1 or pilihan > len(menu_kopi):
                print("Nomor menu tidak tersedia. Silakan pilih 1-7.")
                continue
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue
            
        indeks = pilihan - 1
        pilihan_terpilih = menu_kopi[indeks]
        harga_terpilih = harga_kopi[indeks]
        
        print(f"\nAnda memilih: {pilihan_terpilih} (Rp {harga_terpilih:,})")
        
        # Pilih Opsi Suhu dan Kemanisan
        suhu = pilih_suhu()
        kemanisan = pilih_kemanisan()
        
        # Proses Pembayaran QRIS
        status_bayar = proses_pembayaran_qris(harga_terpilih)
        
        # Pembuatan Minuman Jika Pembayaran Selesai
        if status_bayar:
            buat_minuman(pilihan_terpilih, suhu, kemanisan)
            
        # Perulangan untuk Transaksi Berikutnya
        ulang = input("\nApakah ada transaksi lain? (y/t): ").lower()
        if ulang != 'y':
            print("\nTerima kasih telah membeli di Jumpstart Coffee! Sampai jumpa!")
            break

# Eksekusi Program
if __name__ == "__main__":
    main()