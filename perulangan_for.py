#perulangan For
#perulangan for digunakan untuk mengulangi kode yang sama berulang kali dengan jumlah yang sudah diketahui.
#contoh penggunaan perulangan for

for i in range(5):
    print("Perulangan ke-", i)
#hasilnya:
#Perulangan ke- 0
#Perulangan ke- 1
#Perulangan ke- 2
#Perulangan ke- 3
#Perulangan ke- 4

#perulangan for juga dapat digunakan untuk mengulangi kode dengan jumlah yang sudah diketahui pada list, tuple, atau string
#contoh penggunaan perulangan for pada list, tuple, atau string

nama = ["Budi", "Andi", "Caca"]
for n in nama:
    print("Halo", n)


#perulangan for juga dapat digunakan untuk mengulangi kode dengan jumlah yang sudah diketahui pada dictionary
#contoh penggunaan perulangan for pada dictionary

siswa = {
    "nama": "Budi",
    "umur": 10,
    "alamat": "Jakarta"
}
for key in siswa:
    print(key, ":", siswa[key])
