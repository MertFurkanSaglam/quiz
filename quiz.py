sorular = [
    "Geleneksel dans türü 'Hula' ile ünlü olan ülke hangisidir? \nA) Japonya \nB) Hawaii \nC) Meksika \nD) Hindistan\n\n",
    "Brezilya'da kutlanan ünlü karnavalın adı nedir? \nA) Ölüler Günü \nB) Oktoberfest \nC) Mardi Gras \nD) Diwali\n\n",
    "Hangi tarihi anıt, Mugal İmparatoru Şah Cihan'ın eşi için bir mezar olarak inşa edilmiştir? \nA) Çin Seddi \nB) Eyfel Kulesi \nC) Tac Mahal \nD) Giza Piramitleri\n\n",
    "Hangi şehir genellikle 'Aşk Şehri' olarak adlandırılır ve romantik atmosferiyle ünlüdür? \nA) Paris \nB) Venedik \nC) New York \nD) Rio de Janeiro\n\n",
    "Hangi Afrika ülkesi, vahşi yaşamıyla ünlüdür ve 'Büyük Beş' - aslan, fil, bufalo, leopar ve gergedan - ev sahibidir? \nA) Mısır \nB) Kenya \nC) Güney Afrika \nD) Nijerya\n\n"
]

cevaplar = ["B", "C", "C", "A", "B"]

doğru_cevaplar = 0
yanlış_cevaplar = 0

for i in range(len(sorular)):
    cevap = input(sorular[i])
    if cevap.upper() == cevaplar[i]:
        print("Cevabınız doğru\n")
        doğru_cevaplar += 1
    else:
        print("Cevabınız yanlış. Doğru cevap: {}\n".format(cevaplar[i]))
        yanlış_cevaplar += 1

print("Doğru cevap sayısı:", doğru_cevaplar)
print("Yanlış cevap sayısı:", yanlış_cevaplar)
