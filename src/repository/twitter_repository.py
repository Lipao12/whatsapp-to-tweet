import tweepy

class TwitterRepository:
    def __init__(self, client:tweepy.Client, api:tweepy.API) -> None:
        self.client = client
        self.api = api
    
    def tweet_with_image(self, message:str, image_path:str):
        try:
            media = self.api.media_upload(image_path)
            
            response = self.client.create_tweet(text=message,
                                media_ids=[media.media_id])
            print("Twetted Successfully!")
            print(f"https://twitter.com/user/status/{response.data['id']}")
        except Exception as exception:
            print("Erro ao fazer o tweet: ", str(exception))
                  
    def tweet_with_text(self, message:str):
        try:
            response = self.client.create_tweet(
                text=message
            )
            print("Twetted Successfully!")
            print(f"https://twitter.com/user/status/{response.data['id']}")
        except Exception as exception:
            print("Erro ao fazer o tweet: ", str(exception))
