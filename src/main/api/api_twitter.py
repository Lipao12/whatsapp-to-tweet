import os
from dotenv import load_dotenv
import tweepy
load_dotenv()

client = tweepy.Client(bearer_token=os.getenv("BEARER_TOKEN"))
client = tweepy.Client(consumer_key=os.getenv("API_KEY"), consumer_secret=os.getenv("API_KEY_SECRET"), 
                       access_token=os.getenv("ACCESS_TOKEN"), access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"))

auth = tweepy.OAuthHandler(os.getenv("API_KEY"), os.getenv("API_KEY_SECRET"))
auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
api = tweepy.API(auth)