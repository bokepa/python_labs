from __future__ import print_function
import twitter

import keys as keys


# Create an Api instance.
api = twitter.Api(consumer_key=keys.CONSUMER_KEY,
                  consumer_secret=keys.CONSUMER_SECRET,
                  access_token_key=keys.ACCESS_TOKEN,
                  access_token_secret=keys.ACCESS_TOKEN_SECRET)

users = api.GetFriends()

print([u for u in users])

