---
type: quiz
week: 12
day: 5
title: "Quiz: Lab CRUD REST API"
total_questions: 5
---

### Q1
**Type:** Multiple Choice
**Question:** Dalam skema pengerjaan simulasi aplikasi *REST API In-Memory*, peringatan penolakan bertajuk keterangan teks galat `Cannot GET /` sering kali terpampang spontan di tatapan peramban *browser* ketika kamu menjalankan pendaratan pengetesan pengaksesan rute paling awal beranda titik `http://localhost:8080/`. Menurutmu, galat ketiadaan tersebut menyiratkan kelalaian arsitektur implementasi pada sisi peladen mana?
- [ ] A. Akses jalur pelabuhan jaringan *port* peladen disadap sistem OS lantaran diindikasikan belum memiliki penguncian otentik sandi transmisi sertifikat enkripsi *SSL/HTTPS* secara.
- [ ] B. Mesin prosesor V8 peramban *Chrome* terjangkit kelumpuhan virus pembeku instalasi pemroses memori statis lokal RAM.
- [x] C. Pemrogram kemungkinan luput atau belum menancapkan blok pemetaan rutinitas penanganan respons awal rute akar (*root path* pelabuhan garis miring `/`), melalui peresmian metode interaksi `app.get('/',...)`, dan malah sibuk mendaftarkan spesifikasi perutean cabang parsial URL lainnya, misal: di dahan spesifik `/api/arsip`.
- [ ] D. Node.js otomatis mewajibkan sistem merestui pelabuhan deklarasi gerbang instalasi *MySQL* dipatenkan di lingkungan operasional (*Environment*) sebelum peramban bisa merender penampil teks respons *JSON* ke halaman antarmuka pengunjung awan .

### Q2
**Type:** True/False
**Question:** Saat sebuah muatan parameter entitas payload data disembunyikan menumpang di rongga relung bodi terenkripsi dari rutinitas skema metode pengiriman rute permintaan komando transmisi *POST*, penata logik program skrip kerangka Node.js wajib merengkuhnya di lapisan penengah ekstrak penerima (*server handler*) menggunakan fungsionalitas tangkapan `req.params`.
**Answer:** False

### Q3
**Type:** Short Answer
**Question:** Selain piranti *browser Chrome* biasa yang primitif karena tidak menunjang pengujian mutasi, instalasi sebutkan setidaknya dua contoh aplikasi alat bantu pihak ketiga (*software client penguji*) apa pun (baik dalam wujud *standalone* lepas aplikasi desktop atau format *VS Code Extension*) yang lumrah dan esensial digunakan meluncurkan simulasi uji bidikan parameter pengujian ragam aneka metode *Request REST API* lengkap selayaknya tipe simulasi eksekusi rute muatan payload rumit (seperti pengetesan rute pengujian rute: `POST`, `PUT`, `DELETE`, perombakan *header*, *auth key*)!
**Answer:** Thunder Client, Postman, Insomnia, atau cURL.

### Q4
**Type:** Short Answer
**Question:** Agar instalasi server kerangka peladen sanggup menginspeksi, membongkar lalu membedah secara teknis paket parameter lalu lintas data berformat balutan muatan teks skrip `JSON` (yang diikutsertakan menunggang membonceng bodi *HTTP Request* klien *REST*), rantaian peresmian penangkal koding *Middleware* krusial (berformat modul fungsi bawaan Express `app.use(...)`) apa yang fardhu dicangkokkan pada skrip struktur *backend* di lapisan atas penyadapan rute-rutekan sebelum memproses penanganan pelampauan rute *POST / PUT* tersebut?
**Answer:** express.json()

### Q5
**Type:** Short Answer
**Question:** Di lorong rute *URL Parameter* pembawa nilai dinamis peladen kerangka Express.js, bilamana konfigurasi alamat menyertakan format titik sisipan identitas pengenal parameter dengan awalan bertanda dua titik kustom `:id` (*sebagai pelengkap rancangan URL misalnya `/api/user/:id`*), objek atribut ekstraksi properti *Request Node* (dengan awalan `req....`) manakah yang menjadi penampung khusus untuk membaca ekstrak nilai masukan ID variabel URL tangkapan pengintai peramban klien tersebut?
**Answer:** req.params (atau req.params.id).
