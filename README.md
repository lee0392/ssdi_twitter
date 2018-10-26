# Twitter api analysis

## Working of the given python program is as follows:

1. Get access token, access secret, consumer key, consumer secret from twitter
api.

2. Get Inputs (keyword, to date, from date, number of tweets) from user.

3. Configure tweepy object using the keys defined in step 1.

4. Using api.search, list of tweets are retrieved containing the keyword and
between to and from date

5. Iterate through tweets using tweepy.Cursor.

Uses:

- We can use this code to get a list of tweets. Along with the tweet, the api will also
return name of the person responsible for tweet, his followers count, retweet count,
tweet time.
http://docs.tweepy.org/en/v3.5.0/api.html

- The code can be used to detect active twitter followers and members.

- It can also be used to find fake twitter holders

- It can be used to find inactive users

- It can be useful for the administrator to delete users who are inactive on
twitter

- It can be used to send offer or update related emails to users who are often
active on twitter
