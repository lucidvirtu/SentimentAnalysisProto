import tweepy
from tweepy import OAuthHandler
import cleaner as cl
import classify as cs
import matplot as res
 
consumer_key = ''
consumer_secret = ''
access_token = '386460129-'
access_secret = ''
 

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)


def tweet_ret(keyword):
	k = keyword+" -filter:retweets"
	tweetfile = open("raw_data.txt", "w")
	#csvWriter = csv.writer(csvFile)

	for tweet in tweepy.Cursor(api.search, q=k, lang="id").items(50):
		text = tweet.text.encode('unicode_escape', errors='replace')
		text2 = text.decode('utf8', errors='ignore')
		text3 = text2.replace('\\n', ' ')
		text4 = str(text3)
		tweetfile.write(text4+'\n')
		#csvWriter.writerow([text2])
		print (tweet.id)

	tweetfile.close()
	#except tweepy.TweepError as tpp:
	#print (str(tpp))
def exec(a):
	tweet_ret(a)
	cl.exec_clean()
	cl.exec_stop()
	cs.classifier()
	res.plot(a)
#exec()










