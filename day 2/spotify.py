daftar_lagu_senang [a, b, c, d, e]:
daftar_lagu_sedih [f, g, h, i, j];
  print(len(daftar_lagu_senang))

mood = input("Mood: ")
pilihan_angka = int(input(f"Pilih angka dari {0}-{len(daftar_lagu_senang)}:"))

if mood.lower() == "senang":
  if 0 <= pilihan_angka <= len(daftar_lagu_senang):
    print(daftar_lagu_senang[pilihan_angka])
  else:

#END
