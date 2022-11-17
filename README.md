---
author:
- 'Ronggo Tsani Musyafa -- `21/473988/PA/20449`'
- 'Rhazes Wahyu Ramadhan Setiawan -- `21/479159/PA/20783`'
- 'Faiz Unisa Jazadi -- `21/475298/PA/20563`'
fontfamily: cmbright
subtitle: Praktikum Sistem Komputer dan Jaringan
title: 'Tugas Kelompok: Konsep Program Socket Programming'
---

# Rencana

Kita ingin membuat aplikasi socket server (dan client) kalender sederhana.
Gambaran sederhana sebagai berikut.

    Kalener v1.0
    2022-11-16 09:58:44

    Agenda
    ======
    2022-11-17 Rapat acara Pengumuman Makomji 2022/2023
    2022-11-18 Pengumuman Makomji 2022/2023
    2022-11-25 Briefing persiapan Outbound OmahTI 2022
    2022-11-25 Lengkapi catatan persiapan UAS 2022 Gasal

    [1] Tambah agenda   [2] Hapus agenda    [3] Refresh

    Masukkan perintah: 1

    > Nama agenda : Print catatan persiapan UAS 2022
    > Tanggal     : 2022-11-30

    Agenda berhasil ditambahkan!

    <sleep 1s>
    <clear screen, then start over>

```{=tex}
\pagebreak
```

## Protokol

  Description        Client request                        Server response
  ------------------ ------------------------------------- -----------------
  Tambah agenda      `add <data:iso-8601> <event name>`    `OK` or `ERROR`
  Hapus agenda       `del <date> [<event name keyword>]`   `OK` or `ERROR`
  Tampilkan agenda   `list`                                Serialized data

## Model Koneksi

Model koneksi yang dipilih adalah satu koneksi digunakan untuk mengirim 1
perintah dan menerima 1 respon.

    <initiate connection>
    -> add 2022-11-11 Briefing Pengumuman Makomji 2022
    <- OK
    <connection closed>

Model koneksi ini dipilih untuk alasan simplisitas -- tidak perlu memastikan
status koneksi di sisi client. Model koneksi ini juga lebih menghemat resource
pada server (client hanya membuka koneksi jika diperlukan).

## Database (Server)

Data agenda disimpan di file teks biasa dengan format tertentu.

    2022-11-10 Agenda 1
    2022-11-09 Agenda 2

Data disimpan dalam bentuk ini karena lebih sederhana dan mudah
diimplementasikan.
