# Getting tweets using snscrape

# run on terminal: pip install snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd

# setting the query, empty list and limit of tweets
query = '(from:elonmusk) until:2020-01-01 since:2010-01-01'
tweets = []
limit = 5000

# loop for tweets
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

# saving on dataframe
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])

# saving dataframe on csv file
df.to_csv('maytweets.csv', index=False, encoding='utf-8-sig')
