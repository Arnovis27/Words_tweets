﻿import tweepy
from tweepy import OAuthHandler
import csv
from os import remove
from os import path

consumer_key= "Your keys.."
consumer_secret= "Your keys.."
access_token= "Your Token.."
access_token_secret= "Your Token.."

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit= True, wait_on_rate_limit_notify=True)


places = api.geo_search(query="Colombia", granularity="country")
place_id = places[0].id  
searchTerms= "#Covid -filter:retweets"

if path.exists("./data/twitter.csv"):
    remove('./data/twitter.csv')

# Open/create a file to append data to
csvFile = open('./data/twitter.csv', 'a',encoding="utf_8_sig")

#Use csv writer
csvWriter = csv.writer(csvFile, lineterminator="\n",delimiter=";")

print("\nIniciando Guardado...")

for tweet in tweepy.Cursor(api.search, 
                        q='{} place:{}'.format(searchTerms, place_id), 
                        since = "2020-10-01", #actualiza fechas cada cierto tiempo
                        until = "2020-11-16",
                        lang = "es").items(200):
    #print(tweet.created_at, tweet.text,tweet.place.name)
    csvWriter.writerow([tweet.created_at, tweet.text])

print("\n¡Guardado!\n")
csvFile.close()