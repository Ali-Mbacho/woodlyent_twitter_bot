import tweepy
from enum import Enum
import os


class Config(Enum):
    consumer_key = os.environ['CONSUMER_KEY'] = "CONSUMER_KEY"
    consumer_secret = os.environ['CONSUMER_SECRET'] = "CONSUMER_SECRET"
    key = os.environ['KEY'] = "KEY"
    secret = os.environ['SECRET'] = "SECRET"





def authenticate_api():
    auth = tweepy.OAuthHandler(Config.consumer_key, Config.consumer_secret)
    auth.set_access_token(Config.key, Config.secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api
    
FILE_NAME = "last_seen_id.txt"

def retrive_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(file_name, last_seen_id):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

last_seen_id = retrive_last_seen_id(FILE_NAME) 

def auto_retweet():
    public_tweets = authenticate_api.home_timeline(last_seen_id, tweet_mode = 'extended')
    for tweet in reversed(public_tweets):
        try:
            print(str(tweet.id) + '--' + tweet.full_text)
            # last_seen_id = tweet.id
            authenticate_api.retweet(tweet.id)
            authenticate_api.create_favorite(tweet.id)
            store_last_seen_id(file_name, tweet.id)
        except tweepy.TweepError as e:
            print(e.reason)