---
type: quiz
week: 14
day: 5
title: "Quiz: Lab Securing the API"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Di simulasi peladen API, serangkaian rantai pertahanan *Backend* telah digabung paripurna. Dari daftar perlindungan mutakhir berikut ini, kombinasi padanan manakah yang secara akurat merangkul fungsi pertahanan sesuai peruntukan sasar penangkal kerentanannya?
- [x] A. Kueri Berparameter `?` diklaim menjegal serangan *SQL Injection*; Jaring *Middleware Helmet.js* mengkarantina bahaya eksploitasi paparan *Header HTTP Misconfiguration*; Konfigurasi jaring batas cegat *Rate Limit* merepresi serangan percobaan volume *DDoS* maupun tebakan masif *Brute-Force*.
- [ ] B. *Helmet.js* merombak kerentanan otorisasi *IDOR*, selagi pemanfaatan kueri `?` difungsikan khusus menangkis serangan peretasan pop-up *XSS*.
- [ ] C. *Rate Limit* mencekik ekstrak *Stored XSS* agar berhenti memutasi payload antarmuka peramban di Database SQL berbasis arsitektur *SQLite3*.
- [ ] D. *Bcrypt* dipastikan memusnahkan eksistensi jejak galat *Stack Trace* berbendera indikasi stempel *500 Internal Error*.

### Q2
**Type:** True/False
**Question:** Ketika mengarsiteki tameng berlapis penyaring keamanan siber aplikasi, pemicu arsitektur lapisan gerbang pembaca bodi *express.json()* wajib dideklarasikan dan dipanggil posisinya secara teknis membelakangi (ditulis setelah/mengalah) pada penetapan baris komando *Routing* operasional peramban semacam `app.post('/api/pasukan')`.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Modul ekstensi penawar kerentanan peladen (diseludupkan kelengkapan konfigurasinya lewat bursa *NPM*) manakah yang secara de facto dinobatkan merangkul penyematan lapis penyedia sinkronisasi selubung payload identitas parameter berkas pembaca fail `.env` agar konfigurasi variabel sandi wujud rahasianya diintegrasikan tersembunyi membaur merasuk kerangka memori lingkungan arsitektur *Node OS Environment* (dapat dipanggil via objek `process.env`)?
**Answer:** dotenv.

### Q4
**Type:** Short Answer
**Question:** Pada pengujian penetrasi pelacak badai serangan serangan eksploitasi skrip klien *Postman*, jikalau meriam tersebut melontarkan rentetan pelaporan jutaan transmisi rute percobaan *Request* melampaui dan mendobrak volume ketahanan bendungan ambang wewenang batas peladen *Rate Limit*, lantas sistem penjegal mencekik memblokir rutenya seraya melempar nomor stempel deklarasi parameter sandi galat *HTTP* balasan pelaporan kelebihan muatan transmisi. Berapakah indikasi nomer sandi pelaporan galat status spesifik tersebut (yang secara harfiah dimaknai mewakili pesan penolakan jaringan *Too Many Requests*)?
**Answer:** 429.

### Q5
**Type:** Short Answer
**Question:** Mengupas penjabaran rincian teknikal atas arsitektur perutean tatanan operasional filosofis logik penangkal kerentanan arsitektur kelalaian *Broken Access Control / IDOR* di rute implementasi pengunduhan parameter peladen, perbandingan ganda pengecekan atribut dua properti ID manakah (*sebutkan nama struktur deklarasi properti objek pemanggilan req.xxx nya*) yang mesti diadu, ditubrukkan, lantas diuji kesetaraannya demi menjamin secara murni logik penegakan keabsahan kewenangan si agen penarik pengakses payload data rahasia peladen tersebut?
**Answer:** req.params.id dan req.user.id.
