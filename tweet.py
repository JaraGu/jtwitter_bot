import tweepy
import time
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)  # Api key = consumer_key , Api secret key = consumer_secret


api = tweepy.API(auth)

myself = api.verify_credentials()
print(myself.name)  # prints your name.
print(myself.screen_name)  # prints your twitter handle
print(myself.followers_count)

search = "AI"
numberOfTweets = 5


def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.TooManyRequests:
            time.sleep(1000)


# print out all the followers of our account
for follower in limit_handler(tweepy.Cursor(api.get_followers).items()):
    if follower.name == 'Usernamehere':
        print(follower.name)
        follower.follow()

# for retweeting anything based on a keyword
for tweet in tweepy.Cursor(api.search_tweets, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepyException as e:
        print(e)
    except StopIteration:
        break
