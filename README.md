# Atlas Anatomi Manusia 3D

**Bahasa Indonesia** | [English](README.en.md)

Website pembelajaran anatomi tubuh manusia dengan model 3D interaktif. Pengguna dapat memutar, memperbesar, dan mengeklik langsung struktur tubuh (tulang, otot, saraf, organ, pembuluh darah, dan sistem limfatik), lalu membaca nama (Indonesia, Latin, Inggris), deskripsi, fungsi, hubungan (persarafan, suplai darah, struktur terkait), dan korelasi klinis.

> **Catatan penting:** konten ditulis untuk keperluan belajar dan **bukan pengganti rujukan medis**. Periksa kembali dengan buku teks anatomi sebelum dipakai sebagai bahan ajar resmi.

---

## Daftar isi

1. [Fitur](#fitur)
2. [Cakupan data](#cakupan-data)
3. [Menjalankan dan men-deploy](#menjalankan-dan-men-deploy)
4. [Struktur repositori](#struktur-repositori)
5. [Teknologi yang digunakan](#teknologi-yang-digunakan)
6. [Bagaimana proyek ini dikembangkan](#bagaimana-proyek-ini-dikembangkan)
7. [Format data](#format-data)
8. [Menambah sistem atau struktur baru](#menambah-sistem-atau-struktur-baru)
9. [Keterbatasan yang diketahui](#keterbatasan-yang-diketahui)
10. [Kredit](#kredit)
11. [Lisensi](#lisensi)

---

## Fitur

- **Ruang 3D interaktif**: putar (seret), zoom (scroll atau cubit), geser (klik kanan), reset, dan putar otomatis.
- **Sidebar bertingkat** dengan tab Rangka, Otot, Saraf, dan Organ, dikelompokkan per daerah atau sistem, dilengkapi pencarian.
- **Klik langsung pada model** untuk memilih struktur, dengan label nama saat kursor di atasnya (desktop).
- **Sorot atau Isolasi**: struktur lain dibuat samar atau disembunyikan.
- **Filter sisi** kanan atau kiri tubuh.
- **Konteks rangka**: tulang tampil samar di balik otot, saraf, dan organ supaya letaknya mudah dipahami.
- **Panel deskripsi** berbentuk kartu yang dapat dibuka, ditutup, dan diatur tingginya; sidebar dapat dibuka, ditutup, dan diatur lebarnya.
- **Tema terang dan gelap** dengan latar bintik seperti kanvas diagram.
- **Pemuatan per sistem (lazy loading)**: data model hanya diunduh saat sistem dipilih.
- Dapat digunakan di ponsel (tata letak responsif).

## Cakupan data

Seluruh model berasal dari satu tubuh pria (lihat [Kredit](#kredit)). Jumlah struktur dihitung per "item" di sidebar (sisi kanan dan kiri digabung), sedangkan mesh adalah objek 3D individual.

| Sistem | Item | Mesh | Segitiga | Catatan |
|---|---:|---:|---:|---|
| Rangka | 159 | 277 | 329 rb | Tulang dan tulang rawan; nama ID/Latin/Inggris; deskripsi lengkap |
| Otot | 211 | 591 | 266 rb | Nama Indonesia/Latin untuk otot utama |
| Saraf | 120 | 468 | 152 rb | Nama Indonesia/Latin untuk saraf utama |
| Pernapasan | 48 | 88 | 169 rb | Paru, bronkus sampai segmental, trakea, faring, pleura, diafragma |
| Pencernaan | 40 | 55 | 199 rb | Mulut, kelenjar ludah, saluran cerna, hati, empedu, pankreas, omentum |
| Reproduksi pria | 10 | 20 | 37 rb | Testis sampai penis |
| Urinari | 5 | 8 | 20 rb | Ginjal, ureter, kandung kemih, uretra |
| Endokrin | 10 | 13 | 31 rb | Hipotalamus, hipofisis, pineal, tiroid, paratiroid, adrenal, timus |
| Jantung dan pembuluh besar | 49 | 49 | 273 rb | Ruang, katup, koroner, sirkulasi paru, aorta, vena besar |
| Pembuluh darah (6 daerah) | 368 | 627 | 3,5 jt | Arteri dan vena per daerah; sekitar 60 pembuluh utama dengan nama dan penjelasan rinci |
| Limfatik | 106 | 159 | 111 rb | Kelompok kelenjar getah bening, limpa, tonsil palatina |

Tingkat penjelasan:

- **Rinci** (deskripsi, fungsi, persarafan, suplai darah, struktur terkait, korelasi klinis): semua tulang, semua sistem organ (pernapasan, pencernaan, reproduksi pria, urinari, endokrin, jantung), dan sekitar 60 pembuluh utama.
- **Umum**: otot dan saraf di luar struktur utama, pembuluh darah lainnya, dan kelompok kelenjar getah bening memakai penjelasan umum per jenis. Halaman menampilkan catatan ketika penjelasan bersifat umum untuk sebuah kelompok.

## Menjalankan dan men-deploy

Halaman memuat `data/*.json` dengan `fetch`, sehingga **tidak bisa dibuka lewat `file://`**. Gunakan server statis apa pun.

### Lokal

```bash
git clone <url-repo-kamu>
cd <nama-repo>
python3 -m http.server 8000
# buka http://localhost:8000
```

### GitHub Pages

1. Push seluruh isi repositori.
2. Settings, lalu Pages.
3. Source: *Deploy from a branch*, branch `main`, folder `/ (root)`.
4. Situs tersedia di `https://<username>.github.io/<repo>/`.

Total data sekitar 60 MB; file terbesar sekitar 16 MB, di bawah batas 100 MB per file GitHub. Perlu diingat bahwa git menyimpan riwayat tiap perubahan file data.

## Struktur repositori

```
.
├── index.html          # Aplikasi (HTML, CSS, JS dalam satu file)
├── LICENSE             # Lisensi kode (MIT)
├── README.md           # README bahasa Indonesia
├── README.en.md        # README bahasa Inggris
├── data/
│   ├── LICENSE             # Teks lengkap CC BY-SA 4.0 (data dan teks)
│   ├── NOTICE.md           # Asal data, perubahan, dan atribusi
│   ├── atlas_rangka.json
│   ├── atlas_otot.json
│   ├── atlas_saraf.json
│   ├── atlas_organ.json    # pernapasan
│   ├── atlas_cerna.json    # pencernaan
│   ├── atlas_repro.json    # reproduksi pria
│   ├── atlas_urin.json     # urinari
│   ├── atlas_endo.json     # endokrin
│   ├── atlas_jantung.json  # jantung dan pembuluh besar
│   ├── atlas_vsKa.json     # pembuluh: kepala-leher (arteri)
│   ├── atlas_vsKv.json     # pembuluh: kepala-leher (vena)
│   ├── atlas_vsTo.json     # pembuluh: toraks
│   ├── atlas_vsAb.json     # pembuluh: abdomen dan pelvis
│   ├── atlas_vsLe.json     # pembuluh: lengan dan tangan
│   ├── atlas_vsTu.json     # pembuluh: tungkai dan kaki
│   └── atlas_limfa.json    # limfatik
└── tools/              # Skrip Python pengolah model (referensi)
```

Nama file data mengikuti kunci layer di `index.html` (`atlas_<kunci>.json`).

## Teknologi yang digunakan

**Aplikasi (front-end)**

- HTML, CSS, dan JavaScript murni (tanpa framework dan tanpa build step), semuanya dalam satu `index.html`.
- [three.js](https://threejs.org/) r128 untuk rendering 3D (`MeshStandardMaterial`, `Raycaster`), dimuat dari CDN cdnjs.
- `OrbitControls` dari paket `three@0.128.0` (CDN jsDelivr) untuk putar, zoom, dan geser.
- CSS variables untuk tema terang dan gelap, `ResizeObserver` untuk menyesuaikan kanvas, Pointer Events untuk seret panel dan klik model.

**Pengolahan data (tools, offline)**

- Python 3 dengan `numpy` (dan `scipy` tersedia) untuk membaca OBJ, membuang duplikat, menyederhanakan mesh, dan mengemas data biner.
- Node.js untuk memeriksa sintaks skrip dan menyusun ulang blok data pada halaman.

**Hosting**

- Versi pengembangan dipublikasikan sebagai halaman web dengan file data terpisah.
- Versi repositori ini memakai jalur relatif `data/…` sehingga cocok untuk GitHub Pages atau server statis lain.

**Pengembangan**

- Proyek ini dikembangkan secara iteratif bersama asisten AI (Claude, Anthropic): perancangan arsitektur, penulisan kode, skrip pengolah model, dan penyusunan teks anatomi. Lihat [Kredit](#kredit) dan [Keterbatasan](#keterbatasan-yang-diketahui) mengenai verifikasi konten.

## Bagaimana proyek ini dikembangkan

Urutan pengerjaan, dari awal sampai sekarang:

1. **Perancangan konten.** Menentukan kerangka materi: sel dan jaringan, sebelas sistem organ, anatomi regional, dan struktur data seragam untuk setiap struktur (nama ID/Latin/Inggris, kategori dan lokasi, deskripsi dan fungsi, hubungan, korelasi klinis).
2. **Prototipe tampilan.** Tata letak dua bagian: sidebar di kiri, ruang 3D dan panel deskripsi di kanan. Versi pertama memakai bentuk 3D prosedural sederhana (silinder dan bola) sebagai pengganti sementara.
3. **Model nyata.** Berkas OBJ Z-Anatomy (seluruh atlas, sekitar 1,3 GB, 4.878 objek) diolah menjadi data yang ringan untuk web.
4. **Penambahan lapisan bertahap**: rangka, lalu otot dan saraf, lalu organ per sistem, lalu pembuluh darah dan limfatik.
5. **Perbaikan antarmuka**: tema terang dan gelap, latar bintik, klik langsung pada model, sorot dan isolasi, filter sisi, panel dapat diatur ukurannya, perbaikan tampilan ponsel.
6. **Pemisahan data per sistem (lazy loading)** agar halaman tetap kecil dan sistem baru bisa ditambah tanpa batas ukuran satu file.

### Alur pengolahan model (`tools/`)

1. **Ekstraksi** — membaca OBJ baris demi baris (streaming) dan menyimpan objek yang dipilih berdasarkan indeks urutan dan pola nama.
2. **Seleksi** — memilih rentang objek untuk tiap sistem. Contoh: tulang dari indeks awal, organ dari rentang viscera, pembuluh dari rentang arteri dan vena.
3. **Pembuangan duplikat** — banyak saluran (ureter, uretra, sebagian bronkus dan duktus, hampir semua pembuluh) tersimpan sebagai dua objek identik di sumbernya. Objek dengan bentuk identik dibuang.
4. **Penyederhanaan** — pada rangka, otot, saraf, pernapasan, dan pencernaan, mesh disederhanakan dengan *vertex clustering* (penggabungan titik pada grid) dengan target jumlah segitiga per objek. Pada sistem lain (reproduksi, urinari, endokrin, jantung, pembuluh, limfatik) **tidak ada penurunan detail**; dua mesh pembuluh yang melebihi batas indeks 16-bit dipecah menjadi beberapa bagian tanpa mengurangi detail.
5. **Kuantisasi dan pengemasan** — posisi vertex dikuantisasi ke 16-bit dalam kotak batas layer, indeks segitiga 16-bit, lalu seluruhnya di-base64 dan ditulis sebagai JSON.
6. **Pengelompokan dan penamaan** — struktur dikelompokkan per sisi, jenis, atau daerah; nama Indonesia dan Latin ditulis untuk struktur utama.
7. **Penulisan konten** — deskripsi, fungsi, persarafan, suplai darah, struktur terkait, dan korelasi klinis ditulis per struktur atau per kelompok.

### Keputusan desain

- **Satu file HTML tanpa build step** supaya mudah di-host dan dipahami.
- **Data terpisah per sistem** agar halaman awal kecil (sekitar 350 KB) dan model baru diunduh hanya saat dibutuhkan.
- **Struktur yang menempel pada permukaan struktur lain** (segmen hati, taenia kolon) disembunyikan sampai dipilih supaya tidak berkedip karena permukaan yang berimpit.
- **Selaput tipis** (pleura, mukosa, omentum, mesokolon) ditampilkan transparan dan dikecualikan dari klik di model supaya tidak menghalangi struktur di belakangnya.
- **Pengelompokan daerah pembuluh** ditentukan dari posisi titik pusat struktur (ketinggian dan jarak dari garis tengah) karena nama pembuluh tidak memuat informasi daerah.

## Format data

Setiap `data/atlas_<kunci>.json` berisi:

```json
{
  "b": "<base64 biner>",
  "m": {
    "mn": [x, y, z],
    "sc": 1.7,
    "meta": [["Nama_objek.r", jumlahVertex, jumlahSegitiga, offsetVertex, offsetIndeks], "..."]
  }
}
```

- Biner terdiri dari semua posisi vertex (3 × `uint16` per vertex, dikuantisasi) diikuti semua indeks segitiga (`uint16`).
- Posisi dunia dihitung sebagai `mn + nilai / 65535 × sc` pada setiap sumbu.
- `offsetVertex` dan `offsetIndeks` dihitung dalam satuan `uint16` pada aliran biner yang sama.
- Daftar nama, kelompok, dan teks deskripsi ada di `index.html`:
  - `BL[kunci].g` — kelompok dan item sidebar (`id`, `n` nama utama, `l` Latin, `e` Inggris, `r` daerah, `s` sisi, `p` indeks mesh, `d` kunci deskripsi, `g` bila penjelasan bersifat umum).
  - `DET[kunci]` — teks (`desc`, `fn`, `nerve`, `blood`, `rel`, `clin`).
  - `AID` — peta kunci layer (versi hosting platform); pada repositori ini jalur data dibentuk dari `data/atlas_<kunci>.json`.

## Menambah sistem atau struktur baru

1. **Ekstrak dan kemas** objek dari OBJ dengan skrip di `tools/` untuk menghasilkan `data/atlas_<kunci>.json` dan daftar mesh.
2. **Buat kelompok item** dengan `id` (nama dasar objek), `n`, `l`, `e`, `r`, `s`, `p` (indeks mesh), dan `d` (kunci teks).
3. **Tambahkan teks** ke `DET` (enam bidang), atau gunakan kunci umum dengan `g: 1`.
4. **Daftarkan layer** di `index.html`:
   - tambahkan `BL[kunci]`,
   - tambahkan kunci ke `NAMES`, `TITLE`, `LATIN`, `HELP`, dan `EM`,
   - tambahkan kunci ke fungsi `isOrg` bila ingin memakai warna organ,
   - tambahkan opsi di dropdown sistem organ.
5. **Warna**: sesuaikan fungsi `ocol` bila perlu warna khusus per struktur.

> Skrip di `tools/` bersifat referensi: memakai path lokal dan butuh berkas OBJ sumber (tidak disertakan karena ukurannya). Sesuaikan path sebelum menjalankan.

## Keterbatasan yang diketahui

- **Model tubuh pria**: organ reproduksi wanita tidak ada.
- **Struktur yang tidak ada di model sumber**, antara lain ileum, sekum, rektum, dan kanal anus sebagai objek terpisah; vena kava superior; septum interventrikular; nodus SA dan AV; perikardium; alveolus dan laring bagian dalam; pembuluh limfe dan duktus torasikus.
- **Penjelasan umum** untuk sebagian besar pembuluh darah, otot dan saraf di luar struktur utama, serta kelompok kelenjar getah bening; nama Inggris dari file sumber masih dipakai di banyak tempat.
- **Pengelompokan otomatis**: daerah pembuluh dan kelenjar getah bening, serta pemisahan otot dan saraf dari berkas sumber, ditentukan dari pola nama dan posisi. Beberapa struktur di perbatasan mungkin masuk kelompok yang kurang tepat.
- **Kualitas model**: rangka, otot, saraf, pernapasan, dan pencernaan telah disederhanakan; detail halus berkurang dibanding model aslinya.
- **Verifikasi konten**: teks anatomi disusun dengan bantuan AI dan belum ditinjau oleh pakar anatomi atau klinisi. Periksa dengan sumber rujukan sebelum dipakai untuk pengajaran resmi.
- **Performa**: layer pembuluh kepala-leher (arteri) berukuran sekitar 16 MB dan sekitar 1,3 juta segitiga; pada perangkat lawas bisa terasa berat. Label hover dimatikan otomatis pada layer yang sangat padat.

## Kredit

- **[Z-Anatomy](https://github.com/Z-Anatomy)** — sumber model 3D (seluruh atlas dalam format Blender/OBJ), dilisensikan [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Repositori yang relevan: *Models-of-human-anatomy* dan *The-blend*.
- **BodyParts3D** — © The Database Center for Life Science (DBCLS), Jepang. Basis data model 3D yang menjadi dasar Z-Anatomy. Halaman unduhan resmi: <https://dbarchive.biosciencedbc.jp/en/bodyparts3d/download.html>.
- **[three.js](https://threejs.org/)** — pustaka rendering 3D (lisensi MIT), termasuk `OrbitControls`.
- **Terminologia Anatomica** — standar internasional penamaan struktur anatomi yang menjadi rujukan penamaan Latin.
- **Claude (Anthropic)** — asisten AI yang membantu perancangan, pengodean, skrip pengolah data, dan penulisan teks anatomi dalam proyek ini.

Teks atribusi yang disarankan untuk dicantumkan di situs atau slide:

> Model 3D: BodyParts3D © The Database Center for Life Science, melalui Z-Anatomy (CC BY-SA 4.0), telah diolah dan disederhanakan untuk web.

## Lisensi

**Ringkasan:** kode aplikasi berlisensi **MIT**; data model 3D dan teks anatomi berlisensi **CC BY-SA 4.0**. Berkas lisensi: [`LICENSE`](LICENSE) (MIT, akar repo), [`data/LICENSE`](data/LICENSE) (teks lengkap CC BY-SA 4.0), dan [`data/NOTICE.md`](data/NOTICE.md) (asal data, perubahan, atribusi).

| Komponen | Lisensi | Catatan |
|---|---|---|
| Model 3D (`data/`) | **CC BY-SA 4.0** (turunan Z-Anatomy dan BodyParts3D) | Wajib mencantumkan atribusi dan membagikan karya turunan dengan lisensi yang sama (*share-alike*). Model di sini sudah diseleksi, dideduplikasi, dikuantisasi, dan sebagian disederhanakan, sehingga termasuk karya turunan. |
| Kode aplikasi (logika di `index.html`, `tools/`) | **MIT** | Berkas `LICENSE` di akar repo. Hanya mencakup kode, bukan data model atau teks anatomi. |
| Teks deskripsi dan terjemahan (di dalam `index.html`) | **CC BY-SA 4.0** | Selaras dengan lisensi data model. Teks tertanam di `index.html` bersama kode, sehingga file itu memuat dua lisensi: logika kode MIT, teks anatomi CC BY-SA 4.0. |
| three.js | MIT | Dimuat dari CDN. |

### Ketentuan lisensi sumber (Z-Anatomy)

Lisensi: [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).

> With regard to this content, you are licensed to:
> * freely access part or whole of this database, and acquire data;
> * freely redistribute part or whole of the data from this database;
> * and freely create and distribute database and other derivative works based on part or whole of the data from this database, under the license, as long as you comply with the following conditions:
> * You must attribute this database in the manner specified by the author or licensor when distributing part or whole of this database or any derivative work.
> * You must distribute any derivative work based on part or whole of the data from this database under the same license.

Artinya untuk proyek ini:

- Kamu **boleh** mengakses, mendistribusikan ulang, dan membuat karya turunan dari data model.
- **Atribusi wajib** dicantumkan sesuai cara yang ditentukan pemilik lisensi saat mendistribusikan data atau karya turunan. Kutipan di atas tidak merinci format atribusinya, jadi periksa README atau halaman resmi Z-Anatomy untuk format yang diminta. Teks atribusi di bagian [Kredit](#kredit) adalah usulan awal.
- **Karya turunan harus memakai lisensi yang sama** (CC BY-SA 4.0). Folder `data/` di repositori ini adalah karya turunan, sehingga harus dilisensikan CC BY-SA 4.0.

Hal yang perlu diperhatikan:

1. **Lisensi per bagian di sumber.** Untuk BodyParts3D, atribusi yang diminta pada versi 4.0 berbunyi: *"BodyParts3D, © The Database Center for Life Science licensed under CC Attribution 4.0 International"*; versi lama memakai CC BY-SA 2.1 Japan. Z-Anatomy menyatakan CC BY-SA 4.0 (lihat ketentuan di atas). Namun saya sempat menemukan laporan bahwa **sebagian struktur berlisensi non-komersial** (misalnya ginjal dan telinga dalam); ini belum saya verifikasi sendiri dan tidak disebut dalam kutipan README di atas. Ginjal dipakai pada sistem urinari proyek ini. Sebelum penggunaan komersial, cek lisensi per model di repositori Z-Anatomy.
2. **Lengkapi berkas lisensi.** Pastikan `LICENSE` (MIT) sudah berisi tahun dan nama pemegang hak cipta yang benar, dan `data/LICENSE` berisi teks lengkap CC BY-SA 4.0 yang disalin dari situs Creative Commons.
3. **Pertahankan atribusi** di situs (misalnya pada footer atau panel info) dan di README.

---

*Dibuat untuk tujuan edukasi. Jika menemukan kesalahan anatomi atau penamaan, silakan buka issue atau kirim koreksi.*
