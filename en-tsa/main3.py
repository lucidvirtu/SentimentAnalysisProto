import sys
import os
import tweepy
import csv
import json
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream

consumer_key = '8AJLxl8YdVQwKsByCQFWvLuwj'
consumer_secret = 'FaTgO1j2RhT6IQ0qsrOuw0gQRMUQYE6oN2XjpEoAE82urgQiw8'
access_token = '386460129-sLTrNtYm5P1BY0ZaJX1py5f91Bwa3XTdpb7v7t9Z'
access_secret = 'WkqG2SFO2K305FJu7Fui51m4jhhQ4pHoUoPx0XSzqnk86'
 

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

searchQuery = '#najibrazak'  # this is what we're searching for
maxTweets = 10000000 # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
fName = 'tweetssample.txt' # We'll store the tweets in a text file.


# If results from a specific ID onwards are reqd, set since_id to that ID.
# else default to no lower limit, go as far back as API allows
sinceId = None

# If results only below a specific ID are, set max_id to that ID.
# else default to no upper limit, start from the most recent tweet matching the search query.
max_id = 0

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, lang="id", count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, lang="id", count=tweetsPerQry,
                                            since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, lang="id", count=tweetsPerQry,
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, lang="id", count=tweetsPerQry,
                                            max_id=str(max_id - 1),
                                            since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json, unpicklable=False) +
                        '\n')
            tweetCount += len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break

print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))