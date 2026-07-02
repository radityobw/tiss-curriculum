# 📡 Week 9 · Day 2: Logika & Kondisi

> **Rank**: PACKET | **Minggu ke-9**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 9 · Day 2/5 | PACKET Rank (Minggu 5 dari 5) | Overall: 42/120 hari (35%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep percabangan (If-Else) dalam pemrograman Bash
2. **Menerima** masukan (input) dari pengguna secara interaktif menggunakan `read`
3. **Menggunakan** perulangan (*For Loops*) untuk melakukan pekerjaan yang sama berkali-kali secara otomatis

---

## 📖 Materi Inti

### Membuat Program Jadi Pintar (If/Else)

Kemarin program kita hanya membaca dari atas ke bawah. Dalam dunia nyata, *hacker* membuat program yang bisa "mengambil keputusan". 
Misal: *JIKA server merespons PING, maka lapor sukses. JIKA TIDAK, lapor server mati.*

Struktur logika If-Else di Bash sedikit unik karena kurung sikunya butuh spasi!
```bash
#!/bin/bash
umur=20

# Perhatikan SPASI setelah tanda [ dan sebelum tanda ]!
if [ $umur -ge 18 ]; then
 echo "Kamu boleh mengakses server ini."
else
 echo "Akses ditolak! Kamu masih di bawah umur."
fi
```
*(Catatan: `fi` adalah kebalikan dari kata `if`, menandakan blok logika selesai).*

**Operator Matematika Bash (Aneh tapi nyata!):**
Karena tanda `>`, `<`, dan `=` sudah dipakai Linux untuk fungsi manipulasi file, Bash menggunakan singkatan huruf Inggris:
- `-eq` : Sama dengan (*Equal*)
- `-ne` : Tidak sama dengan (*Not Equal*)
- `-gt` : Lebih besar dari (*Greater Than*)
- `-lt` : Lebih kecil dari (*Less Than*)
- `-ge` : Lebih besar atau sama dengan (*Greater or Equal*)

### Meminta Input dari User (`read`)

Agar programmu interaktif (bisa ngobrol), kita butuh perintah `read`. Perintah ini menyuruh terminal berhenti sejenak, menunggu *user* mengetik sesuatu, lalu menyimpan ketikan itu ke dalam variabel.

Sintaksnya sangat gampang: `read -p "Kalimat Pertanyaan " nama_variabel`

Contoh:
```bash
#!/bin/bash
read -p "Masukkan IP Target: " target
echo "Target yang Anda pilih adalah: $target"
```

### Melakukan Perulangan (For Loops)

Ini adalah inti dari *otomatisasi*. Daripada menulis baris `ping` 10 kali untuk 10 IP yang berbeda, kamu bisa menyuruh Bash mengulanginya dengan **For Loop**.

Cara bacanya: *"Untuk setiap [item] di dalam [daftar item], kerjakan [tugas ini], lalu selesai."*

```bash
#!/bin/bash
# Daftar nama dipisahkan dengan spasi
for nama in Budi Alice Charlie
do
 echo "Hacking komputer milik $nama..."
done
```
Output-nya otomatis:
*Hacking komputer milik Budi...*
*Hacking komputer milik Alice...*
*Hacking komputer milik Charlie...*

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari buat aplikasi "Tebak Umur Hacker" (Buka Terminal, ketik `nano tebak.sh`).

**Tugas:**
Tulis *script* interaktif yang:
1. Bertanya siapa namamu.
2. Bertanya berapa umurmu.
3. Menggunakan If-Else:
 - Jika umur lebih dari atau sama dengan (`-ge`) 18, cetak "Kamu sudah legal main Hacking!".
 - Jika tidak (kurang dari 18), cetak "Awas, jangan sampai masuk penjara !".

<details>
<summary>🔑 Kunci Kode Mini Lab</summary>

```bash
#!/bin/bash

read -p "Siapa nama kamu? " nama
read -p "Berapa umur kamu? " umur

echo "Halo $nama!"

if [ $umur -ge 18 ]; then
 echo "Kamu sudah legal main Hacking!"
else
 echo "Awas, jangan sampai masuk penjara !"
fi
```
*Jangan lupa save, `chmod +x tebak.sh`, lalu jalankan `./tebak.sh`!*

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa yang terjadi jika kamu mengetik `if [$umur -ge 18]` tanpa menambahkan SPASI di dalam kurung siku tersebut?</summary>

**Jawaban:** Akan terjadi **Error syntax**. Di dalam Bash, kurung siku pembuka `[` sebenarnya adalah sebuah program tersendiri yang dipanggil oleh sistem. Jika ia disambung langsung dengan variabel, sistem tidak akan mengenali perintahnya. Selalu berikan spasi seperti ini: `[ $umur -ge 18 ]`.

</details>

<details>
<summary>❓ Bagaimana cara kamu menerjemahkan kalimat logika matematika ini ke dalam operator Bash: "Jika nilai A lebih kecil dari 10"?</summary>

**Jawaban:** `if [ $A -lt 10 ]; then`
(Menggunakan `-lt` yang merupakan singkatan dari *Less Than*).

</details>

<details>
<summary>❓ Pada struktur perulangan 'For Loop', kata kunci apa yang digunakan untuk memulai blok tindakan (action) dan menutup blok tindakan?</summary>

**Jawaban:** Dimulai dengan kata **`do`** (lakukan tindakan berikut) dan diakhiri dengan kata **`done`** (perulangan selesai/tutup blok).

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya hafal operator perbandingan Bash (-eq, -ne, -gt, -lt, -ge)
- [ ] Saya ingat bahwa `[ ]` (If statement) di Bash HARUS ada spasinya
- [ ] Saya bisa menggunakan `read -p` untuk membuat script interaktif
- [ ] Saya memahami logika `for... do... done` (For Loops)
- [ ] Saya berhasil membuat dan menjalankan script `tebak.sh`
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Bash If..Else Statements (Linuxize)](https://linuxize.com/post/bash-if-else-statement/) — Daftar lengkap operator logika Bash (Termasuk operator untuk menebak apakah sebuah file itu ada atau tidak di harddisk!).

---

## ➡️ Besok

**Day 3: Otomatisasi Perintah** — Hari ini kamu belajar bahasanya (variabel, if, loop). Besok kita akan menggabungkannya dengan alat jaringan! Kamu akan membuat *script* peretasan (*recon*) pertamamu yang bisa melacak informasi domain secara otomatis.

---

*📅 TISS Null Teaming · Week 9 · Day 2 · PACKET Rank*
