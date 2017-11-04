import win32com.client as wincl
import pymysql
import tweepy

speak = wincl.Dispatch("SAPI.SpVoice")

db = pymysql.connect(host="localhost", user="root", passwd="*********", db="tweet")
cur = db.cursor()

CONSUMER_KEY = 'YOUR_CONSUMER_KEY'
CONSUMER_SECRET = 'YOUR_CONSUMER_SECRET'

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
ACCESS_TOKEN_SECRET = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

USER = 'deadmau5'

def is_tweet_read(ID):
    """
    - Checks if the tweet ID is in the database.
    """
    done = cur.execute("SELECT * FROM IDs where tweet_ID = \"{}\"".format(ID))
    if done == 1:
        return True
    else:
        return False

def add_to_db(ID):
    """
    - Adds the tweet ID to the database.
    """
    try:
        cur.execute("INSERT INTO IDs VALUES(\"{}\")".format(ID))
        db.commit()
    except:
        db.rollback()

while True:
    user = api.get_user(USER)
    status = user.status
    if is_tweet_read(status.id) == False:
        speak.Speak(status.text)
        add_to_db(status.id)

db.close()
