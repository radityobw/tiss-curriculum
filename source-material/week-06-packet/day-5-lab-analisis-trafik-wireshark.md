# 📡 Week 6 · Day 5: Lab & Weekly Mission

> **Rank**: PACKET | **Minggu ke-6**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓▓▓░░░░░░] 40% — PACKET Rank (Minggu 2 dari 5)

### Overall Journey
[▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░] 25% — Hari 30 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → 🔄 PACKET → ⬜ FORGE → ⬜ BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Minggu ini kamu sudah mempelajari:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | TCP vs UDP | TCP = Andal & Lambat (3-way handshake). UDP = Cepat & Bodo amat (Streaming). |
| Day 2 | HTTP & HTTPS | GET vs POST. HTTP Status (200 OK, 404 Not Found, 500 Error). HTTPS dienkripsi TLS. |
| Day 3 | DNS, ARP, DHCP, ICMP | Protokol pendukung yang berjalan secara magis di background jaringan. |
| Day 4 | Pengenalan Wireshark | Cara kerja packet sniffer dan menggunakan display filter agar tidak mabuk data. |

---

## 🧪 Hands-On Lab

Hari ini kita akan mengasah insting detektif jaringanmu dengan mempraktikkan konsep bahaya *Plaintext* menggunakan Wireshark.

### Prerequisites
- Aplikasi Wireshark sudah terinstal dan bisa melakukan *capture*
- Browser biasa
- Repository `cybersec-journey`

### Step 1: Merekam Jejak (Sniffing)

1. Buka **Wireshark**. Pilih adapter WiFi/Ethernet yang aktif dan klik ikon "Sirip Hiu" biru di pojok kiri atas untuk memulai **Start Capture**.
2. Biarkan Wireshark menyala. Sekarang buka browsermu (Chrome/Firefox).
3. Kunjungi website percobaan yang sengaja dibuat tidak aman ini (Jangan khawatir, ini legal dari organisasi keamanan Acunetix):
 **`http://testphp.vulnweb.com/login.php`** 
 *(Perhatikan bahwa URL-nya HTTP, bukan HTTPS!)*
4. Di halaman login website tersebut, masukkan data sembarangan:
 - Username: `hacker_tiss`
 - Password: `PasswordSuperRahasia123`
5. Klik tombol **Login**.
6. Segera kembali ke Wireshark, dan klik kotak merah (Stop Capture).

**Expected Output:**
```
Wireshark sudah menyimpan jutaan bit data yang terjadi di komputermu selama kamu login.
```

### Step 2: Menemukan Jarum di Tumpukan Jerami

Sekarang mari kita buktikan mengapa login HTTP (tanpa S/TLS) adalah bencana.

1. Di kotak **Display Filter** (baris warna hijau di atas), ketik: `http.request.method == "POST"` lalu tekan Enter.
 *(Ini memfilter paket dan hanya menyisakan aktivitas di mana kamu MENGIRIM form data).*
2. Kamu seharusnya hanya melihat 1 atau 2 baris paket tersisa. 
3. Klik pada baris yang *Info*-nya tertulis `POST /login.php HTTP/1.1`.
4. Sekarang perhatikan layar **Packet Details** (kotak tengah). Buka anak panah yang bernama **HTML Form URL Encoded: application/x-www-form-urlencoded**.

BAM! Kamu akan melihat `uname: hacker_tiss` dan `pass: PasswordSuperRahasia123` tertulis dengan sangat jelas dan telanjang!

> ⚠️ Jika *attacker* (hacker) satu jaringan WiFi Cafe denganmu sedang menjalankan Wireshark saat kamu login ke website HTTP, inilah persisnya apa yang akan mereka lihat. Sandi-mu dicuri bahkan sebelum kamu sadar.

### 🔧 Troubleshooting

| Masalah | Solusi |
|---------|--------|
| Filter POST tidak menampilkan paket apa-apa | Pastikan URL-nya `http://` (Bukan `https://`). Jika otomatis ter-redirect ke https oleh browsermu (fitur HTTPS-Only mode), matikan sementara fitur itu di setting browser, atau gunakan browser beda (seperti Edge/Safari mode Incognito). |

---

## 🎯 Weekly Mission

### Misi: "Network Analyst — Inspeksi Paket"

**Deskripsi:**
Kamu telah membuktikan rapuhnya protokol tanpa enkripsi. Sekarang saatnya membuktikan bahwa kamu mengerti anatomi sebuah paket dari atas ke bawah sesuai lapisan OSI.

**Deliverables:**
1. Buka repository `cybersec-journey` di VS Code.
2. Buka folder `week-06`.
3. Di dalamnya, buat file `wireshark-analysis.md`.
4. Berdasarkan paket `POST /login.php` yang kamu tangkap di Lab, bedah isi *Packet Details* (kotak tengah Wireshark) dan isikan informasi berikut ke dalam Markdown:

```markdown
# Wireshark Packet Analysis Report

## 1. Frame Details (Layer 2)
- **Source MAC Address**: [Klik 'Ethernet II', cari 'Source']
- **Destination MAC Address**: [Cari 'Destination']

## 2. IP Details (Layer 3)
- **Source IP Address**: [Klik 'Internet Protocol Version 4', cari 'Source Address']
- **Destination IP Address**: [Cari 'Destination Address']
- **Time to Live (TTL)**: [Cari nilai TTL]

## 3. Transport Details (Layer 4)
- **Protokol yang digunakan**: [Apakah TCP atau UDP?]
- **Source Port**: [Klik 'Transmission Control Protocol', cari 'Source Port']
- **Destination Port**: [Cari 'Destination Port']

## 4. Application Details (Layer 7)
- **Protokol Utama**: HTTP
- **Tipe Method**: POST
- **Host Target**: testphp.vulnweb.com
- **Credential yang disadap**: [Tulis username dan password yang kamu tangkap]

## Kesimpulan
[Tulis 2 kalimat menjelaskan mengapa form login harus selalu menggunakan HTTPS]
```

**Kriteria Sukses:**
- [ ] Folder `week-06` berisi file `wireshark-analysis.md`
- [ ] Nilai MAC, IP, Port, dan Credential terisi dengan benar (tidak masalah jika nilai MAC dan IP milikmu berbeda dari temanmu, yang penting cara mencarinya tahu).
- [ ] Kesimpulan logis tertulis.
- [ ] Ter-commit dan di-push ke GitHub.

**Estimasi Waktu:** 1.5 jam

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Port berapa yang umumnya digunakan oleh protokol HTTP dan HTTPS?</summary>

**Jawaban:** **Port 80** untuk HTTP (tidak aman), dan **Port 443** untuk HTTPS (aman terenkripsi).

</details>

<details>
<summary>❓ [SEDANG] Di dalam Wireshark, apa bedanya menggunakan display filter `http` vs `tcp`?</summary>

**Jawaban:** 
- Filter `tcp` akan memunculkan *semua* komunikasi yang mengandalkan keandalan TCP (termasuk HTTPS, FTP, SSH, dan proses *Three-Way Handshake*).
- Filter `http` HANYA akan memunculkan komunikasi di Layer 7 yang menggunakan protokol web yang tidak dienkripsi.

</details>

<details>
<summary>❓ [SULIT] Saat kita mengirim paket POST ke testphp.vulnweb.com (IP: 44.228.249.3), mengapa "Destination MAC Address" di paket Layer 2 kita BUKANLAH MAC Address milik server web testphp, melainkan MAC Address router WiFi kita?</summary>

**Jawaban:** Karena konsep Layer 2 (Switching lokal)! Komputermu tahu bahwa IP `44.228.249.3` tidak ada di jaringan rumah/kosanmu. Oleh karena itu, komputermu mengemas paket (Layer 2) dengan MAC Address milik *Default Gateway* (Router WiFi), dengan harapan Router tersebut akan meneruskannya ke luar negeri hingga sampai ke server target (Routing Layer 3). MAC Address hanya bertahan 1 lompatan!

</details>

---

## 📋 Weekly Checklist

- [ ] Saya memahami alur kerja TCP Handshake
- [ ] Saya bisa menjelaskan siklus HTTP Request dan Response
- [ ] Saya hafal perbedaan fungsi DHCP, DNS, ARP, dan ICMP
- [ ] Saya sudah menyelesaikan Hands-On Lab menyadap jaringan sendiri
- [ ] Saya menemukan password plaintext di dalam Wireshark
- [ ] Saya sudah mengerjakan Weekly Mission `wireshark-analysis.md`
- [ ] File mission sudah ter-push ke GitHub

---

## 💬 Diskusi Minggu Ini

1. Setelah melihat sendiri betapa mudahnya password disadap jika menggunakan HTTP biasa, apakah pandanganmu terhadap jaringan *Public WiFi* (seperti di Cafe atau Bandara) berubah?
2. Saat kalian mengecek "Source Port" pada Misi Mingguan (Layer 4), apakah angkanya 80? (Hint: Bukan. Lalu angka berapakah itu dan mengapa komputer kita memilih angka acak tersebut?). Diskusikan di grup!

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 🎖️ PACKET SNIFFER │
│ Week 6 Complete │
│ "There are no secrets on the wire,│
│ only plaintext waiting to be │
│ read." │
│ │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 7: Linux — Memulai dari Nol (PACKET Rank)**

Ucapkan selamat tinggal pada GUI (Grafis) yang dimanjakan oleh Mouse!
Minggu depan kita akan menyelami sistem operasi yang paling dicintai sekaligus ditakuti: **Linux**. Sebagai peretas dan penjaga jaringan, terminal Linux adalah tempat kamu akan menghabiskan sisa hidupmu. Kita mulai dari 0!

> 🚀 *"Unix is user-friendly. It just isn't promiscuous about which users it's friendly with."* — Steven Levy

---

*📅 TISS Null Teaming · Week 6 · Day 5 · PACKET Rank*
