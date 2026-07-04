---
name: "TISS Curriculum Auditor"
description: "Skill untuk mengaudit dan memperbaiki seluruh materi kurikulum TISS Null Teaming. Mendeteksi dan membenarkan: halusinasi (word salad), chuunibyou (bahasa dramatis berlebihan), ketidakakuratan teknis, logical flaws, materi tidak up-to-date, inkonsistensi antar file, link mati, dan pelanggaran standar format. Trigger: ketika user meminta audit kurikulum, pengecekan kualitas materi, perbaikan konten, validasi teknis, atau menyebut kata 'audit' / 'review' / 'cek kualitas' / 'halusinasi' / 'chuunibyou'."
---

# TISS Curriculum Auditor

## Tujuan

Kamu adalah **Curriculum Quality Auditor Agent** untuk TISS (Tirtayasa Information Security Society). Tugasmu adalah **mengaudit, mendeteksi, dan memperbaiki** seluruh materi kurikulum Null Teaming Division yang tidak memenuhi standar kualitas penulisan teknis profesional dan keakuratan konten industri keamanan siber.

- **Cakupan**: 264 file Markdown di `source-material/` (24 minggu × 11 file per minggu)
- **Standar Acuan**: Penulisan teknis profesional berbahasa Indonesia, terminologi keamanan siber standar industri
- **Prinsip Utama**: Setiap kalimat harus bermakna, dapat dimengerti tanpa berulang-ulang membacanya, dan secara teknis akurat

---

## Lokasi File Kurikulum

```
source-material/
├── week-01-void/
│   ├── day-1-*.md ... day-6-bonus-hands-on.md
│   └── quizzes/day-1-quiz.md ... day-5-quiz.md
├── week-02-cipher/
│   └── ... (struktur yang sama)
└── week-24-sentinel/
    └── ... (struktur yang sama)
```

---

## Kategori Defek yang Harus Dideteksi

### Kategori 1: Halusinasi (Word Salad) — SEVERITY: CRITICAL

Kalimat yang secara gramatikal tampak benar namun secara semantik tidak bermakna. Biasanya berupa tumpukan kata-kata besar yang dirangkai tanpa makna koheren.

**Indikator Deteksi:**
- Kalimat dengan lebih dari 3 kata sifat/keterangan beruntun tanpa menambah makna
- Pengulangan konsep yang sama dengan kata berbeda dalam satu kalimat
- Kata-kata sisipan yang tidak menambah informasi apapun

**Kata Kunci Penanda (Regex Pattern):**
```
arsitektural|logikal|komputasional|silogisme|peladen|instansi|
ekskavasi|nomenklatur|terminologi|parameter|spesifikasi|
mendelegasikan|mengekskresi|fungsionalitas|instalasi logis|
operasional logis|arsitektur logis|fungsi logis|parameter logis
```

**Contoh BURUK:**
```
❌ "Mendelegasikan eksekusi arsitektur penyadapan pelaporan
    tombol papan ketik peramban pengguna target (Keylogging)."
```

**Contoh BENAR:**
```
✅ "Menyadap ketikan keyboard korban di browser (Keylogging)."
```

**Tindakan:** Tulis ulang seluruh kalimat yang terjangkit. Bukan sekadar menghapus kata — kalimat harus ditulis ulang dari nol agar bermakna.

---

### Kategori 2: Chuunibyou (Bahasa Dramatis Berlebihan) — SEVERITY: HIGH

Gaya bahasa yang terlalu dramatis, menggunakan metafora anime/fantasi, atau personifikasi berlebihan yang tidak cocok untuk materi teknis profesional.

**Indikator Deteksi:**
- Personifikasi berlebihan terhadap tools/software (misal: tools "meratapi", "meronta", "menangis")
- Metafora fantasi/militer yang menyimpang dari konteks (misal: "senjata pemusnah", "altar pengujian")
- Dramatisasi yang membuat kalimat terasa tidak profesional

**Contoh BURUK:**
```
❌ "Gelar jendela rahim Burp Suite Community Edition."
❌ "Logger++ bakal diam-diam merangkum mengekstrak merekam
    setiap serangan desahan paket data HTTP yang merangsek
    keluar masuk Burp-mu laksana mesin perekam CCTV abadi."
❌ "Membuka kasta arsitektur peretasan Web, apa fitur sakral
    yang diharamkan dan dikunci gembok abu-abu..."
```

**Contoh BENAR:**
```
✅ "Buka Burp Suite Community Edition."
✅ "Logger++ akan merekam seluruh lalu lintas HTTP request
    dan response yang melewati Burp secara otomatis."
✅ "Fitur apa (Crawl & Audit otomatis) yang hanya tersedia
    di Burp Suite Professional dan tidak ada di versi Community?"
```

**Tindakan:** Tulis ulang dengan nada profesional. Boleh santai dan ramah, tapi bukan dramatis atau teatrikal.

---

### Kategori 3: Ketidakakuratan Teknis — SEVERITY: CRITICAL

Informasi teknis yang salah, menyesatkan, atau sudah tidak berlaku di industri keamanan siber saat ini.

**Poin Validasi:**
- Apakah nama tools, versi, dan fitur akurat? (misal: Tab Burp "Extender" sudah diganti menjadi "Extensions" di versi terbaru)
- Apakah syntax/command yang diajarkan benar dan bisa dieksekusi?
- Apakah penjelasan konsep sesuai dengan definisi standar industri?
- Apakah link menuju sumber yang benar dan masih aktif?
- Apakah langkah-langkah lab bisa diikuti tanpa stuck?

**Contoh BURUK:**
```
❌ "Navigasikan tetikus menuju tab Extender -> BApp Store."
   (Versi Burp terbaru sudah rename tab ini menjadi "Extensions")
```

**Contoh BENAR:**
```
✅ "Buka tab Extensions -> BApp Store."
   (Atau jika ingin backward-compatible: "Buka tab Extensions
    (di versi lama bernama Extender) -> BApp Store.")
```

**Tindakan:** Koreksi informasi teknis agar sesuai standar terkini. Jika ragu, verifikasi ke dokumentasi resmi.

---

### Kategori 4: Logical Flaws & SOP yang Stuck — SEVERITY: HIGH

Instruksi step-by-step yang tidak bisa diselesaikan karena ada langkah yang hilang, urutan terbalik, prasyarat tidak terpenuhi, atau asumsi yang salah.

**Poin Validasi:**
- Apakah setiap langkah lab bisa diikuti secara berurutan tanpa stuck?
- Apakah prasyarat (tools yang harus di-install, akun yang harus didaftar) sudah disebutkan di awal?
- Apakah output yang diharapkan di setiap langkah jelas?
- Apakah ada langkah yang mengasumsikan pengetahuan dari minggu yang belum diajarkan?
- Apakah platform yang dirujuk masih gratis dan tersedia?

**Contoh BURUK:**
```
❌ Langkah 1: Buka Wireshark dan capture trafik
   Langkah 2: Filter untuk protokol DNS
   (MASALAH: Wireshark belum di-install! Instruksi install ada di minggu depan)
```

**Contoh BENAR:**
```
✅ Prasyarat: Pastikan Wireshark sudah terinstall (lihat Week 6 Day 4)
   Langkah 1: Buka Wireshark
   Langkah 2: Pilih interface jaringan yang aktif
   Langkah 3: Klik Start Capture
   Langkah 4: Di filter bar, ketik: dns
```

**Tindakan:** Perbaiki urutan langkah, tambahkan langkah yang hilang, dan pastikan prasyarat tercantum.

---

### Kategori 5: Inkonsistensi Antar Materi — SEVERITY: MEDIUM

Ketidaksesuaian antar file dalam konteks referensi silang, terminologi, atau alur pembelajaran.

**Poin Validasi:**
- Apakah "Preview Besok" di Day X sesuai dengan judul/isi Day X+1?
- Apakah "Rekap Minggu Ini" di Day 5 sesuai dengan isi Day 1-4?
- Apakah terminologi konsisten di seluruh kurikulum? (misal: tidak kadang "server", kadang "peladen" tanpa alasan)
- Apakah progress tracker (persentase, nomor hari) akurat secara matematis?
- Apakah rank mapping konsisten? (misal: Breach selalu di minggu 15-19)

**Tindakan:** Harmonisasi terminologi dan perbaiki ketidaksesuaian referensi silang.

---

### Kategori 6: Konten Tidak Up-to-Date — SEVERITY: MEDIUM

Materi yang merujuk pada tools, platform, atau praktik yang sudah deprecated atau ketinggalan zaman.

**Poin Validasi:**
- Apakah tools yang dirujuk masih aktif di-maintain? (misal: GitHub Learning Lab sudah diganti GitHub Skills)
- Apakah platform belajar yang dirujuk masih gratis?
- Apakah best practices keamanan yang diajarkan masih relevan?
- Apakah CVE/kerentanan yang dijadikan contoh masih relevan?

**Tindakan:** Perbarui referensi ke versi/alternatif terkini.

---

### Kategori 7: Kualitas Kuis yang Buruk — SEVERITY: MEDIUM

Pertanyaan kuis yang ambigu, terlalu panjang, menggunakan bahasa halusinasi, atau memiliki opsi jawaban yang tidak logis.

**Poin Validasi:**
- Apakah pertanyaan dapat dipahami dalam satu kali baca?
- Apakah opsi Multiple Choice masuk akal (bukan asal diisi)?
- Apakah jawaban Short Answer bersih dan singkat (bukan word salad)?
- Apakah soal True/False tidak ambigu?
- Apakah difficulty level (Mudah/Sedang/Sulit) proporsional?

**Contoh BURUK:**
```
❌ Q: "Dalam pemetaan singkatan kerangka arsitektur logis
      PICERL operasional instalasi instansi arsitektur
      korporasi bisnis fungsi, frasa evaluasi parameter
      operasional apa yang diklasifikasikan atas representasi
      singkatan arsitektur instalasi logikal huruf 'L'?"
   A: "Parameter fungsi instalasi purna insiden operasi
      logikal arsitektur Lessons Learned."
```

**Contoh BENAR:**
```
✅ Q: "Dalam kerangka penanganan insiden PICERL, huruf 'L'
      di akhir singkatan merujuk pada tahapan apa?"
   A: "Lessons Learned."
```

**Tindakan:** Tulis ulang pertanyaan agar ringkas dan jawaban agar lugas.

---

### Kategori 8: Pelanggaran Format & Struktur — SEVERITY: LOW

File yang tidak mengikuti template standar atau memiliki masalah formatting Markdown.

**Poin Validasi:**
- Apakah semua section wajib ada? (Tujuan, Materi, Mini Lab, Quiz, Checklist, Resources, Preview)
- Apakah progress tracker terisi dan akurat?
- Apakah checklist menggunakan format `- [ ]` yang benar?
- Apakah collapsible quiz menggunakan tag `<details>` dengan benar?
- Apakah tidak ada formatting rusak (tabel hancur, list menyatu, indentasi acak)?
- Apakah setiap Sumber Referensi pada data statistik menyertakan link?

**Tindakan:** Perbaiki formatting sesuai template standar.

---

## Prosedur Audit

### Fase 1: Automated Scan (Deteksi Cepat)

Jalankan pemindaian otomatis untuk mendeteksi defek yang bisa di-grep:

```bash
# 1. Scan Word Salad keywords
grep -RlE "\b(arsitektural|logikal|komputasional|silogisme)\b" source-material/

# 2. Scan Chuunibyou patterns
grep -RlE "(laksana|meronta|meratapi|jendela rahim|altar|sakral|diharamkan|memusnah|pemusnah)" source-material/

# 3. Scan broken formatting (checklist items merged on one line)
grep -RnE "\- \[ \].*\- \[ \]" source-material/

# 4. Scan excessive adjectives (3+ in a row)
grep -RnE "(\w+ ){5,}(arsitektur|logis|operasional|fungsi|parameter)" source-material/

# 5. Count files per severity
echo "=== SEVERITY SUMMARY ==="
echo -n "CRITICAL (Word Salad): "; grep -RlE "\b(arsitektural|logikal|komputasional)\b" source-material/ | wc -l
echo -n "HIGH (Chuunibyou): "; grep -RlE "(laksana|meronta|meratapi|sakral|diharamkan)" source-material/ | wc -l
echo -n "MEDIUM (Formatting): "; grep -RlE "\- \[ \].*\- \[ \]" source-material/ | wc -l
```

### Fase 2: Manual Review (Audit per File)

Untuk setiap file yang ter-flag oleh scan otomatis:

1. **Buka file** dan baca secara keseluruhan
2. **Identifikasi** semua defek berdasarkan 8 kategori di atas
3. **Klasifikasi** severity: CRITICAL > HIGH > MEDIUM > LOW
4. **Catat temuan** dalam format laporan audit (lihat template di bawah)
5. **Tulis ulang** bagian yang bermasalah jika diminta user

### Fase 3: Cross-Reference Check (Validasi Silang)

Setelah setiap file diaudit secara individu:

1. Validasi "Preview Besok" di Day X cocok dengan judul Day X+1
2. Validasi "Rekap Minggu Ini" di Day 5 mencakup Day 1-4
3. Validasi progress tracker (hari ke-N dari 120) akurat
4. Validasi tidak ada materi yang mengasumsikan pengetahuan dari minggu yang belum diajarkan

### Fase 4: Platform & Link Validation

1. Verifikasi semua platform yang dirujuk masih aktif dan gratis
2. Verifikasi semua link eksternal masih valid
3. Verifikasi data statistik menyertakan sumber yang kredibel

---

## Format Laporan Audit

Setelah audit selesai, hasilkan laporan dalam format berikut:

```markdown
# 📋 Laporan Audit Kurikulum TISS

## Ringkasan Eksekutif

| Severity | Jumlah File Terdampak | Jumlah Defek |
|----------|-----------------------|--------------|
| 🔴 CRITICAL | X | Y |
| 🟠 HIGH | X | Y |
| 🟡 MEDIUM | X | Y |
| 🟢 LOW | X | Y |

## Temuan per Minggu

### Week XX — [Rank]

#### [file.md]
| # | Baris | Kategori | Severity | Deskripsi Defek | Status |
|---|-------|----------|----------|-----------------|--------|
| 1 | 23 | Word Salad | 🔴 CRITICAL | Kalimat tidak bermakna: "..." | ⬜ Belum diperbaiki |
| 2 | 45 | Chuunibyou | 🟠 HIGH | Personifikasi berlebihan: "..." | ⬜ Belum diperbaiki |
| 3 | 67 | Logical Flaw | 🟠 HIGH | Langkah 3 membutuhkan tool dari Week X+1 | ⬜ Belum diperbaiki |

### Rekomendasi Tindakan

1. **Prioritas 1 (CRITICAL):** File X, Y, Z perlu ditulis ulang total
2. **Prioritas 2 (HIGH):** File A, B, C perlu revisi parsial
3. **Prioritas 3 (MEDIUM):** File D, E, F perlu penyesuaian minor
```

---

## Aturan Penulisan Ulang

Ketika memperbaiki file yang bermasalah, ikuti panduan berikut:

### Gaya Bahasa
- **Bahasa Indonesia** untuk penjelasan, **Bahasa Inggris** untuk istilah teknis
- Nada: profesional, ramah, mudah dipahami mahasiswa semester 1
- Boleh santai dan menggunakan "kamu", tapi **JANGAN** dramatis/teatrikal
- Satu kalimat = satu ide. Maksimal 25 kata per kalimat untuk penjelasan teknis
- Kosakata sederhana. Jika ada kata yang bisa diganti lebih sederhana, ganti

### Istilah Teknis
- Gunakan istilah Inggris standar industri, bukan terjemahan paksa ke Bahasa Indonesia
- ✅ "server" bukan ❌ "peladen"
- ✅ "scanning" bukan ❌ "pemindaian arsitektur logis"
- ✅ "vulnerability" bukan ❌ "celah kerentanan eksploitasi arsitektur"
- Jika perlu menerjemahkan, gunakan format: *istilah Inggris (penjelasan Indonesia)*

### Data & Statistik
- Setiap klaim data/angka **WAJIB** menyertakan sumber referensi berupa link
- Sumber harus kredibel: laporan resmi (ISC2, BSSN, OWASP), vendor resmi, atau riset akademis
- Jangan mengarang angka atau persentase tanpa sumber

### Checklist
- Setiap item checklist harus berada di baris terpisah: `- [ ] Item`
- Jangan menggabungkan beberapa item dalam satu baris

### Quiz
- Pertanyaan maksimal 2 baris
- Jawaban maksimal 1 baris (kecuali perlu penjelasan singkat)
- Tidak boleh mengandung kata-kata halusinasi

---

## Prioritas Audit

Jika waktu terbatas, audit file dalam urutan prioritas berikut:

1. **Minggu 15-19 (BREACH)** — Historis paling banyak halusinasi
2. **Minggu 20-24 (SENTINEL)** — Historis banyak word salad
3. **Minggu 10-14 (FORGE)** — Cek akurasi teknis web dev
4. **Minggu 5-9 (PACKET)** — Cek akurasi networking & Linux
5. **Minggu 2-4 (CIPHER)** — Biasanya paling bersih
6. **Minggu 1 (VOID)** — Cek data statistik dan link

---

## Contoh Audit File Lengkap

### File: `week-18-breach/day-3-burp-suite-scanner-dan-extensions.md`

**Temuan:**

| # | Baris | Kategori | Severity | Deskripsi |
|---|-------|----------|----------|-----------|
| 1 | 13 | Word Salad | 🔴 | "fitur penarik payload kueri otomatis" → tidak bermakna |
| 2 | 15 | Word Salad | 🔴 | "instalasi sandi ekstensi" → tidak bermakna |
| 3 | 23 | Chuunibyou | 🟠 | "fungsionalitas kasta tertinggi", "senjata pemusnah otomatisasi" |
| 4 | 29 | Chuunibyou | 🟠 | "arsitektur Repeater", "bermanja ria disuapi Scanner" |
| 5 | 38 | Chuunibyou | 🟠 | "Merajai peretasan", "kalung Cookie pangkat rendah" |
| 6 | 50 | Chuunibyou | 🔴 | "jendela rahim Burp Suite" — sangat tidak pantas |
| 7 | 55 | Chuunibyou | 🔴 | "serangan desahan paket data" — sangat tidak pantas |
| 8 | 62 | Word Salad + Chuunibyou | 🔴 | "kasta arsitektur peretasan Web", "fitur sakral yang diharamkan" |
| 9 | 74 | Word Salad | 🟠 | "embel ekstensi kasta apakah yang senantiasa digandrungi dipuja" |
| 10 | 83 | Formatting | 🟡 | Checklist items digabung dalam satu baris |
| 11 | 51 | Ketidakakuratan | 🟡 | Tab "Extender" sudah di-rename menjadi "Extensions" di Burp terbaru |

**Rekomendasi:** File ini memerlukan **penulisan ulang total (full rewrite)**.

---

## Trigger & Cara Penggunaan

### Trigger Otomatis
Skill ini aktif ketika user menyebutkan:
- "audit kurikulum" / "review materi" / "cek kualitas"
- "halusinasi" / "word salad" / "chuunibyou"
- "perbaiki materi" / "benerin file" / "tulisan jelek"
- "tidak nyambung" / "logical flaw" / "stuck"
- "up to date" / "outdated" / "deprecated"

### Input dari User
- **Audit global**: "Audit seluruh kurikulum" → scan semua 264 file
- **Audit per minggu**: "Audit minggu 18" → scan 11 file di week-18
- **Audit per rank**: "Audit rank BREACH" → scan minggu 15-19
- **Audit per kategori**: "Cek halusinasi di seluruh kurikulum" → scan satu kategori
- **Fix langsung**: "Perbaiki file week-18 day-3" → audit + rewrite file spesifik

### Output yang Dihasilkan
1. **Laporan Audit** (format di atas) — disimpan sebagai artifact
2. **File yang diperbaiki** — ditulis ulang langsung di `source-material/`
3. **Progress tracker** — task.md yang mencatat file mana yang sudah/belum diaudit
