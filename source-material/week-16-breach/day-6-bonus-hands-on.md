# 🎯 Week 16 · Day 6 (Bonus): Hands-On Learning

> **Rank**: BREACH | **Minggu ke-16** | Bonus Day

---

## 🌐 Platform Hari Ini

**[PortSwigger Web Security Academy — SQL Injection Labs](https://portswigger.net/web-security/sql-injection)**
Laboratorium SQL Injection gratis dari PortSwigger yang menyediakan lingkungan web nyata untuk mempraktikkan berbagai teknik SQLi: UNION-based, Blind, dan authentication bypass.

💰 **Biaya**: Gratis (semua lab gratis, tanpa batasan)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Menyelesaikan minimal 3 lab SQL Injection di PortSwigger
2. Mempraktikkan teknik UNION-based SQLi yang dipelajari di Day 1
3. Menulis writeup langkah demi langkah untuk setiap lab yang diselesaikan

---

## 📋 Requirement

* Akun PortSwigger (gratis)
* Peramban web modern (Chrome/Firefox)
* Burp Suite Community Edition (sudah diinstal, atau gunakan browser langsung)

> ⚠️ **Jika belum punya akun PortSwigger**: Buka [portswigger.net](https://portswigger.net/users/register), daftar dengan email aktif. Gratis.

> ⚠️ **Burp Suite opsional untuk lab ini.** Lab bisa dikerjakan langsung di browser tanpa Burp Suite untuk level Apprentice.

---

## 📝 Prosedur

### Langkah 1: Akses Lab
1. Login ke [PortSwigger Web Security Academy](https://portswigger.net/web-security)
2. ke **SQL Injection** → klik **View all labs**
3. Mulai dari lab berlabel **APPRENTICE** (tingkat pemula)

### Langkah 2: Lab 1 — SQL Injection in WHERE Clause
1. Klik lab **"SQL injection vulnerability in WHERE clause allowing retrieval of hidden data"**
2. Klik **Access the lab** — environment web akan terbuka
3. Eksplorasi: Ini adalah toko online dengan kategori produk
4. Perhatikan URL saat mengklik kategori: `...?category=Gifts`
5. Coba modifikasi parameter URL:
 ```
?category=Gifts' OR 1=1--
 ```
6. Jika semua produk muncul (termasuk yang tersembunyi) — lab solved! ✅

> 💡 **Konsep**: `OR 1=1` membuat kondisi WHERE selalu TRUE, sehingga semua baris data dikembalikan. `--` mengkomentari sisa query.

### Langkah 3: Lab 2 — Login Bypass
1. Kembali ke daftar lab, pilih lab **"SQL injection vulnerability allowing login bypass"**
2. Klik **Access the lab**
3. Buka halaman login (`/login`)
4. Di kolom username, masukkan: `administrator'--`
5. Di kolom password, masukkan sembarang teks
6. Klik Login — jika masuk sebagai administrator, lab solved! ✅

### Langkah 4: Lab 3 — UNION Attack (Determining Columns)
1. Pilih lab **"SQL injection UNION attack, determining the number of columns"**
2. Klik **Access the lab**
3. Klik salah satu kategori produk, perhatikan URL
4. Coba tentukan jumlah kolom dengan UNION:
 ```
?category=Gifts' UNION SELECT NULL--
?category=Gifts' UNION SELECT NULL,NULL--
?category=Gifts' UNION SELECT NULL,NULL,NULL--
 ```
5. Terus tambahkan NULL sampai halaman tidak error — itu jumlah kolomnya

> 💡 **Jika stuck**: Baca penjelasan di bagian atas halaman lab. PortSwigger menyediakan teori + petunjuk untuk setiap lab. Klik **"Solution"** hanya jika benar-benar stuck lebih dari 20 menit.

### Langkah 5: Dokumentasi Writeup
Untuk setiap lab yang diselesaikan, tulis writeup:
```
Lab: [nama lab]
Tipe SQLi: [UNION/Blind/Auth Bypass]
Payload yang digunakan: [payload]
Penjelasan: [mengapa payload ini bekerja]
```

---

## 🏁 Target Output

* ✅ Minimal **3 lab SQLi** berhasil diselesaikan (solved)
* 📝 **Writeup** untuk setiap lab: nama lab, payload, dan penjelasan
* 📸 Tangkapan layar PortSwigger menunjukkan lab status "Solved"

---

## 🔄 Fallback

Jika PortSwigger tidak bisa diakses:
1. Gunakan **DVWA (Damn Vulnerable Web Application)** — self-hosted:
 ```bash
 docker pull vulnerables/web-dvwa
 docker run -d -p 8080:80 vulnerables/web-dvwa
 ```
2. Buka `http://localhost:8080`, login dengan `admin` / `password`
3. Set security level ke **Low**
4. Kerjakan modul **SQL Injection** di DVWA
