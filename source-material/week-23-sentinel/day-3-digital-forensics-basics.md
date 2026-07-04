# 🛡️ Week 23 · Day 3: Digital Forensics Basics

> **Rank**: SENTINEL | **Minggu ke-23**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 23 · Day 3/5 | SENTINEL Rank (Minggu 4 dari 5) | Overall: 113/120 hari (94%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** urgensi investigasi pasca-insiden (Digital Forensics) dalam proses penegakan hukum.
2. **Menerapkan** kaidah integritas barang bukti elektronik (*Chain of Custody*).
3. **Mengerti** proses penciptaan salinan identik dari perangkat (*Forensic Imaging* & *Hashing*).

---

## 📖 Materi Inti

### Digital Forensics (Forensik Digital)

Meskipun sistem pemantauan seperti SIEM memberikan visibilitas jaringan yang kuat, log peringatan (*Alerts*) saja belum cukup kuat untuk dijadikan alat bukti sah di pengadilan. Ketika insiden siber menyebabkan kerugian finansial atau pencurian data, perusahaan harus beralih ke metode investigasi formal berstandar hukum yang disebut **Digital Forensics**.

Digital Forensics adalah serangkaian prosedur terstandarisasi untuk mengamankan (*Preserve*), mengidentifikasi (*Identify*), mengekstraksi (*Extract*), dan mendokumentasikan *(Document)* bukti elektronik (seperti *Hard Disk*, *Flashdisk*, atau Memori RAM komputer), dengan tujuan utama mempertahankan keabsahan barang bukti tersebut di mata hukum (*Admissibility of Evidence*).

### Integritas Barang Bukti: Chain of Custody

Dalam persidangan, keabsahan barang bukti elektronik dapat dengan mudah digugurkan jika pengacara lawan bisa membuktikan adanya celah kelalaian selama penyimpanan bukti, yang membuka peluang terjadinya manipulasi data (*Data Tampering*).

Untuk mencegah hal ini, spesialis forensik wajib mendokumentasikan seluruh perpindahan barang bukti menggunakan **Chain of Custody (Rantai Kustodi)**.
Dokumen hukum ini mencatat kronologi fisik bukti:
- Tanggal dan waktu pasti (*Timestamp*) saat bukti (misal: Laptop tersangka) disita.
- Identitas setiap orang yang menyentuh, membawa, atau menganalisis barang bukti tersebut.
- Lokasi penyimpanan barang bukti (misal: brankas khusus).
Jika ada kekosongan waktu (*Gap*) yang tidak tercatat, *Chain of Custody* dianggap putus dan barang bukti otomatis kehilangan integritas legalnya.

### Modifikasi Protektif: Forensic Imaging & Hashing

Dalam forensik digital, ada satu aturan mutlak: **DILARANG MENGAKSES ATAU MENYALAKAN KOMPUTER BARANG BUKTI SECARA LANGSUNG!**

Menyalakan sistem operasi (*Booting*) secara otomatis akan merubah ribuan metadata *Timestamp* di dalam sistem, menulis file *log* baru, dan menghapus memori *RAM*, yang secara hukum berarti Anda telah "merusak" barang bukti.
Prosedur forensik yang sah meliputi:
1. **Write Blocker:** Gunakan perangkat *Hardware Write Blocker* sebagai jembatan antara *Hard disk* tersangka dan komputer Analis. Alat ini memastikan tidak ada satupun perintah tulis (*Write Command*) yang bisa masuk ke *Hard disk* bukti.
2. **Forensic Imaging:** Analis tidak menyelidiki *Hard disk* asli, melainkan membuat salinan identik tingkat bit (*Bit-by-bit Clone*) dari perangkat tersebut tanpa kompresi (biasanya berformat `.E01` atau `.dd`). Penyelidikan hanya boleh dilakukan pada *file* salinan (*Image*) ini.
3. **Hashing (Integritas Data):** Untuk membuktikan di pengadilan bahwa salinan (*Image*) 100% identik dengan *Hard disk* aslinya, analis menghitung nilai **Hash** (menggunakan algoritma *MD5* atau *SHA-256*) dari keduanya. Jika nilai *Hash* antara sumber asli dan salinan cocok (*Match*), maka salinan tersebut diakui sah secara hukum.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merancang simulasi konsep integritas forensik!

1. **Skenario:** Anda bertugas sebagai spesialis forensik. Tim baru saja menyita *Hard Disk Drive (HDD)* 1TB milik tersangka peretas.
2. **Langkah 1 (Hashing Sumber):** Berdasarkan SOP, Anda segera menghitung nilai *Hash SHA-256* dari HDD asli tersebut, dan mendapatkan hasil: `a1b2c3d4e5...`.
3. **Langkah 2 (Imaging):** Anda melakukan duplikasi (*Forensic Imaging*) dari HDD tersebut untuk membuat *file* `.E01`.
4. **Langkah 3 (Verifikasi):** Keesokan harinya, Anda menghitung nilai *Hash* dari *file* duplikat (`.E01`) tersebut.
5. **Pendeteksian Anomali:** Hasil *Hash* dari *file* salinan ternyata berbeda, yaitu: `f9e8d7c6b5...`.
6. **Kesimpulan Forensik:** Terdapat indikasi kerusakan atau perubahan data (*Hash Mismatch*)! Hal ini bisa disebabkan oleh alat *Imaging* yang cacat, atau prosedur penyalinan yang tidak menggunakan *Write Blocker*. Salinan data ini otomatis batal demi hukum dan tidak bisa digunakan di persidangan.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Dalam investigasi siber, apa nama dokumen yang mencatat riwayat pemindahan fisik barang bukti elektronik secara kronologis agar legalitasnya di pengadilan tidak dibatalkan?</summary>

**Jawaban:** *Chain of Custody* (Rantai Kustodi).
</details>

<details>
<summary>❓ Mengapa spesialis forensik dilarang keras untuk menyalakan langsung komputer tersangka (*Booting OS*) setelah penyitaan dilakukan?</summary>

**Jawaban:** Proses *Booting* akan otomatis melakukan aktivitas penulisan (*Write*) ke dalam media penyimpanan, yang merubah metadata *Timestamp* dan struktur *file* sistem. Perubahan sekecil apapun pada sumber asli akan membatalkan integritas barang bukti secara hukum.
</details>

<details>
<summary>❓ Algoritma kriptografi apa (contohnya MD5/SHA-256) yang wajib digunakan untuk memverifikasi bahwa salinan forensik (<i>Image</i>) 100% identik dengan barang bukti aslinya?</summary>

**Jawaban:** Hashing.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami pentingnya *Digital Forensics* dalam penegakan hukum.
- [ ] Saya mengetahui fungsi dokumen *Chain of Custody*.
- [ ] Saya memahami alasan tidak boleh menyalakan langsung (*booting*) barang bukti elektronik.
- [ ] Saya mengerti fungsi *Write Blocker*, *Forensic Imaging*, dan validasi *Hashing*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [NIST: Guide to Integrating Forensic Techniques](https://csrc.nist.gov/publications/detail/sp/800-86/final) — Panduan resmi dari *NIST* (National Institute of Standards and Technology) mengenai standar prosedur penanganan insiden forensik.

---

## ➡️ Besok

**Day 4: Memory & Disk Forensics** — Setelah mengamankan salinan *Image*, langkah selanjutnya adalah membedah isinya! Besok kita akan mempelajari investigasi media penyimpanan (*Disk Forensics*) untuk mencari *file* yang sudah dihapus, serta *Memory Forensics* menggunakan alat **Volatility** untuk mengekstrak data dari memori RAM (seperti *password* yang belum sempat tersimpan ke *hard disk*).

---

*📅 TISS Null Teaming · Week 23 · Day 3 · SENTINEL Rank*
