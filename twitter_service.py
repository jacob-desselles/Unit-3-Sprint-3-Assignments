import os
from dotenv import load_dotenv
from tweepy import OAuthHandler, API

load_dotenv()
#Since I still haven't been approved for Twitter development,
#All I could do is input the methods that I would normally use.
TWITTER _API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

auth = OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN,TWITTER_ACCESS_TOKEN_SECRET)

api= tweepy.API(auth)
print("API CLIENT:", api)
user = api.get_user("LacesShoe")
print("TWITTER USER:", user)
print(user.id)
print(user.screen_name)
print(user.name)
breakpoint()