import tweepy
import time

ACCESS_TOKEN = '964881732901142530-pcD6zkE3JVgoySgHbH6P7Q6AIQ61EKD'
ACCESS_SECRET = '3W1kfjhUpRWmg8GEs5DjXTSCirtuDXWoSiWwCscQrAZM9'
CONSUMER_KEY = 'WsWFWwk0c07oMdXWovQKVoA3g'
CONSUMER_SECRET = 'rVDyLDBLzTHlnO8uqixmfEg8KagNMqWRnPsXcqJIkdCrdxRczb'

#list(tweepy.Cursor(api.search, q=query, result_type='recent').items(limit))

SEARCH=input("Enter the search string ")
FROM=input("Enter the from date (YYYY-MM-DD format) ")
TO=input("Enter the to data (YYYY-MM-DD format) ")
INPUT_FILE_PATH= './'+SEARCH+'.txt'

num=int(input("Enter the number of tweets you want to retrieve for the search string "))
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
i=0;

f = open(INPUT_FILE_PATH, 'w', encoding='utf-8')

#for res in tweepy.Cursor(api.search, q=SEARCH, rpp=100, count=20, result_type="recent", since = FROM,until =TO, lang="en").items(num):
for res in tweepy.Cursor(api.search, q=("{}&since:{}&until:{}").format(SEARCH,FROM,TO), rpp=100, count=20, result_type="recent", include_entities=True, lang="en").items(num):
#for res in tweepy.Cursor(api.search, q=SEARCH, result_type="recent", lang="en").items(num):
	i+=1
	f.write(res.user.screen_name)
	f.write(' ')
	f.write('[')
	f.write(res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z"))
	f.write(']')	
	f.write(" ")
	f.write('"')
	f.write(res.text.replace('\n',''))
	f.write('"')
	f.write(" ")
	f.write(str(res.user.followers_count))
	f.write(" ")
	f.write(str(res.retweet_count))
	f.write('\n')
f.close
print("Tweets retrieved ",i)