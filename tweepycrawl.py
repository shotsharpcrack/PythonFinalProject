from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.


ckey = 'nuvV3gdnxdLW2vdL2esrgqFhM'
csecret = 'lookE9GOqSTpsZJmB530ie4qBaSN3AlxDFSTSKRUGm3vfXSWvw'

atoken = '787120483816857601-VGlu5mkfgDq1Dhz053yGW2WN8LJ1RSr'
asecret = 'NQr4DvxxIJBGGy73uwXsPJ68JzaUjX3ZBsPOYvR0rjUpn'

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)	
        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)
        print(tweet, sentiment_value, confidence)
        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])
