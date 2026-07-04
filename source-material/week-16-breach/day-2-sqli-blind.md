# 💀 Week 16 · Day 2: SQL Injection Blind (Boolean & Time)

> **Rank**: BREACH | **Minggu ke-16**, Hari 2/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 16 · Day 2/5 | BREACH Rank (Minggu 2 dari 5) | Overall: 77/120 hari (64%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** karakteristik serangan *UNION-based SQLi* dengan *Blind SQLi*.
2. **Mengekstraksi** data *database* yang tidak menampilkan hasil *error* atau *query* ke layar menggunakan taktik *Boolean-based Blind*.
3. **Mengekstraksi** data menggunakan fungsi perlambatan waktu respons (*Time-based Blind SQLi*).

---

## 📖 Materi Inti

### Meretas Dalam Kegelapan (Blind SQLi)

Berbeda dengan serangan *UNION-based* yang memuntahkan seluruh data curian secara transparan ke layar web, peladen (*server*) yang dikonfigurasi dengan baik biasanya **TIDAK MENCETAK INDIKATOR APAPUN** (seperti *Syntax Error* atau hasil kueri) saat diserang.

Situs akan meredam pesan galat dan hanya memberikan respons normal (layar kosong, halaman *Not Found*, atau HTTP 200/500). Kondisi di mana penyerang berhasil menyuntikkan perintah SQL, namun hasilnya tidak ditampilkan ke layar web, disebut sebagai **Blind SQL Injection (Injeksi Buta)**.

Lalu, bagaimana cara mencuri data jika layarnya membisu?
Jawabannya: **Memaksa server untuk menjawab "Ya" atau "Tidak" melalui perubahan perilakunya.**

### 1. Boolean-based Blind (Evaluasi Sinyal Benar/Salah)

Alih-alih menyuruh *database* menampilkan seluruh isi tabel, *hacker* melemparkan tebakan logika untuk mengekstrak data **huruf demi huruf**.
Asumsikan ada URL yang rentan: `toko.com/produk?id=1`

Hacker menyisipkan perintah *Boolean* (Benar/Salah):
`toko.com/produk?id=1' AND (SELECT substring(password,1,1) FROM users WHERE username='admin') = 'a' --`

*(Artinya: Tampilkan produk ID 1 JIKA DAN HANYA JIKA huruf pertama dari password admin adalah 'a'.)*

- Jika halaman web **MUNCUL NORMAL**, berarti tebakan huruf 'a' itu **BENAR (TRUE)**.
- Jika halaman web tiba-tiba **HILANG/KOSONG/ERROR 404**, berarti tebakan itu **SALAH (FALSE)**.

Melalui jutaan tebakan (yang nantinya bisa diotomatisasi dengan *tools*), penyerang bisa merangkai seluruh *password* admin huruf demi huruf tanpa pernah melihat pesan *error* sedikit pun!

### 2. Time-based Blind (Sinyal Deteksi Jeda Waktu)

Terkadang, sebuah aplikasi web akan selalu merender halaman yang sama (*normal page rendering*) terlepas dari apakah kueri injeksi kita bernilai *TRUE* atau *FALSE*. Tidak ada perubahan layar (Boolean) yang bisa diamati.

Dalam situasi ini, *hacker* menggunakan taktik manipulasi durasi waktu: **Memaksa server untuk menunda atau "tertidur" (*SLEEP*) sebelum membalas respons halaman.**

Hacker meluncurkan serangan:
`id=1' AND IF((SELECT substring(password,1,1) FROM users)='a', SLEEP(10), 0) --`

*(Artinya: Apabila huruf pertama password admin adalah 'a', maka BERHENTILAH bekerja selama 10 DETIK. Jika salah, langsung proses secara normal.)*

Jika *browser* tiba-tiba mengalami *loading* yang sangat lama (tepat 10 detik atau lebih) sebelum menampilkan halaman, penyerang mendapatkan konfirmasi bahwa tebakannya (huruf 'a') adalah **BENAR**. Penyerang berhasil mencuri data hanya dengan mengamati seberapa lama napas server saat merespons permintaan!

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyimulasikan kekuatan serangan pembuktian *Blind SQLi* via modifikasi ekstensi *Cookie* di *browser*!

1. Kunjungi lab: [PortSwigger: Blind SQL Injection (Time Delays)](https://portswigger.net/web-security/sql-injection/blind).
2. Temukan skenario di mana fitur pencatatan pengunjung (melalui *Cookie* `TrackingId=xyz`) rentan terhadap injeksi SQL.
3. Kita akan menguji apakah parameter *Cookie* ini rentan terhadap *Time-based Blind SQLi*.
4. Gunakan ekstensi *browser* (atau *Burp Suite*) untuk mengubah nilai *Cookie* menjadi:
 `TrackingId=xyz' || pg_sleep(10)--`
 *(Catatan: `pg_sleep()` adalah fungsi jeda waktu khusus untuk database PostgreSQL).*
5. Segarkan (*Refresh*) halaman. Apakah halaman tersebut tiba-tiba mengalami *loading* lama (*macet*) yang presisi selama lebih dari 10 detik?
6. Jika ya, itu adalah bukti sah bahwa *server* memproses kueri SQL kamu dan sangat rentan terhadap serangan *Blind SQLi*!

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa perbedaan utama antara hasil serangan <i>UNION-based SQLi</i> dengan <i>Blind SQLi</i>?</summary>

**Jawaban:** Pada *UNION-based*, hasil curian data (*password*, *username*, dll) langsung dicetak dan terpampang di layar *browser*. Sementara pada *Blind SQLi*, *server* membisu dan tidak memunculkan *error* atau data di layar. Penyerang hanya bisa menebak dan mencuri data dengan memantau perubahan perilaku aplikasi web (apakah tampilannya berubah secara Boolean, atau waktu *loading*-nya melambat).
</details>

<details>
<summary>❓ Dalam taktik <i>Boolean-based Blind SQLi</i>, bagaimana penyerang mengetahui bahwa tebakan data mereka (misalnya tebakan abjad huruf sandi) adalah benar?</summary>

**Jawaban:** Penyerang mengajukan pertanyaan logika kueri *True/False* (misalnya: "Apakah huruf pertamanya A?"). Jika halaman web merender dengan tampilan utuh (normal), berarti kondisi logika di *database* terpenuhi (*TRUE*) dan tebakannya terkonfirmasi benar. Jika halamannya *error* atau kosong, tebakannya salah (*FALSE*).
</details>

<details>
<summary>❓ Perintah SQL jenis apa yang disuntikkan penyerang untuk melakukan konfirmasi dalam serangan <i>Time-based Blind SQLi</i>?</summary>

**Jawaban:** Perintah penundaan atau jeda waktu eksekusi (*SLEEP*, `pg_sleep()`, `WAITFOR DELAY`, dll). Jika kondisi tebakan benar, *database* akan disuruh "tidur" selama durasi tertentu, sehingga waktu *loading browser* pengunjung akan terasa sangat lambat (membuktikan bahwa kueri tersebut dieksekusi).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami mengapa *Blind SQLi* jauh lebih sunyi dibandingkan eksekusi *UNION*.
- [ ] Saya mengerti cara kerja logika *True/False* pada teknik *Boolean-based Blind*.
- [ ] Saya mengetahui fungsi instruksi jeda waktu (*SLEEP*) pada teknik *Time-based Blind*.
- [ ] Saya menyadari mengapa proses *Blind SQLi* bisa memakan waktu jutaan iterasi tebakan secara manual (satu huruf per tebakan).
- [ ] Saya telah menuntaskan validasi materi dan kuis hari ini.

---

## 🔗 Resources

- [PortSwigger Blind SQLi](https://portswigger.net/web-security/sql-injection/blind) — Panduan referensi dan praktik komprehensif untuk eksploitasi sistem *Blind SQL Injection*.

---

## ➡️ Besok

**Day 3: SQLMap (Automated Exploitation)** — Melakukan *Blind SQLi* secara manual (menebak indeks huruf demi huruf, dari 'a' sampai 'z', untuk setiap baris *database*) adalah pekerjaan yang bisa memakan waktu harian, bahkan mingguan! Di industri nyata, waktu sangat berharga. Besok, kamu akan diperkenalkan pada senjata andalan para *Pentester* profesional: **SQLMap**. Kita akan mengotomatisasi seluruh proses eksploitasi SQLi yang melelahkan ini menjadi operasi yang berjalan dalam hitungan menit!

---

*📅 TISS Null Teaming · Week 16 · Day 2 · BREACH Rank*
