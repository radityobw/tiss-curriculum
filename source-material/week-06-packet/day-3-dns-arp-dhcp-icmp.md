# 📡 Week 6 · Day 3: DNS, ARP, DHCP, ICMP

> **Rank**: PACKET | **Minggu ke-6**, Hari 3/5 | **Durasi**: ~40 menit

📊 **Progress**: Week 6 · Day 3/5 | PACKET Rank (Minggu 2 dari 5) | Overall: 28/120 hari (23%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** empat protokol krusial yang mengotomatisasi konektivitas jaringan
2. **Menjelaskan** cara DHCP membagikan alamat IP secara otomatis
3. **Memahami** proses konversi IP Address ke MAC Address menggunakan ARP

---

## 📖 Materi Inti

### Pahlawan Jaringan Tanpa Tanda Jasa

Saat kamu membawa laptop ke kampus dan terhubung ke WiFi kampus, kamu tidak perlu mengonfigurasi IP, DNS, atau rute apa pun secara manual. Tiba-tiba saja kamu bisa internetan.

Itu semua berkat protokol-protokol di belakang layar. Kita akan membahas empat "unsung heroes" ini: **DHCP, DNS, ARP, dan ICMP.**

---

### 1. DHCP (Dynamic Host Configuration Protocol)
*Si Pemberi Alamat Otomatis*

Dulu, setiap nambah komputer baru, orang IT harus jalan ke meja itu dan mengetikkan IP address yang kosong secara manual. Repot sekali!

**DHCP** mengotomatisasi ini. Saat laptopmu connect ke WiFi kampus:
1. **Discover**: Laptopmu teriak (Broadcast), *"Halo! Adakah DHCP Server di sini? Saya butuh IP!"*
2. **Offer**: Router kampus menjawab, *"Oh ada, ini aku pinjamkan IP 192.168.10.25 ya."*
3. **Request**: Laptopmu membalas, *"Oke, aku setuju pakai IP itu."*
4. **Ack**: Router mencatat, *"Sip, IP itu aku pinjamkan ke kamu selama 24 jam."*

*(Ini disebut proses D-O-R-A).*

---

### 2. DNS (Domain Name System)
*Si Buku Telepon*

Sudah dibahas sekilas di minggu lalu. DNS bekerja di Layer 7 (Application) menggunakan **UDP Port 53** (karena butuh super cepat).
- Komputer: *"DNS Server, apa IP-nya academy.tiss.or.id?"*
- DNS: *"IP-nya adalah 103.111.90.5."*

> ⚠️ **Hacker Note**: Karena DNS sering tidak terenkripsi, hacker (lewat teknik *DNS Spoofing*) bisa meretas DNS lokalmu sehingga saat kamu mengetik `bca.co.id`, kamu justru diarahkan ke IP website palsu milik hacker.

---

### 3. ARP (Address Resolution Protocol)
*Si Pencari KTP Fisik*

Ini yang paling sering membingungkan pemula. 
- **IP Address (L3)** digunakan untuk mengirim data antar benua (Global).
- Tapi di dalam ruangan yang sama, *Switch* (L2) hanya peduli pada **MAC Address (L2)**!

Bagaimana komputer tahu MAC Address teman di sebelahnya? Jawabannya: **ARP**.

1. Komputermu (IP `10.5`) ingin kirim file ke komputer teman (IP `10.8`). Kamu tahu IP-nya, tapi tidak tahu MAC Address-nya.
2. Komputermu teriak (ARP Broadcast) ke seluruh ruangan: *"Woy! Siapa yang punya IP 10.8? Tolong kasih tahu MAC Address-mu ke aku!"*
3. Komputer temanmu diam-diam membalas (Unicast): *"Itu aku. Ini MAC Address-ku: AA:BB:CC:11:22:33."*
4. Komputermu menyimpannya dalam *ARP Cache*, dan data pun dikirim.

---

### 4. ICMP (Internet Control Message Protocol)
*Si Alat Diagnosa*

ICMP bukanlah protokol pengirim data aplikasi (seperti video atau chat). ICMP adalah protokol *diagnostik* (pemeriksa kesehatan jaringan).
Beroperasi di **Layer 3 (Network)**, ia tidak menggunakan TCP maupun UDP! 

Alat jaringan legendaris seperti `ping` dan `traceroute` menggunakan paket ICMP.
- Pesan ICMP Type 8: **Echo Request** ("Halo, kamu hidup?")
- Pesan ICMP Type 0: **Echo Reply** ("Ya, saya hidup!")
- Pesan ICMP Type 3: **Destination Unreachable** ("Maaf, komputernya tidak ketemu di jaringan").

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari bongkar meja kerja ARP dan DHCP di komputermu sendiri!

**Melihat Tabel ARP:**
1. Buka Terminal atau Command Prompt (cmd).
2. Ketik: `arp -a`
3. Kamu akan melihat daftar IP Address dan *Physical Address* (MAC) perangkat-perangkat (seperti HP, SmartTV, atau komputer teman) yang baru saja "ngobrol" dengan komputermu di jaringan rumah/kosan yang sama.

**Melihat IP Server DHCP dan DNS (Windows):**
1. Ketik: `ipconfig /all`
2. Cari baris **DHCP Server** dan **DNS Servers**. Biasanya IP-nya sama dengan IP *Default Gateway* (karena router rumahan seperti Indihome merangkap tiga jabatan sekaligus: jadi Router, jadi DHCP Server, dan jadi DNS Forwarder).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Singkatan D-O-R-A merujuk pada proses apa di protokol DHCP?</summary>

**Jawaban:** Proses komputer meminta IP otomatis. 
**D**iscover (Mencari server), **O**ffer (Server menawarkan IP), **R**equest (Komputer menyetujui), **A**cknowledge (Server mencatat/mengkonfirmasi).

</details>

<details>
<summary>❓ Mengapa kita membutuhkan ARP? Bukankah alamat IP sudah cukup untuk mengirim pesan?</summary>

**Jawaban:** IP Address hanya berguna untuk *Routing* di Layer 3 (membawa paket jarak jauh). Namun, di jarak dekat (di dalam satu jaringan lokal / LAN yang sama), perangkat keras jaringan seperti Switch bekerja di Layer 2 dan HANYA bisa mengirim data menggunakan **MAC Address**. ARP menjembatani keduanya dengan menerjemahkan IP menjadi MAC Address.

</details>

<details>
<summary>❓ Jika kamu mengetik "ping 8.8.8.8" dan mendapat respons "Destination Host Unreachable", protokol apa yang sedang mengirimkan pesan error tersebut ke layarmu?</summary>

**Jawaban:** **ICMP**. `ping` dan pesan *error/diagnostic* jaringan adalah domain eksklusif milik protokol ICMP.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami bahwa DHCP membebaskan kita dari penderitaan mengetik IP manual
- [ ] Saya paham D-O-R-A process
- [ ] Saya paham mengapa MAC address tetap butuh dicari (ARP) meski sudah ada IP
- [ ] Saya tahu bahwa command `ping` di balik layar menggunakan ICMP
- [ ] Saya sudah melakukan lab `arp -a`
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [PowerCert: ARP Explained](https://www.youtube.com/watch?v=cn8ZJqhfQRo) — Video visual yang sangat jelas tentang bagaimana ARP teriak di dalam jaringan untuk mencari MAC Address.

---

## ➡️ Besok

**Day 4: Pengenalan Wireshark** — Ini dia momen yang ditunggu-tunggu! Besok kita akan meng-install *software* "Hacker Jaringan" paling ikonis di dunia: **Wireshark**. Kita akan mulai "menyadap" (*sniffing*) semua protokol yang kita pelajari minggu ini saat melintas di udara! 🦈

---

*📅 TISS Null Teaming · Week 6 · Day 3 · PACKET Rank*
