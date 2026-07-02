# 📡 Week 9 · Day 1: Pengenalan Bash Scripting

> **Rank**: PACKET | **Minggu ke-9**, Hari 1/5 | **Durasi**: ~40 menit

📊 **Progress**: Week 9 · Day 1/5 | PACKET Rank (Minggu 5 dari 5) | Overall: 41/120 hari (34%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** konsep dasar otomatisasi tugas (*Scripting*)
2. **Membuat** file *script* Bash pertamamu menggunakan editor terminal (`nano` atau `vim`)
3. **Mendeklarasikan** *Shebang* (`#!/bin/bash`) dan variabel di dalam *script*
4. **Mengeksekusi** *script* buatan sendiri setelah memberikan izin eksekusi (`+x`)

---

## 📖 Materi Inti

### Hacker yang Baik adalah Hacker yang Malas

Seorang peretas atau *System Administrator* seringkali harus melakukan hal yang sama berulang-ulang. Misalnya: "Ping 100 komputer di jaringan kampus ini satu-satu untuk ngecek mana yang hidup."
Mengetik perintah `ping` 100 kali secara manual itu membuang waktu. 

Solusinya: **Bash Scripting**. 
Bash Scripting adalah seni menuliskan daftar perintah Terminal (seperti `ls`, `grep`, `ping`) ke dalam sebuah file teks, dan menyuruh Linux untuk menjalankan isi file tersebut baris demi baris secara otomatis dari atas ke bawah. Ini adalah cikal bakal *Programming/Coding* pertamamu!

### Anatomi Script Bash

Sebuah *script* (naskah) Bash punya aturan standar. Buka text editor di terminal (seperti `nano`) dan buat file bernama `hello.sh`. Extensi `.sh` adalah penanda bahwa ini file *shell script*.

Struktur wajib di baris paling pertama:
```bash
#!/bin/bash
```
Ini disebut **Shebang** (Kombinasi *Sharp* `#` dan *Bang* `!`). Baris ini memberi tahu OS Linux: *"Hai Linux, tolong jalankan teks di bawah ini menggunakan bahasa pemrograman Bash."*

### Mencetak Teks dan Variabel

Untuk menyuruh komputer berbicara (mencetak teks ke layar terminal), gunakan perintah `echo`.
```bash
#!/bin/bash

# Ini adalah komentar, tidak akan dieksekusi mesin
echo "Halo dunia! Saya sedang belajar hacking."
```

Kamu juga bisa menyimpan data (seperti nama, IP, atau umur) ke dalam kotak penyimpanan sementara yang disebut **Variabel**.
Aturan penting: **Jangan beri spasi saat mengisi variabel!**
- ❌ Salah: `nama = "Budi"`
- ✅ Benar: `nama="Budi"`

Untuk memanggil isi kotak variabel tersebut, tambahkan simbol Dolar `$` di depannya.
```bash
#!/bin/bash
target_ip="192.168.1.100"
echo "Menyerang target dengan IP: $target_ip"
```

### Mengubah Izin agar Bisa Dieksekusi (Penting!)

Kamu sudah membuat file `hello.sh` dan isinya sudah benar. Saat kamu mencoba menjalankannya dengan mengetik `./hello.sh`, terminal menolak:
`bash:./hello.sh: Permission denied`

Ingat pelajaran minggu lalu? File teks buatanmu awalnya hanya punya izin Read & Write (rw-). Ia **belum punya izin Execute (x)**.
Kamu harus mengubahnya dulu!
```bash
$ chmod +x hello.sh
```
*(Tanda `+x` adalah jalan pintas dari chmod angka, artinya "Tambahkan izin eksekusi untukku").*
Setelah itu, file-nya akan berwarna hijau di terminal, dan kamu bisa menjalankannya:
```bash
$./hello.sh
```

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Mari buat program "Pengenal Diri" pertamamu di terminal lokalmu (WSL/Mac/Linux)!

1. Buka Terminal. Ketik: `nano perkenalan.sh` (Ini akan membuka layar editor teks di dalam terminal).
2. Ketikkan kode ini persis seperti yang tertulis:
 ```bash
 #!/bin/bash
 
 nama="John Doe"
 os="Linux"
 
 echo "======================="
 echo "PROFIL KADER TISS"
 echo "======================="
 echo "Nama saya adalah $nama."
 echo "Saya sedang belajar $os."
 echo "User saya saat ini adalah: $USER"
 ```
 *(Note: `$USER` adalah variabel ajaib bawaan Linux yang otomatis tahu namamu tanpa perlu dideklarasikan!).*
3. Simpan dan Keluar: Tekan `CTRL + O`, lalu `Enter` (untuk save). Lalu tekan `CTRL + X` (untuk keluar).
4. Beri izin eksekusi: `chmod +x perkenalan.sh`
5. Jalankan: `./perkenalan.sh`

Keren, kan? Terminalmu baru saja berubah menjadi program kecil milikmu sendiri!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa fungsi dari baris "#!/bin/bash" di awal sebuah file script?</summary>

**Jawaban:** Baris tersebut disebut **Shebang**. Fungsinya adalah sebagai deklarasi untuk memberitahu sistem operasi (Linux) bahwa file ini harus dieksekusi menggunakan interpreter (penerjemah) `/bin/bash`.

</details>

<details>
<summary>❓ Mengapa kita tidak bisa memanggil variabel langsung dengan mengetik namanya? Misalnya: `echo nama` alih-alih `echo $nama`.</summary>

**Jawaban:** Karena tanpa simbol dolar `$`, bash akan menganggap kata "nama" sebagai teks biasa (*string* literal). Akibatnya, perintah `echo nama` hanya akan mencetak kata "nama" ke layar. Simbol `$` memberitahu bash untuk "membuka kotak variabel" dan mencetak ISINYA.

</details>

<details>
<summary>❓ Kenapa saat kita ingin menjalankan script, kita harus mengetik `./` (titik dan garis miring) sebelum nama filenya? (Contoh: `./hello.sh`)</summary>

**Jawaban:** Titik (`.`) berarti "direktori saat ini". Mengetik `./` berarti *"Tolong jalankan file hello.sh yang ada di dalam folder tempat saya berdiri saat ini"*. Jika kamu hanya mengetik `hello.sh` tanpa `./`, Linux akan kebingungan dan mencari nama perintah itu di folder sistem (seperti folder `/bin` tempat perintah `ls` atau `cd` berada), lalu melaporkan "Command not found".

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya paham apa fungsi Bash Scripting (Otomatisasi)
- [ ] Saya hafal sintaks Shebang
- [ ] Saya tahu cara mendeklarasikan dan memanggil variabel pakai `$`
- [ ] Saya mengerti kenapa saya harus melakukan `chmod +x`
- [ ] Saya tahu mengapa saya butuh awalan `./` untuk mengeksekusi script
- [ ] Saya berhasil membuat dan menjalankan script `perkenalan.sh`
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Bash Scripting Tutorial for Beginners (FreeCodeCamp)](https://www.freecodecamp.org/news/bash-scripting-tutorial-linux-shell-script-and-command-line-for-beginners/) — Panduan bacaan yang sangat ramah untuk pemula jika kamu buntu.

---

## ➡️ Besok

**Day 2: Logika & Kondisi** — Program di atas sangat lurus dan membosankan. Besok kita akan memberi "otak" pada *script*-mu agar ia bisa mengambil keputusan (Jika ini terjadi, lakukan A, jika tidak, lakukan B) menggunakan IF, ELSE, dan FOR LOOP!

---

*📅 TISS Null Teaming · Week 9 · Day 1 · PACKET Rank*
