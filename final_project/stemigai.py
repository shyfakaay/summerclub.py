import random
input("Halo, selamat datang di Stemigai (STEM in Ikigai)! Tekan enter untuk melanjutkan.")

main_menu_message = """
STEM (Science, Technology, Engineering, and Mathematics) adalah kurikulum pendidikan yang sangat berfokus pada mata pelajaran Sains, Teknologi, Teknik, dan Matematika. Let's find your Ikigai in STEM!
Stemigai Menu : (Please choose an option)
1. Science
2. Technology
3. Engineering
4. Mathematics
5. Surprise Figure
6. Suprise Fact
7. Surprise Benefit
8. Exit
Pilihan: """

sciences = [["Biologi",
            "Ilmu hayat adalah kajian tentang kehidupan, dan organisme hidup, termasuk struktur, fungsi, pertumbuhan, evolusi, persebaran, dan taksonominya."],
           ["Fisika", 
            "Sains atau ilmu alam yang mempelajari materi beserta gerak dan perilakunya dalam lingkup ruang dan waktu, bersamaan dengan konsep yang berkaitan seperti energi dan gaya."],
           ["Kimia", 
            "Cabang dari ilmu fisik yang mempelajari tentang susunan, struktur, sifat, dan perubahan materi."],
            ["Astronomi", 
            "Ilmu alam yang mempelajari benda langit dan fenomena alam yang terjadi di luar Bumi, termasuk fenomena di atmosfer atas Bumi yang berasal dari luar angkasa seperti meteor dan aurora."],
            ["Geologi",
            "Salah satu cabang ilmu kebumian yang mempelajari tentang Bumi dan segala isi di dalamnya."]]

technologies = [["Computer Science",
            "Ilmu Komputer merupakan bidang studi yang identik dengan computer programming."],
           ["Cyber Security", 
            "Sistem dan proses yang diperlukan untuk melindungi komputer, jaringan, dan perangkat seluler dari serangan siber berbahaya."],
           ["Web Development", 
            "Ilmu yang mempelajari sebuah proses pembangunan dan pemeliharaan situs web."],
            ["Data Science", 
            "Ilmu yang menggabungkan sebuah kemahiran di bidang ilmu tertentu dengan keahlian pemrograman, matematika, dan statistik."],
            ["Internet of Things (IoT)",
            "Konsep yang bertujuan untuk memperluas manfaat dari konektivitas internet yang tersambung secara terus-menerus."]]

engineerings = [["Teknik Arsitektur",
            "Keilmuan yang mempelajari mendesain dan merancang bangunan dan struktur."],
           ["Teknik Sipil", 
            "Ilmu yang mempelajari tentang bagaimana merancang, membangun, merenovasi tidak hanya gedung dan infrastruktur tetapi juga mencakup lingkungan untuk kemaslahatan hidup manusia."],
           ["Teknik Informatika", 
            "Ilmu yang mempelajari terkait penggunaan komputer untuk mengatur dan menganalisis data yang berukuran besar, baik data maupun informasi pada mesin berbasis komputasi."],
            ["Teknik Mesin", 
            "Ilmu teknik mengenai aplikasi dari prinsip fisika untuk analisis, desain, manufaktur dan pemeliharaan sebuah sistem mekanik."],
            ["Teknik Elektro",
            "Ilmu teknik mengenai aplikasi listrik untuk memenuhi kebutuhan masyarakat, melibatkan konsep, perancangan, pengembangan, dan produksi peralatan listrik dan elektronik."]]

maths = [["Kalkulus",
            "Ilmu yang mempelajari perubahan, sebagaimana geometri yang mempelajari bentuk dan aljabar yang mempelajari operasi dan penerapannya untuk memecahkan persamaan."],
           ["Geometri", 
            "Cabang matematika yang bersangkutan dengan pertanyaan bentuk, ukuran, posisi relatif gambar, dan sifat ruang."],
           ["Statistika", 
            "Ilmu yang mempelajari bagaimana cara merencanakan, mengumpulkan, menganalisis, lalu menginterpretasikan, dan akhirnya mempresentasikan data"],
            ["Linear Algebra", 
            "Bidang studi matematika yang mempelajari sistem persamaan linear seperti pemetaan linear seperti dan representasinya dalam ruang vektor maupun dengan matriks. "],
            ["Differential Equations",
            "Persamaan matematika untuk fungsi satu variabel atau lebih, yang menghubungkan nilai fungsi itu sendiri dan turunannya dalam berbagai orde."]]

def random_inspiration():
  list_tokoh = [
    ["Marie Curie", "Marie Curie dianggap sebagai tokoh wanita terbesar dalam sains. Beliau menjadi wanita pertama yang menerima Hadiah Nobel pada tahun 1903 (fisika), kemudian menjadi penerima Hadiah Nobel ganda pada tahun 1911 (kimia), keduanya untuk karyanya tentang radiasi."],
    ["Rachel Carlson", "Rachel Carson adalah seorang ahli biologi laut dan konservasionis. Beliau merupakan salah satu pionir penggiat kelestarian alam dengan karyanya yang paling terkenal The Silent Spring yang menggambarkan betapa menyedihkan alam yang sudah rusak akibat ulah manusia. Bukunya menjadi pemicu protes terhadap penggunaan insektisida DDT yang akhirnya dilarang secara luas."],
    ["Valentina Tereshkova", "Valentina adalah seorang kosmonaut asal Uni Soviet yang menjadi wanita pertama di luar angkasa setelah dipilih dari lebih dari empat ratus pelamar dan lima finalis untuk pilot wahana Vostok 6 pada 16 Juni 1963. Dia menyelesaikan 48 orbit Bumi selama tiga hari di ruang angkasa."],
    ["Margaret Hamilton", "Hamilton adalah programer komputer dibalik suksesnya misi Apollo NASA mendarat di Bulan. Dia mengenalkan istilah software engineering sebagai salah satu cabang teknik, sama seperti hardware engineering."],
    ["Elizabeth Blackburn", "Blackburn adalah seorang Professor Biokimia dan Biofisika yang menemukan enzim telomerase dan hubungan antara telomer pada kromosom dengan proses penuaan. Telomer dijadikan sebagai sasaran studi pengobatan kanker pada penelitian lebih lanjut"]
  ]
  
  random_indeks = random.randint(0, len(list_tokoh) - 1)
  
  random_tokoh = list_tokoh[random_indeks]
  print(f"Kamu kenal {random_tokoh[0]}. Dia itu {random_tokoh[1]}")

def random_fact():
  list_fact = [
    ["50% of economic growth in the last 50 years was due to advances in technology. All key companies revolutionizing our lives (Google, Facebook, Apple, Amazon, etc) – STEM powers them."],
    ["Math and STEM would be key drivers of long-term economic growth."],
    ["Between 2017 and 2027, the number of STEM jobs is expected to double, compared to non-STEM jobs—with positions in computing, engineering, and advanced manufacturing leading the way."],
    ["STEM jobs would pay twice the average salary of non-STEM jobs. Generally, 90% of future jobs require digital literacy."],
    ["The demand in STEM-related careers will be greater than the number of individuals interested in those careers."],
    ["58% of all new jobs in STEM are in computing (coding, etc)"],
    ["China and India had the most STEM graduates in 2016 with 4.7 million and 2.6 million graduates respectively."],
    ["Anyone can move into a STEM-related career. Students can pursue a STEM education outside of school – summer camps, online, volunteer programs, etc"],
    ["Over 50% of teenagers have never considered a career in a STEM-related field"],
    ["Only 1 in 5 College students feel that their primary and secondary school education prepared them for STEM college courses"],
  ["More than half of teenagers (55%) would be more interested in STEM simply by having teachers who enjoy the subjects they teach."],
    ["If we don’t engage students by 5th grade in STEM, 92% of boys and 97% of girls will lose interest."],   
  ]
  
  random_indeks = random.randint(0, len(list_fact) - 1)
  
  random_fact = list_fact[random_indeks]
  print(f"{random_fact[0]}.")

def random_benefit():
  list_benefit = [
    ["Fosters ingenuity and creativity", "Ingenuity and creativity can pair with STEM and lead to new ideas and innovations. Without ingenuity and creativity, the recent developments in artificial intelligence or digital learning would not be possible. These technologies were created by people who learned that if the human mind can conceive it, the human mind can achieve it. No doubt they had a great K-12 STEM education teacher."],
    ["Builds resilience", "During STEM education activities, students learn in a safe environment that allows them to fall and try again. STEM education stresses the value of failure as a learning exercise, which will enable students to embrace mistakes as part of the learning process. This allows students to build confidence and resilience, which will enable them to keep going when the going gets rough. After all, failure is part of a process that ultimately leads to success."],
    ["Encourages experimentation", "Without a little risk-taking, and experimentation, many of the technological advancements that have occurred in the last couple of decades would not be possible. Many of these innovations were created by people who were told that their ideas wouldn’t work and their response was, Let’s try it and see. This type of attitude can be encouraged with STEM learning during the K-12 years. How can you accomplish this? By allowing students to experiment and take risks during learning activities."],
    ["Encourages teamwork", "STEM education can be taught to students of all ability levels. Students of varying levels of ability can work together in teams to find solutions to problems, record data, write reports, give presentations, etc. The end result is students who understand how to collaborate with others and thrive in a team-oriented environment."],
    ["Encourages knowledge application", "In STEM education, students are taught skills that they can use in the real world. This motivates students to learn, as they know that the skills that they acquire can be utilized immediately, and in ways that positively impact them and their loved ones. The ability to apply their knowledge to new and novel tasks will bode well for them when they enter the workforce."],
    ["Encourages tech use", "STEM learning teaches kids about the power of technology and innovation. So, when students encounter new technologies, they will be prepared to embrace them, instead of being hesitant or fearful. This will give them the upper hand in the global landscape, as the world is becoming increasingly tech-centered."],
    ["Teaches problem-solving", "STEM education teaches students how to solve problems by using their critical thinking skills. By engaging in STEM learn experiences, students learn how to examine problems and then create a plan to solve them."],
    ["Encourages adaption", "To succeed in life, students have to be able to apply what they have learned to a variety of scenarios. STEM education teaches them to adapt the concepts that they learn to various iterations of a problem or issue."]
  ]
  random_indeks = random.randint(0, len(list_benefit) - 1)
  
  random_benefit = list_benefit[random_indeks]
  print(f"{random_benefit[0]}, {random_benefit[1]}")

keluar = False
while not keluar:
  pilihan = int(input(main_menu_message))
  if pilihan == 1:
    
    print("Sub-major in Science")
    indeks_science = 1
    for science in sciences:
      print(f"{indeks_science}. {science[0]}")
      indeks_science += 1
    pilihan_science = int(input("Pilihan science: "))
    print(sciences[pilihan_science - 1][1])
  
  elif pilihan == 2:
    print("Sub-major in technology")
    indeks_technology = 1
    for technology in technologies:
      print(f"{indeks_technology}. {technology[0]}")
      indeks_technology += 1
    pilihan_technology = int(input("Pilihan technology: "))
    print(technologies[pilihan_technology - 1][1])
  
  elif pilihan == 3:
    print("Sub-major in engineering")
    indeks_engineering = 1
    for engineering in engineerings:
      print(f"{indeks_engineering}. {engineering[0]}")
      indeks_engineering += 1
    pilihan_engineering = int(input("Pilihan engineering: "))
    print(engineerings[pilihan_engineering - 1][1])
      
  elif pilihan == 4:
    print("Sub-major in math")
    indeks_math = 1
    for math in maths:
      print(f"{indeks_math}. {math[0]}")
      indeks_math += 1
    pilihan_math = int(input("Pilihan math: "))
    print(maths[pilihan_math - 1][1])
  
  elif pilihan == 5:
    random_inspiration()

  elif pilihan == 6:
    random_fact()

  elif pilihan == 7:
    random_benefit()
    
  elif pilihan == 8:
    print("Atasi STEM Inequality, Bersama Stemigai! Powered by Shyfa Kay (@generationgirl.id)")
    keluar = True
  else:
    print("Pilihan tidak dikenali")