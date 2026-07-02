# 🌀 Week 1 · Day 3: CIA Triad & Etika Hacking

> **Rank**: VOID (Unranked) | **Minggu ke-1**, Hari 3/5 | **Durasi**: ~40 menit

📊 **Progress**: Week 1 · Day 3/5 | VOID Rank (Minggu 1 dari 1) | Overall: 3/120 hari (3%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Menjelaskan** CIA Triad dan memberikan contoh nyata untuk setiap prinsip
2. **Membedakan** white hat, grey hat, dan black hat hacker
3. **Memahami** batas hukum dalam hacking di Indonesia (UU ITE)

---

## 📖 Materi Inti

### CIA Triad — Fondasi Seluruh Cyber Security

Seluruh bidang keamanan siber dibangun di atas tiga prinsip fundamental yang dikenal sebagai **CIA Triad**:

```
 ╔═══════════════════╗
 ║ 🔒 CIA TRIAD ║
 ╚═══════════════════╝
 ╱ │ ╲
 ╱ │ ╲
 ╱ │ ╲
 ┌──────┐ ┌──────┐ ┌──────┐
 │ C │ │ I │ │ A │
 └──────┘ └──────┘ └──────┘
 Confidentiality Integrity Availability
```

| Prinsip | Arti | Contoh Pelanggaran | Contoh Perlindungan |
|---------|------|-------------------|--------------------| 
| **Confidentiality** | Data hanya bisa diakses oleh pihak berwenang | Data pribadi mahasiswa bocor ke publik | Enkripsi, access control, MFA |
| **Integrity** | Data tidak bisa diubah tanpa izin | Nilai mahasiswa diubah oleh hacker | Hashing, digital signatures, checksums |
| **Availability** | Sistem tersedia kapan pun dibutuhkan | SIAKAD down saat KRS karena DDoS | Redundancy, load balancing, backup |

> 💡 **Analogi kampus**: **Confidentiality** = hanya kamu yang bisa lihat transkrip nilaimu. **Integrity** = tidak ada yang bisa mengubah nilaimu secara diam-diam. **Availability** = SIAKAD bisa diakses kapan saja, termasuk saat KRS-an.

### Setiap Serangan Menyerang Minimal 1 Pilar

```
Serangan DDoS → Menyerang AVAILABILITY
Data breach → Menyerang CONFIDENTIALITY
Defacing website → Menyerang INTEGRITY
Ransomware → Menyerang AVAILABILITY + CONFIDENTIALITY
Man-in-the-Middle → Menyerang CONFIDENTIALITY + INTEGRITY
```

### Etika Hacking — Siapa Boleh "Hack"?

| Tipe | Deskripsi | Legal? |
|------|-----------|--------|
| ⬜ **White Hat** | Hacking **dengan izin** untuk menemukan kelemahan | ✅ Legal |
| 🔲 **Grey Hat** | Hacking **tanpa izin** tapi tanpa niat jahat, lalu melaporkan | ⚠️ Grey area |
| ⬛ **Black Hat** | Hacking **dengan niat jahat** (mencuri data, merusak) | ❌ Ilegal |

**UU ITE di Indonesia** (UU No. 11/2008 jo. UU No. 19/2016):
- **Pasal 30**: Akses tidak sah ke sistem komputer → pidana
- **Pasal 32**: Mengubah/merusak data elektronik → pidana
- **Pasal 33**: Mengganggu sistem elektronik → pidana

> ⚠️ **Aturan emas**: Di TISS, kita **HANYA** berlatih pada platform legal (TryHackMe, HackTheBox, PortSwigger) dan target yang sudah mendapat **izin tertulis**. Tidak pernah menyerang sistem tanpa izin.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Identifikasi serangan terhadap CIA yang mana:

Baca skenario berikut dan tentukan CIA mana yang diserang:

| # | Skenario | C? | I? | A? |
|---|----------|----|----|----| 
| 1 | Hacker mencuri database customer dari toko online |? | | |
| 2 | Attacker mengganti harga produk di website e-commerce | |? | |
| 3 | Website pemerintah tidak bisa diakses karena serangan DDoS | | |? |
| 4 | Ransomware mengenkripsi semua file di komputer korban |? | |? |
| 5 | Penyerang mengubah DNS agar mengarahkan ke website palsu |? |? | |

<details>
<summary>🔑 Klik untuk lihat jawaban</summary>

| # | Skenario | C | I | A |
|---|----------|---|---|---|
| 1 | Database customer dicuri | ✅ | | |
| 2 | Harga produk diubah | | ✅ | |
| 3 | DDoS membuat website down | | | ✅ |
| 4 | Ransomware (data dienkripsi = tidak bisa diakses + data terbaca attacker) | ✅ | | ✅ |
| 5 | DNS hijacking (traffic diarahkan ke fake site = data dicuri + data diubah) | ✅ | ✅ | |

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Apa itu CIA Triad dan sebutkan ketiga prinsipnya!</summary>

**Jawaban:** CIA Triad adalah **3 prinsip fundamental** keamanan siber:
1. **Confidentiality** — kerahasiaan data
2. **Integrity** — keutuhan/keaslian data
3. **Availability** — ketersediaan sistem

Setiap kebijakan dan teknologi keamanan dirancang untuk melindungi minimal salah satu dari ketiga prinsip ini.

</details>

<details>
<summary>❓ Seorang mahasiswa menemukan kelemahan di website kampusnya tanpa izin, lalu melaporkannya ke admin IT. Termasuk kategori hacker apa dia?</summary>

**Jawaban:** **Grey Hat**. Dia menemukan kelemahan **tanpa izin** (melanggar hukum), tapi tidak mengeksploitasi dan justru melaporkan. Di Indonesia, secara hukum ini tetap bisa dikenai pidana berdasarkan **Pasal 30 UU ITE** meskipun niatnya baik. Cara yang benar adalah meminta **izin tertulis** terlebih dahulu atau melaporkan melalui program **bug bounty** resmi jika ada.

</details>

<details>
<summary>❓ Serangan ransomware menyerang CIA yang mana dan mengapa?</summary>

**Jawaban:** Ransomware menyerang **Confidentiality** dan **Availability**:
- **Confidentiality** — attacker bisa membaca/mencuri data sebelum mengenkripsinya
- **Availability** — korban tidak bisa mengakses datanya sendiri karena terenkripsi

Beberapa ransomware modern juga mengancam akan **mempublikasikan** data (double extortion), semakin memperkuat pelanggaran Confidentiality.

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya bisa menjelaskan CIA Triad dan memberikan contoh nyata
- [ ] Saya memahami perbedaan White Hat, Grey Hat, dan Black Hat
- [ ] Saya memahami konsekuensi hukum dari hacking tanpa izin di Indonesia
- [ ] Saya sudah menyelesaikan mini lab CIA identification
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [OWASP - What is CIA Triad](https://owasp.org/www-community/CIA_Triad) — Penjelasan resmi dari OWASP
- [UU ITE Indonesia (JDIH)](https://jdih.kominfo.go.id) — Teks undang-undang lengkap

---

## ➡️ Besok

**Day 4: Sistem Ranking & Roadmap 24 Minggu** — Kenali jalur perjalananmu dari Void sampai Sentinel, plus apa itu CTF (Capture The Flag) — "olahraga" favorit para hacker! 🏴

---

*📅 TISS Null Teaming · Week 1 · Day 3 · VOID Rank*
