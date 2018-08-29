#Armazenando os tweets capturados no mongodb#
from textblob import TextBlob as tb
from pymongo import MongoClient
import tweepy
import sys

connect = MongoClient('127.0.0.1')
db = connect['tweets_python']

consumer_key = 'YOUR KEY'
consumer_secret = 'YOUR SECRET KEY'

access_token = 'YOUR TOKEN'
access_token_secret = 'YOUR SECRET TOKEN'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

public_tweets = tweepy.Cursor(api.search, q=sys.argv[1],lang="pt",tweet_mode="extended").items(int(sys.argv[2]))


for tweet in public_tweets:
   db.tweets.insert(tweet._json)
   #print(tweet.full_text)
   print("Registro Inserido com sucesso !!")
