import tweepy
import csv
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
 
consumer_key = '8AJLxl8YdVQwKsByCQFWvLuwj'
consumer_secret = 'FaTgO1j2RhT6IQ0qsrOuw0gQRMUQYE6oN2XjpEoAE82urgQiw8'
access_key = '386460129-sLTrNtYm5P1BY0ZaJX1py5f91Bwa3XTdpb7v7t9Z'
access_secret = 'WkqG2SFO2K305FJu7Fui51m4jhhQ4pHoUoPx0XSzqnk86'

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print (("getting tweets before %s") % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print (("...%s tweets downloaded so far") % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["text"])
		writer.writerows(outtweets)
	
	pass



x = input("Input the name of a Tweet user: ")
get_all_tweets(x)