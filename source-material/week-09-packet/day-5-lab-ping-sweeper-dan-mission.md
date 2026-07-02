# 📡 Week 9 · Day 5: Lab & Ujian Kenaikan Rank (PACKET Finale!)

> **Rank**: PACKET | **Minggu ke-9**, Hari 5/5 | **Durasi**: ~90–120 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓▓▓▓▓▓▓] 100% — PACKET Rank (Minggu 5 dari 5)

### Overall Journey
[▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░] 37% — Hari 45 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → ✅ PACKET → 🔄 FORGE → ⬜ BREACH → ⬜ SENTINEL

---

## 📝 Rekap Rank PACKET (Week 5 - 9)

Sebulan terakhir, kamu baru saja mempelajari jantung dari Ilmu Komputer!

| Topik Utama | Key Takeaway yang harus dikuasai |
|------|-------------|
| **Networking Dasar** | Paham OSI Layer. IP itu alamat jauh, MAC itu alamat dekat. DNS menerjemahkan nama ke IP. TCP itu hati-hati, UDP itu sembrono. HTTPS mengamankan web dengan TLS. |
| **Linux Fundamentals**| Akar sistem adalah `/`. Jauhi `rm -r`. Gunakan `grep` untuk mencari jarum di tumpukan teks. `sudo` = kekuatan tuhan sementara. Hak akses `rwx` bukan main-main. |
| **Shell Automation** | Hacker benci mengetik. Bungkus perintahmu di dalam file `.sh` (Bash). Gunakan *For Loop*, dan jadwalkan dengan *Cron* 5 Bintang. |

---

## 🧪 Hands-On Lab (Misi Capstone Ping Sweeper)

Hari ini adalah misi pemungkas. Kita tidak akan membaca teori lagi. Kamu akan menguji pemahaman *Networking* (Ping/IP) dan *Bash Scripting* (For Loop) secara bersamaan.

Di dunia *cybersecurity*, serangan tidak dimulai dengan retasan canggih. Ia dimulai dengan **Pemindaian Jaringan (Network Sweep)**: Hacker datang ke WiFi kantor, diam-diam menanyakan "Hai, adakah komputer yang hidup di ruangan ini?", lalu mencatat semua alamat IP yang menjawab, untuk diserang nanti.

Hari ini, kamu akan membangun *Ping Sweeper* milikmu sendiri dari nol!

### Prerequisites
- OS Windows (WSL), Linux, atau macOS.
- Repository `cybersec-journey` (Folder `week-09`).

### Tahap 1: Merancang Script Bash
1. Buka folder `week-09` dan buat file bernama `sweeper.sh`.
2. Sebuah jaringan lokal rumah/kosan standar (kelas C) biasanya memiliki alamat IP berawalan `192.168.1.[nomor]`. Nomor belakang ini (disebut *host*) dimulai dari 1 hingga 254.
3. Alih-alih mengetik `ping` 254 kali, kita akan menggunakan *For Loop* dengan urutan rentang angka (Sequence).

Tulis kode berbahaya ini di dalam file `sweeper.sh`:

```bash
#!/bin/bash

# Pastikan script ini dimatikan pakai CTRL+C jika kelamaan
echo "=============================="
echo "💀 TISS PING SWEEPER 💀"
echo "=============================="

# Kita minta 3 angka depan IP (Subnet-nya) dari user
read -p "Masukkan 3 angka depan IP (Contoh: 192.168.1) : " subnet

echo "Memulai penyapuan pada jaringan $subnet.0/24..."
echo "Mohon tunggu. Proses ini akan mengecek dari IP 1 hingga 254..."

# FOR LOOP Kematian: Mengurutkan angka dari 1 sampai 254
for ip in {1..254}
do
 # Kita gabungkan $subnet dengan nomor urut $ip (contoh jadi 192.168.1.5)
 # Ping 1 kali (-c 1), kalau butuh cepat batasi waktu 1 detik (-W 1)
 
 # MAGIC: Kita saring (grep) hanya tanggapan yang tulisannya "bytes from" 
 # (yang berarti komputer itu hidup dan menjawab ping kita).
 
 ping -c 1 -W 1 $subnet.$ip | grep "bytes from" | awk '{print $4}' | cut -d ":" -f 1 &
 
 # Simbol '&' di ujung perintah membuat proses ini berjalan paralel (multitasking).
 # Agar 254 ping jalan berbarengan dalam sedetik!
done

wait
echo "=============================="
echo "Penyapuan Selesai!"
```

### Tahap 2: Eksekusi Serangan

1. Simpan script tersebut (`CTRL+O`, `CTRL+X`).
2. Berikan izin eksekusi: `chmod +x sweeper.sh`
3. Cek IP komputermu sendiri (buka tab terminal baru, ketik `ipconfig` / `ifconfig` atau `ip a`). Lihat 3 angka depan IP WiFimu. Misalkan komputermu mendapat `192.168.100.22`. Berarti 3 angka depannya adalah `192.168.100`.
4. Jalankan script: `./sweeper.sh`
5. Masukkan 3 angka depan tadi.
6. Lihat ajaibnya layarmu akan langsung menampilkan deretan angka-angka (Misal: `192.168.100.1`). Itulah daftar gadget (HP, Kulkas pintar, Laptop teman) yang saat ini nyala dan terkoneksi di WiFimu secara realtime!

> ⚠️ **Catatan Etika:** Tool buatanmu ini sekarang setara dengan fungsi alat *hacking* asli (seperti Nmap). Jangan menyapu (*sweep*) jaringan kosan teman lalu menyerang IP-nya tanpa izin (Gunakan sebatas *Ping* penanda kehadiran saja).

---

## 🎯 Weekly Mission (Capstone Writeup)

### Misi: "Buku Panduan Jaringan"

**Deskripsi:**
Kamu sudah menyelesaikan *script* peretasan pertamamu! Untuk meluluskanmu dari rank PACKET, kamu harus menyetorkan file dokumentasi akhir ke GitHub.

**Deliverables:**
Di folder `week-09`, buat file `packet-final-report.md`. Isikan laporan singkat terkait skrip buatanmu.

```markdown
# PACKET Rank Finale: Network Sweeper

## 1. Bukti Kode
[Copy-Paste isi script sweeper.sh milikmu di sini di dalam format ```bash ]

## 2. Analisis Hasil
- **Subnet yang disapu**: [Contoh: 192.168.1]
- **Berapa jumlah IP yang hidup terdeteksi?**: [Hitung berapa baris IP yang muncul dari scriptmu]
- **Asumsi**: [Berdasarkan hasil, kira-kira IP mana yang merupakan Router WiFi-nya? (Hint: Biasanya IP terkecil berakhiran 1, atau IP teratas)]

## 3. Penjelasan Teknis
- Kenapa kita harus menggunakan command `chmod +x` pada file `sweeper.sh`? [Tulis jawabanmu]
- Apa arti rentang `{1..254}` pada loop di dalam script? [Tulis jawabanmu]
```

**Kriteria Sukses:**
- [ ] Folder `week-09` berisi file `sweeper.sh` yang bisa dieksekusi (jalan sukses)
- [ ] Folder `week-09` berisi file `packet-final-report.md` yang lengkap
- [ ] Seluruh file ter-commit dan di-push ke GitHub

---

## 💡 Knowledge Check (PACKET Final Quiz)

<details>
<summary>❓ [MUDAH] Kamu ingin *script* Bash buatanmu yang berjalan diam-diam (background) me-log kejadian otomatis setiap HARI MINGGU pukul 05:00 pagi. Bagaimana formasi 5 bintang (Cron) untuk jadwal ini?</summary>

**Jawaban:** `0 5 * * 0` (Menit 0, Jam 5, Tanggal bebas, Bulan bebas, Hari ke-0/Minggu).

</details>

<details>
<summary>❓ [SEDANG] Pada script Sweeper yang kita buat, kita meletakkan simbol `&` (Ampersand) di ujung perintah ping di dalam *loop*. Apa yang terjadi jika simbol tersebut kita hapus?</summary>

**Jawaban:** Jika simbol `&` (Background process/Multitasking) dihapus, *For Loop* akan berjalan **berurutan (sekuensial)**. Script akan mem-ping `192.168.1.1`, *menunggu selama 1 detik* sampai selesai, baru bergeser ke ping IP ujung `.2`, dan seterusnya. Menyapu 254 IP akan memakan waktu nyaris 4-5 menit! Dengan simbol `&`, 254 perintah ping dilempar ke background secara bersamaan, sehingga penyapuan selesai kurang dari 2 detik!

</details>

<details>
<summary>❓ [SULIT] Hubungkan ilmu Jaringan dan Linux: Mengapa saat kita menjalankan `ping google.com` pada Ubuntu, aplikasi Ping tersebut bisa otomatis tahu IP Address Google? Apa nama layanan (service) sistem atau protokol di belakang layar yang mencari IP tersebut?</summary>

**Jawaban:** Sistem Linux menggunakan **DNS Resolver** di latar belakang. Saat kamu mengetik nama domain, secara *default* Linux akan memeriksa file lokal `/etc/hosts` terlebih dahulu. Jika tidak ada, sistem akan bertanya pada **DNS Server** luar (biasanya pakai port UDP 53) untuk meminta terjemahan alamat IP-nya.

</details>

---

## 📋 PACKET Rank Final Checklist

- [ ] Saya telah menaklukkan konsep dasar *Networking* TCP/IP dan OSI
- [ ] Saya telah menaklukkan terminal hitam putih *Linux* (Tidak butuh GUI!)
- [ ] Saya telah berhasil membuat *Bash Script* pertamaku dan memahaminya
- [ ] Saya menyelesaikan Misi Capstone Ping Sweeper
- [ ] Repositori GitHub ter-update!

---

## 💬 Diskusi Penutup Rank PACKET

1. Dari 5 minggu terakhir, apa topik yang membuat otakmu paling "meledak" atau paling sulit dimengerti? Apakah saat OSI layer, menghafal perintah Bash, atau OverTheWire?
2. Bagaimana rasanya ketika kamu menekan tombol Enter pada `sweeper.sh` buatanmu dan tiba-tiba daftar IP di kosan/rumahmu bermunculan? Apakah kamu merasa kekuasaan ada di ujung jarimu? 😈

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────────┐
│ │
│ 🎖️ PACKET COMPLETE │
│ Week 9 of 24 Complete │
│ "Your foundation is solid. │
│ The network obeys your command." │
│ │
│ 📡 Rank: PACKET → CLEARED! │
│ 📊 Progress: 37% │
│ 🔜 Next Rank: FORGE │
│ │
└─────────────────────────────────────────┘
```

---

## ➡️ Preview Rank Selanjutnya

Selamat beristirahat di akhir pekan panjang!

Mulai **Minggu ke-10**, kita akan meninggalkan infrastruktur dan masuk ke ranah **Aplikasi Web**. Kamu akan naik pangkat ke rank **🛠️ FORGE**. Selama 5 minggu ke depan, kamu akan diajarkan dari nol (seperti bayi) bagaimana cara *website* modern dibangun. Kamu akan belajar HTML, CSS, JavaScript, hingga Database SQL.

Mengapa calon peretas harus belajar bikin *website*?
> 🚀 *"Kamu tidak akan pernah bisa menghancurkan atau meretas sebuah bangunan, jika kamu tidak tahu bagaimana cara arsitek menyusun batu batanya."*

Persiapkan dirimu. Selamat datang di dunia Web Development!

---

*📅 TISS Null Teaming · Week 9 · Day 5 · PACKET Rank*
