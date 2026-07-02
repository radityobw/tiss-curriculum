# 🎯 Week 22 · Day 6 (Bonus): Hands-On Learning

> **Rank**: SENTINEL | **Minggu ke-22** | Bonus Day

---

## 🌐 Platform Hari Ini

**[Splunk Free — Tutorial Dataset (Self-Hosted)](https://www.splunk.com/en_us/download/splunk-enterprise.html)**
Splunk Enterprise versi gratis (lisensi Free, hingga 500MB/hari) dengan tutorial dataset bawaan untuk mempelajari SPL (Splunk Processing Language) dan dashboard monitoring.

💰 **Biaya**: Gratis (Splunk Free license, 500MB/hari — cukup untuk pembelajaran)
⏱️ **Estimasi Waktu**: ~90 menit

---

## 🎯 Objektif

Setelah menyelesaikan hands-on ini, kamu akan mampu:
1. Menggunakan SPL dasar untuk mencari dan memfilter log di Splunk
2. Membuat visualisasi sederhana (chart, table) dari data log
3. Mengkorelasikan temuan Splunk dengan konsep SIEM dari Day 1-3

---

## 📋 Requirement

* Terminal Linux atau Windows (untuk instalasi Splunk)
* Minimal 4GB RAM bebas
* Koneksi internet (untuk download Splunk, ~500MB)
* Browser modern (Chrome/Firefox)

> ⚠️ **Splunk memerlukan instalasi lokal.** Ikuti langkah instalasi di bawah. Jika gagal, gunakan **Fallback** di akhir dokumen.

---

## 📝 Prosedur

### Langkah 1: Instal Splunk Free

**Linux (Ubuntu/Debian):**
```bash
# Unduh Splunk (perlu membuat akun gratis di splunk.com terlebih dahulu)
# Setelah download file.deb:
sudo dpkg -i splunk-*.deb
sudo /opt/splunk/bin/splunk start --accept-license
# Buat username admin dan password saat diminta
```

**Atau menggunakan Docker (lebih mudah):**
```bash
docker pull splunk/splunk:latest
docker run -d -p 8000:8000 -e SPLUNK_START_ARGS='--accept-license' \
 -e SPLUNK_PASSWORD='TissPass123!' splunk/splunk:latest
```

Buka browser: `http://localhost:8000`
Login: `admin` / `TissPass123!` (atau password yang kamu buat)

> 💡 **Jika instalasi gagal**: Langsung menuju bagian **Fallback** di bawah — kamu tetap bisa belajar analisis log tanpa Splunk.

### Langkah 2: Ingest Sample Data
1. Di Splunk web interface, klik **Settings** → **Add Data**
2. Pilih **Upload** → cari file log untuk di-upload
3. Jika tidak punya file log, gunakan tutorial dataset bawaan Splunk:
 - Klik **Search & Reporting** app
 - Di search bar, ketik: `| makeresults count=1` → klik Search (untuk verifikasi Splunk berfungsi)
4. Atau unduh sample log dari [SecRepo.com](https://www.secrepo.com/):
 ```bash
 wget https://www.secrepo.com/self.logs/access.log.2017-01-01.gz
 gunzip access.log.2017-01-01.gz
 ```
5. Upload file tersebut via **Add Data** → **Upload**

### Langkah 3: Praktik SPL Queries
Buka **Search & Reporting**, ketik query SPL berikut satu per satu:

```spl
# 1. Lihat semua data yang di-ingest
index=* | head 20

# 2. Hitung jumlah event
index=* | stats count

# 3. Distribusi berdasarkan source IP (jika data access log)
index=* | stats count by src_ip | sort -count | head 10

# 4. Cari indikator serangan
index=* "UNION SELECT" OR "/etc/passwd" OR "<script>"

# 5. Timeline event per jam
index=* | timechart span=1h count

# 6. Tabel status code
index=* | stats count by status | sort -count
```

> 💡 **SPL mirip dengan pipeline CLI** (`|`): setiap command mengambil output dari command sebelumnya. Jika kamu sudah terbiasa dengan `grep | sort | uniq`, SPL akan terasa familiar.

### Langkah 4: Buat Visualisasi
1. Jalankan query: `index=* | timechart span=1h count`
2. Klik tab **Visualization** (di bawah search bar)
3. Pilih tipe chart: **Line Chart** atau **Bar Chart**
4. Ini adalah dashboard monitoring sederhana pertamamu!
5. (Opsional) Klik **Save As** → **Dashboard Panel** untuk menyimpan ke dashboard

### Langkah 5: Dokumentasi
```markdown
# SOC Shift Handover Log — Week 22
- Tool: Splunk Free
- Dataset: [nama file log]

## SPL Queries yang Digunakan
| Query | Hasil |
|-------|-------|
| `index=* \| stats count by src_ip` | Top IP: [IP] dengan [N] request |
| `index=* "UNION SELECT"` | Ditemukan [N] indikator SQLi |

## Visualisasi
[Tangkapan layar chart timeline]
```

---

## 🏁 Target Output

* ✅ Splunk Free berhasil terinstal dan berjalan
* ✅ Minimal **1 file log** berhasil di-ingest ke Splunk
* 📝 **5 SPL queries** yang berhasil dijalankan beserta hasilnya
* 📸 Tangkapan layar visualisasi (chart/graph) di Splunk
* 📝 SOC Shift Handover Log

---

## 🔄 Fallback

Jika Splunk gagal diinstal (RAM kurang, instalasi error, dll):

**Opsi A — Analisis Log Manual dengan CLI:**
```bash
# Unduh sample log
wget https://www.secrepo.com/self.logs/access.log.2017-01-01.gz
gunzip access.log.2017-01-01.gz

# Analisis yang sama seperti SPL, tapi dengan CLI tools:

# Top 10 IP
awk '{print $1}' access.log.2017-01-01 | sort | uniq -c | sort -rn | head 10

# Cari indikator serangan
grep -iE "(union|select|script|alert|passwd)" access.log.2017-01-01

# Distribusi status code
awk '{print $9}' access.log.2017-01-01 | sort | uniq -c | sort -rn

# Timeline per jam
awk '{print $4}' access.log.2017-01-01 | cut -d: -f1-2 | sort | uniq -c
```

**Opsi B — Gunakan ELK Stack Online Demo:**
1. Buka [demo.elastic.co](https://demo.elastic.co) (jika tersedia)
2. Eksplorasi dashboard Kibana dengan sample data bawaan
3. Pelajari konsep SIEM melalui interface Kibana

Tetap tulis SOC Shift Handover Log berdasarkan analisis yang berhasil dilakukan.
