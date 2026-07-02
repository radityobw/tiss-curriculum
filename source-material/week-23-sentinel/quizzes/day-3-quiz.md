---
type: quiz
week: 23
day: 3
title: "Quiz: Digital Forensics Basics"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Di ranah administrasi hukum (*Digital Forensics*), mengapa pengisian dan pemeliharaan dokumen kontrol *Chain of Custody (Rantai Kustodi)* diwajibkan secara mutlak?
- [x] A. Karena tanpa riwayat pencatatan administrasi *Chain of Custody* yang memuat bukti pergerakan kronologis kepemilikan alat bukti fisik secara konsisten (mencakup waktu penyitaan, akses pihak pemeriksa, dan rute penyimpanan), validitas dan integritas barang bukti akan dianggap batal secara hukum di hadapan sistem peradilan perdata atau pidana.
- [ ] B. Karena dokumen tersebut menjadi kunci akses untuk menjalankan aplikasi *Ransomware*.
- [ ] C. Karena *Chain of Custody* merupakan prosedur implementasi operasi kriptografi *Hashing*.
- [ ] D. Karena instansi penegak hukum mewajibkan pengumpulan format laporan *SIEM Splunk*.

### Q2
**Type:** True/False
**Question:** Ketika seorang personel analis forensik menyita perangkat keras (misal *Laptop*) dalam penyidikan kejahatan, prosedur mengaktifkan sistem operasi target (*Booting*) sangat dilarang. Larangan ini didasarkan pada fakta bahwa proses *booting* secara fundamental merombak parameter *Metadata Timestamps* pada penyimpanan data yang membatalkan integritas alat hukum.
**Answer:** True

### Q3
**Type:** Short Answer
**Question:** Di dalam tahapan akuisisi berkas penyelidikan forensik digital, prosedur penyalinan yang menargetkan penciptaan klon secara komprehensif tanpa modifikasi rasio data *Bit-by-Bit (Bit-stream copy)* pada infrastruktur sistem penyimpanan tersangka biasanya diistilahkan sebagai apa?
**Answer:** Forensic Imaging (atau Disk Cloning).

### Q4
**Type:** Short Answer
**Question:** Saat analis forensik menyelesaikan kloning data arsip *Image*, implementasi parameter fungsi kriptografi apa (seperti *SHA-256*) yang difungsikan untuk menjamin keidentikan 100% parameter data hasil duplikasi dengan nilai sistem sumber aslinya?
**Answer:** Hashing (Atau kalkulasi Hash/Checksum).

### Q5
**Type:** Short Answer
**Question:** Agar parameter pencegahan penulisan intervensi data mutlak berfungsi saat menyambungkan penyimpanan *Hard Disk* tersangka dengan workstation penganalisis, perangkat keras pencegah modifikasi baca-tulis *(Hardware)* apa yang lazim wajib dikonfigurasikan di tengah jalur koneksi mereka?
**Answer:** Write Blocker.
