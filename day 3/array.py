menu_makanan = [
  "nasi goreng",
  "burger",
  "chicken",
  "dada ayam",
  "eclair"
]

indeks_makanan = 1
# array[indeks]
# array[start:stop:step]
# stop-nya gaada maka defaultnya akan sampai indeks terakhir
# 0, 2, 3
for makanan in menu_makanan[0::2]:
  print(f"{indeks_makanan}. {makanan}")
  indeks_makanan += 1