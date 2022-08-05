# Get tweets for one user at time
# Luan Santos
# 05-08-2022

import tweepy
import pandas as pd

bearer_token = 'replace here'

client = tweepy.Client(bearer_token=bearer_token)

# Username for user you searching for
username = 'elonmusk'

user = client.get_users(usernames=username)

# Saving the id for user
id = user.data[0].data['id']

# getting the latest 100 tweets excluding retweets
tweets = client.get_users_tweets(id=id, max_results=100,
                                 tweet_fields=['created_at', 'lang'],
                                 expansions=['author_id'],
                                 exclude='retweets')

# saving on dataframe
data = []
columns = ['time', 'tweet']

for tweet in tweets.data:
    data.append([tweet.created_at, tweet.text])

df = pd.DataFrame(data, columns=columns)
df['username'] = username

df.head()

