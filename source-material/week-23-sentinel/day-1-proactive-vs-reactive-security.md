# 🛡️ Week 23 · Day 1: Proactive vs Reactive Security

> **Rank**: SENTINEL | **Minggu ke-23**, Hari 1/5 | **Durasi**: ~45 menit

📊 **Progress**: Week 23 · Day 1/5 | SENTINEL Rank (Minggu 4 dari 5) | Overall: 111/120 hari (92%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Membedakan** antara paradigma keamanan reaktif dan keamanan proaktif (Threat Hunting).
2. **Memahami** pendekatan berbasis hipotesis (*Hypothesis-Driven Approach*).
3. **Mengidentifikasi** pentingnya kapabilitas analitik manusia (*Human Element*) dalam berburu ancaman.

---

## 📖 Materi Inti

### Keterbatasan Sistem Otomatis: Paradigma Reaktif vs Proaktif

Selama beberapa minggu terakhir, kamu telah mempelajari konstruksi sistem keamanan terpusat. Kamu mengonfigurasi *Splunk*, menetapkan parameter *Alerts*, dan mendelegasikan *Suricata* sebagai sensor pencegahan. Pendekatan ini diklasifikasikan sebagai **Reactive Security (Keamanan Reaktif)**. Analis dalam mode ini cenderung menunggu hingga sistem menghasilkan peringatan, barulah kemudian merespons anomali tersebut.

Namun, dalam skenario operasional yang nyata, kelompok peretas tingkat lanjut *(Advanced Persistent Threats / APT)* dirancang untuk menghindari sensor peringatan tersebut. Mereka kerap mengeksploitasi fungsi bawaan sistem operasi yang sah (*Living off the Land*), yang sangat sulit dibedakan oleh algoritma SIEM dari aktivitas administrator normal.

Untuk mengantisipasi celah tersebut, industri keamanan informasi menerapkan **Proactive Security (Keamanan Proaktif)** melalui disiplin ilmu **Threat Hunting (Perburuan Ancaman)**.

### Apa itu Threat Hunting?

**Threat Hunting** adalah proses investigasi aktif dan berulang (Iteratif) yang dilakukan oleh analis keamanan menyusuri jaringan infrastruktur untuk mendeteksi serta mengisolasi ancaman siber persisten yang sukses menghindari pengamanan otomatis (*SIEM/IDS*).
Di dalam proses ini, *Human Element* (kapabilitas naluri, pengalaman, dan intuisi logis analis) tidak bisa sepenuhnya digantikan oleh otomasi kecerdasan buatan (AI). Algoritma andal dalam memproses jutaan pola data, namun spesialis manusia lebih andal dalam merangkai skenario taktis eksploitasi.

### Hypothesis-Driven Approach (Pendekatan Berbasis Hipotesis)

Seorang *Threat Hunter* tidak melakukan penelusuran data log secara acak. Mereka bekerja menggunakan metodologi terstruktur: **Pendekatan Berbasis Hipotesis (Hypothesis-Driven Approach)**.

Tahapan implementasi investigasi perburuan:
1. **Perumusan Hipotesis:** Menyusun kerangka dugaan analitik. Misal: *"Terdapat publikasi kerentanan baru pada layanan RDP Windows (CVE-2026-XYZ). Hipotesis saya adalah kelompok APT mungkin telah mengeksploitasi celah ini pada server segmen Finance kita minggu ini."*
2. **Proses Investigasi:** Berbekal hipotesis, analis mengekstraksi data *Splunk* secara spesifik pada log *Server Finance*, memfilter pencarian ke rutinitas *Event ID 4624 (Logon RDP)* yang terjadi di luar jam kerja operasional dalam periode satu minggu terakhir.
3. **Membongkar Pola (Uncovering Patterns):** Proses pengujian hipotesis untuk menemukan korelasi anomali, seperti deteksi alamat IP eksternal yang mencurigakan.
4. **Tahap Respons (Triage & Analytics):** Jika valid, analis segera memprakarsai protokol eskalasi tanggap insiden dan memperbarui parameter *Rule SIEM* operasional agar di masa mendatang, skenario tersebut dapat terdeteksi secara otomatis (Mentransformasi temuan *Proaktif* menjadi pertahanan *Reaktif*).

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Mari menyusun rancangan Hipotesis Perburuan (Threat Hunting)!

1. Siapkan aplikasi pengolah teks (Notepad).
2. Asumsikan Anda menerima laporan intelijen : *"Grup peretas 'DarkBear' baru-baru ini menyerang institusi finansial regional melalui metode lampiran email PDF berformat khusus. Ketika file tersebut dibuka, secara rahasia ia akan mengeksekusi terminal `powershell.exe` di latar belakang sistem Windows untuk memuat malware."*
3. **Misi Operasional:** Rumuskan satu arsitektur Hipotesis Perburuan untuk mengamankan institusi perusahaan Anda!
4. **Perumusan Hipotesis Taktis:**
 *"Berdasarkan tren serangan terkini, hipotesis awal saya menyatakan bahwa grup DarkBear kemungkinan sedang menguji coba vektor serangan yang sama ke jaringan perusahaan. Saya akan memburu log penciptaan proses (Event ID 4688) untuk menginspeksi kejadian di mana aplikasi pembaca PDF (Acrobat.exe) bertindak sebagai proses induk (Parent Process) yang secara anomali melahirkan proses `powershell.exe` pada infrastruktur Endpoint pegawai (User)."*
5. Implementasi selesai! Kini Anda telah bertransisi dari fase pasif menunggu peringatan ke fase proaktif dalam merumuskan penyaringan ancaman keamanan secara mandiri.

---

## 💡 Quiz Kilat

<details>
<summary>❓ Membahas filosofi operasional keamanan siber, apa diferensiasi antara implementasi <i>Reactive Security</i> dengan <i>Proactive Security (Threat Hunting)</i>?</summary>

**Jawaban:** *Reactive Security* bertindak secara pasif, bergantung penuh pada mesin sensor (SIEM/IDS) untuk membangkitkan peringatan (*Alert*) sebelum tim keamanan mengambil tindakan mitigasi. Sebaliknya, *Proactive Security* berpusat pada spesialis manusia yang secara aktif, berkala, dan iteratif menyusuri data operasional jaringan (tanpa pemicu peringatan otomatis) guna melacak ancaman siber canggih yang berhasil lolos dari sensor pengawasan standar.
</details>

<details>
<summary>❓ Dalam disiplin ilmu perburuan ancaman keamanan, mengapa peran dominan kapabilitas manusia (Human Element) dipandang belum dapat sepenuhnya disubstitusi oleh otomatisasi sistem atau kecerdasan buatan (AI)?</summary>

**Jawaban:** sistem keamanan (termasuk AI) dirancang untuk merespons parameter dan pola perilaku yang telah diprogramkan sebelumnya, sehingga efektif namun relatif kaku. Di sisi lain, peretas tingkat lanjut (*Advanced Persistent Threats/APT*) secara konstan meracik skenario modifikasi serangan (Misal: eksploitasi *Zero-day*). Mengatasi inovasi penyerangan ini membutuhkan intuisi kritis, analisis kontekstual, dan insting logis deduktif dari seorang analis (*Threat Hunter*).
</details>

<details>
<summary>❓ Pada perancangan teknikal metodologi perburuan, terminologi apakah yang merujuk kepada prosedur di mana analis tidak melakukan inspeksi data secara acak, melainkan berpedoman pada rumusan skenario dugaan terarah (misal: "Mengasumsikan peretas mengeksploitasi rute VPN selama masa pemeliharaan sistem")?</summary>

**Jawaban:** Pendekatan Berbasis Hipotesis (Hypothesis-Driven Approach).
</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami keterbatasan solusi *Reactive Security*.
- [ ] Saya fasih merumuskan kerangka *Hypothesis-Driven Approach*.
- [ ] Saya menguasai pemahaman dasar penelusuran ancaman *APT*.
- [ ] Saya mengerti fungsi krusial insting logis *Human Element*.
- [ ] Saya sudah menjawab semua quiz kilat.

---

## 🔗 Resources

- [CrowdStrike: What is Threat Hunting?](https://www.crowdstrike.com/cybersecurity-101/threat-hunting/) — Referensi komprehensif mengenai konsep fundamental dan filosofi praktik operasional perlindungan *Threat Hunting*.

---

## ➡️ Besok

**Day 2: MITRE ATT&CK Framework** — Menyusun hipotesis operasional yang relevan tidak dapat dilakukan tanpa merujuk pada standar data taktik intrusi keamanan komprehensif. Esok hari, operasional pelatihan akan beralih pada taksonomi basis pengetahuan intelijen ancaman global: **MITRE ATT&CK Framework**. Materi tersebut akan mendemonstrasikan perancangan pemetaan anatomi perilaku (Tactics, Techniques, Procedures / TTPs) serta peracikan matriks skenario pertahanan melalui platform *ATT&CK Navigator*.

---

*📅 TISS Null Teaming · Week 23 · Day 1 · SENTINEL Rank*
