import tweepy, time, os
from image import create_image
from kanjiAPI import getKanji
from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()



CONSUMER_KEY = os.environ.get('TWITTER_API_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_API_SECRET_KEY')
ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


@sched.scheduled_job('cron', hour=20)
def schedule_tweet():
    kanji = getKanji()

    tweet = f"""
Kanji of the day:   {kanji['character']}

Meanings: {kanji['meaning']}

Example: {kanji['japanese_example']}
Meaning: {kanji['english_example']}

#japaneselanguage  #nihongo #日本語勉強中 #kanji #learnjapanese #日本語
    """    
    
    create_image(kanji)
    api.update_with_media('Kanji.jpg', tweet)
    os.remove('Kanji.jpg')

sched.start()


