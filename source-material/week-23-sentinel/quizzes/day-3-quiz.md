---
type: quiz
week: 23
day: 3
title: "Quiz: Digital Forensics Basics"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam investigasi *Digital Forensics*, mengapa pengisian dan pemeliharaan dokumen kontrol *Chain of Custody (Rantai Kustodi)* sangat diwajibkan?
- [x] A. Karena tanpa dokumen yang mencatat riwayat pergerakan kepemilikan barang bukti secara kronologis (mencakup waktu penyitaan, akses pihak pemeriksa, dan rute penyimpanan), integritas barang bukti akan dianggap cacat dan batal demi hukum di pengadilan.
- [ ] B. Karena dokumen tersebut menjadi kunci sandi untuk membuka *file Ransomware*.
- [ ] C. Karena *Chain of Custody* adalah nama lain dari proses *Forensic Imaging*.
- [ ] D. Karena instansi penegak hukum mewajibkan pengumpulan laporan *SIEM Splunk*.

### Q2
**Type:** True/False
**Question:** Ketika analis forensik menyita barang bukti komputer, prosedur menyalakan sistem operasi komputer tersebut (*Booting*) sangat dilarang. Hal ini karena proses *booting* secara otomatis akan mengubah ribuan *Metadata Timestamps* dan menulis log baru, yang secara hukum merusak keaslian barang bukti.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Dalam tahapan investigasi digital forensik, apa sebutan untuk prosedur pembuatan salinan data yang 100% identik tingkat bit (*Bit-by-Bit / Bit-stream copy*) dari media penyimpanan milik tersangka tanpa kompresi?
**Answer:** Forensic Imaging (Atau Disk Cloning).

### Q4
**Type:** Short Answer
**Question:** Saat analis forensik selesai membuat salinan data (*Image*), metode kriptografi apa (seperti *SHA-256*) yang digunakan untuk memverifikasi dan menjamin bahwa salinan tersebut 100% identik dan tidak berubah dari *Hard disk* aslinya?
**Answer:** Hashing (Atau Kalkulasi Hash / Checksum).

### Q5
**Type:** Short Answer
**Question:** Agar tidak ada data sekecil apapun yang tidak sengaja tertulis ke dalam *Hard disk* tersangka saat disambungkan ke komputer analis, perangkat keras keamanan apa yang wajib dipasang di tengah jalur koneksinya?
**Answer:** Write Blocker.
