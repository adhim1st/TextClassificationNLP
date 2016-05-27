from textblob import TextBlob
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from stopword import get_stop

factory = StemmerFactory()
stemmer = factory.create_stemmer()

stop_words = set(get_stop())

def get_berita(url):
    teks = """

    """
    fo = open(url)

    teks = fo.read()

    fo.close()

    return teks

def stem_words(url,type="text"):

    if type != "text":
        output = get_berita(url)
    else:
        output = url

    sentence2 = TextBlob(output.lower())

    word_token = sentence2.words

    filtered_sentence = []

    for w in word_token:
        w = stemmer.stem(w)
        if w not in stop_words:

            filtered_sentence.append(w)

    print(" ".join(filtered_sentence), "\n")


    return " ".join(filtered_sentence)