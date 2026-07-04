# 🔤 Week 3 · Day 2: Email Profesional & Komunikasi

> **Rank**: CIPHER | **Minggu ke-3**, Hari 2/5 | **Durasi**: ~40 menit

📊 **Progress**: Week 3 · Day 2/5 | CIPHER Rank (Minggu 2 dari 3) | Overall: 12/120 hari (10%)

---

## 🎯 Tujuan Hari Ini

Setelah menyelesaikan materi hari ini, kamu akan mampu:

1. **Menulis** email profesional dalam bahasa Inggris dengan format yang benar
2. **Menerapkan** etika *How to Ask Questions The Smart Way* di forum teknis
3. **Membangun** reputasi yang baik di komunitas open-source dan keamanan siber

---

## 📖 Materi Inti

### Seni Menulis Email Profesional

Sebagai anggota TISS dan praktisi IT, kamu akan sering mengirim email ke dosen, mentor, perusahaan, atau vendor. Email berbahasa Inggris memiliki *tone* (nada) dan struktur yang spesifik.

**Struktur Email yang Baik:**
1. **Subject Line**: Singkat, jelas, langsung ke inti.
2. **Salutation**: Sapaan profesional.
3. **The Hook / Purpose**: Mengapa kamu mengirim email ini (di paragraf pertama).
4. **Body**: Detail, gunakan *bullet points* jika panjang.
5. **Call to Action (CTA)**: Apa yang kamu harapkan dari penerima.
6. **Sign-off**: Penutup dan nama.

**Contoh Template Melaporkan Celah (*Vulnerability Disclosure*):**

> **Subject:** Security Vulnerability Report: XSS on [Website Name]
>
> **Dear Security Team,** *(Salutation)*
>
> **My name is [Name], an independent security researcher. I am writing to responsibly disclose a vulnerability I found on your website.** *(Purpose)*
> 
> **During a routine check, I discovered a Cross-Site Scripting (XSS) vulnerability on the `/search` endpoint. This could allow attackers to execute malicious scripts on your users' browsers.** *(Body)*
>
> **Please find the attached Proof of Concept (PoC) document for details on how to reproduce the issue. Let me know if you need any further information or clarification.** *(CTA)*
>
> **Best regards,** *(Sign-off)*
> **[Your Name]**

### Etika Bertanya: "How To Ask Questions The Smart Way"

Di komunitas teknis internasional (StackOverflow, Reddit `r/netsec`, Discord hacker), orang-orang sangat tidak mentolerir pertanyaan malas. Eric S. Raymond pernah menulis manifesto terkenal berjudul *"How To Ask Questions The Smart Way"*.

**Aturan Emas Saat Bertanya:**
1. **Jangan Tanya untuk Bertanya** ❌ ("*Bro, ada yang bisa bantu Linux nggak?*"). Langsung utarakan masalahnya! ✅ ("*Bagaimana cara memperbaiki error 'permission denied' saat menjalankan Apache di Ubuntu?*").
2. **Sebutkan Apa yang Sudah Kamu Coba** ("*Saya sudah mencoba mengubah hak akses pakai chmod 777 tapi tetap gagal...*"). Ini menunjukkan kamu tidak malas.
3. **Gunakan Judul yang Spesifik**, bukan sekadar "TOLONG BANTUAN".
4. **Sertakan Log/Pesan Error Aslinya**, jangan di-screenshot jika berupa teks panjang. Gunakan *Pastebin* atau *code block*.

---

## 🧪 Mini Lab

**Durasi**: ~10 menit

Identifikasi kesalahan pada email di bawah ini, dan coba perbaiki secara mental (atau tulis ulang di catatanmu).

**Subject:** HELP ME BROKEN TOOL!!!1!
**Message:**
Hi,
I installed nmap yesterday and it's not working. Every time I scan my network it says error. Pls fix. Im using a laptop.
Thanks,
John

**Masalah pada email di atas:**
1. Subject tidak profesional dan *all caps* (seperti teriak).
2. Tidak sopan (Hi, Pls fix).
3. Sangat tidak spesifik (tidak menyebut OS apa, command apa yang diketik, error message-nya apa).

<details>
<summary>🔑 Contoh Perbaikan yang Profesional</summary>

**Subject:** Error starting Nmap scan on Windows 10: "Failed to open device"

**Message:**
Dear Nmap Support Team,

I am experiencing an issue while trying to run a basic scan using Nmap on my Windows 10 laptop. 

When I execute the command `nmap 192.168.1.1`, I receive the following error:
*"dnet: Failed to open device eth0"*

I have already tried reinstalling Npcap and running the command prompt as Administrator, but the issue persists. Could you please point me in the right direction to resolve this?

Thank you for your time.

Best regards,
John

</details>

---

## 💡 Quiz Kilat

<details>
<summary>❓ Mengapa penting untuk menyebutkan "apa yang sudah kamu coba" saat bertanya di forum?</summary>

**Jawaban:** Karena komunitas *open-source* dan *cybersecurity* berisi profesional yang sibuk dan membantu secara sukarela. Menyebutkan apa yang sudah dicoba membuktikan bahwa kamu **menghargai waktu mereka** dengan tidak menyuruh mereka memberikan solusi yang sebenarnya sudah kamu coba dan gagal, serta menunjukkan bahwa kamu bukan pemalas.

</details>

<details>
<summary>❓ Apa itu "Call to Action" dalam sebuah email?</summary>

**Jawaban:** Call to Action (CTA) adalah kalimat di akhir email yang memperjelas **apa langkah selanjutnya** atau respons apa yang kamu inginkan dari penerima. Contoh: *"Let me know if we can schedule a meeting on Friday"* atau *"Please advise on the next steps."*

</details>

<details>
<summary>❓ Mengapa kita tidak disarankan menggunakan screenshot untuk membagikan error log teks yang panjang di forum?</summary>

**Jawaban:** Karena teks di dalam gambar **tidak bisa di-copy-paste** oleh orang yang ingin membantumu (untuk mencari error itu di Google atau menganalisisnya), dan gambar tidak bisa di-*index* oleh mesin pencari (sehingga orang lain dengan masalah yang sama tidak akan menemukan post-mu). Selalu gunakan teks (`code blocks`).

</details>

---

## 📋 Checklist Hari Ini

- [ ] Saya memahami struktur email profesional (Subject, Salutation, Body, CTA, Sign-off)
- [ ] Saya tahu cara melaporkan celah dengan format email yang benar
- [ ] Saya paham etika *"How to Ask Questions the Smart Way"*
- [ ] Saya berjanji tidak akan menggunakan "Ask to Ask" (Tanya untuk bertanya) lagi
- [ ] Saya sudah menjawab semua quiz kilat

---

## 🔗 Resources

- [How To Ask Questions The Smart Way (Eric S. Raymond)](http://www.catb.org/~esr/faqs/smart-questions.html) — Manifesto legendaris wajib baca bagi semua anak IT. (Minimal baca bagian *Introduction* dan *Before You Ask*).

---

## ➡️ Besok

**Day 3: Bug Report Writing Basics** — Email sudah, sekarang kita menulis isi laporannya! Besok kita belajar membuat *Bug Report* ala program *Bug Bounty*, lengkap dengan *Proof of Concept* (PoC).

---

*📅 TISS Null Teaming · Week 3 · Day 2 · CIPHER Rank*
