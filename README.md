# setaksetik
Sebuah aplikasi yang didekasikan untuk pecinta dan calon pecinta steak!

---

# Table of Contents
1. [Anggota Kelompok](#anggota-kelompok)
2. [Deskripsi Aplikasi](#deskripsi-aplikasi)
3. [Daftar Modul](#daftar-modul)
4. [Sumber Initial Dataset](#sumber-initial-dataset)
5. [Role atau Peran Pengguna](#role-atau-peran-pengguna)
6. [Tautan Deployment](#tautan-deployment)


# Anggota Kelompok
- 2306211401  |  Haliza Nafiah Syakira Arfa
- 2306244955  |  Muhammad Faizi Ismady Supardjo
- 2306165692  |  Nadira Aliya Nashwa
- 2306165963  |  Aimee Callista Ferlintera Prudence Ernanto
- 2306217304  |  Clara Aurelia Setiady


# Deskripsi Aplikasi
Untuk menjawab kebingungan pengguna dalam memilih menu steak yang tepat, **setaksetik** hadir sebagai solusi lengkap bagi para pecinta steak. Aplikasi ini dirancang dengan beragam fitur yang tidak hanya memudahkan pengguna dalam memilih menu, tetapi juga memberikan pengalaman bersantap yang lebih personal dan menyenangkan. 

**setaksetik** dikembangkan dengan berbagai modul yang mendukung kemudahan dalam pemilihan menu serta kenyamanan pengguna. Fitur autentikasi memungkinkan pengguna untuk login dengan mudah melalui akun Google, Facebook, atau Apple, serta menyimpan preferensi pribadi seperti tingkat kematangan _steak_ dan jenis daging favorit. Pengguna juga dapat mengakses riwayat pesanan, menyimpan _wishlist_ menu yang ingin dicoba, dan melacak program reward berdasarkan pesanan dan _review_. Selain itu, fitur "Spin the Wheel" menambahkan elemen hiburan dalam menentukan pilihan menu, sementara _filter_ menu yang komprehensif membantu pengguna menyesuaikan pencarian berdasarkan rasa, metode masak, harga, dan kriteria lainnya.

Saat ini, aplikasi ini dirancang untuk pecinta steak berbasis Jakarta. Dataset yang digunakan adalah menu dan _steakhouse_ yang tersebar di segala penjuru Jakarta. Jadi, jika menjejakkan kaki di Jakarta dan mendambakan steak, tak perlu bingung tak perlu ragu, **setaksetik** akan membantu!


# Daftar Modul
1. **Autentikasi**
   - Pengguna melakukan aktivitas login dan logout.
   - Aktivitas login dapat melalui Google, Facebook, dan Apple.
   - Profil pengguna menyimpan informasi seperti:
       - Preferensi pribadi (tingkat kematangan steak dan jenis daging favorit)
       - Riwayat pesanan
       - Review
   - Terdapat fitur wishlist yang memungkinkan pengguna untuk menyimpan menu yang ingin dicoba.
   - Terdapat tracking reward program atau poin loyalitas yang diberikan berdasarkan pesanan dan review yang dibuat.
   - Pada fitur riwayat pesanan, pengguna dapat melihat pesanan sebelumnya dan memesan kembali menu favorit.

2. **Spin the Wheel - “Makan apa hari ini”**
   - Pengguna melakukan _spin wheel_ yang disesuaikan dengan preferensi pribadi terakhir.
   - Pengguna dapat menambah atau menghapus daftar menu yang dijadikan opsi pada _spin wheel_
   - Hasil _spin_ dapat disimpan sebagai rekomendasi menu.
   - Pengguna dapat membagikan hasil _spin_ ke sosial media.

3. **Menu dan Filter Menu**
   - Pengguna dapat memfilter menu berdasarkan:
     - Rasa (manis, gurih)
     - Tingkat kematangan steak
     - Jenis saus (BBQ, jamur, lada hitam)
     - Side dish (kentang, salad)
     - Harga per porsi
     - Asal daging (lokal atau impor)
     - Metode masak (grill, pan-seared, sous-vide)

4. **Rating dan Review**
   - Pengguna dapat memberikan _review_ dan _rating_ pada setiap menu yang telah dicoba.
   - Review dapat dilengkapi dengan foto menu yang dipesan.
   - Terdapat fitur _upvote_ dan _downvote_ untuk review pengguna lain.
   - Terdapat _reward_ yang diberikan kepada pengguna yang paling aktif dalam memberikan _review_, misalnya "Steak Expert" atau "Meat Lover".

5. **Make it by Yourself**
   - Fitur ini memungkinkan pengguna memilih menu steak yang dapat dimasak sendiri di rumah dengan filter berdasarkan jenis daging.
   - Pengguna dapat membuat daftar belanja bahan steak dan langsung memesan bahan dari aplikasi.
   - Terdapat estimasi biaya bahan-bahan yang dibutuhkan.
   - Terdapat fitur video tutorial cara memasak steak dari chef atau konten kreator.

6. **MeatUp - Teman Makan**
   - Pengguna dapat membuat "public wishlist" tentang menu yang berencana ingin dimakan.
   - Pengguna lain dengan wishlist serupa dapat saling terhubung sehingga mereka dapat berdiskusi tentang menu yang ingin dicoba.
   - Terdapat fitur book together yang memungkinkan beberapa pengguna untuk melakukan pemesanan secara bersamaan.

7. **Booking restoran**
   - Booking dilakukan berdasarkan restoran, nama pemesan, dan jumlah orang.
   - Pengguna memesan berdasarkan jumlah porsi.
   - Dikolaborasikan dengan fitur MeatUp untuk beberapa pengguna yang melakukan _booking_ bersamaan.


# Sumber Initial Dataset
Kategori utama produk berupa menu _steak_ unggulan dari berbagai _steakhouse_ di Jakarta.

Berikut sumber initial [dataset](https://www.kaggle.com/datasets/miradelimanr/steakhouse-jakarta?resource=download) kami.


# Role atau Peran Pengguna
1. **Pengguna Umum (Customer)**
   - Akses:
     - Mengakses seluruh konten publik seperti daftar menu, informasi restoran, harga, dan ulasan.
     - Membuat akun dan login/logout menggunakan akun Google, Facebook, atau Apple.
   - Fitur:
     - **Wishlist**: Menyimpan menu-menu favorit yang ingin dicoba di masa depan.
     - **Ulasan & Rating**: Memberi rating dan review pada menu yang sudah dicoba, serta mengunggah foto makanan.
     - **Spin the Wheel**: Menggunakan fitur "spin the wheel" untuk memilih menu secara acak.
     - **Teman Makan**: Berinteraksi dengan pengguna lain melalui "public wishlist" dan fitur in-app messaging.
     - **Booking Restoran**: Melakukan pemesanan tempat di restoran dan melihat riwayat booking.
       
2. **Admin**
   - Akses:
     - Mengelola konten website.
   - Fitur:
     - **Pengelolaan Menu & Restoran**: Menambah, mengedit, atau menghapus informasi tentang menunya (termasuk foto, harga, dan deskripsi).
     - **Manajemen Ulasan**: Memoderasi ulasan pengguna, menghapus ulasan yang tidak sesuai, atau menandai ulasan yang melanggar kebijakan.
     - **Manajemen Pengguna**: Mengelola akun pengguna, memblokir akun yang bermasalah, atau memberi hak akses khusus kepada pengguna tertentu.
     - **Manajemen Booking**: Memantau dan mengelola booking dari seluruh _steakhouse_.
       
3. **Pemilik Steakhouse**
   - Akses:
     - Mengelola informasi khusus tentang steakhouse mereka sendiri.
   - Fitur:
     - **Pengelolaan Menu & Harga**: Menambah, mengedit, atau menghapus menu, harga, jam operasional, dan promosi yang berlaku di _steakhouse_ mereka.
     - **Manajemen Ulasan & Feedback**: Melihat dan menanggapi ulasan pengguna untuk restoran mereka.
     - **Manajemen Booking**: Mengelola pemesanan dari pengguna, menerima atau menolak booking, serta menambahkan opsi pemesanan tambahan jika diperlukan untuk _steakhouse_ mereka.


# Tautan Deployment
Tautan deployment aplikasi **setaksetik**.
