# 📡 Week 5 · Day 5: Lab & Weekly Mission

> **Rank**: PACKET | **Minggu ke-5**, Hari 5/5 | **Durasi**: ~60–90 menit

---

## 📊 Progress Tracker

### Rank Progress
[▓▓░░░░░░░░] 20% — PACKET Rank (Minggu 1 dari 5)

### Overall Journey
[▓▓▓▓▓░░░░░░░░░░░░░░░░░░░] 20% — Hari 25 dari 120

### Rank Map
✅ VOID → ✅ CIPHER → 🔄 PACKET → ⬜ FORGE → ⬜ BREACH → ⬜ SENTINEL

---

## 📝 Rekap Minggu Ini

Minggu ini kamu sudah mempelajari:

| Hari | Topik | Key Takeaway |
|------|-------|-------------|
| Day 1 | OSI Layer (Bawah) | Memecah jaringan jadi L1 (Kabel), L2 (MAC/Switch), L3 (IP/Router), L4 (Port/Transport). |
| Day 2 | OSI Layer (Atas) | Memahami L5 (Sesi), L6 (Enkripsi), L7 (Aplikasi/HTTP) & proses Encapsulation. |
| Day 3 | Model TCP/IP | Di dunia nyata, TCP/IP (4 Layer) yang digunakan, meski teori belajar pakai OSI. |
| Day 4 | IP, Subnet & DNS | IP Public vs Private, dan tugas DNS yang menerjemahkan nama web menjadi angka IP. |

---

## 🧪 Hands-On Lab

Sebagai *Security Engineer*, Terminal/Command Prompt adalah rumah keduamu. Hari ini kita akan menggunakan 3 tool *Command Line* paling dasar untuk jaringan komputermu.

### Prerequisites
- Komputer dengan OS Windows, macOS, atau Linux
- Terkoneksi ke Internet

### Step 1: Identifikasi IP Kamu Sendiri (`ipconfig` / `ifconfig`)

Kita akan mencari tahu apa IP Private dan MAC Address komputermu.

1. Buka **Command Prompt (cmd)** atau **Terminal**.
2. **Windows**: Ketik `ipconfig /all` lalu Enter.
 **Mac/Linux**: Ketik `ifconfig` (atau `ip a`) lalu Enter.
3. Cari bagian yang berhubungan dengan koneksi aktifmu (Misal: *Wireless LAN adapter Wi-Fi* atau *en0*).
4. Catat 3 hal ini di notes-mu:
 - **IPv4 Address**: (Contoh: `192.168.1.5`)
 - **Subnet Mask**: (Contoh: `255.255.255.0`)
 - **Default Gateway**: (Ini adalah IP Router/WiFi-mu, biasanya `192.168.1.1`)

**Expected Output:**
```
Kamu berhasil menemukan identitas komputermu di dalam jaringan lokal (Layer 3).
```

### Step 2: Menguji Konektivitas (`ping`)

`ping` bekerja dengan mengirim paket "Halo" (ICMP Echo Request) ke alamat tujuan, lalu komputer tujuan akan membalas "Ya, saya ada di sini" (ICMP Echo Reply).

1. Mari kita uji apakah router WiFi-mu hidup. Ketik:
 `ping [IP Default Gateway yang kamu catat di Step 1]` (Contoh: `ping 192.168.1.1`)
2. Mari kita uji koneksi internet luar. Ketik:
 `ping 8.8.8.8` (Ini adalah IP DNS milik Google).

**Expected Output:**
```
Kamu mendapatkan pesan "Reply from..." yang berarti komputermu bisa berkomunikasi ke router dan ke internet.
```

### Step 3: Melacak Jejak Rute (`traceroute` / `tracert`)

Saat kamu buka `google.com`, datamu akan melompat dari satu router ke router lain di berbagai kota/negara sebelum sampai ke server Google. Mari kita lacak jejak lompatan (*hops*)-nya!

1. **Windows**: Ketik `tracert google.com`
 **Mac/Linux**: Ketik `traceroute google.com`
2. Tekan Enter dan perhatikan outputnya yang muncul baris demi baris.

Setiap baris yang muncul mewakili satu *Router* yang dilewati oleh paket datamu (Mulai dari router rumah/Indihome, masuk ke *backbone* telkom, mungkin ke kabel bawah laut Singapura, hingga masuk ke server Google).

### 🔧 Troubleshooting

| Masalah | Solusi |
|---------|--------|
| Hasil ping menampilkan "Request timed out" | Ada dua kemungkinan: Internetmu benar-benar mati, atau server yang kamu tuju mematikan fitur balasan Ping demi keamanan (Firewall memblokir ICMP). |
| Hasil traceroute muncul simbol bintang (`* * *`) | Normal. Beberapa router di internet memang menolak memberitahukan identitasnya (demi privasi), sehingga di-masking dengan bintang. Biarkan proses selesai. |

---

## 🎯 Weekly Mission

### Misi: "Network Detective — Laporan Recon Dasar"

**Deskripsi:**
Bosmu di Divisi Infrastruktur memintamu untuk melaporkan profil jaringan dari komputermu saat ini. Dia juga ingin memastikan kamu paham di layer mana tools yang kamu pakai bekerja.

**Deliverables:**
1. Buka repository `cybersec-journey` di VS Code.
2. Buat folder `week-05`.
3. Di dalamnya, buat file `network-report.md`.
4. Isi file tersebut dengan format berikut:

```markdown
# Network Configuration Report

## 1. Local Network Identity
- **My Private IP Address**: [Tulis IP-mu]
- **My Subnet Mask**: [Tulis Subnet-mu]
- **My Router/Gateway IP**: [Tulis IP Gateway-mu]

*Catatan: Konfigurasi IP ini berjalan pada OSI Layer 3 (Network Layer).*

## 2. Public Network Identity
- **My Public IP Address**: [Buka browser, cari di google "What is my IP", lalu tulis hasilnya di sini]

## 3. Connectivity Test
Saya telah melakukan Ping ke IP Gateway dan berhasil. Ini membuktikan bahwa Layer 1 (kabel/sinyal fisik) dan Layer 2 (MAC address/switch) berfungsi dengan baik tanpa masalah.

## 4. Traceroute Analysis
Target: `untirta.ac.id` (Ganti dengan domain favoritmu).
- **Jumlah Hops/Lompatan**: [Tulis butuh berapa baris/lompatan dari traceroute sampai berstatus 'trace complete']
- **Kesimpulan**: Paket data saya harus melewati setidaknya [X] buah router di internet sebelum sampai ke target.
```

**Kriteria Sukses:**
- [ ] Folder `week-05` berisi file `network-report.md`
- [ ] Data Private IP, Subnet, dan Gateway terisi benar dari *ipconfig/ifconfig*
- [ ] Mampu membedakan Public IP (dilihat dari web) dengan Private IP (dilihat dari terminal)
- [ ] Berhasil melakukan `traceroute` ke satu domain dan menghitung *hops*
- [ ] Ter-commit dan di-push ke GitHub

**Estimasi Waktu:** 1 – 1.5 jam

---

## 💡 Knowledge Check

<details>
<summary>❓ [MUDAH] Layer OSI yang bertanggung jawab atas alamat IP dan *Routing* jaringan adalah...</summary>

**Jawaban:** Layer 3 (Network Layer).

</details>

<details>
<summary>❓ [MUDAH] Mengapa kita memerlukan "Default Gateway" dalam konfigurasi jaringan?</summary>

**Jawaban:** Default Gateway adalah pintu keluar (biasanya router/modem). Jika komputermu ingin mengirim data ke perangkat di luar jaringan rumahmu (misalnya ke internet), komputer akan mengirimkan paket tersebut ke pintu keluar (Gateway) agar bisa diteruskan.

</details>

<details>
<summary>❓ [SEDANG] Saat kamu melakukan `ping google.com` dan berhasil, Layer OSI mana saja yang terbukti BEKERJA dengan baik di komputermu?</summary>

**Jawaban:** Layer 1, 2, dan 3. Ping (ICMP) berjalan di atas IP (Layer 3). Jika sukses, secara logika Layer 1 (Kabel/WiFi) dan Layer 2 (Switching lokal) pasti tidak ada masalah.

</details>

<details>
<summary>❓ [SULIT] Temanmu mengeluh: "Aku nggak bisa buka youtube.com sama sekali, tapi pas ngetik IP YouTube di browser langsung kebuka!" <br>Berdasarkan keluhan tersebut, komponen apa di komputernya yang sedang bermasalah?</summary>

**Jawaban:** Komponen **DNS (Domain Name System)**. Temanmu punya koneksi internet yang sehat (dibuktikan bisa memuat web lewat IP), tapi "buku telepon"-nya rusak. DNS tidak bisa meresolusi nama menjadi IP.

</details>

---

## 📋 Weekly Checklist

- [ ] Saya paham urutan 7 Layer OSI Model
- [ ] Saya paham perbedaan Layer OSI vs TCP/IP di dunia nyata
- [ ] Saya tahu bedanya Private IP (Lokal) dan Public IP (Internet)
- [ ] Saya sudah mengerti fungsi dasar dari DNS dan Subnet Mask
- [ ] Saya sudah menyelesaikan Hands-On Lab (ipconfig, ping, tracert)
- [ ] Saya sudah mengerjakan Weekly Mission `network-report.md`
- [ ] File mission sudah ter-push ke GitHub

---

## 💬 Diskusi Minggu Ini

1. Setelah tahu bagaimana traceroute (tracert) bekerja dan melompat dari satu alat ke alat lain di berbagai tempat, apakah menurutmu internet itu tempat yang aman untuk mengirim chat tanpa enkripsi?
2. Berapa jumlah Hops/Lompatan traceroute terbanyak yang kalian temui ke sebuah website? Website apa itu dan kira-kira ada di benua mana servernya? Coba *share* di grup!

---

## 🏆 Achievement Unlocked!

```
┌─────────────────────────────────────┐
│ │
│ 🎖️ PING MASTER │
│ Week 5 Complete │
│ "Hello, World. I see your routes."│
│ │
└─────────────────────────────────────┘
```

---

## ➡️ Preview Minggu Depan

**Minggu 6: Protokol Jaringan & Analisis Trafik (PACKET Rank)**

Minggu ini kamu belajar teorinya. Minggu depan kita akan memakai **"Kacamata Sinar-X"** (Wireshark)! Kita akan mencegat trafik jaringan di udara, melihat isi paket data secara langsung, dan memahami mengapa login tanpa perlindungan enkripsi adalah bencana besar. Bersiaplah untuk melihat sisi lain dari jaringan! 🦈

---

*📅 TISS Null Teaming · Week 5 · Day 5 · PACKET Rank*
