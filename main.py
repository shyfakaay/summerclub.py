cangkir_putih = "kopi"
cangkir_bening = "teh"
gelas_bening = ""

print(f"Kondisi awal")
print(f"Cangkir putih: {cangkir_putih}")
print(f"Cangkir bening: {cangkir_bening}")
print(f"Gelas bening: {gelas_bening}")

# Step 1
gelas_bening = cangkir_bening

# Step 2
cangkir_bening = cangkir_putih

# Step 3
cangkir_putih = gelas_bening

print(f"\nKondisi akhir")
print(f"Cangkir putih: {cangkir_putih}")
print(f"Cangkir bening: {cangkir_bening}")
print(f"Gelas bening: {gelas_bening}")