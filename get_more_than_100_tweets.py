# getting more than 100 tweets
import tweepy
import pandas as pd

# setting access tokens to twitter api
bearer_token = 'replace here'

client = tweepy.Client(bearer_token=bearer_token)

# Username for user you searching for
username = 'elonmusk'

user = client.get_users(usernames=username)

# Saving the id for user
id = user.data[0].data['id']

tweets = []

for tweet in tweepy.Paginator(client.get_users_tweets,
                              id=id, max_results=100,
                              tweet_fields=['created_at'],
                              exclude='retweets').flatten(limit=1000):
    tweets.append(tweet.data)

# saving on dataframe
data = []
columns = ['time', 'tweet']

for tweet in tweets[:]:
    data.append([tweet['created_at'], tweet['text']])

df = pd.DataFrame(data, columns=columns)

df['username'] = username

df.head()
