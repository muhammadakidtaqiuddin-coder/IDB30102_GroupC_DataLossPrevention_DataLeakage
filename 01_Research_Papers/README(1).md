# 📁 01_Research_Papers/

Folder ini berisi kumpulan paper penelitian (research papers) yang digunakan sebagai referensi pendukung Proposal Penelitian, khususnya **Bab 2 – Tinjauan Pustaka (Literature Review)**.

Untuk setiap paper penting, informasi berikut telah diringkas: judul, penulis, tahun, masalah penelitian, metode/teknik, dataset/tools, temuan utama, keterbatasan, dan relevansinya terhadap penelitian yang diusulkan.

> ⚠️ **Penting:** Jangan mengunggah paper penelitian berhak cipta (copyrighted) ke repository GitHub publik kecuali artikel tersebut secara legal tersedia untuk didistribusikan ulang. Jika diperlukan, sertakan sitasi, DOI, atau tautan artikel resmi sebagai gantinya. Paper open-access dapat disertakan jika diizinkan.

---

## 1. Data Loss Prevention Solution for Linux Endpoint Devices

| Item | Required Information |
|---|---|
| **Paper Title** | Data Loss Prevention Solution for Linux Endpoint Devices |
| **Author(s)** | Lukas Daubner, Adam Považanec |
| **Year** | 2023 |
| **Research Problem** | Kurangnya solusi DLP (Data Loss Prevention) open-source yang tersedia luas untuk endpoint berbasis Linux, khususnya untuk mengaudit dan mengontrol operasi file system serta perangkat USB eksternal guna mencegah kebocoran data oleh insider. |
| **Method / Technique** | Perbandingan pendekatan audit/kontrol file system (fanotify, Linux Security Modules, LD_PRELOAD, system call table hijacking, ftrace hooking) dan kontrol perangkat USB (udev + sysfs); implementasi prototipe DLP bernama **Failsafe** menggunakan hooking kernel berbasis ftrace. |
| **Dataset / Tools** | Prototipe *Failsafe* (library `libFSHook` dan `libUSBControl`, ditulis dalam C); pengujian pada Ubuntu 22.04.1 LTS (VM) dengan skenario upload web (Chrome), instant messaging (Slack), file manager (Nautilus), dan cloud sync (Dropbox). |
| **Main Findings** | Hooking fungsi kernel dengan **ftrace** dinilai paling layak untuk mengaudit/mengontrol operasi file system karena tersedia luas di distribusi populer, API matang, dan cakupan operasi yang luas. Kombinasi **udev + sysfs** efektif untuk audit dan kontrol perangkat USB. Dampak performa terhadap operasi copy/move/delete relatif minor (linear terhadap jumlah operasi). |
| **Limitation** | Logika deteksi bergantung pada heuristik khusus aplikasi (hard-coded untuk Nautilus, Chrome, Dropbox) sehingga sulit digeneralisasi ke aplikasi lain; rawan false positive (mis. membuka PDF di browser terdeteksi sebagai upload); atribut perangkat USB yang belum terautorisasi masih terbatas dan kurang andal. |
| **Relevance to Proposed Research** | Menjadi referensi teknis mengenai pendekatan *endpoint-level* DLP berbasis kernel hooking (ftrace) untuk memantau operasi file dan perangkat USB — relevan sebagai dasar mekanisme deteksi/pencegahan kebocoran data pada level endpoint dalam penelitian yang diusulkan. |

---

## 2. A Hybrid Framework for Data Loss Prevention and Detection

| Item | Required Information |
|---|---|
| **Paper Title** | A Hybrid Framework for Data Loss Prevention and Detection |
| **Author(s)** | Atul Srivastava, Vijay Shankar Sharma, Priyam Srivastava, Anuradha Pillai |
| **Year** | 2024 |
| **Research Problem** | Sistem DLP berbasis *signature* tidak mampu mendeteksi serangan baru/tidak dikenal (zero-day/insider), sedangkan sistem berbasis *anomaly* memiliki tingkat false positive tinggi dan biaya operasional (waktu respons) yang mahal karena setiap alert perlu dianalisis manual. |
| **Method / Technique** | Framework hibrida yang menggabungkan **anomaly-based detection** (white-box, otomatis membangun profil perilaku normal pengguna) dengan **signature-based prevention** — operator memberi umpan balik terhadap alert untuk secara otomatis membuat/memperbarui aturan (rule tree) yang memblokir transaksi serupa di masa depan. |
| **Dataset / Tools** | Plugin **RapidMiner**; data sintetis (synthetic data) berupa log peristiwa keamanan (malware detected, suspicious network activity, unauthorized access) dari beberapa alamat IP sumber. |
| **Main Findings** | Framework berhasil mengurangi **rata-rata waktu deteksi kebocoran data sebesar 67%**, menurunkan insiden pelanggaran data sebesar 40%, upaya akses tidak sah sebesar 35%, dan tingkat false positive sebesar 50%. |
| **Limitation** | Belum diuji pada lingkungan produksi nyata (masih menggunakan data sintetis); efektivitas rule tree bergantung pada kualitas analisis akar penyebab (root cause) oleh operator; belum dibahas skalabilitas untuk volume transaksi enterprise yang sangat besar. |
| **Relevance to Proposed Research** | Memberikan model pendekatan hibrida (anomaly + signature) dengan mekanisme umpan balik (feedback loop) yang dapat dijadikan referensi arsitektur deteksi-sekaligus-pencegahan pada sistem DLP yang diusulkan, khususnya untuk menyeimbangkan deteksi ancaman baru dan efisiensi respons. |

---

## 3. Designing Data Loss Prevention System for The Enhancement of Data Integrity in Cyberspace

| Item | Required Information |
|---|---|
| **Paper Title** | Designing Data Loss Prevention System for The Enhancement of Data Integrity in Cyberspace |
| **Author(s)** | Isha Yadav, Himanshu Gupta |
| **Year** | 2023 |
| **Research Problem** | Pendekatan DLP tradisional yang hanya berfokus pada satu jenis solusi (mis. endpoint DLP saja atau network DLP saja) tidak memadai untuk menghadapi lanskap ancaman siber yang kompleks dan terus berkembang, sehingga integritas data sulit dipertahankan. |
| **Method / Technique** | Mengusulkan metodologi **hybrid DLP** yang mengombinasikan tiga pendekatan: **behavior-based DLP**, **machine learning-based DLP**, dan **network-based DLP**, melalui tahapan: identifikasi data sensitif, implementasi endpoint/network/ML DLP, integrasi solusi, serta monitoring dan pelaporan berkelanjutan. |
| **Dataset / Tools** | Studi kasus/tinjauan literatur (mis. implementasi di sektor finansial, kesehatan/Mayo Clinic, dan e-commerce); data statistik pelanggaran data historis (2011–2018) dari sumber sekunder (Statista, laporan pasar DLP). |
| **Main Findings** | Kombinasi ketiga pendekatan DLP memberikan perlindungan data yang lebih komprehensif dibanding pendekatan tunggal, mampu mendeteksi berbagai jenis ancaman (malware, phishing, insider threat) secara real-time, serta membantu kepatuhan terhadap regulasi seperti GDPR, HIPAA, dan PCI-DSS. |
| **Limitation** | Bersifat konseptual/metodologis tanpa implementasi teknis atau pengujian kuantitatif langsung terhadap sistem yang diusulkan; efektivitas bergantung pada studi kasus pihak ketiga yang dikutip, bukan eksperimen orisinal penulis. |
| **Relevance to Proposed Research** | Mendukung justifikasi perlunya pendekatan **hybrid/multi-layer** (behavior + machine learning + network) dalam merancang sistem DLP yang diusulkan, serta memberikan kerangka tahapan implementasi yang dapat diadaptasi. |

---

## 4. Data Leakage Prevention Approach Based On Insider Trust Calculation

| Item | Required Information |
|---|---|
| **Paper Title** | Data Leakage Prevention Approach Based On Insider Trust Calculation |
| **Author(s)** | Mohammed EL MOUDNI, Elhoussine ZIYATI |
| **Year** | 2023 |
| **Research Problem** | Sistem DLP konvensional umumnya hanya mengandalkan kebijakan (policy) tanpa mempertimbangkan profil dan tingkat kepercayaan (trust) insider, padahal mayoritas kebocoran data berasal dari pengguna internal (insider) yang memiliki akses sah. |
| **Method / Technique** | Model berbasis **multi-agent system** yang mengumpulkan log dari berbagai server (LDAP, antivirus/endpoint security, proxy), memprosesnya dengan teknik **ETL (Extract, Transform, Load)**, lalu menghitung **tingkat kepercayaan insider (insider trust)** berdasarkan peran (role-based) dan jenis kontrak (contract-based) melalui *trust matrix*, untuk menghasilkan keputusan permit/deny. |
| **Dataset / Tools** | Arsitektur konseptual dengan agen: Logs Collector (LC), ETL Agent (EA), Trust Calculator (TC), dan Decision Maker (DM); sumber log berupa Windows security events, log proxy internet, dan log endpoint security. |
| **Main Findings** | Model yang diusulkan menambahkan lapisan verifikasi kedua (setelah kebijakan DLP standar tidak terlanggar) berdasarkan kalkulasi trust insider, dengan keunggulan skalabilitas, optimasi penyimpanan, kecepatan pemrosesan log, dan profiling pengguna yang lebih mendalam dibanding metode konvensional. |
| **Limitation** | Paper bersifat proposal desain — **belum ada eksperimen atau validasi empiris** (disebutkan eksplisit akan dibahas pada publikasi terpisah di masa depan); pengembangan classifier machine learning untuk deteksi juga masih dalam tahap rencana. |
| **Relevance to Proposed Research** | Relevan sebagai referensi pendekatan **insider profiling & trust calculation** sebagai lapisan tambahan (bukan pengganti) kebijakan DLP konvensional, memperkaya dimensi analisis perilaku pengguna dalam sistem yang diusulkan. |

---

## 5. Data Leakage Prevention System for Internal Security

| Item | Required Information |
|---|---|
| **Paper Title** | Data Leakage Prevention System for Internal Security |
| **Author(s)** | Bhavya Singh Shishodia, Manisha J. Nene |
| **Year** | 2022 |
| **Research Problem** | Organisasi kesulitan memilih dan menerapkan solusi DLP komersial yang tepat karena minimnya literatur mengenai proses instalasi, integrasi, dan tantangan operasional DLP industri berskala besar. |
| **Method / Technique** | Studi implementasi (studi kasus nyata) DLP di **Social Security Administration (SSA)**; mengevaluasi teknik DLP umum (intelligent documents, encryption, hash matching, virtual file system, minifilters, biometrik, hypervisor) serta kriteria pemilihan vendor menggunakan sistem skor (0–4) untuk membandingkan beberapa produk. |
| **Dataset / Tools** | Produk DLP **Symantec** dan beberapa vendor pembanding (Firm B, C, D); parameter perbandingan meliputi network monitoring, email/web prevention, data discovery, endpoint protection, dsb. |
| **Main Findings** | Symantec DLP dipilih setelah evaluasi menyeluruh dengan skor tertinggi pada mayoritas kriteria; ditemukan tantangan teknis nyata seperti masalah integrasi ICAP (perlu penyesuaian batas request/response) dan kebutuhan sumber daya agent (min. 30MB RAM, 80MB storage); jumlah insiden menurun signifikan setelah kebijakan disesuaikan secara bertahap. |
| **Limitation** | Studi berbasis satu organisasi (SSA) sehingga generalisasi terbatas; perbandingan vendor bersifat subjektif berdasarkan skor internal peneliti, bukan benchmark independen; tidak membahas solusi berbasis machine learning terbaru. |
| **Relevance to Proposed Research** | Memberikan wawasan praktis (lessons learned) tentang tantangan **implementasi DLP di dunia nyata** — kriteria pemilihan vendor, kebutuhan sistem, dan manajemen kebijakan — yang berguna sebagai pertimbangan aspek operasional pada penelitian yang diusulkan. |

---

## 6. A Holistic View on Data Protection for Sharing, Communicating, and Computing Environments: Taxonomy and Future Directions

| Item | Required Information |
|---|---|
| **Paper Title** | A Holistic View on Data Protection for Sharing, Communicating, and Computing Environments: Taxonomy and Future Directions |
| **Author(s)** | Ishu Gupta, Ashutosh Kumar Singh |
| **Year** | 2022 (arXiv preprint, cs.CR) |
| **Research Problem** | Data sensitif tersebar di berbagai perangkat komputasi dan jalur akses jaringan sehingga rentan terhadap kebocoran (data leakage); dibutuhkan pemetaan menyeluruh (taksonomi) terhadap tantangan, solusi, dan celah penelitian di bidang perlindungan data. |
| **Method / Technique** | **Survei literatur (literature review) & taksonomi** — mengklasifikasikan Data Leakage Protection Systems (DLPTS) berdasarkan status data (at rest, in use, in transit), skema deployment, dan teknik analisis (statistical, watermarking, fingerprinting, machine learning). |
| **Dataset / Tools** | Tidak ada eksperimen/dataset primer — analisis berbasis kompilasi studi-studi terdahulu dan statistik kebocoran data sekunder (mis. laporan Ponemon Institute, Privacy Rights Clearinghouse, Statista). |
| **Main Findings** | Mengidentifikasi lima celah penelitian utama pada solusi DLP yang ada: overhead tinggi, penanganan permintaan yang statis, pendekatan single-objective (deteksi *atau* pencegahan saja, bukan keduanya), keterlibatan modifikasi data, dan tingkat false-positive tinggi; merekomendasikan arah riset ke depan berupa pendekatan multi-objective berbasis machine learning. |
| **Limitation** | Sebagai paper survei, tidak mengusulkan atau menguji solusi baru secara empiris; cakupan taksonomi sangat luas sehingga pembahasan tiap teknik relatif ringkas. |
| **Relevance to Proposed Research** | Sangat relevan sebagai **landasan tinjauan pustaka (state-of-the-art)** — taksonomi dan celah penelitian yang diidentifikasi dapat digunakan untuk memposisikan kontribusi/orisinalitas penelitian yang diusulkan terhadap penelitian-penelitian DLP terdahulu. |

---

## 7. A Learning Oriented DLP System based on Classification Model

| Item | Required Information |
|---|---|
| **Paper Title** | A Learning Oriented DLP System based on Classification Model |
| **Author(s)** | Kishu Gupta, Ashwani Kush |
| **Year** | 2020 |
| **Research Problem** | Diperlukan mekanisme klasifikasi dokumen otomatis yang akurat untuk menentukan tingkat sensitivitas data (restricted/internal/unrestricted) sebelum data diizinkan keluar dari organisasi, guna mencegah kebocoran data. |
| **Method / Technique** | Pendekatan **statistik & machine learning** untuk klasifikasi dokumen: **Bag-of-Words (BoW)** untuk ekstraksi fitur, **TF-IDF** untuk pembobotan term, **Vectorization**, dan algoritma yang diusulkan yaitu **IGBCA (Improvised Gradient Boosting Classification Algorithm)**, divalidasi dengan K-Fold Cross Validation (StratifiedKFold) dan RandomizedSearchCV. |
| **Dataset / Tools** | Dataset dokumen berlabel tiga kelas (Restricted, Internal, Unrestricted); library **scikit-learn** (TfidfVectorizer, SelectKBest/chi2, GradientBoostingClassifier, StratifiedKFold, RandomizedSearchCV). |
| **Main Findings** | Model IGBCA mencapai akurasi keseluruhan (overall accuracy) sekitar **96%**, dengan sensitivitas 95,1%, spesifisitas 96,5%, presisi 93,3%, dan F1-score 94,3%, serta error rate hanya ~3,96% — menunjukkan performa klasifikasi dokumen yang sangat baik untuk mendukung keputusan DLP (allow/block/encrypt). |
| **Limitation** | Kecepatan klasifikasi (speed) dan overhead sistem lain disebutkan penulis sebagai faktor yang masih perlu ditangani di penelitian mendatang; ukuran/keberagaman dataset pelatihan terbatas sehingga generalisasi ke domain dokumen lain belum teruji. |
| **Relevance to Proposed Research** | Menyediakan referensi teknik **klasifikasi konten berbasis machine learning (TF-IDF + Gradient Boosting)** yang dapat diadopsi sebagai komponen *content-aware detection* dalam sistem DLP yang diusulkan, lengkap dengan metrik evaluasi yang dapat dijadikan pembanding. |

---

## Daftar File Sumber

| No | Nama File | Sumber/Konferensi |
|---|---|---|
| 1 | `1.pdf` | ARES 2023 (ACM), DOI: 10.1145/3600160.3605036 |
| 2 | `A_Hybrid_Framework_for_Data_Loss_Prevention_and_Detection.pdf` | IEEE SPARC 2024, DOI: 10.1109/SPARC61891.2024.10828891 |
| 3 | `Designing_Data_Loss_Prevention_System_for_The_Enhancement_of_Data_Integrity_in_Cyberspace.pdf` | IEEE ICAC3N 2023, DOI: 10.1109/ICAC3N60023.2023.10541823 |
| 4 | `Data_Leakage_Prevention_Approach_Based_On_Insider_Trust_Calculation.pdf` | IEEE WINCOM 2023, DOI: 10.1109/WINCOM59760.2023.10322935 |
| 5 | `Data_Leakage_Prevention_System_for_Internal_Security.pdf` | IEEE INCOFT 2022, DOI: 10.1109/INCOFT55651.2022.10094509 |
| 6 | `2202_11965v1.pdf` | arXiv:2202.11965 [cs.CR] |
| 7 | `2312_13711v1.pdf` | INFOCOMP, v.19, no.2, 2020 |
