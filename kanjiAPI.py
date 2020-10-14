import requests
import os
import random

def getKanji():
    url = "https://kanjialive-api.p.rapidapi.com/api/public/kanji/all"

    headers = {
        'x-rapidapi-host': "kanjialive-api.p.rapidapi.com",
        'x-rapidapi-key': os.environ.get('KANJI_API_KEY')
        }
    response = requests.request("GET", url, headers=headers)
    response_json_raw = response.json()
    rand_num = random.randint(0, len(response_json_raw))
    response_json = response_json_raw[rand_num]
    response_kanji = response_json['kanji']
    response_ex_JP = response_json['examples'][0]['japanese']
    response_ex_EN = response_json['examples'][0]['meaning']['english']
    kanji = {
        "character": response_kanji['character'],
        "meaning":  response_kanji['meaning']['english'],
        "onyomi": response_kanji['onyomi']['katakana'].replace("'","").replace("n/a","None").split('、'),
        "kunyomi": response_kanji['kunyomi']['hiragana'].replace("'","").replace("n/a","None").split('、'),
        "japanese_example": response_ex_JP,
        "english_example": response_ex_EN
    }
    #Transform list into string for multimedia 
    kanji['onyomi'] = ' \n \n'.join(kanji['onyomi'][0:3]) 
    kanji['kunyomi'] = ' \n \n'.join(kanji['kunyomi'][0:3])
    return kanji

#print(getKanji())
