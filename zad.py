import enchant
import json

def what_lang(text_in):
    # paste all files from .\dicts to
    # \.Python\site-packages\enchant\data\mingw64\share\enchant\hunspell
    with open("dicts.json") as f:
        dicts = json.load(f)
    res = {}

    text = "hello gutten morgen Schmetterling cześć"
    text = text_in

    for word in text.split(' '):
        res[word] = []

    for lang in dicts:
        d = enchant.Dict(lang)
        for word in res.keys():
            if d.check(word):
                res[word].append(lang)
    return(res)
