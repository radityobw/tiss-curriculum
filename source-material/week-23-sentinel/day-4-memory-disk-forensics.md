# 🛡️ Week 23 · Day 4: Memory & Disk Forensics

> **Rank**: SENTINEL | **Minggu ke-23**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 23 · Day 4/5 | SENTINEL Rank (Minggu 4 dari 5) | Overall: 114/120 hari (95%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** antara investigasi bukti pada memori sementara (*RAM*) dan media penyimpanan permanen (*Disk/Non-Volatile*).
2. **Memahami** prinsip *Order of Volatility* dalam memprioritaskan ekstraksi bukti.
3. **Mengenali** penggunaan *Volatility Framework* untuk menganalisis temuan *Memory Forensics*.

---

## 📖 Materi Inti

### Segmentasi Investigasi: Disk vs RAM

Saat spesialis forensik menangani insiden siber, ekstraksi bukti dilakukan pada dua area utama berdasarkan sifat penyimpanan datanya:

1. **Disk Forensics (Penyimpanan Permanen / Non-Volatile):**
   Investigasi pada media penyimpanan seperti Hard Disk Drive (HDD) atau SSD. Di sinilah tersimpan *Event Logs* sistem operasi, riwayat *Browser*, dan *file* yang diunduh peretas. Perlu diketahui, ketika pengguna menghapus file (bahkan dengan Shift+Delete), *file* tersebut tidak benar-benar terhapus dari piringan *Hard Disk* seketika. Analis seringkali dapat memulihkan (*Data Recovery*) bukti tersebut menggunakan *software* forensik.
2. **Memory Forensics (Penyimpanan Sementara / Volatile):**
   Investigasi pada memori sementara atau RAM (Random Access Memory). RAM merekam aktivitas sistem yang sedang berjalan (*live*). RAM sangat krusial karena seringkali menyimpan *Malware Fileless* (Malware yang hanya berjalan di RAM tanpa menyentuh *Hard disk*), kunci enkripsi (*Decryption Key*) dari serangan *Ransomware* yang sedang aktif, serta *password* pengguna yang sedang *login* (terkadang dalam bentuk teks terang/ *Clear-text*).

### Hierarki Prioritas Bukti (Order of Volatility)

Kaidah utama dalam akuisisi bukti digital adalah memprioritaskan data berdasarkan tingkat kerentanannya untuk hilang, atau dikenal sebagai **Order of Volatility**.

Data yang ada di dalam RAM sangat rentan (*Volatile*). Jika komputer di-*restart* atau kabel listriknya dicabut, seluruh data yang ada di RAM akan terhapus dan hilang secara permanen seketika!

Karena alasan inilah, jika Analis menemukan komputer sedang diserang (misalnya oleh *Ransomware*), instruksi pertamanya BUKAN mematikan atau mencabut kabel listrik komputer tersebut! Tindakan yang benar adalah mencabut kabel jaringan (kabel LAN) untuk mengisolasi sistem, kemudian segera melakukan proses ekstraksi (penggandaan) data dari RAM yang sedang berjalan tersebut (*Live Memory Capture*).

### Analisis RAM dengan Volatility Framework

Setelah analis berhasil mengekstrak salinan dari isi RAM (*Memory Dump File*, biasanya berekstensi `.raw` atau `.mem`), isi *file* tersebut hanyalah kumpulan kode heksadesimal acak yang tidak bisa dibaca manusia.
Untuk membongkarnya, analis menggunakan alat CLI (*Command Line Interface*) standar industri berbasis Python yang bernama **Volatility Framework**.

Beberapa perintah dasar *Volatility* untuk mencari bukti di memori:
- `vol.py -f memory_dump.raw windows.pslist`: Memerintahkan Volatility untuk menampilkan seluruh daftar proses aplikasi yang sedang berjalan pada saat *RAM* disalin (Sangat berguna untuk mencari proses *malware* yang bersembunyi di memori).
- `vol.py -f memory_dump.raw windows.hashdump`: Mengekstrak daftar otentikasi (Password Hashes) pengguna Windows yang tersisa atau tersangkut di dalam memori OS.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari merancang simulasi penanganan insiden *Ransomware*!

1. **Skenario:** Anda adalah *Incident Responder*. Seorang karyawan melaporkan bahwa setelah ia membuka lampiran email, layarnya terkunci oleh peringatan *Ransomware* yang meminta tebusan.
2. **Kepanikan:** Karyawan tersebut panik dan berniat menekan tombol *Power* untuk mematikan dan me-`restart` komputernya.
3. **Intervensi Analis:** Anda harus segera berteriak: *"JANGAN DIMATIKAN ATAU DI-RESTART! Biarkan menyala. Cukup cabut kabel LAN/Wi-Fi saja!"*
4. **Analisis Keputusan:** *Ransomware* sedang bekerja mengenkripsi *file*. Kunci untuk membuka enkripsi (*Decryption Key*) tersebut saat ini sedang aktif berada di dalam memori RAM komputer. Jika karyawan melakukan *restart*, RAM akan terhapus. Kunci dekripsi tersebut akan hilang selamanya, dan data yang terkunci mungkin tidak akan pernah bisa diselamatkan lagi.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa perbedaan mendasar antara cakupan <i>Disk Forensics</i> dengan <i>Memory Forensics</i>?</summary>

**Jawaban:** *Disk Forensics* menganalisis data pada penyimpanan permanen (*Hard disk/SSD*) yang datanya tetap ada meski komputer dimatikan. *Memory Forensics* menganalisis data sementara pada RAM (seperti *password* atau *malware* aktif) yang datanya akan langsung hilang jika komputer dimatikan.
</details>

<details>
<summary>❓ Mengapa mengamankan data dari memori RAM harus menjadi prioritas utama (<i>Order of Volatility</i>) dibandingkan mengamankan data dari Hard Disk?</summary>

**Jawaban:** Karena RAM bersifat *Volatile* (sangat rentan hilang). Data di dalam RAM akan hilang secara permanen jika komputer di-`restart` atau dimatikan, sedangkan data di *Hard Disk* akan tetap bertahan.
</details>

<details>
<summary>❓ *Software* penganalisis memori (berbasis *Command Line Python*) apa yang paling banyak digunakan oleh spesialis forensik untuk mengekstrak informasi seperti <i>password hashes</i> dan daftar proses yang berjalan dari file <i>Memory Dump</i>?</summary>

**Jawaban:** Volatility Framework.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya mengetahui perbedaan antara *Disk Forensics* dan *Memory Forensics*.
- [ ] Saya memahami prinsip *Order of Volatility*.
- [ ] Saya mengetahui alasan tidak boleh me-`restart` komputer yang sedang terinfeksi *Ransomware*.
- [ ] Saya mengetahui fungsi dari alat *Volatility Framework*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [Volatility Foundation: Volatility 3](https://www.volatilityfoundation.org/) — Dokumentasi resmi kerangka kerja forensik *Volatility* versi 3 (Berbasis Python 3).

---

## ➡️ Besok

**Day 5: Lab & Mission: Threat Hunting Exercise** — Setelah mempelajari kerangka intelijen *MITRE ATT&CK Framework*, manajemen barang bukti *Chain of Custody*, serta konsep isolasi *Digital Forensics*, besok kita akan melaksanakan laboratorium terpadu. Anda akan berlatih menjadi spesialis keamanan proaktif dengan menyusun **Threat Hunting Playbook** (Buku Panduan Perburuan Ancaman) berdasarkan taktik dari MITRE ATT&CK.

---

*📅 TISS Null Teaming · Week 23 · Day 4 · SENTINEL Rank*
