import tweepy
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


places = api.geo_search(query="COLOMBIA", granularity="country")
place_id = places[0].id  
searchTerms= "#Disney"

if path.exists("./data/twitter.csv"):
    remove('./data/twitter.csv')

# Open/create a file to append data to
csvFile = open('./data/twitter.csv', 'a')

#Use csv writer
csvWriter = csv.writer(csvFile)

print("\nIniciando Guardado...")

for tweet in tweepy.Cursor(api.search, 
                        q='{} place:{}'.format(searchTerms, place_id), 
                        since = "2020-11-01", 
                        until = "2020-11-03",
                        lang = "es").items():
    print (tweet.created_at, tweet.text,tweet.place.name)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

print("\nGuardado Finalizado...")
csvFile.close()