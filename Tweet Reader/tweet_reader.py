import win32com.client as wincl
import tweepy

speak = wincl.Dispatch("SAPI.SpVoice")



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

USER = 'deadmau5'

user = api.get_user(USER)

#speak.Speak(str(user.name))

print((user.name))
