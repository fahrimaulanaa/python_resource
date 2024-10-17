#perulangan While
#perulangan while digunakan untuk mengulangi kode yang sama berulang kali dengan jumlah yang belum diketahui.
#contoh penggunaan perulangan while

i = 0
while i < 5:
    print("Perulangan ke-", i)
    i += 1

#perulangan while juga dapat digunakan bersama-sama dengan else
#contoh penggunaan perulangan while bersama-sama dengan else

i = 0
while i < 5:
    print("Perulangan ke-", i)
    i += 1
else:
    print("Perulangan selesai")

#perulangan while juga dapat digunakan bersama-sama dengan break
#contoh penggunaan perulangan while bersama-sama dengan break

i = 0
while i < 5:
    print("Perulangan ke-", i)
    if i == 3:
        break
    i += 1
else:
    print("Perulangan selesai")

#perulangan while juga dapat digunakan bersama-sama dengan continue
#contoh penggunaan perulangan while bersama-sama dengan continue

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("Perulangan ke-", i)
else:
    print("Perulangan selesai")
