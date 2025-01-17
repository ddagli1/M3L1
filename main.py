from flask import Flask
import random

# Flask uygulaması başlatılıyor
app = Flask(__name__)

# İlginç gerçekleri bir liste içinde topladık
facts_list = [
    "Elon Musk, sosyal ağların içeriği görüntülemek için mümkün olduğunca fazla zaman harcamamız için bizi platformun içinde tutmak üzere tasarlandığını iddia ediyor.",
    "2018 yılında yapılan bir araştırmaya göre 18-34 yaş arası kişilerin %50'den fazlası akıllı telefonlarına bağımlı olduğunu düşünüyor.",
    "Sosyal ağların olumlu ve olumsuz yanları var ve bu platformları kullanırken her ikisinin de farkında olmalıyız.",
    "Teknoloji bağımlılığı çalışması, modern bilimsel araştırmanın en alakalı alanlarından biridir."
]

# Ana sayfa: Ziyaretçilere bir hoş geldiniz mesajı gösteriliyor
@app.route("/")
def index():
    return f'<h1>Teknolojik bağımlılıklar hakkında birkaç ilginç gerçeği öğrenebilirsiniz!</h1><a href="/rastgele_gercek">İlginç Gerçekler</a>'

# Rastgele bir gerçeği kullanıcıya gösteren sayfa
@app.route("/rastgele_gercek")
def facts():
    # Listeden rastgele bir gerçek seçiliyor
    return f'<p>{random.choice(facts_list)}</p><a href="/">Ana Sayfa</a>'

# Uygulama başlatılıyor
app.run(debug=True)  # Debug modu: Hataları hızlıca görmek ve düzeltmek için açık tutuluyor
