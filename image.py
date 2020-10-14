from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import datetime
import random
from colors import pallete




def make_list(kanji, key):
    temp = kanji[key][1:-1].replace("'", '').replace(' ', '')
    temp_list = list(temp.split(","))
    return ' \n \n'.join(temp_list[0:3])


def create_image(kanji):
    rand_pallete =  random.randint(1, 1000) % (len(pallete))
    colors = pallete[rand_pallete]
    now = datetime.datetime.now()
    time = f'{now.day}/{now.month}/{now.year}'


    out = Image.new("RGB", (1500, 1000), colors['background'])
    fnt = ImageFont.truetype("./fonts/MEIRYOB.TTC", 450)
    fnt_title = ImageFont.truetype("./fonts/arial.ttf", 100)
    fnt_kun = ImageFont.truetype("./fonts/ipam.ttf", 50)
    fnt_title_yomi = ImageFont.truetype("./fonts/arial.ttf", 70)


    title = "Kanji of the day"
    key = kanji['character']
    readings_kun =  kanji['kunyomi']
    readings_on = kanji['onyomi']
    kun_title = "Kunyomi"
    on_title = "Onyomi"


    w_kanji, h_kanji = fnt.getsize(key)
    w_title,h_title = fnt_title.getsize(title)
    w_date, h_date = fnt_title_yomi.getsize(time)

    d = ImageDraw.Draw(out)
    d.multiline_text(((1500-w_kanji) / 2.55,75), title, font=fnt_title, fill=colors['title'])
    d.multiline_text(((1500 - w_kanji)/2,(1000 - h_kanji)/3.15), key, font=fnt, fill=colors['kanji'])
    d.multiline_text((150, 375), readings_kun, font=fnt_kun, fill= colors['title'])
    d.multiline_text((125,275), kun_title, font=fnt_title_yomi, fill=colors['kanji'])
    d.multiline_text((1120, 375), readings_on, font=fnt_kun, fill= colors['title'])
    d.multiline_text((1095,275), on_title, font=fnt_title_yomi, fill= colors['kanji'])
    d.multiline_text(((1500-w_date)/1.9 ,700), time, font=fnt_kun, fill= colors['title'])

    out.save('Kanji.jpg', format=None)
    #out.show()

