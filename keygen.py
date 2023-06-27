import numpy as np

# Memasukkan peringatan tentang batasan ukuran kunci
print("!!! Perhatian, lebar dan tinggi kunci harus LEBIH KECIL dari dimensi koefisien LL yang akan digunakan untuk menyisipkan informasi!")
print("Catatan: Pada level 1 transformasi wavelet, LL_h sama dengan setengah dari tinggi gambar (Image_h/2), LL_w sama dengan setengah dari lebar gambar (Image_w/2). Pada level 2 transformasi wavelet, LL_h sama dengan seperempat dari tinggi gambar (Image_h/4), LL_w sama dengan seperempat dari lebar gambar (Image_w/4), dan seterusnya.")
high_LL_min = input("Silakan masukkan tinggi minimal kunci: ")
high_LL_min = int(high_LL_min)
width_LL_min = input("Silakan masukkan lebar minimal kunci: ")
width_LL_min = int(width_LL_min)

# Pengaturan ukuran kunci
key = np.zeros((2,high_LL_min * width_LL_min))

# Algoritma Pembentukan Kunci
jj = 0
ii = 0
count = 0

for j in range(0,high_LL_min * width_LL_min):
    key[0][j] = ii
    key[1][j] = jj
    jj += 1
    count += 1
    if jj == width_LL_min:
        jj = 0
    if count == width_LL_min:
        ii += 1
        count = 0


# Menyimpan kunci ke file
key_file_name = 'key'
np.save(key_file_name, key)

print("Program berhasil. Kunci yang dihasilkan tersimpan dalam file: " + key_file_name + ".npy")