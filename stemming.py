from Sastrawi.Stemmer.StemmerFactory import StemmerFactory


factory = StemmerFactory()
stemmer = factory.create_stemmer()


sentence = """Polresta Palembang Bekuk 4 Pria Bejat yang Perkosa ABG Pekanbaru - Polresta Palembang menangkap empat pria ABG (Anak Baru Gede) dalam kasus dugaan perkosaan. Korbannya merupakan ABG yang dikenal lewat jaringan sosial di facebook (FB).

Demikian disampaikan Kasat Reskrim Polresta Palembang, Kompol Maruly Pardede kepada detikcom, Senin (7/3/2016). Maruly menjelaskan, korbannya ABG usia 16 tahun warga Palembang. Sedangkan pelakunya, ada empat pria ABG juga yakni, NS (17), RS (18), KS (18), dan RA (17).

"Para pelaku memperkosa korban secara bergiliran. Mereka sudah kita amankan," kata Maruly.

Kasus perkosaan ini bermula dari perkenalan korban dengan tersangka NS (17) melalui FB. Terjadi hubungan asmara. Pada 2 Maret 2016, NS dan korban janjian bertemu. NS menyuruh rekannya RS menjemput korban di warnet. Dari sana, korban dibawa ke Jl Sosial Palembang. Mereka berbonceng tiga dengan motor.

Mereka nongkrong di sebuah mes cucian mobil. NS memaksa korban untuk melakukan hubungan seks. Setelah NS melampiaskan nafsunya, dia menyuruh temannya RA untuk melakukan hal yang sama termasuk rekannya KS.

"Kasus perkosaan ini dilaporkan orangtua korban. Atas laporan itu kita lantas melakukan penyelidikan keberadaan para pelaku," kata Maruly.

Usai melampiaskan nafsu, pelaku merampas HP korban. "HP itu mereka jual dengan harga Rp400 ribu. Sekarang empat tersangka lagi menjalani pemeriksaan lebih lanjut," tutup Maruly."""

renum = ''.join([i for i in sentence if not i.isdigit()])

output = stemmer.stem(renum)
print(output)


