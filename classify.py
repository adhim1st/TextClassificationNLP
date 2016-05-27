from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import training
import timeit
from stemstop import stem_words

factory = StemmerFactory()
stemmer = factory.create_stemmer()

cl = NaiveBayesClassifier(training.train)

print("akurasi data training %f\n" %cl.accuracy(training.test))

text = """Jombang - Nurul Huda (47), pria asal Kelurahan Kranggan, Kecamatan Prajurit Kulon, Kota Mojokerto ini diringkus polisi lantaran diduga mencabuli, menyiksa, dan memeras seorang santri di sebuah pondok pesantren di Jombang. Untuk melancarkan aksinya, tersangka menyamar menjadi putra kiai (biasa dipanggil Gus) yang bisa mengajarkan ilmu kebatinan kepada korban.

Kasat Reskrim Polres Jombang AKP Wahyu Hidayat mengatakan korban adalah remaja laki-laki asal Kabupaten Malang yang merupakan santri. Sementara tersangka juga biasa mengaji di pondok pesantren itu.

Perbuatan bejat Nurul bermula pada 2014 lalu. Saat itu, korban berusia sekitar 16 tahun atau masih di bawah umur. Kepada korban, pria yang sehari-hari berjualan pulsa ini mengaku sebagai putra kiai dan biasa dipanggil Gus Nurul.

"Korban diajak tersangka ke musala di dekat pondok. Saat kondisi sepi dan hanya berdua dengan korban, tersangka mencabuli korban," kata Wahyu kepada wartawan, Minggu (20/3/2016).

Lantaran menganggap Nurul sebagai Gus, korban pun tak berani menolak permintaan tersangka. Terlebih lagi, tersangka membujuk korban bahwa perbuatan cabul itu untuk memasukkan ilmu kebatinan ke tubuh korban.

"Tersangka berdalih untuk mengajari korban ilmu tasawuf. Nyatanya itu hanya untuk memuluskan niat tersangka agar bisa mencabuli korban," ungkapnya.

Menurut Wahyu, perbuatan cabul itu dilakukan tersangka kepada korban berulang kali selama 2 tahun terakhir. Bahkan korban diminta membayar uang kepada tersangka setiap kali usai melakukan pencabulan. Nilainya antara Rp 200.000 hingga jutaan rupiah.

"Tersangka juga meminta uang dari korban berulang kali. Total kerugian korban Rp 40 juta," sebutnya.

Tak tahan dengan perbuatan Nurul, lanjut Wahyu, korban pun memutuskan buka mulut ke teman sesama santri. Mendapat dukungan dari teman-temannya, korban memberanikan diri melapor ke Polres Jombang, Kamis (17/3).

Pada hari yang sama, polisi memutuskan menjebak tersangka. "Saat korban menyerahkan uang yang terakhir kepada tersangka, saat itu tersangka langsung kami tangkap," jelasnya.

Akibat perbuatannya, kini Nurul harus mendekam di Rutan Polres Jombang. Tersangka dijerat dengan Pasal 80 ayat (1) juncto Pasal 82 ayat (1) UU RI No 35 Tahun 2014 tentang Perlindungan Anak dengan ancaman pidana maksimal 15 tahun penjara.

"Kalau ada yang merasa menjadi korban perbuatan tersangka ini, jangan malu melapor, akan kami jaga identitasnya. Karena itu bisa memberatkan tersangka," pungkasnya. """

tic = timeit.default_timer()
renum = ''.join([i for i in text if not i.isdigit()])
text = stem_words(renum)
print("text diatas setelah diklasifikasi yaitu %s\n" % cl.classify(text))
toc = timeit.default_timer()
print ("waktu klasifikasi : ")
print(toc-tic)

print(cl.show_informative_features(20))
# classifier = TextBlob(stemstop_output, classifier=cl)
# print(classifier.classify())

