# 💀 Week 18 · Day 1: Burp Suite Proxy & Intercept

> **Rank**: BREACH | **Minggu ke-18**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 18 · Day 1/5 | BREACH Rank (Minggu 4 dari 5) | Overall: 86/120 hari (71%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Memahami** nalar filosofis arsitektur di balik pengerahan peranti pencegat lalu lintas Web (*Proxy*).
2. **Mengonfigurasi** infrastruktur *Burp Suite* agar merajut silang koneksi *Browser*.
3. **Mencegat** lantas memanipulasi payload paket (*Intercept & Modify Requests*).

---

## 📖 Materi Inti

### Mengenal : Burp Suite

Selama 3 minggu, Anda arsitektur peretasan dengan mengandalkan terminal *Nmap*, *SQLMap*, dan mengekskavasi manual *Source Code* HTML di peramban. Mulai hari ini, tinggalkan cara manual usang tersebut!

Sambutlah **Burp Suite** (Racikan *PortSwigger*). Ini adalah nomor satu di industri keamanan siber dunia untuk pengujian peretasan web. Tanpanya, seorang spesialis pemburu kerentanan (*Bug Hunter*) sama saja terjun ke medan pengujian cuma bersenjata arsitektur yang amat terbatas.

### Jantung Arsitektur Burp Suite: Proxy

*Browser* (Chrome/Firefox) normalnya mentransmisikan permintaan (*Request*) secara langsung ke peladen Server, lalu server merespons dengan membalas (*Response*). Semuanya berlalu begitu cepat.
**Burp Suite Proxy** secara merubah takdir itu. 

*Burp* memposisikan dirinya laksana penengah (*Man-in-the-Middle*) tepat di tengah-tengah jalan tol rute komunikasi antara perangkat Komputer-mu dan Server sasaran.
1. Browser klien mengirim kueri `Request`.
2. Payload `Request` itu **dicegat dan ditahan (*Intercept*)** oleh fitur *Burp*. (Browser klien akan terus *loading* memutar terus-menerus tanpa respons!).
3. Di dalam antarmuka *Burp*, Anda bebas perintah untuk **membongkar, mengedit, dan memanipulasi** isi paket `Request` itu sebelum dikirim!
4. Setelah penganalisis puas memanipulasi, penganalisis klik tombol **Forward** untuk meneruskannya mendarat ke Server.

### Manipulasi Parameter Karena Anda bisa menahan lantas mengedit payload *Request* tepat di tengah jalan komunikasi, tameng pelindung *Frontend* (validasi Javascript, pembatasan atribut `maxlength` di dokumen HTML) menjadi sama sekali **TIDAK BERGUNA** murni.

Contoh :
Programmer merancang form *Transfer Uang* dengan menu *dropdown* di HTML yang membatasi pengguna cuma bisa transfer mentok 1 Juta. Hacker secara antarmuka menyetujui di web, tapi saat pesan itu melintas ditransmisikan lantas dicegat di *Burp Suite*, Penganalisis Hacker menghapus nilai 1 Juta lantas arsitektur merubah bodinya jadi 1 Miliar, lalu menekan tombol **Forward**. Server lantas menerima kueri 1 Miliar dan mengamininya karena Server naif mempercayai inputan tanpa validasi ulang!

---

## 🧪 Mini Lab

**Durasi**: ~15 menit

Ayo menyimulasikan pemasangan pencegat *Burp Proxy*!

1. Buka **Burp Suite Community Edition** (Biasanya bawaan instalasi Kali Linux).
2. Klik tab **Proxy** > lantas pastikan tombol **Intercept is on** berstatus menyala.
3. Buka peramban *Browser* bawaan Burp dengan mengeklik tombol **Open Browser** di tab Proxy.
4. Kunjungi pelataran web pengujian, semisal web kampusmu atau `tokopedia.com`.
5. Saat Anda mengetik alamat URL lantas menekan enter, halamannya akan melambat macet (*loading*) tak kunjung tampil!
6. Buka kembali jendela *Burp Suite-mu*. *Bingo!* Serpihan payload *Request HTTP* orisinal bertumpuk di layarmu.
7. Coba temukan baris bodi *Header* `User-Agent: Mozilla/5.0...`. Hapus tu sandi *Mozilla* lantas ganti paksa modifikasinya jadi `User-Agent: Mesin-Peretas-Dewa`.
8. Klik tombol kuning **Forward**! Kamu baru saja berhasil menipu peladen server dengan identitas peramban (*User-Agent*) fiktif racikanmu sendiri!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membedah arsitektur peretasan <i>Man-in-the-Middle</i> Web, apa tugas pokok fitur <i>Proxy</i> pada bodi <i>Burp Suite</i>?</summary>

**Jawaban:** Memposisikan arsitektur dirinya laksana perantara di tengah arus lalu lintas komunikasi, bertugas mencegat (*Intercept*), menahan paket, lantas peretas guna membedah dan memanipulasi payload paket <i>Request/Response</i> HTTP sebelum itu diteruskan mendarat ke peladen Server target.
</details>

<details>
<summary>❓ Ketika meluncurkan serangan eksploitasi pencegatan (Intercept), mengapa seluruh validasi pembatasan pengamanan di layar HTML Frontend (seperti embel atribut `maxlength="10"` atau menu *dropdown* mati) dinilai mustahil menangkis serangan ?</summary>

**Jawaban:** Lantaran peretas mengutak-atik lantas memanipulasi nilai variabel *Request* di dalam rahim antarmuka *Burp Suite* pasca paket itu meronta meninggalkan peramban Browser. Artinya, tameng validasi Javascript/HTML yang cuma bekerja di peramban itu sukses ditelikung dilewati mentah-mentah di tengah jalan tol komunikasi.
</details>

<details>
<summary>❓ Ketika penganalisis menenggak ekstraksi <i>Burp Suite Proxy</i> lantas memanipulasi payload yang dicegat, tombol apakah (berawalan abjad F) yang mesti ditekan agar payload yang tertahan itu dikirimkan lepas meluncur ke alamat Server sebenarnya?</summary>

**Jawaban:** Tombol Forward.
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya menyerap dominasi letak arsitektur penahan *Proxy*
- [ ] Saya fasih membuka peramban intaian via *Open Browser Burp*
- [ ] Saya menguasai titah manipulasi bodi tameng pencegat *Intercept*
- [ ] Saya sukses mengubah arsitektur sandi *User-Agent* di Mini Lab - [ ] Saya telah menjawab seluruh ulasan *quiz kilat*

---

## 🔗 Resources

- [PortSwigger Burp Proxy Docs](https://portswigger.net/burp/documentation/desktop/tools/proxy) — Kitab referensi suci pusaka seluruh rentetan arsitektur sandi pencegat web dunia.

---

## ➡️ Besok

**Day 2: Burp Suite Repeater & Intruder** — Mencegat satu payload paket lalu memencet tombol *Forward* itu lumayan melelahkan secara bila kamu harus mencoba 100 injeksi arsitektur SQLi manual! Esok hari, Web menuntut penganalisis merengkuh dua pemicu ajaib *Burp*: **Repeater** (untuk mengirim serangan eksploitasi manual berulang-ulang tanpa perlu menekan tombol *Browser*) dan **Intruder** (Mesin senapan otomatis penembak tebakan ribuan payload eksploitasi *Brute Force*)!

---

*📅 TISS Null Teaming · Week 18 · Day 1 · BREACH Rank*
