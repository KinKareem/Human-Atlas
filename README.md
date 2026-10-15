# Atlas Anatomi Manusia (3D)

Website pembelajaran anatomi tubuh manusia dengan model 3D interaktif: putar, zoom, klik langsung pada struktur, sorot atau isolasi, filter sisi kanan atau kiri, tema terang dan gelap.

## Isi

| Tab / sistem | Keterangan |
|---|---|
| Rangka | 277 struktur tulang dan tulang rawan (159 jenis), nama Indonesia, Latin, Inggris, dan deskripsi |
| Otot | 211 kelompok otot |
| Saraf | 120 kelompok saraf |
| Organ | Pernapasan, pencernaan, reproduksi pria, urinari, endokrin, jantung dan pembuluh besar |
| Organ (pembuluh) | Arteri dan vena per daerah: kepala-leher (arteri dan vena), toraks, abdomen-pelvis, lengan, tungkai |

Data model dimuat per sistem saat dipilih (lazy loading) dari folder `data/`.

## Menjalankan secara lokal

Halaman memuat file `data/*.json` dengan `fetch`, jadi **tidak bisa dibuka langsung lewat `file://`**. Jalankan server statis:

```bash
cd atlas-anatomi
python3 -m http.server 8000
# buka http://localhost:8000
```

## Deploy ke GitHub Pages

1. Push seluruh folder ini ke repositori GitHub.
2. Buka Settings, lalu Pages.
3. Pilih Deploy from a branch, branch `main`, folder `/ (root)`.
4. Tunggu beberapa menit, situs tersedia di `https://<username>.github.io/<repo>/`.

Total data sekitar 60 MB (file terbesar ~16 MB), masih di bawah batas 100 MB per file di GitHub.

## Struktur

```
index.html        aplikasi (HTML, CSS, JS dalam satu file; three.js dari CDN)
data/atlas_*.json model 3D per sistem (base64 + metadata)
tools/            skrip Python untuk mengekstrak dan memadatkan model dari OBJ (referensi)
```

Setiap file data berisi `{ b: <base64 biner>, m: { mn, sc, meta } }`: posisi vertex 16-bit terkuantisasi, indeks segitiga 16-bit, dan daftar mesh. Daftar nama, kelompok, dan teks deskripsi tertanam di `index.html` (konstanta `BL` dan `DET`).

## Sumber model dan lisensi (penting)

- Model 3D berasal dari **Z-Anatomy** (CC BY-SA 4.0), yang diturunkan dari **BodyParts3D** (© The Database Center for Life Science, Jepang).
- Model sudah **diolah** (diseleksi, diduplikasi dibuang, sebagian disederhanakan) untuk web. Karena sifat *share-alike*, karya turunan harus memakai lisensi yang sama dan mencantumkan atribusi.
- **Periksa lisensi per bagian.** Sebagian struktur di Z-Anatomy dilaporkan memakai lisensi non-komersial (misalnya ginjal dan telinga dalam). Sebelum dipakai untuk tujuan komersial, cek ulang syarat di repositori Z-Anatomy.
- three.js: lisensi MIT (dimuat dari CDN).
- Teks deskripsi dan terjemahan ditulis untuk proyek ini dan **bukan pengganti rujukan medis**. Periksa kembali dengan buku teks anatomi sebelum dipakai sebagai bahan ajar resmi.

Sebelum merilis publik, putuskan lisensi untuk kode (misalnya MIT) dan untuk data (CC BY-SA 4.0), lalu tambahkan berkas `LICENSE`. Saya bukan penasihat hukum, jadi pastikan kembali syarat lisensinya.

## Keterbatasan yang diketahui

- Model berasal dari tubuh pria, jadi organ reproduksi wanita belum ada.
- Nama arteri dan vena (tab pembuluh) masih memakai nama Inggris dari file model, dengan penjelasan umum.
- Beberapa struktur tidak ada di model (misalnya ileum, rektum, vena kava superior, nodus SA/AV).
