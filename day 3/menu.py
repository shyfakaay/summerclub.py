main_menu_message = """
Menu
1. Let's talk about movie
2. Let's talk about food
3. Let's talk about boyband
4. Exit
Pilihan: """

movies = ["Dr. Strange", "Ngeri-ngeri Sedap"]

keluar = False
while not keluar:
  pilihan = int(input(main_menu_message))
  if pilihan == 1:
    
    keluar_movie = False
    while not keluar_movie:
      print("Daftar film")
      indeks_movie = 1
      for movie in movies:
        print(f"{indeks_movie}. {movie}")
        indeks_movie += 1
      pilihan_movie = int(input("Pilihan movie: "))
      print(movies[pilihan_movie - 1])
  
  elif pilihan == 2:
    print("Pizza is yummy!")
  elif pilihan == 3:
    print("BTS gonna be hiatus..")
  elif pilihan == 4:
    keluar = True
  else:
    print("Pilihan tidak dikenali")