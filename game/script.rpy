# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# define e = Character("Eileen")
define aditya = Character("Aditya") # polisi
define dito = Character("Dito") # pejabat koruptor
define akbar = Character("Akbar") # kepala polisi
define informan = Character("Informan") # informan misterius
define ahmad = Character("Ahmad") # mandor
define andre = Character("Andre") # manajer proyek
define bodyguard = Character("Bodyguard") # bodyguard

image aditya happy = im.Scale("images/chara/aditya/aditya happy.png", 360, 920)
image aditya angry = im.Scale("images/chara/aditya/aditya angry.png", 360, 920)
image dito happy = im.Scale("images/chara/dito/dito happy.png", 360, 920)
image dito sad = im.Scale("images/chara/dito/dito sad.png", 360, 920)
image akbar = im.Scale("images/chara/akbar/akbar.png", 360, 920)
image informan = im.Scale("images/chara/informan/informan.png", 360, 920)
image ahmad happy = im.Scale("images/chara/ahmad/ahmad happy.png", 480, 920)
image ahmad sad = im.Scale("images/chara/ahmad/ahmad sad.png", 480, 920)
image andre = im.Scale("images/chara/andre/andre.png", 360, 920)
image bodyguard = im.Scale("images/chara/bodyguard/bodyguard.png", 360, 920)

# image bg rumah day = im.Scale("images/bg/rumah day.png", 1920, 1080)
image bg prison = im.Scale("images/bg/bg prison.png", 1920, 1080)
image bg lapangan night = im.Scale("images/bg/bg lapangan night.png", 1920, 1080)

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg kantor day with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    "Pada tahun 1994 Kota Koralia, suatu kota di suatu negara kepulauan tropis, sedang dihebohkan oleh kasus ambruknya suatu jembatan yang menewaskan puluhan orang."

    "Setelah diselidiki, ternyata hampir setengah dari anggaran untuk membangun jembatan tersebut tidak digunakan semestinya."

    "Akibatnya jembatan tersebut terpaksa dibangun dengan material tidak sesuai dengan standar. Dan akhirnya menewaskan puluhan orang yang tidak bersalah."

    "Lalu akhirnya kepolisian kota tersebut mengutus seorang polisi untuk mengusut tuntas kasus korupsi tersebut."

# SCENE 1
label scene1:
    scene bg kantor day with fade

    show akbar at left
    akbar "Aditya, mulai hari ini kamu resmi menjadi penyidik utama dari kasus korupsi ini!"
    hide akbar

    show aditya happy at right
    aditya "Baik pak, saya tidak akan mengecewakan bapak."
    hide aditya

    show akbar at left
    akbar "Bagus, karena jika kamu gagal, kamu bukan hanya mengecewakan saya, tapi juga kamu akan mengecewakan warga kota ini semua. "
    hide akbar

    show aditya happy at right
    aditya "Siap pak, apakah kita mempunyai petunjuk di kasus ini?"
    hide aditya

    show akbar at left
    akbar "Ya, kamu bisa mengunjungi mandor dari proyek jembatan itu, Ahmad Surya, di rumahnya di Jalan Serumpun No 5"
    hide akbar

    jump scene2
    
# SCENE 2
label scene2:
    scene bg halaman day with fade

    show aditya happy
    play sound "suara ketuk pintu.mp3"
    aditya "*Mengetuk pintu*"
    hide aditya

    show ahmad happy
    play sound "suara buka pintu.mp3"
    ahmad "*Membuka pintu*"
    hide ahmad

    show aditya happy
    aditya "Selamat pagi pak Ahmad, saya Aditya dari kepolisian ingin bertanya beberapa hal."
    hide aditya

    show ahmad sad
    ahmad "Loh tapi kan kemarin saya sudah ke kantor polisi dan terbukti tidak bersalah."
    hide ahmad

    show aditya happy
    aditya "Iya saya tahu pak, kebetulan saya adalah penyidik utama dalam kasus ini, saya hanya ingin mengkonfirmasi kembali."
    hide aditya

    show ahmad sad
    ahmad "Ck, ya sudah , apa mau ditanyakan?"
    hide ahmad

    show aditya happy
    aditya "Baik, pertama-tama beritahu saya semua hal yang bapak ketahui mengenai proyek jembatan kemarin!"
    hide aditya

    show ahmad sad
    ahmad "Proyek itu “dipegang” oleh PT Taruna Alam yang bekerjasama dengan Dinas Pekerjaan Umum Kota Koralia."
    ahmad "Saya hanya bekerja sebagai mandor saja disana. Atasan saya, Pak Andre Gunawan, beliau yang bertanggung jawab penuh atas proyek jembatan itu."
    hide ahmad

    show aditya happy
    aditya "Apa benar jembatan tersebut dibangun menggunakan material yang tidak sesuai dengan standar?"
    hide aditya

    show ahmad sad
    ahmad "Ya benar, pada saat itu kami terpaksa untuk melakukannya karena anggaran kami benar-benar tipis."
    hide ahmad

    show aditya happy
    aditya "Lalu apa yang dikatakan oleh Pak Andre mengenai hal itu?"
    hide aditya

    show ahmad sad
    ahmad "Beliau tidak pernah memberikan jawaban jelas, selalu menghindar."
    hide ahmad

    show aditya happy
    aditya "Dan untuk Dinas Pekerjaan Umum? Apakah anda tahu siapa saja yang terlibat dalam proyek ini?"
    hide aditya

    show ahmad sad
    ahmad "Kalau itu saya tidak tahu apa-apa. Karena Pak Andre yang mengurus semua hal itu."
    hide ahmad

    show aditya happy
    menu:
        "Baik, apakah saya boleh minta alamat Pak Andre?":
            jump scenario1
        "Kok rasanya bapak seperti berbohong ya?":
            jump scenario2


label scenario1:
    show aditya happy
    aditya "Hmm… Baik, boleh saya minta alamat rumahnya Pak Andre?"
    hide aditya

    show ahmad happy
    ahmad "Sebenarnya saya tidak boleh memberikan informasi ini, tapi akan saya bantu anda untuk mengusut kasus ini. Rumah beliau ada di Jalan Matahari No 43."
    hide ahmad

    show aditya happy
    aditya "Baik, terima kasih, mohon maaf mengganggu waktunya Pak Ahmad."
    hide aditya

    jump scene3

# SCENE 3
label scene3:
    scene bg rumah day with fade

    show aditya happy
    play sound "suara ketuk pintu.mp3"
    aditya "*Mengetuk pintu*"
    hide aditya

    show andre
    play sound "suara buka pintu.mp3"
    andre "*Membuka pintu*"
    hide andre

    show aditya happy
    aditya "Selamat siang pak, apa benar ini kediaman Bapak Andre Gunawan?"
    hide aditya

    show andre
    andre "Siang, iya benar, bapak pasti dari kepolisian."
    hide andre

    show aditya happy
    aditya "Benar pak, saya kesini hanya ingin bertanya mengenai beberapa hal saja."
    hide aditya

    show andre
    andre "Hm."
    hide andre

    show aditya happy
    aditya "Apa saja yang bapak ketahui mengenai proyek jembatan kemarin?"
    hide aditya

    show andre
    andre "Saya rasa bapak sudah tahu semua hal yang saya ketahui tentang proyek jembatan itu."
    hide andre

    show aditya happy
    aditya "Ok,  tapi bisakah bapak beritahu saya mengenai siapa saja yang terlibat dalam proyek ini di Dinas Pekerjaan Umum Kota Koralia?"
    hide aditya

    show andre
    andre "Dinas Pekerjaan Umum? Saya tidak apa-apa tentang itu."
    hide andre

    show aditya happy
    menu:
        "Hmm... Baiklah.":
            jump scenario1_2
        "Anda jangan coba membohongi saya!":
            jump scenario1_1

label scenario1_1:
    show aditya happy
    aditya "Anda jangan coba membohongi saya! Saya tahu bapak yang berurusan dengan Dinas Pekerjaan Umum selama mengerjakan proyek itu."
    hide aditya

    show andre
    andre "..."
    hide andre

    show aditya happy
    aditya "Sekarang saya ingin anda memberitahu siapa saja yang terlibat dalam proyek itu dari Dinas Pekerjaan Umum. Dan jangan coba membohongi saya lagi."
    hide aditya

    show andre
    andre "Pak Dito Saputra."
    hide andre

    show aditya happy
    aditya "Dito Saputra?"
    hide aditya

    show andre
    andre "Iya. Direktorat Jenderal Bina Konstruksi Dinas Pekerjaan Umum Kota Koralia."
    hide andre
    
    show aditya happy
    aditya "Siapa lagi yang terlibat?"
    hide aditya

    show andre
    andre "Hanya dia saja dan bawahannya."
    hide andre

    show aditya angry
    aditya "Anda yakin? Jangna coba untuk membohongi saya lagi!"
    hide aditya

    show andre
    andre "Ya."
    hide andre

    show aditya happy
    aditya "Ok, terima kasih atas waktunya."
    hide aditya

    jump scene5

# SCENE 5
label scene5:
    scene bg room with fade

    show aditya happy at right
    aditya "Selamat siang, Pak Dito."
    hide aditya

    show dito happy at left
    dito "Pak Aditya ya? Asisten saya memberitahu bahwa bapak akan datang, jadi sudah saya siapkan kopi untuk bapak."
    hide dito

    show aditya happy at right
    aditya "Bapak tidak usah repot-repot. Saya tidak akan lama."
    hide aditya

    show dito happy at left
    dito "Ah repot apa? Sudah menjadi kewajiban saya sebagai tuan rumah untuk menjamu tamu. Apa yang bisa saya bantu hari ini?"
    hide aditya

    show aditya happy at right
    aditya "Saya ingin bertanya beberapa hal mengenai proyek jembatan itu. Saya dengar peran bapak cukup besar dalam proyek itu. Apa itu benar?"
    hide aditya

    show dito happy at left
    dito "Ya benar sekali Pak Aditya. Saya memiliki kewajiban untuk mengawasi proyek itu dan juga anggarannya."
    hide dito

    show aditya happy at right
    aditya "Anggaran? Apakah saya bisa melihat riwayat transaksinya?"
    hide aditya

    show dito happy at left
    dito "Ya tentu, saya ambilkan dulu. Oh ya, selama saya mengambil berkasnya, bapak bisa meminum kopinya terlebih dahulu, itu kopi asli dari kampung halaman saya."
    hide dito

    show aditya happy at right
    aditya "Oh iya terima kasih Pak, maaf merepotkan."
    aditya "*Minum kopi*"
    hide aditya

    show dito happy at left
    dito "Ini dia berkasnya pak."
    hide dito

    show aditya happy at right
    aditya "Terima kasih Pak. Saya cek terlebih dahulu."
    aditya "*Membaca berkas*"
    aditya "..."
    aditya "LOH?! Kenapa banyak uang yang..."
    aditya "Bapak adalah koruptornya! Bapak adalah orang yang telah menyebabkan puluhan nyawa tidak bersalah menghilang!"
    hide aditya

    show dito happy at left
    dito "*Menepuk tangan*"
    dito "Selamat Pak Aditya, Anda telah menemukan sang koruptor."
    hide dito

    show aditya angry at right
    aditya "Angkat tangan anda! Anda ditangkap atas tuduhan korupsi!"
    hide aditya

    show dito happy at left
    dito "Sabar Pak Aditya, saya ingin menawarkan suatu kesempatan kepada bapak."
    dito "Saya akan menanggung semua kebutuhan kehidupan bapak dan keluarga bapak."
    dito "Tetapi saya ingin bapak untuk bergabung dengan saya."
    hide dito

    show aditya happy
    menu:
        "Baiklah saya setuju":
            jump scenario1_1_1
        "Tidak, saya tidak akan pernah bergabung dengan anda!":
            jump scenario1_1_2

label scenario1_1_1:
    show aditya happy at right
    aditya "Baiklah saya setuju untuk bergabung dengan anda."
    hide aditya

    show dito happy at left
    aditya "Haha, suatu keputusan yang bijak sekali Pak Aditya!"
    hide dito

    # BAD ENDING
    scene black with fade
    "Sebuah keputusan yang sangat tercela untuk seorang petugas kepolisian, bergabung dengan koruptor dan menjadi bagian dari kejahatan itu sendiri."
    return 

label scenario1_1_2:
    show aditya angry at right
    aditya "Tidak, saya tidak akan pernah bergabung dengan anda!"
    hide aditya

    show dito happy at left
    dito "Haha, suatu keputusan yang bodoh sekali Pak Aditya!"
    hide dito

    show aditya angry at right
    aditya "Sekarang, angkat tangan an.."
    hide aditya

    show dito happy at left
    dito "Kenapak Pak Aditya? Mengantuk ya??"
    hide dito

    show aditya angry at right
    aditya "..."
    aditya "Apa yang..."
    aditya "..."
    aditya "KOPINYA?! Anda racuni kop-"
    play sound "suara jatuh ke lantai.mp3"
    aditya "*Jatuh ke lantai*"
    hide aditya

    jump scene14

# SCENE 14
label scene14:
    scene bg lapangan night with fade

    show aditya happy
    aditya "Argh... pusing sekali kepala ku."
    hide aditya

    show dito happy
    dito "Ya, itu efek samping obatnya."
    hide dito

    show aditya happy
    aditya "HEY! Lepaskan saya sekarang juga!"
    hide aditya

    show dito happy
    dito "Saya sudah memberi Anda kesempatan Pak Aditya."
    hide dito

    show akbar
    akbar "Hm..."
    hide akbar

    show aditya happy
    aditya "LOH?! Pak Kepala, kenapa Anda di sini?! Cepat bantu saya!"
    hide aditya

    show akbar
    akbar "Sayang sekali harus berakhir seperti ini Aditya."
    akbar "Kamu menyia-nyiakan kesempatan itu."
    hide akbar

    show aditya happy
    aditya "APA?! Arghhh Anda ternyata komplotan koruptor juga, dasar polisi licik!"
    hide aditya

    show akbar
    akbar "Bukan licik tapi pintar."
    akbar "Sangat disayangkan, padahal kita baru saja bertemu, tetapi sekarang kita harus berpisah lagi, untuk selamanya."
    akbar "Selamat tinggal Pak Aditya, senang bertemu dengan anda."
    hide akbar

    show aditya happy
    aditya "Bicara apa And-"
    hide aditya

    scene black

    play sound "suara tembakan.mp3"
    "*Suara Tembakan*"
    # WORST ENDING
    
    "Menjadi seorang penegak keadilan adalah hal yang terpuji, tetapi menyelam ke sana dengan naif dan tanpa persiapan yang matang adalah hal yang bodoh."

    return

label scenario2:
    show aditya happy
    aditya "Kok rasanya, bapak seperti berbohong ya?"
    hide aditya

    show ahmad sad
    ahmad "Apa? kurang ajar sekali anda, anda sudah mengganggu saya pagi-pagi lalu menuduh saya berbohong? Pergi sana dan jangan pernah kembali lagi!"
    hide ahmad

    jump scene4

label scenario1_2:
    show aditya happy
    aditya "Hmm..."
    hide aditya

    show andre
    andre "Apa ada yang ingin Anda tanyakan lagi?"
    hide andre

    show aditya happy
    aditya "Sepertinya tidak, terima kasih atas waktunya Pak Andre."
    hide aditya

    jump scene4

label scene4:
    scene bg kantor day with fade

    show akbar at left  
    akbar "Bagaimana? Dapat informasi penting?"
    hide akbar

    show aditya happy at right  
    aditya "Sayangnya tidak Pak."
    hide aditya

    show akbar at left
    akbar "Saya tidak mau tahu, kamu harus selesaikan kasus ini secepatnya!"
    hide akbar

    show aditya happy at right
    aditya "Baik pak."
    hide aditya

    show akbar at left
    akbar "Oh iya, sekitar satu jam lalu ada surat buat kamu. Saya simpan di meja kamu."
    hide akbar

    show aditya happy at right
    aditya "Surat?"
    hide aditya

    show aditya happy
    aditya "*Membaca surat*"
    aditya '"Halo Pak Aditya, saya dengar bapak baru saja ditunjuk menjadi penyidik utama untuk kasus jembatan itu ...'
    aditya '... Siapa saya itu tidaklah penting, tetapi saya mempunyai informasi yang mungkin ingin bapak ketahui, seorang koruptor di Dinas Pekerjaan Umum yang terlibat dalam proyek itu. ...'
    aditya '... Jika anda ingin mengetahui informasi itu, datanglah ke Jalan Suryagiri No 45 jam 3 sore ini, belakang Toko Roti Sahaja, kita bertemu disana. ...'
    aditya '... Tapi, DATANGLAH SENDIRI, jika anda memberitahu rekan anda atau Kepala Polisi tentang ini, anda tidak akan mendapatkan apa-apa. ...'
    aditya '... Karena saya tahu anda polisi yang jujur, tapi sayangnya saya tidak mempunyai pemikiran yang sama tentang rekan anda. ...'
    aditya '... Saya tahu beberapa rekan anda itu \'kotor\', maka dari itu saya meminta anda untuk datang sendiri."'

    menu:
        "*Beritahu Kepala Polisi*":
            jump scenario2_1
        "*Datang sendiri*":
            jump scenario2_2

label scenario2_1:
    show aditya happy at right  
    aditya "Pak, ada informasi penting yang bapak harus ketahui."
    aditya "*Memberikan surat*"
    hide aditya

    show akbar at left  
    akbar "*Membaca surat*"
    akbar "Hmm.. Aditya, siapkan pasukkan, kita sergap dia di toko roti itu."
    akbar "Saya yakin adalah sebuah jebakan."
    akbar "Informan ini pasti orang suruhan sang koruptor yang dibayar untuk menutupi kasus ini."
    hide akbar

    jump scene7

# SCENE 7
label scene7:
    scene bg jalan afternoon

    play sound "suara langkah kaki.mp3"
    "*Suara langkah kaki*"

    show aditya happy
    "*???*"
    hide aditya

    show informan  
    informan "Halo Pak Aditya."
    hide informan

    show aditya happy
    aditya "Siapa anda?"
    hide aditya

    show informan
    informan "Sabar Pak Aditya, ada beberapa syarat yang harus anda penuhi terlebih dahulu."
    hide informan

    show aditya happy
    aditya "Syarat? Apa itu?"
    hide aditya

    show informan
    informan "Keamanan, saya mempertaruh keamanan saya dan keluarga saya dengan membocorkan informasi ini kepada anda."
    hide informan

    show aditya happy
    aditya "Maaf, tapi sepertinya saya tidak bisa memberikan anda itu."
    hide aditya

    show akbar  
    akbar "Hm.."
    hide akbar

    show informan
    informan "Apa?! Eh, apa ini?! Kenapa anda datang dengan rekan anda?!"
    hide informan

    show akbar
    akbar "Angkat tangan! Anda ditangkap!"
    hide akbar

    show informan
    informan "Arghh!!! Saya pikir saya bisa mempercayai anda Pak Aditya!"
    hide informan

    show aditya happy
    aditya "Anda memang bisa mempercayai saya, tapi saya tidak bisa mempercayai anda."
    hide aditya

    jump scene8

# SCENE 8
label scene8:
    scene bg kantor day with fade

    show akbar at left  
    akbar "Benar dugaan saya, tadi itu adalah sebuah jebakan."
    akbar "Dia adalah Reza Kurniawan, seorang pegawai di Dinas Pekerjaan Umum Kota Koralia."
    akbar "Setelah menginterogasi dan menekannya, akhirnya dia buka mulut."
    akbar "Dia bilang Andre Gunawan, sang manajer proyek lah yang telah melakukan korupsi pada proyek jembatan itu."
    hide akbar

    show aditya happy at right  
    aditya "Andre Gunawan?! Apa buktinya?"
    hide aditya

    show akbar at left
    akbar "Dia bilang terdapat berkas yang berisikan informasi tentang hal itu di kantor Dinas Pekerjaan Umum."
    akbar "Aditya, sekarang kamu pergi ke rumah Andre, dan tangkap dia. Kami akan mengurus berkas itu."
    hide akbar

    show aditya happy at right
    aditya "Dan bagaimana dengan informasi yang dia sebut dalam surat?"
    hide aditya 

    show akbar at left
    akbar "Itu tidak lebih dari hanya bualan dia saja untuk menjebakmu."
    akbar "Untungnya kamu melaporkan surat itu kepada saya."
    akbar "Jika tidak, saya tidak tahu apa yang akan terjadi kepadamu. Sekarang, pergilah ke rumah Andre!"
    hide Akbar

    show aditya happy at right
    aditya "Apakah saya boleh bertemu dengan Reza terlebih dahulu?"
    hide aditya

    show akbar at left
    akbar "Tidak perlu! Kita harus bergerak cepat sebelum Andre kabur!"
    hide akbar

    show aditya happy at right
    aditya "Siap pak!"
    hide aditya
    
    jump scene10

# SCENE 10
label scene10:
    scene bg rumah day with fade

    show aditya happy
    play sound "suara ketuk pintu.mp3"
    "*Mengetuk pintu*"
    hide aditya

    show andre
    play sound "suara buka pintu.mp3"
    andre "*Membuka pintu*"
    andre "Ada yang bisa say... arghhh"
    hide andre

    show aditya angry
    aditya "Jangan bergerak! Anda ditangkap!"
    hide aditya

    show andre
    andre "Loh apa-apaan ini?"
    hide andre

    show aditya angry
    aditya "Diam! Anda dapat menjelaskannya semua di kantor polisi!"
    hide aditya

    jump scene11

# SCENE 11
label scene11:
    scene bg prison

    show andre at left  
    andre "Apa-apaan ini?!"
    hide andre

    show aditya happy at right  
    aditya "Anda adalah koruptor dari proyek jembatan itu kan?"
    hide aditya

    show andre at left
    andre "HAH?! Apa maksud anda?! Apa buktinya?! Jangan sembarangan menuduh orang!"
    hide andre

    show aditya happy at right
    aditya "Kita telah menangkap orang suruh mu, Reza."
    aditya "Setelah anda mengetahui bahwa saya adalah penyidik utama kasus ini, anda berusaha untuk menjebak saya dengan menyuruh bawahan anda berpura-pura menjadi seorang informankan?"
    hide aditya

    show andre at left
    andre "REZA?! Reza siapa?!"
    hide andre

    show aditya happy at right
    aditya "Reza Kurniawan, seorang pegawai di Dinas Pekerjaan Umum yang sekaligus bawahan anda. Tidak usah pura-pura pikun anda!"
    hide aditya

    show andre at left
    andre "HAH?????"
    hide andre

    show akbar  
    play sound "suara buka pintu.mp3"
    akbar "*Membuka pintu*"
    hide akbar

    show akbar at right
    akbar "Kami mendapatkan berkas itu, memang benar dia adalah seorang koruptor."
    akbar "*Menyerahkan berkas*"
    hide akbar

    show aditya happy at left
    aditya "*Membaca berkas*"
    aditya "Hm. Pak Andre, anda ditangkap atas tuduhan korupsi yang menyebabkan hilangnya puluhan nyawa orang tidak bersalah."

    # BAD ENDING

    scene black with fade
    "Kamu terlalu naif untuk mencari keadilan di dunia ini. Sehingga kamu tidak sadar bahwa kamu telah menjadi boneka dari 'keadilan' itu sendiri. Andre tidak bersalah."

    return

label scenario2_2:
    jump scene6

label scene6:
    scene bg jalan afternoon
    play sound "suara langkah kaki.mp3"
    "*Suara langkah kaki*"

    show aditya happy
    "*???*"
    hide aditya

    show informan
    informan "Halo Pak Aditya."
    hide informan

    show aditya happy
    aditya "Siapa anda?"
    hide aditya

    show informan
    informan "Sudah saya katakan, itu tidaklah penting."
    hide informan

    show aditya happy
    aditya "Ok, lalu informasi apa yang anda ingin bagikan?"
    hide aditya

    show informan
    informan "Sabar Pak Aditya, ada beberapa syarat yang harus anda penuhi terlebih dahulu."
    hide informan

    show aditya happy
    aditya "Syarat? Apa itu?"
    hide aditya

    show informan
    informan "Keamanan, saya mempertaruh keamanan saya dan keluarga saya dengan membocorkan informasi ini kepada anda."
    hide informan

    show aditya happy
    aditya "Lalu kenapa Anda memberikannya?"
    hide aditya

    show informan
    informan "Koruptor itu sudah menyakiti banyak orang, dia tidak pantas hidup enak dan bebas."
    hide informan

    show aditya happy
    aditya "Ok, saya akan memberikan anda keamanan."
    hide aditya

    show informan
    informan "Baik, anda polisi yang jujur, saya percaya pada anda."
    hide informan

    show aditya happy
    aditya "Ok, lalu apa informasinya?"
    hide aditya

    show informan 
    informan "Koruptor itu adalah Dito Saputra, Direktorat Jenderal Bina Konstruksi di Dinas Pekerjaan Umum Kota Koralia. Dia juga sudah menyuap beberapa polisi untuk menutupi kasus ini."
    hide informan

    show aditya happy
    aditya "Dito Saputra? Apak buktinya?"
    hide aditya

    show informan
    informan "Sayangnya saya tidak mempunyai buktinya sekarang, tapi saya tahu dimana anda akan menemukannya."
    informan "Di dalam kantor Pak Dito terdapat brankas miliknya. Didalamnya terdapat sejumlah informasi mengenai riwayat transaksi yang dia lakukan."
    informan "Termasuk semua uang suap yang dia berikan kepada polisi."
    informan "Besok pagi, Pak Dito akan ada mengadakan rapat di kota sebelah, curilah informasi itu dari brankasnya tapi sayangnya saya tidak tahu kunci brankas itu."
    informan "Untungnya Pak Dito adalah seorang pelupa, saya yakin dia menyimpan kuncinya di dalam kantor nya, tapi berhati-hatilah, jika anda salah memasukkan kunci brankasnya dua kali maka akan ada alarm yang berbunyi dan mengunci ruangan itu."
    hide informan
    
    show aditya happy
    aditya "Bagaimana saya tahu kalau ini bukan jebakan?"
    hide aditya

    show informan
    informan "*Menunjukan koran dengan berita tentang seseorang yang ditemukan meninggal mengenaskan di kebun*"
    informan "Dia adalah teman dekat saya, dibunuh dan tubuhnya dibuang begitu saja layaknya seekor hewan oleh Dito. Saya tidak ingin ini terjadi kepada siapapun."
    hide informan

    show aditya happy
    aditya "..."
    aditya "Saya turut berduka atas kematian teman anda."
    hide aditya happy

    show informan
    informan "Terima kasih pak, tapi berhati-hatilah, Dito Saputra adalah orang yang berbahaya, dia akan melakukan apa saja untuk keuntungannya dia sendiri."
    informan "Dan berhati-hati juga dengan siapa yang anda percayai di kepolisian, Dito memiliki beberapa 'boneka' disana."
    hide informan

    show aditya happy
    aditya "Baik, untuk sekarang saya sarankan anda dan keluarga anda keluar kota untuk sementara, setidaknya sampai situasi di kota ini aman."
    hide aditya

    show informan
    informan "Baik Pak Aditya, saya tahu anda akan membongkar kebusukan Dito Saputra."
    hide informan

    jump scene9

# SCENE 9
label scene9:
    scene bg room with fade

    show aditya angry
    aditya "Ah, akhirnya aku berhasil masuk."
    aditya "Sekarang saatnya untuk mencari kunci brankas itu."

    # Loop menu and hide option that player choose. Loop until all option is hidden.
    $ meja = True
    $ rak = True
    $ brankas = True

    while meja or rak or brankas:
        menu:
            "Cari di meja kerja":
                aditya "Ah ada nomor di belakang foto pernikahannya. 251070"
                $ meja = False
            "Cari di rak buku":
                aditya "Ada nomor di salah satu bukunya. 202122"
                $ rak = False
            "Cari di dekat brankas":
                aditya "Ah terdapat kertas dengan nomor 892645"
                $ brankas = False

    $ coba = 0
    while coba < 2:
        menu:
            "Masukkan kode 251070":
                jump scenario2_3
            "Masukkan kode 202122":
                play sound "suara salah kode.mp3"
                aditya "Sial! Salah!"
                $ coba += 1
            "Masukkan kode 892645":
                play sound "suara salah kode.mp3"
                aditya "Sial! Salah!"
                $ coba += 1
    jump scenario2_4

label scenario2_3:
    show aditya happy
    aditya "Ah kodenya benar!"
    aditya "*Mengambil berkas*"
    aditya "Ok, saatnya pergi dari sini."
    hide aditya

    scene bg kantor day with fade

    show aditya happy
    aditya "Ok, sekarang aku sudah mempunyai bukti yang cukup kuat untuk menangkap Dito Saputra, tetapi belum cukup kuat untuk menangkap 'bonekanya' yang ada di kepolisian."
    aditya "Aku harus menyelidiki berkas ini lagi jika ingin menangkap 'bonekanya' Dito."

    menu:
        "*Tangkap Dito dengan bukti yang ada*":
            jump scenario2_3_1
        "*Selidiki berkas lagi*":
            jump scenario2_3_2

label scenario2_3_1:
    jump scene13

# SCENE 13
label scene13:
    scene bg room

    show aditya angry at right
    aditya "Angkat tangan! Anda ditangkap!"
    hide aditya

    show dito sad at left
    dito "HAH?! Apa ini? Apa maksud anda?!"
    hide dito

    show aditya angry at right
    aditya "Tidak usah pura-pura tidak tahu, saya tahu anda adalah koruptor dari proyek jembatan itu. Sekarang ikut saya ke kantor polisi!"
    hide aditya

    # Good Ending

    scene black
    "Kamu telah berhasil menangkap Dito Saputra, koruptor yang telah menyebabkan puluhan nyawa orang tidak bersalah menghilang. Kamu telah berhasil membersihkan nama baik kepolisian."

    return

label scenario2_3_2:
    jump scene15

label scene15:
    scene bg room
    
    show aditya angry at right
    aditya "Angkat tangan! Anda ditangkap!"
    hide aditya

    show dito sad at left
    dito "HAH?! Apa ini? Apa maksud anda?!"
    hide dito

    show aditya angry at right
    aditya "Tidak usah pura-pura tidak tahu, saya tahu anda adalah koruptor dari proyek jembatan itu. Sekarang ikut saya ke kantor polisi!"
    hide aditya
    
    jump scene16

label scene16:
    scene bg kantor day with fade

    show aditya angry at right
    aditya "Angkat tangan anda Pak Kepala!"
    hide aditya

    show akbar at left
    akbar "Apa-apaan kamu?! Lancang kamu!"
    hide akbar

    show aditya angry at right
    aditya "Saya tahu anda komplotan Pak Dito dalam korupsi proyek jembatan itu"
    aditya "Ini buktinya."
    aditya "*Menyerahkan berkas*"

    # BEST ENDING

    scene black with fade
    "Kamu telah berhasil menangkap Dito Saputra, koruptor yang telah menyebabkan puluhan nyawa orang tidak bersalah menghilang, selain itu kamu juga berhasil menangkap Akbar, Kepala Polisi yang ternyata adalah komplotan Dito. Kamu telah berhasil membersihkan nama baik kepolisian."

    return

label scenario2_4:
    show aditya angry
    aditya "Sial! Sudah dua kali salah kode."
    hide aditya

    play sound "suara alarm.mp3"
    "*Alarm berbunyi dan ruangan terkunci"

    scene black with fade
    "Beberapa menit kemudian"

    scene bg room with fade

    show dito happy at left
    dito "Ah selamat datang Pak Aditya. Anda orang yang memiliki inisiatif yang cukup tinggi ya, sudah masuk ke ruangan saya sebelum saya undang."
    hide dito

    show aditya angry at right
    aditya "Bagaimana anda tahu nama saya?"
    hide aditya

    show dito happy at left
    dito "Hahaha, itu karena saya mempunyai 'telinga' di kepolisian."
    hide dito

    show aditya angry at right
    aditya "APA?! Berarti memang benar anda koruptornya."
    hide aditya

    show dito happy at left
    dito "Jika ya, apa yang anda mau lakukan? Menangkap saya? Dengan bukti apa?"
    hide dito

    show aditya angry at right
    aditya "Argh… cepat buka brankas itu atau anda saya tangkap sekarang juga!"
    hide aditya

    show dito happy at left
    dito "Ya ampun Pak Aditya, anda memang senaif itu ternyata."
    dito "Sudahlah, saya ingin memberi anda sebuah kesempatan."
    dito "Saya ingin anda ada di pihak saya, akan cukup menguntungkan untuk mempunyai polisi seperti anda."
    dito "Dan anda tidak perlu khawatir tentang kehidupan anda dan keluarga anda lagi, akan saya tanggung."
    hide dito

    show aditya angry at right
    menu:
        "Hmm… Baiklah saya akan bergabung dengan anda":
            jump scenario2_4_1
        "Tidak, saya tidak akan pernah bergabung dengan anda!":
            jump scenario2_4_2

label scenario2_4_1:
    aditya "Baiklah saya akan bergabung dengan anda."
    hide aditya

    show dito happy at left
    dito "Haha, suatu keputusan yang bijak sekali Pak Aditya!"
    hide dito

    # BAD ENDING

    scene black with fade
    "Sebuah keputusan yang sangat tercela untuk seorang petugas kepolisian, bergabung dengan koruptor dan menjadi bagian dari kejahatan itu sendiri."

    return

label scenario2_4_2:
    aditya "Tidak, saya tidak akan pernah bergabung dengan anda!"
    hide aditya

    show dito happy at left
    dito "Haha, suatu keputusan yang bodoh sekali Pak Aditya!"
    hide dito

    show bodyguard
    play audio "suara pukulan.mp3"
    bodyguard "*Memukul Aditya hingga pingsan*"
    hide bodyguard

    jump scene12

# SCENE 12
label scene12:
    scene bg lapangan night with fade

    show aditya happy
    aditya "Argh... pusing sekali kepala ku."
    aditya "Dimana saya?"
    aditya "Hei! Apa-apaan ini? Lepaskan saya sekarang!"
    hide aditya

    show dito happy
    dito "Saya sudah memberi anda kesempatan Pak Aditya, dan anda menolaknya."
    dito "Ini adalah konsekuensi dari keputusan anda, Sayang sekali, padahal kita baru bertemu tapi kita akan berpisah lagi, selamanya."
    dito "Selamat tinggal Pak Aditya, senang bertemu dengan anda."
    hide dito

    show aditya happy
    aditya "HAH? Apa maksud and-"
    hide aditya

    scene black
    play sound "suara tembakan.mp3"
    "*Suara Tembakan*"
    "Menjadi seorang penegak keadilan adalah hal yang terpuji, tetapi adil saja tidak cukup, dunia ini memerlukan kecerdasan dan kehati-hatian."

    # WORST ENDING

    return