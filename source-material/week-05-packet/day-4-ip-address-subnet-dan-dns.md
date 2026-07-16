# 📡 Week 5 · Day 4: IP Address, Subnet & DNS

> **Rank**: PACKET | **Minggu ke-5**, Hari 4/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 5 · Day 4/5 | PACKET Rank (Minggu 1 dari 5) | Overall: 24/120 hari (20%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** struktur dasar IPv4 dan perbedaannya dengan Public/Private IP
2. **Mengenali** tujuan dari *Subnetting* secara logika awam
3. **Menjelaskan** bagaimana sistem DNS menerjemahkan nama website menjadi IP address

---

## 📖 Materi Inti

### IPv4: Alamat Rumah di Internet (Layer 3)

IP Address (Internet Protocol Address) adalah alamat unik yang diberikan kepada SETIAP perangkat yang terhubung ke jaringan agar bisa saling mengirim paket data.

Format standar yang saat ini masih paling banyak dipakai adalah **IPv4**:
Terdiri dari 4 blok angka (disebut *Oktet*) yang dipisahkan oleh titik.
Contoh: `192.168.1.5` atau `8.8.8.8` (Setiap blok nilainya berkisar antara 0 - 255).

### IP Public vs IP Private

Dunia kehabisan alamat IPv4 (hanya ada sekitar 4.3 Miliar kombinasi, sementara manusia punya milyaran HP dan laptop). Solusinya adalah membaginya menjadi dua jenis:

1. **IP Public**: Alamat unik di internet global yang dikenali seluruh dunia. (Seperti alamat kantormu di jalan raya). Harus dibeli/disewa dari ISP (Indihome, Biznet).
2. **IP Private**: Alamat gratis yang hanya berlaku di *dalam* jaringan lokal rumah/kantormu (LAN). Tidak dikenali internet. 
 - Contoh IP Private yang paling sering kamu lihat: `192.168.x.x` atau `10.x.x.x`.

> 💡 **Fakta**: Seluruh perangkat di rumahmu (HP, Laptop, Smart TV) memiliki **IP Private** berbeda, tapi saat kalian buka YouTube, server YouTube melihat kalian semua berasal dari SATU **IP Public** yang sama (yaitu IP dari router Indihome/modem WiFi-mu). Proses perwakilan ini disebut **NAT (Network Address Translation)**.

### Subnet Mask (Konsep Dasar)

Jika IP adalah alamat lengkap, **Subnet** adalah pembatas yang memisahkan mana bagian "Nama Jalan" (Network) dan mana bagian "Nomor Rumah" (Host).

Contoh Subnet paling umum: `255.255.255.0` (Atau sering ditulis `/24`).
Artinya: Tiga angka pertama dari IP tidak boleh berubah (Nama Jalan), dan satu angka terakhir bebas diisi (Nomor Rumah).
- Jika IP-mu `192.168.1.10`, kamu bisa mengirim pesan langsung ke `192.168.1.25` (satu jalan).
- Tapi kamu TIDAK BISA kirim langsung ke `192.168.2.10` tanpa melalui rute khusus (beda jalan).

### DNS (Domain Name System)

Komputer hanya peduli pada angka (IP Address). Manusia buruk dalam mengingat angka. 
Kamu tidak mengetik `142.250.191.46` di browser, kamu mengetik `google.com`.

**DNS** adalah "Buku Telepon Raksasa" internet.
Tugasnya sangat sederhana: Menerjemahkan nama (domain) menjadi angka (IP).

**Proses saat kamu mengetik google.com:**
1. Browser tanya ke Komputermu: *"Tahu IP google.com?"*
2. Komputer tanya ke DNS Server (biasanya milik Indihome/Telkomsel): *"Bro, tolong carikan IP google.com!"*
3. DNS Server mencari di buku telepon raksasanya: *"Ketemu! IP-nya 142.250.191.46."*
4. Barulah komputermu mengirim paket data ke IP `142.250.191.46`.

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari kita main dengan Command Line dan melihat fungsi DNS secara langsung!

1. Buka **Command Prompt (cmd)** di Windows atau **Terminal** di Mac/Linux.
2. Kita akan meminta komputer kita melempar sebuah sinyal "Halo" (Ping) ke website dan melihat DNS menerjemahkannya.
3. Ketik perintah ini:
 `ping untirta.ac.id`
 lalu tekan Enter.

**Expected Output:**
```
Pinging untirta.ac.id [103.15.226.2] with 32 bytes of data:
Reply from 103.15.226.2: bytes=32 time=23ms TTL=54
...
```

Perhatikan baris pertama: `Pinging untirta.ac.id [103.15.226.2]`.
Komputermu diam-diam melakukan *query* (pertanyaan) ke DNS, dan DNS memberi tahu bahwa nama itu memiliki IP Public `103.15.226.2`!

Coba ulangi dengan target `youtube.com` atau website favoritmu!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Jika HP kamu terhubung ke WiFi kampus dan mendapat IP 192.168.10.55, apakah temanmu yang berada di rumah bisa mengakses IP tersebut dari internet?</summary>

**Jawaban:** **Tidak bisa**. Karena IP yang dimulai dengan `192.168.x.x` adalah **IP Private**. IP tersebut hanya dikenali dan bisa diakses oleh perangkat-perangkat yang sama-sama terhubung di WiFi/jaringan kampus tersebut.

</details>

<details>
<summary>❓ Mengapa DNS sering disebut "Buku Telepon" internet?</summary>

**Jawaban:** Karena manusia lebih mudah mengingat nama (seperti `tiss.or.id`), sementara jaringan komputer hanya bisa merutekan paket berdasarkan angka (IP Address). Seperti halnya kita mencari nama teman di buku telepon untuk mendapatkan nomor HP-nya, browser meminta DNS mencari nama domain untuk mendapatkan IP-nya.

</details>

<details>
<summary>❓ Apa yang terjadi jika DNS server yang kamu gunakan (misal milik ISP Indihome) mati/down?</summary>

**Jawaban:** Kamu akan mengeluh *"Internet mati!"* karena browser tidak bisa membuka web apa pun menggunakan nama (tampil error DNS_PROBE_FINISHED). Namun faktanya, koneksi internetmu masih menyala. Jika kamu mengetik IP address langsung (misal mengetik `1.1.1.1` di browser), halamannya akan tetap terbuka.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya paham perbedaan IP Public dan IP Private
- [ ] Saya paham mengapa kita perlu NAT (karena IP Public terbatas)
- [ ] Saya mengerti secara logika apa guna Subnet Mask
- [ ] Saya paham cara kerja DNS menerjemahkan nama ke IP
- [ ] Saya sudah melakukan Mini Lab dengan perintah `ping`
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [How IP Addresses Work (Video - PowerCert)](https://www.youtube.com/watch?v=53Z2qP6lXmE) — Penjelasan visual yang sangat detail mengenai IPv4.

---

## ➡️ Besok

**Day 5: Lab & Mission: Identifikasi Jaringan** — Saatnya *Hands-On* penuh! Besok kamu akan berubah menjadi "Network Detective". Kamu akan belajar menggunakan 3 command legendaris jaringan dan mengidentifikasi informasi jaringan dari komputermu sendiri!

---

*📅 TISS Null Teaming · Week 5 · Day 4 · PACKET Rank*
