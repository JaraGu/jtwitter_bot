import tweepy

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)  # Api key = consumer_key , Api secret key = consumer_secret


api = tweepy.API(auth)

myself = api.verify_credentials()
print(myself.name)  # prints your name.
print(myself.screen_name)  # prints your twitter handle
print(myself.followers_count)

# print out all the followers of our account
for follower in (tweepy.Cursor(api.get_followers).items()):
    if follower.name == 'Usernamehere':
        print(follower.name)
    
