import tweepy
from tweepy import OAuthHandler
 
consumer_key = '8AJLxl8YdVQwKsByCQFWvLuwj'
consumer_secret = 'FaTgO1j2RhT6IQ0qsrOuw0gQRMUQYE6oN2XjpEoAE82urgQiw8'
access_token = '386460129-sLTrNtYm5P1BY0ZaJX1py5f91Bwa3XTdpb7v7t9Z'
access_secret = 'WkqG2SFO2K305FJu7Fui51m4jhhQ4pHoUoPx0XSzqnk86'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
fo = open('D:/GitHub/SentimentAnalysisProto/tweets.txt', 'w')
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    fo.write(status.text+"\n")

fo.close()