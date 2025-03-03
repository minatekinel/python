meme_dict = {
            "CRINGE": "UTANDIRICI BİR ŞEY",
            "LOL": "KOMİK BİR ŞEY",
            "CREEPY":"KORKUTUCU",
            }
word = input("anlamadığım kelime")

if word in meme_dict.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(meme_dict[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Böyle bir kelime yok !")
