# 📡 Week 8 · Day 3: Ownership & Privilege Escalation

> **Rank**: PACKET | **Minggu ke-8**, Hari 3/5 | **Durasi**: ~40 menit

📊 **Progress**: Week 8 · Day 3/5 | PACKET Rank (Minggu 4 dari 5) | Overall: 38/120 hari (31%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Mengubah** kepemilikan file menggunakan perintah `chown`
2. **Meminjam** kekuatan Superuser dengan menggunakan perintah `sudo`
3. **Memahami** konsep dasar dari *Privilege Escalation* (Tujuan utama fase peretasan/eksploitasi)

---

## 📖 Materi Inti

### Siapa Pemilik File Ini? (`chown`)

Di Linux, setiap file pasti memiliki **2 Pemilik**:
1. Pemilik Perorangan (*User Owner*)
2. Pemilik Kelompok (*Group Owner*)

Ingat kembali output `ls -l` dari materi kemarin:
`-rwxr-xr-- 1 alice staff 2048 Mar 12 10:00 tugas.txt`

Di sebelah izin `-rwxr-xr--`, kamu melihat kata **alice** (Itu nama *User Owner*), dan **staff** (Itu nama *Group Owner*). Artinya, aturan *permissions* yang kita pelajari kemarin hanya tunduk pada dua entitas ini.

Hanya Root (Superuser) yang boleh mengubah kepemilikan file. Perintahnya adalah **`chown`** (Change Owner).
```bash
# Memberikan file tugas.txt ke akun budi dan grup mahasiswa
$ chown budi:mahasiswa tugas.txt
```

### Sudo: "Superuser Do"

Karena *Root* (UID 0) terlalu kuat, memakainya terus-terusan sangat berbahaya. (Bayangkan kamu nyetir mobil ke pasar tapi pakai mobil Tank berlapis baja. Tersenggol sedikit warung hancur).

Praktek keamanan terbaik (Best Practice) di Linux adalah: **Jangan pernah login langsung sebagai Root**.
Login-lah sebagai akun manusia biasa. Tapi, jika kamu benar-benar butuh mengubah konfigurasi sistem sesekali, pinjamlah kekuatan Root SATU KALI SAJA menggunakan perintah **`sudo`**.

`sudo` artinya: *"Hai sistem, tolong jalankan satu baris perintah di kananku ini SEOLAH-OLAH aku adalah Root."*

**Contoh:**
Kamu adalah user biasa. Kamu mencoba mengedit file konfigurasi server yang dijaga ketat.
```bash
$ nano /etc/nginx.conf
(Akan muncul error: Permission Denied!)

$ sudo nano /etc/nginx.conf
(Sistem akan memintamu mengetik password-MU SENDIRI. Jika kamu punya izin untuk meminjam kekuatan sudo, file akan terbuka secara).
```

### Apa itu Privilege Escalation? (PrivEsc)

Di dunia *Cybersecurity* (terutama tim Red Team / Pentester), ketika kita berhasil menjebol sebuah server, kita biasanya akan masuk sebagai pengguna *level bawah* (misalnya akun bernama `www-data` yang fungsinya cuma buat jalanin web doang). Akun ini sangat lemah, izin `rwx`-nya dibatasi, dan tidak punya izin `sudo`.

Proses mencari celah, bug, atau salah konfigurasi (*misconfiguration*) agar akun *www-data* yang lemah ini bisa tiba-tiba melonjak naik jabatannya menjadi **Root** dinamakan **Privilege Escalation (PrivEsc)**.

**Contoh Skenario PrivEsc (Salah Konfigurasi Sudo):**
Seorang Sysadmin malas membuat aturan: *"Si akun budi boleh menjalankan aplikasi Kalkulator pakai `sudo` (sebagai root) tanpa perlu masukin password."*
Padahal, di dalam aplikasi Kalkulator itu ada fitur "Open File" yang bisa menelusuri seluruh file di harddisk! Si hacker yang meretas akun `budi` akan membuka Kalkulator pakai *sudo*, dan lewat kalkulator itu, ia meretas seluruh sistem! Ini nyata terjadi!

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari uji pemahaman logis tentang bahaya *sudo*.

Sistem operasi Ubuntu tidak pernah memberikan/mengeset *password* untuk akun `root` secara default. Sebagai gantinya, mereka memberikan akses `sudo` kepada *user* pertama yang kamu buat saat instalasi (misalnya akun bernama `ryo`).

**Tugas Refleksi:**
Menurutmu, mengapa sistem operasi sengaja "mengunci" akun Root secara langsung, namun malah memberikan tongkat sihir sakti `sudo` ke akun biasa? Apa keuntungan keamanannya dibandingkan membiarkan orang login bebas pakai username 'root'?

<details>
<summary>🔑 Pembahasan Keamanan</summary>

1. **Mencegah Hacker Brute-Force**: Hacker di seluruh dunia tahu bahwa *username* tertinggi di Linux adalah "root". Jika root diaktifkan, hacker tinggal menebak jutaan *password* (brute-force). Namun jika root dimatikan, hacker harus menebak *dua* hal sekaligus: Nama user aslimu (yang dia tidak tahu) DAN password-mu! Jauh lebih sulit dijebol.
2. **Akuntabilitas (Log Jejak)**: Jika ada 5 admin IT di kantor semua login pakai akun "root" dan server rusak, bos tidak tahu siapa pelakunya. Tapi jika 5 admin login pakai nama mereka sendiri-sendiri lalu mengetik `sudo rm -rf`, sistem (log) akan mencatat siapa nama asli admin yang menggunakan kekuatan super itu!

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Perintah apa yang digunakan untuk mengubah siapa pemilik suatu file?</summary>

**Jawaban:** **`chown`** (Change Owner).

</details>

<details>
<summary>❓ Jika kamu di Terminal menjalankan perintah "apt update" dan mendapati error "Permission Denied: Are you root?", kata ajaib apa yang harus kamu tambahkan di awal perintah tersebut?</summary>

**Jawaban:** **`sudo`**. (Sehingga menjadi `sudo apt update`).

</details>

<details>
<summary>❓ Singkatnya, apa yang dimaksud dengan Privilege Escalation dalam tahapan peretasan (Hacking)?</summary>

**Jawaban:** Proses melompat/mendaki hierarki keamanan sistem (meningkatkan hak akses) dari yang awalnya hanya sebagai user biasa dengan izin sangat terbatas, menjadi **Superuser/Root** yang bisa menguasai seluruh isi komputer.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami struktur kepemilikan file (User & Group)
- [ ] Saya tahu cara kerja perintah `chown`
- [ ] Saya paham mengapa kita menggunakan `sudo` ketimbang login langsung jadi root
- [ ] Saya mengerti secara konsep apa itu *Privilege Escalation*
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Sudo vs Su: What's the difference?](https://www.youtube.com/watch?v=F0k8rNn3gBw) — Penjelasan ringkas soal bedanya `su` (Switch User) yang kita pelajari di Day 1 dengan `sudo`.

---

## ➡️ Besok

**Day 4: Proses & Services** — Server Linux berjalan 24 jam sehari. Bagaimana cara melihat program apa saja yang sedang jalan di balik layar? Dan bagaimana cara "membunuh" program yang sedang *hang*/nge-lag? Besok kita belajar jadi malaikat dengan perintah `kill`!

---

*📅 TISS Null Teaming · Week 8 · Day 3 · PACKET Rank*
