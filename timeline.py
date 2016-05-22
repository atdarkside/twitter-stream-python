#coding: UTF-8
import tweepy
import setting
from datetime import timedelta

class Listener(tweepy.StreamListener):
    def on_status(self, status):
        status.created_at += timedelta(hours=9)
        print("--------------------------------------")
        print(status.text)
        print(u"{name}({screen}) {created} via {src}\n".format(
            name=status.author.name, screen=status.author.screen_name,
            created=status.created_at, src=status.source))
        return True
        def on_error(self, status_code):
            print('Got an error with status code: ' + str(status_code))
            return True
        def on_timeout(self):
            print('Timeout...')
            return True
auth = tweepy.OAuthHandler(setting.CK,setting.CS)
auth.set_access_token(setting.AT,setting.AS)

listener = Listener()
stream = tweepy.Stream(auth, listener)
stream.userstream()
