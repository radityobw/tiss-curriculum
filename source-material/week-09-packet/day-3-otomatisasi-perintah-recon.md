# 📡 Week 9 · Day 3: Otomatisasi Perintah (Recon Script)

> **Rank**: PACKET | **Minggu ke-9**, Hari 3/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 9 · Day 3/5 | PACKET Rank (Minggu 5 dari 5) | Overall: 43/120 hari (35%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Menggabungkan** perintah terminal asli (`ping`, `host`, `curl`) ke dalam *script* Bash
2. **Memanfaatkan** fitur *Command Substitution* `$()` untuk menyimpan hasil terminal ke dalam variabel
3. **Membangun** sebuah *script reconnaissance* (pengintaian jaringan) dasar 

---

## 📖 Materi Inti

### Kekuatan Super Bash: Mengendalikan Terminal

Tujuan utama kita belajar *Bash Scripting* bukanlah untuk membuat program berhitung matematika. Tujuannya adalah untuk mengendalikan alat-alat Linux! 

Semua perintah (command) yang pernah kita pelajari di terminal (seperti `ls`, `ping`, `grep`, `mkdir`) bisa kamu tulis langsung di dalam file `.sh` layaknya kamu mengetiknya di terminal.

### Command Substitution `$()`

Ini adalah sihir Bash. Bagaimana jika kamu menjalankan `ping`, lalu hasilnya tidak dicetak ke layar, melainkan ditangkap dan dimasukkan ke dalam variabel? 

Gunakan format **Dolar dan Tanda Kurung**: `$(perintah)`

**Contoh Kasus:**
Kamu ingin membuat variabel bernama "waktu" yang isinya adalah waktu server saat ini. (Perintah terminal untuk ngecek waktu adalah `date`).

```bash
#!/bin/bash
waktu=$(date)
echo "Waktu peretasan dimulai pada: $waktu"
```
*(Saat script dijalankan, Bash akan memproses `date` dulu secara rahasia, lalu mengisi hasilnya ke dalam variabel waktu).*

### Membuat Script "Recon" Pertamamu

*Reconnaissance (Recon)* atau Pengintaian adalah fase pertama saat seorang *hacker* menargetkan sebuah perusahaan. Ia harus mencari tahu IP address mereka, lokasi server mereka, dan teknologi yang mereka pakai.

Kita akan menggunakan 2 alat dasar yang otomatis terpasang di Linux/Mac:
1. `ping` (Sudah kita pelajari: mengecek server hidup/mati).
2. `host` (Fungsinya persis seperti DNS: Menerjemahkan nama web menjadi alamat IP).

Mari kita rancang sebuah alat pencari IP (*IP Finder Script*) sederhana.
Jika kita mengetik perintah manual:
```bash
$ host google.com
# Hasilnya: google.com has address 142.250.191.46
```
Hasil itu terlalu panjang. Kita akan memotong/menyaring teksnya menggunakan alat pipa `|` dan `awk` (kombinasi `grep`).

---

## 🧪 Mini Lab

**Durasi**: ~20 menit

Waktunya coding! Buat file bernama `recon.sh` (`nano recon.sh`).
Tulis script interaktif di bawah ini:

```bash
#!/bin/bash

# 1. Bersihkan layar terminal dulu agar rapi
clear 
echo "=============================="
echo "💀 TISS AUTO RECON TOOL 💀"
echo "=============================="

# 2. Minta input nama website dari user
read -p "Masukkan URL Target (contoh: untirta.ac.id): " target

echo "Memulai pengintaian pada $target..."
echo "------------------------------"

# 3. Jalankan perintah 'host', tangkap hasil IP-nya saja (kolom ke-4), dan simpan di variabel!
# (Jangan panik melihat awk, ini hanya alat pemotong teks bawaan Linux)
ip_address=$(host $target | awk '{print $4}' | head -n 1)

# 4. Tampilkan hasilnya!
echo "[*] Target IP Ditemukan: $ip_address"

# 5. Uji apakah IP tersebut hidup dengan ping 1 kali (-c 1)
echo "[*] Mengirim paket mematikan..."
ping -c 1 $ip_address

echo "------------------------------"
echo "Recon selesai!"
```

**Cara Menjalankan:**
1. Save dan tutup nano (`CTRL+O`, Enter, `CTRL+X`).
2. Beri izin eksekusi: `chmod +x recon.sh`
3. Jalankan: `./recon.sh`
4. Saat ditanya target, masukkan website kampusmu, atau website favoritmu!

> **Keren kan?** Hanya dengan memasukkan nama web, scriptmu secara otomatis (di belakang layar) menembak server DNS, mengambil IP-nya, dan melakukan tes uji hidup (ping) dalam hitungan detik. 
> *Inilah cara kerja tools hacking sungguhan di dunia nyata!* Mereka hanyalah gabungan skrip bash.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa kita sangat membutuhkan format `$(...)` (Command Substitution) dalam Bash Scripting tingkat lanjut?</summary>

**Jawaban:** Karena jika kita mengetik perintah terminal secara langsung (seperti `date` atau `ping`), hasilnya akan langsung tercetak hancur ke layar (Output Stream). Dengan `$(...)`, kita mencegat hasil perintah tersebut secara diam-diam dan menyimpannya ke dalam **Variabel**. Dengan begitu, kita bisa mengolah, memotong, atau menggunakan nilai tersebut berulang kali tanpa membuat layar terminal kotor.

</details>

<details>
<summary>❓ Dalam script recon di atas, kita menggunakan opsi `-c 1` pada perintah ping. Apa gunanya?</summary>

**Jawaban:** `-c 1` (Count 1) berarti perintah PING hanya akan mengirim 1 paket "Halo" ke server target dan langsung berhenti. Di sistem Linux, jika kamu tidak menggunakan opsi ini, perintah `ping` akan berjalan terus selamanya sampai kamu menekan tombol `CTRL + C` secara manual. (Script akan macet!).

</details>

<details>
<summary>❓ Apa yang akan terjadi jika kamu mencoba menjalankan script `./recon.sh` tetapi komputermu tidak terkoneksi ke internet sama sekali?</summary>

**Jawaban:** Script akan menampilkan error saat mencoba menjalankan proses substitusi `host`. Perintah `host` akan gagal menerjemahkan nama website (karena tidak bisa menjangkau DNS server di internet), sehingga variabel `ip_address` akan bernilai kosong. Ketika lanjut ke baris berikutnya, perintah `ping` juga akan gagal karena IP-nya tidak ada/kosong.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya paham cara memanggil *command terminal asli* di dalam *script Bash*
- [ ] Saya memahami apa fungsi substitusi `$()` (untuk menculik *output* terminal ke variabel)
- [ ] Saya berhasil mengetik ulang dan menjalankan script `recon.sh`
- [ ] Saya bisa menjelaskan alur logika dari script recon di atas
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Bash Command Substitution (Linuxize)](https://linuxize.com/post/bash-command-substitution/) — Penjelasan lebih teknis tentang bedanya `$(...)` dan penggunaan *Backticks*.

---

## ➡️ Besok

**Day 4: Cron Jobs (Penjadwalan)** — Kamu berhasil membuat *script* otomatis. Tapi kamu masih harus menekan tombol Enter secara manual. Besok, kita akan menyuruh mesin waktu Linux (Cron) agar menjalankan scriptmu sendiri setiap jam 3 subuh tanpa kamu sentuh sama sekali!

---

*📅 TISS Null Teaming · Week 9 · Day 3 · PACKET Rank*
