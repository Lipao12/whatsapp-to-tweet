# docs - https://docs.tweepy.org/en/stable/examples.html
from src.main.api.api_twitter import client, api

# Reposotories
from src.repository.twitter_repository import TwitterRepository

if __name__ == "__main__":
    tweet = TwitterRepository(client, api)
    #tweet.tweet_with_text("#2 tweet from Python")
    tweet.tweet_with_image("#1 tweet from Python - Text and Image", "./mago.jpg")

