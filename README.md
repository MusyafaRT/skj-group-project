# Tugas Kelompok Praktikum SKJ

|||
|--------------------------------|------------------|
|Ronggo Tsani Musyafa            |21/473988/PA/20449|
|Rhazes Wahyu Ramadhan Setiawan  |21/479159/PA/20783|
|Faiz Unisa Jazadi               |21/475298/PA/20563|

## Rencana

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

### Protokol

|Description|Client request|Server response|
|---|---|---|
|Tambah agenda|`add <data:iso-8601> <event name>`|`OK` or `ERROR`|
|Hapus agenda|`del <date> [<event name keyword>]`|`OK` or `ERROR`|
|Tampilkan agenda|`list`|``


### Model Koneksi

Pilihan:

1.  Satu koneksi untuk satu command (koneksi ditutup tiap command)
    -   Kelebihan: tidak harus repot maintain koneksi supaya terus terbuka
    -   Kekurangan: mungkin kesannya lebih boros (tapi sebenarnya tidak juga
        karena diasumsikan aplikasi tidak di-refresh 5 juta kali tiap detik)
2.  Satu koneksi bisa menjalankan banyak command (satu sesi tidak langsung
    ditutup setelah satu command)
    -   Kelebihan: lebih cepat secara performa (walaupun mungkin tidak terasa
        signifikan bedanya)
    -   Kekurangan: sulit memastikan status koneksi agar selalu established

### Database (Server)

Pilihan:

1.  MySQL
    -   Kelebihan: cool aja
    -   Kekurangan: capek, ribet, kesannya mempersulit
2.  Text file: simple dan murah
    -   Kelebihan: file tersimpan, sederhana karena data juga sederhana
    -   Kekurangan: sulit di-manage (tapi untuk apa di-manage? :D)
3.  Memory
    -   Kelebihan: jauh lebih simple daripada file karena data hanya disimpan di
        memory
    -   Kekurangan: kalau server ditutup, data hilang
