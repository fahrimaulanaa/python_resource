#operator pada python

#operator AND digunakan untuk menggabungkan dua kondisi, jika kondisi pertama dan kondisi kedua bernilai benar maka hasilnya adalah benar, jika salah satu kondisi bernilai salah maka hasilnya adalah salah
#contoh penggunaan operator AND

nilai_matematika = 90
nilai_bahasa_indonesia = 80
if nilai_matematika > 80 and nilai_bahasa_indonesia > 75:
    print("Selamat, anda lulus!")
else:
    print("Maaf, anda tidak lulus")

#operator OR digunakan untuk menggabungkan dua kondisi, jika kondisi pertama atau kondisi kedua bernilai benar maka hasilnya adalah benar, jika kedua kondisi bernilai salah maka hasilnya adalah salah
#contoh penggunaan operator OR

nilai_matematika = 70
nilai_bahasa_indonesia = 90
if nilai_matematika > 80 or nilai_bahasa_indonesia > 75:
    print("Selamat, anda lulus!")
else:
    print("Maaf, anda tidak lulus")

#operator NOT digunakan untuk membalikkan kondisi, jika kondisi bernilai benar maka hasilnya adalah salah, jika kondisi bernilai salah maka hasilnya adalah benar
#contoh penggunaan operator NOT

nilai_matematika = 70
nilai_bahasa_indonesia = 90
if not nilai_matematika > 80:
    print("Maaf, anda tidak lulus")
else:
    print("Selamat, anda lulus!")

#operator AND, OR, dan NOT dapat digunakan bersama-sama
#contoh penggunaan operator AND, OR, dan NOT

nilai_matematika = 70
nilai_bahasa_indonesia = 90
if (nilai_matematika > 80 or nilai_bahasa_indonesia > 75) and not (nilai_matematika == 0):
    print("Selamat, anda lulus!")
else:
    print("Maaf, anda tidak lulus")

#operator perbandingan digunakan untuk membandingkan dua nilai, operator perbandingan menghasilkan nilai benar atau salah
#operator perbandingan terdiri dari:
# - lebih besar dari (>)
# - lebih kecil dari (<)
# - sama dengan (==)
# - tidak sama dengan (!=)
# - lebih besar sama dengan (>=)
# - lebih kecil sama dengan (<=)
#contoh penggunaan operator perbandingan

nilai_matematika = 70
nilai_bahasa_indonesia = 90
if nilai_matematika > nilai_bahasa_indonesia:
    print("Nilai matematika lebih besar dari nilai bahasa indonesia")
else:
    print("Nilai matematika lebih kecil dari nilai bahasa indonesia")

#operator perbandingan dapat digunakan bersama-sama dengan operator AND, OR, dan NOT
#contoh penggunaan operator perbandingan bersama-sama dengan operator AND, OR, dan NOT

nilai_matematika = 70
nilai_bahasa_indonesia = 90
if nilai_matematika > 80 and nilai_bahasa_indonesia > 75:
    print("Selamat, anda lulus!")
else:
    print("Maaf, anda tidak lulus")

#operator perbandingan juga dapat digunakan untuk membandingkan dua string
#contoh penggunaan operator perbandingan untuk membandingkan dua string

nama = "Budi"
if nama == "Budi":
    print("Halo Budi!")
else:
    print("Siapa kamu?")

#operator in digunakan untuk mengecek apakah sebuah nilai terdapat dalam sebuah list, tuple, atau string
#contoh penggunaan operator in

nama = "Budi"
if nama in ["Budi", "Andi", "Caca"]:
    print("Halo", nama)
else:
    print("Siapa kamu?")

#operator is digunakan untuk mengecek apakah dua buah variabel merujuk pada objek yang sama
#contoh penggunaan operator is

a = [1, 2, 3]
b = a
if a is b:
    print("a dan b merujuk pada objek yang sama")
else:
    print("a dan b merujuk pada objek yang berbeda")

