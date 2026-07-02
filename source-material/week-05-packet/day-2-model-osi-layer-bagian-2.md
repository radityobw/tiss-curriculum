# 📡 Week 5 · Day 2: Model OSI Layer (Bagian 2)

> **Rank**: PACKET | **Minggu ke-5**, Hari 2/5 | **Durasi**: ~35 menit

📊 **Progress**: Week 5 · Day 2/5 | PACKET Rank (Minggu 1 dari 5) | Overall: 22/120 hari (18%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** fungsi dari Layer 5 hingga Layer 7 (Upper Layers)
2. **Menggabungkan** pemahaman dari Layer 1 hingga 7 menjadi sebuah alur proses (Encapsulation)
3. **Menggunakan** analogi pengiriman paket untuk menjelaskan keseluruhan model OSI

---

## 📖 Materi Inti

### Upper Layers (Layer 5 - 7)

Kemarin kita sudah mengurus urusan pengiriman fisik. Hari ini kita fokus pada lapisan yang berinteraksi langsung dengan sistem operasi dan aplikasi di komputermu.

```
7️⃣ APPLICATION LAYER (Data) ← Kamu berinteraksi di sini
6️⃣ PRESENTATION LAYER (Data)
5️⃣ SESSION LAYER (Data)

[Layer Bawah: Fokus Pengiriman - Sudah dibahas kemarin]
```

#### Layer 5: Session Layer (Sesi)
- **Tugas:** Membuka, menjaga, dan menutup "percakapan" atau sesi koneksi antar aplikasi.
- **Analogi:** Seperti menelepon seseorang (bilang "Halo" di awal, ngobrol, lalu bilang "Sampai jumpa" saat ditutup). Jika tiba-tiba koneksi terputus, layer ini yang mencoba menyambung ulang tanpa harus mulai dari awal.
- **Contoh:** NetBIOS, RPC.

#### Layer 6: Presentation Layer (Presentasi)
- **Tugas:** Penerjemah data. Dia memastikan data dari komputer pengirim bisa dibaca oleh komputer penerima. Di sinilah terjadi proses Kompresi (*Compression*) dan Enkripsi/Dekripsi (*Encryption*).
- **Analogi:** Jika kamu mengirim teks dalam huruf Jepang, layer ini yang menerjemahkan agar bisa ditampilkan dengan baik, lalu menyandikannya (*enkripsi*) agar tidak dibaca penyadap di jalan.
- **Contoh:** SSL/TLS, JPEG, ASCII, MP3.

#### Layer 7: Application Layer (Aplikasi)
- **Tugas:** Ini adalah jembatan langsung antara jaringan dan *software* aplikasimu. Ini BUKAN aplikasinya (bukan Chrome atau WhatsApp-nya), melainkan *protokol* di balik aplikasi tersebut yang meminta data.
- **Analogi:** Resepsionis yang menerima pesananmu dan mengirimkannya ke kurir.
- **Contoh:** HTTP (untuk web), SMTP (untuk email), FTP (untuk transfer file).

### Gambar Utuh: Bagaimana Data Bergerak? (Encapsulation)

Ketika kamu mengirim pesan WhatsApp:
1. Pesanmu masuk ke **Layer 7** (diubah jadi data).
2. Turun ke **Layer 6** (dienkripsi agar rahasia).
3. Turun ke **Layer 5** (sesi dengan server WA dibuka).
4. Turun ke **Layer 4** (data dipecah-pecah jadi segment, diberi Port).
5. Turun ke **Layer 3** (ditempeli alamat IP tujuan).
6. Turun ke **Layer 2** (ditempeli MAC address router WiFi-mu).
7. Turun ke **Layer 1** (diubah jadi sinyal gelombang radio WiFi).

Proses membungkus data dengan label tambahan setiap turun layer disebut **Encapsulation**. Di komputer tujuan, prosesnya dibalik (*Decapsulation*), naik dari Layer 1 sampai ke Layer 7 untuk dibaca penerima.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari buat "Cheat Sheet" atau jembatan keledai (*Mnemonic*) untuk menghafal 7 layer OSI dari bawah (Layer 1) ke atas (Layer 7).

Susunannya:
**P**hysical → **D**ata Link → **N**etwork → **T**ransport → **S**ession → **P**resentation → **A**pplication.

(P-D-N-T-S-P-A)

**Tugas:** Buat singkatan lucu versimu sendiri dalam bahasa Indonesia.
Contoh:
- **P**ak **D**ono **N**onton **T**V **S**ambil **P**akan **A**yam.
- **P**lis **D**ong **N**ext **T**ime **S**emua **P**erhatiin **A**ku.

Tulis singkatanmu di catatan pribadi. Jika kamu bisa menghafal 7 layer ini berurutan, kamu sudah selangkah lebih maju dari mayoritas mahasiswa IT!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Saat kamu membuka website bank (HTTPS), terjadi proses enkripsi agar passwordmu tidak bisa disadap. Proses enkripsi ini terjadi di layer berapa?</summary>

**Jawaban:** **Layer 6 (Presentation Layer)**.

</details>

<details>
<summary>❓ Apakah Layer 7 (Application Layer) merujuk pada aplikasi seperti Google Chrome atau Microsoft Word?</summary>

**Jawaban:** **Tidak**. Layer 7 BUKAN aplikasi itu sendiri, melainkan **protokol jaringan** yang digunakan oleh aplikasi tersebut. Chrome menggunakan protokol HTTP/HTTPS yang berada di Layer 7. Microsoft Word tidak berada di layer mana pun kecuali ia mencoba menyimpan dokumen secara *online*.

</details>

<details>
<summary>❓ Apa itu proses Encapsulation?</summary>

**Jawaban:** Encapsulation adalah proses pembungkusan data saat ia bergerak **turun** dari Layer 7 ke Layer 1 pada komputer pengirim. Setiap layer akan menambahkan informasi pengontrolnya sendiri (seperti menempelkan prangko atau stiker alamat) ke dalam data tersebut sebelum dikirimkan.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya hafal fungsi Layer 5 (Session)
- [ ] Saya hafal fungsi Layer 6 (Presentation)
- [ ] Saya hafal fungsi Layer 7 (Application)
- [ ] Saya bisa menyebutkan 7 Layer OSI secara berurutan
- [ ] Saya memahami konsep *Encapsulation* saat pengiriman data
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [The OSI Model Demystified](https://www.youtube.com/watch?v=HEEnLZV2wGI) — Video animasi yang menunjukkan proses enkapsulasi paket data.

---

## ➡️ Besok

**Day 3: Model TCP/IP & Perbandingan** — OSI Model memang bagus untuk belajar, tapi tahukah kamu internet modern tidak benar-benar menggunakannya? Besok kita pelajari "saingan"-nya yang jauh lebih ringkas dan sebenarnya dipakai oleh seluruh perangkat di bumi: Model TCP/IP.

---

*📅 TISS Null Teaming · Week 5 · Day 2 · PACKET Rank*
