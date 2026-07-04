# 📡 Week 8 · Day 1: User & Group Management

> **Rank**: PACKET | **Minggu ke-8**, Hari 1/5 | **Durasi**: ~35 menit

📊 **Progress**: Week 8 · Day 1/5 | PACKET Rank (Minggu 4 dari 5) | Overall: 36/120 hari (30%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** arsitektur keamanan multi-pengguna (Multi-User) pada Linux
2. **Mengecek** identitas akun yang sedang kamu gunakan (`whoami`, `id`)
3. **Menjelaskan** konsep "Root" (Superuser) dan mengapa ia sangat berbahaya
4. **Berpindah** antar akun (*Switch User*) menggunakan perintah `su`

---

## 📖 Materi Inti

### Linux: Dibangun untuk Banyak Orang Sejak Hari Pertama

Tidak seperti Windows lama yang awalnya didesain untuk dipakai satu orang (*Personal Computer*), Linux diciptakan untuk menjadi sistem server (*Multi-User*). 

Artinya, dalam 1 detik yang sama, bisa ada 100 orang berbeda dari seluruh dunia yang *login* ke satu server Linux yang sama! Agar ke-100 orang ini tidak saling bertengkar (misal: Budi menghapus file tugas milik Andi), Linux membutuhkan sistem pengaturan keamanan **User (Pengguna)** dan **Group (Kelompok)** yang sangat ketat.

### Perintah Identifikasi Diri

Saat kamu berhasil menyusup (meretas) masuk ke sebuah server, hal PERTAMA yang harus kamu ketahui adalah *"Siapa aku di server ini?"*

1. **`whoami`**
 - Perintah super simpel untuk mencetak namamu saat ini.
 - Contoh output: `ryo` atau `www-data` (user mesin).
2. **`id`**
 - Versi lebih detail dari `whoami`. Ia akan menampilkan **UID (User ID)** dan **GID (Group ID)**.
 - Contoh output: `uid=1000(ryo) gid=1000(ryo) groups=1000(ryo),27(sudo)`
 - *Fakta: User biasa pertama yang dibuat saat kamu instal Linux selalu diberi UID 1000.*

### Siapa itu Root? 👑

Di Linux, ada satu akun yang memiliki kekuasaan di atas segalanya. Akun ini bernama **Root** (disebut juga Superuser).
- UID milik Root selalu **0**.
- Root bisa membaca rahasia siapa saja, menghapus apa saja (termasuk menghapus OS itu sendiri), dan menjalankan program apapun tanpa bisa dicegah.
- Tujuan akhir setiap peretas (*Hacker*) adalah mendapatkan akses ke akun Root ini. Proses mendaki dari user biasa menjadi Root disebut **Privilege Escalation** (Eskalasi Hak Istimewa).

Tanda termudah membedakan apakah kamu Root atau manusia biasa di Terminal adalah dengan melihat **karakter terakhir di ujung baris perintahmu (Prompt):**
- Simbol Dolar **`$`** = Kamu adalah *User Biasa*.
- Simbol Pagar **`#`** = Kamu adalah *Root* (Hati-hati mengetik!).

### Berpindah Akun (`su`)

Jika kamu memiliki password orang lain (atau password Root), kamu bisa merasuki akun mereka tanpa perlu *logout/restart* komputer.
Gunakan perintah **`su`** (Switch User / Substitute User).

- `su budi` -> Pindah menjadi user Budi (akan diminta password budi).
- `su -` -> Pindah menjadi Root (Sangat kuat! Membutuhkan password milik root).

Untuk kembali ke wujud aslimu, cukup ketik `exit`.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Buka Terminal/WSL di komputermu dan lakukan penyelidikan identitas ini:

1. Ketik: `whoami`
 (Catat hasilnya).
2. Ketik: `id`
 (Apakah UID kamu bernilai 1000? Kamu masuk ke dalam *Group* apa saja?).
3. Coba ketik: `su root` atau `su -`
 (Terminal akan meminta password. Jika kamu di WSL, kamu mungkin tidak tahu password root-nya dan akan mendapat peringatan *Authentication failure*. Ini membuktikan bahwa pintu menuju kekuasaan absolut itu terkunci rapat!).

---

## 💡 Quiz Kilat

<details>
<summary>❓ Jika kamu mengetik `whoami` dan terminal menjawab "root", karakter apa yang seharusnya muncul di ujung baris perintah/prompt-mu?</summary>

**Jawaban:** Simbol Pagar (**`#`**).

</details>

<details>
<summary>❓ UID berapakah yang selalu dialokasikan secara permanen untuk akun Superuser (Root)?</summary>

**Jawaban:** UID **0**. (Meskipun kamu berhasil membuat akun baru bernama "admin_baru", selama UID-nya bukan 0, ia bukanlah Superuser sejati).

</details>

<details>
<summary>❓ Apa yang terjadi jika kamu mengetik perintah "su alice" tapi kamu tidak memasukkan kata sandi (password)?</summary>

**Jawaban:** Proses *Switch User* akan gagal (*Authentication failure*) dan kamu akan tetap berada di akun aslimu. Kamu tidak bisa menjadi "alice" tanpa mengetahui password-nya.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami Linux adalah OS Multi-User
- [ ] Saya bisa mengecek identitas saya dengan `whoami` dan `id`
- [ ] Saya tahu bahwa Root adalah Tuhan di Linux (UID 0)
- [ ] Saya paham bedanya *prompt* `$` (User) dan `#` (Root)
- [ ] Saya tahu fungsi dari `su` (Switch User)
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [Linux Users and Groups (Linux Journey)](https://linuxjourney.com/lesson/users-and-groups) — Penjelasan detail mengenai konsep UID dan GID di Linux.

---

## ➡️ Besok

**Day 2: File Permissions (rwx)** — Jika Budi dan Alice punya file di komputer yang sama, bagaimana cara Linux mencegah Budi membaca tugas skripsi milik Alice? Besok kita akan memecahkan sandi rahasia: `rwxr-xr--`!

---

*📅 TISS Null Teaming · Week 8 · Day 1 · PACKET Rank*
