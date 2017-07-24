from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


consumer_key = '8AJLxl8YdVQwKsByCQFWvLuwj'
consumer_secret = 'FaTgO1j2RhT6IQ0qsrOuw0gQRMUQYE6oN2XjpEoAE82urgQiw8'
access_token = '386460129-sLTrNtYm5P1BY0ZaJX1py5f91Bwa3XTdpb7v7t9Z'
access_secret = 'WkqG2SFO2K305FJu7Fui51m4jhhQ4pHoUoPx0XSzqnk86'


class listener(StreamListener):

    def on_data(self, data):

        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)

        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])