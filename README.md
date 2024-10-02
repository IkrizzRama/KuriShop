TUGAS 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
5. Mengapa model pada Django disebut sebagai ORM?

Jawab:
1. Definisikan Requirement dari Client:
Client meminta halaman untuk menampilkan daftar produk dengan fitur pencarian dan filter berdasarkan kategori.

URLs.py:
Tentukan URL untuk halaman daftar produk (/products/).
Pastikan terhubung dengan view yang tepat.

Views.py:
Buat view ProductListView yang mengambil data produk dari model.
Terapkan pencarian dan filter berdasarkan kategori.

Models.py:
Definisikan model Product dengan atribut-atribut seperti nama, deskripsi, harga, dan kategori.

Template HTML:
Buat template HTML untuk menampilkan daftar produk.
Tambahkan form pencarian dan filter.

2. Request Client: Tampilkan daftar produk dengan fitur pencarian dan filter berdasarkan kategori.

                      +-------------------+
                      |     urls.py       |
                      +-------------------+
                              |
                              v
                      +-------------------+
                      |     views.py      |
                      +-------------------+
                              |
                              v
          +-----------------------------------------+
          |                 models.py               |
          +-----------------------------------------+
                              |
                              v
                      +-------------------+
                      |   Template HTML   |
                      +-------------------+

3. Git adalah sistem kontrol versi yang memungkinkan pengembang untuk melacak perubahan dalam kode sumber selama pengembangan perangkat lunak. Fungsinya meliputi:

Pencatatan Perubahan: Menyimpan versi kode yang berbeda untuk memudahkan pemantauan dan perubahan.
Kolaborasi Tim: Memungkinkan beberapa pengembang bekerja pada kode yang sama tanpa konflik.
Pemulihan Kode: Memungkinkan kembali ke versi sebelumnya jika diperlukan.
Penyelarasan Proyek: Mengintegrasikan perubahan dari berbagai kontributor ke dalam proyek secara efisien.

4. Django sering dipilih untuk pemula karena:
Kesederhanaan: Django menyediakan struktur proyek yang terorganisir dengan baik dan mudah dipahami.
Pendekatan Berbasis Konvensi: Memiliki aturan konvensi yang jelas membuat pemula dapat fokus pada logika aplikasi daripada konfigurasi.
Dokumentasi yang Baik: Django memiliki dokumentasi yang sangat lengkap dan aktif, menjadikannya mudah dipelajari.

5. Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena:

Menghubungkan Objek dengan Basis Data: Django menggunakan model untuk mendefinisikan struktur data yang terhubung langsung dengan basis data.
Abstraksi Tingkat Tinggi: Memungkinkan pengembang untuk bekerja dengan objek Python daripada SQL mentah, menyederhanakan interaksi dengan basis data.
Portabilitas Kode: Memungkinkan pengembang untuk menggunakan model yang sama dengan berbagai jenis basis data tanpa mengubah logika aplikasi yang mendasarinya.




Tugas 3 
 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Jawab:
1. Kenapa Data Delivery Itu Penting:

Efisiensi Operasional: Data delivery membantu memastikan data dikirim dengan cepat dan efisien. Bayangkan kalau aplikasi lambat karena data nggak sampai dengan baik—itu bikin frustasi, kan?
Akurasi Data: Kita butuh data yang akurat. Kalau data yang dikirim salah, bisa bikin masalah besar. Data delivery yang baik memastikan informasi yang diterima benar.
Interoperabilitas: Kalau platform kita harus terhubung dengan sistem lain, data delivery yang baik bikin komunikasi antar sistem jadi lebih lancar.
Pengalaman Pengguna: Pengguna pasti pengen pengalaman yang mulus dan cepat. Jadi, data delivery yang baik bikin aplikasi lebih responsif dan menyenangkan digunakan.
XML vs. JSON:

2. JSON Lebih Baik? Menurut saya, JSON seringkali lebih baik karena formatnya lebih ringkas dan lebih mudah dibaca. Misalnya, data JSON bisa langsung digunakan di JavaScript tanpa perlu proses tambahan.
Kenapa JSON Populer: JSON jadi pilihan utama karena kesederhanaannya dan kemudahannya dalam penggunaan, terutama di web dan aplikasi mobile. XML memang powerful, tapi kadang bisa terasa berlebihan dengan semua tag dan struktur yang rumit.
Fungsi is_valid() di Form Django:

3. Validasi Data: Method is_valid() itu semacam check-list untuk memastikan data yang dimasukkan pengguna sudah benar dan sesuai dengan aturan yang kita buat.
Kenapa Perlu: Tanpa validasi, data yang salah atau tidak lengkap bisa masuk ke sistem kita, yang bisa bikin masalah atau kerusakan. is_valid() membantu memastikan semuanya sesuai dengan yang diharapkan.
CSRF Token di Django:

4. Apa Itu CSRF Token: CSRF token itu kayak kunci keamanan yang memastikan permintaan yang masuk itu sah dan bukan dari orang yang nggak berhak.
Kenapa Harus Ada: Kalau kita nggak pakai CSRF token, form kita bisa jadi target serangan. Misalnya, penyerang bisa memanfaatkan sesi pengguna untuk melakukan aksi yang berbahaya tanpa izin.
Risiko Tanpa CSRF Token: Tanpa token ini, form kita bisa diakses oleh penyerang yang mungkin bikin kerusakan atau mengubah data tanpa sepengetahuan pengguna.
Implementasi Checklist:

5. Persiapan: Mulailah dengan memahami apa yang dibutuhkan dan bagaimana sistem akan berfungsi. Ini termasuk data delivery, format data, dan keamanan form.
Data Delivery: Rancang cara data dikirim dan diterima, lalu bangun API yang sesuai. Pilih antara XML atau JSON berdasarkan kebutuhan.
Format Data: Pilih format yang sesuai—JSON biasanya jadi pilihan karena lebih efisien.
Form di Django: Buat form di Django, tambahkan validasi dengan is_valid(), dan pastikan data yang masuk sudah benar.
CSRF Token: Tambahkan {% csrf_token %} ke form di template Django. Uji untuk memastikan token bekerja dengan baik dan melindungi form.
Uji Sistem: Setelah semua diimplementasikan, pastikan semuanya berjalan lancar dan sesuai harapan. Uji berbagai skenario untuk memastikan tidak ada masalah.

Penggunaan Postman:
![Screenshot 2024-09-17 233327](https://github.com/user-attachments/assets/fa92629a-57ce-45e2-b4b8-6c37a34c6d25)
![Screenshot 2024-09-17 233343](https://github.com/user-attachments/assets/b04120a3-3a74-45bf-afe0-440ce1d587c7)
![Screenshot 2024-09-17 233358](https://github.com/user-attachments/assets/93349d96-670c-4e8c-b19a-e25a7e6c21ec)
![Screenshot 2024-09-17 233411](https://github.com/user-attachments/assets/11f5619d-8841-4901-bb33-1ecdcc29b9f6)





Tugas 4
 1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
 2. Jelaskan cara kerja penghubungan model Product dengan User!
 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

 Jawab:
 1. HttpResponseRedirect() adalah fungsi yang secara eksplisit membuat respons HTTP untuk mengalihkan pengguna ke URL tertentu. Di sisi lain, redirect() adalah shortcut Django yang lebih ringkas dan otomatis mengarah ke URL atau view yang ditentukan, juga menangani resolusi URL dan pemrosesan URL dengan lebih mudah.

 2. Penghubungan model Product dengan User dilakukan dengan menambahkan field foreign key di model Product, yang merujuk ke model User. Dengan demikian, setiap produk akan memiliki referensi ke pengguna yang membuat atau memiliki produk tersebut.

 3. Authentication adalah proses untuk memverifikasi identitas pengguna, seperti memastikan username dan password yang dimasukkan adalah benar. Ini terjadi saat pengguna login. Sedangkan Authorization adalah proses untuk menentukan apakah pengguna yang terautentikasi memiliki izin untuk mengakses atau melakukan tindakan tertentu dalam aplikasi.
 Django mengimplementasikan authentication melalui sistem pengguna dan grup yang terintegrasi, menggunakan model User dan middleware yang menangani session.

 4. Django menggunakan sesi (sessions) untuk mengingat pengguna yang telah login. Saat pengguna berhasil login, Django menyimpan ID pengguna dalam cookie yang disebut session cookie. Ini memungkinkan Django untuk mengenali pengguna di permintaan berikutnya. Kegunaan lain dari cookies termasuk menyimpan preferensi pengguna, sesi belanja, dan data analitik. Namun, tidak semua cookies aman; penting untuk menggunakan cookies dengan atribut seperti HttpOnly dan Secure untuk melindungi data pengguna.

 5. Implementasi Checklist Secara Step-by-Step
 Membuat Fungsi Registrasi, Login, dan Logout:
 Menggunakan Django’s built-in authentication views untuk membuat form dan views untuk registrasi, login, dan logout.

 Membuat Akun Pengguna dan Dummy Data:
 Membuat skrip atau menggunakan shell Django untuk membuat dua akun pengguna dan menambahkan tiga produk dummy untuk masing-masing.

 Menghubungkan Model Product dengan User:
 Menambahkan foreign key di model Product yang mengarah ke model User, seperti dijelaskan di atas.
 Menampilkan Informasi Pengguna yang Login:
 Memodifikasi template untuk menampilkan username pengguna yang sedang login dan menambahkan logika untuk membaca dan menyimpan cookie last login.

 Menerapkan Cookies:
 Menggunakan Django's session framework untuk mengatur cookies yang menyimpan informasi pengguna yang login, serta menambahkan logika untuk mencatat last login saat pengguna login.


 Tugas 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

Jawab:
1. Dalam CSS, urutan prioritas selector menentukan mana aturan yang diterapkan pada elemen ketika ada beberapa aturan yang mungkin berlaku. Urutan prioritasnya adalah sebagai berikut:

Inline Styles: Gaya yang ditetapkan langsung pada elemen menggunakan atribut style (contoh: <div style="color: red;">).

ID Selectors: Selector dengan ID (contoh: #example), memiliki bobot yang tinggi.
 
Class Selectors, Attribute Selectors, dan Pseudo-classes: Selector dengan kelas (contoh: .example), selector atribut (contoh: [type="text"]), dan pseudo-classes (contoh: :hover) memiliki bobot sedang.

Element Selectors dan Pseudo-elements: Selector untuk elemen (contoh: div, p) dan pseudo-elements (contoh: ::before, ::after) memiliki bobot yang lebih rendah.
# Universal Selector: Selector universal (*) memiliki bobot terendah.
Dalam hal ada selector dengan bobot yang sama, aturan yang didefinisikan lebih dekat dengan elemen HTML akan diterapkan.

2. Responsive design adalah konsep penting dalam pengembangan aplikasi web karena memungkinkan tampilan yang optimal di berbagai perangkat (desktop, tablet, smartphone). Hal ini memastikan bahwa pengguna mendapatkan pengalaman yang baik terlepas dari ukuran layar yang digunakan.

Contoh Aplikasi:
Sudah Menerapkan Responsive Design: Aplikasi e-commerce seperti Amazon atau Shopee, di mana layout dan elemen menyesuaikan dengan ukuran layar perangkat.
Belum Menerapkan Responsive Design: Beberapa situs berita yang memiliki layout statis, sehingga konten tidak tampil optimal pada perangkat kecil, seperti situs yang hanya memiliki desain desktop tanpa versi mobile.

3. Margin: Ruang di luar elemen yang memisahkan elemen tersebut dari elemen lain. Margin tidak mempengaruhi ukuran elemen itu sendiri.
Cara Implementasi:
.element {
    margin: 20px; /* margin atas, bawah, kiri, dan kanan */
}

Border: Garis yang mengelilingi elemen. Border membatasi elemen dan memberikan definisi visual.
Cara Implementasi:
.element {
    border: 2px solid black; /* ketebalan, jenis, dan warna border */
}


Padding: Ruang di dalam elemen antara konten dan batas border. Padding meningkatkan ruang di dalam elemen.
Cara Implementasi:
.element {
    padding: 15px; /* padding atas, bawah, kiri, dan kanan */
}


4. Flexbox: Flexbox adalah model layout satu dimensi yang digunakan untuk mengatur ruang di dalam kontainer. Ini memungkinkan elemen dalam kontainer untuk beradaptasi dengan ukuran ruang yang tersedia. Kegunaannya termasuk mengatur tata letak baris atau kolom secara responsif, menyelaraskan elemen, dan mengontrol arah dan urutan elemen.

Grid Layout: Grid adalah model layout dua dimensi yang digunakan untuk mengatur elemen dalam baris dan kolom. Grid sangat berguna untuk tata letak yang kompleks, seperti galeri gambar atau dashboard. Kegunaannya termasuk pembagian area dalam grid yang dapat mengakomodasi elemen dalam berbagai ukuran.

5. Menghapus dan Mengedit Produk: Saya mulai dengan menambahkan fungsi untuk menghapus dan mengedit produk di aplikasi. Pertama, saya membuka file views.py dan menambahkan fungsi edit_product dan delete_product. Untuk fungsi edit, saya menggunakan form yang sudah ada untuk memudahkan pengeditan produk. Setelah itu, saya menambahkan URL yang sesuai di urls.py agar pengguna bisa mengakses halaman edit. Untuk menghapus produk, saya menambahkan konfirmasi di frontend agar pengguna yakin sebelum menghapus.

Kustomisasi Desain Halaman Login, Register, dan Tambah Produk: Saya kemudian beralih ke halaman login, register, dan tambah produk. Saya menggunakan framework CSS Tailwind untuk membuat desain yang lebih menarik. Saya merombak struktur HTML dengan menambahkan elemen-elemen seperti gambar latar, tombol yang lebih menarik, dan penyesuaian warna agar halaman terlihat lebih hidup.

Kustomisasi Halaman Daftar Produk: Selanjutnya, saya fokus pada halaman daftar produk. Di sini, saya menambahkan kondisi untuk memeriksa apakah ada produk yang terdaftar. Jika tidak ada, saya menampilkan gambar sedih dengan pesan yang menyatakan bahwa belum ada produk yang terdaftar. Jika sudah ada produk, saya menampilkan detail produk dalam bentuk card yang menarik, dengan menggunakan Tailwind CSS untuk styling.

Menambahkan Tombol Edit dan Hapus pada Setiap Card Produk: Dalam setiap card produk, saya menambahkan dua tombol, satu untuk mengedit dan satu lagi untuk menghapus produk. Tombol ini memiliki fungsi yang saya buat sebelumnya, sehingga pengguna dapat dengan mudah melakukan perubahan atau menghapus produk.

Membuat Navigation Bar Responsif: Terakhir, saya membuat navigation bar (navbar) yang responsif untuk aplikasi. Saya menggunakan fitur responsif dari Tailwind untuk memastikan navbar terlihat baik di semua ukuran layar, baik mobile maupun desktop. Saya menambahkan tautan ke halaman login, register, dan daftar produk agar navigasi menjadi lebih mudah.
