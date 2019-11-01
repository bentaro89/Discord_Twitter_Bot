import tweepy
import discord

# Tokens for access to APIs
consumer_key = 'EjoZhoTuAeltdj62d019jaaI7'
consumer_secret = 'tt44EZ3FhtsAEl1IhfDlJNOB8dPvgGzR7Z34GdNrVb03JGeCoL'
access_token = '1184124648084180992-gzd0hdQaKwuHwLkJ7RlZucTR16lKym'
access_secret = 'IY4WAwFWojPSm8fxsGcte9tl90S8qMy39fHn8QVTgVjyc'
discord_token = "NjM3MTg2NDkwMTQwNDU5MDA4.Xbu_JA.kYHExrRbTm4Xfchq48AQz0EOr2"

#Function to get access to Twitter API
def OAuth():
    #Inputs tokens to authenticate Twitter Developer account
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth

#Uses twitter API to tweet whatever
def Tweet(ur_tweet):
    api.update_status(ur_tweet)

# Authenticates and connects to the Twitter API
oauth = OAuth()
api = tweepy.API(oauth)

# Creates a client: used to represent a connection to Discord
# Handles events, tracks state, and generally interacts with Discord APIs
client = discord.Client()

# Used to show that it connects to a client
@client.event
async def on_ready():
    # Confirmation that the bot has entered the server and working well!
    print(f'{client.user} has connected to Discord!')


@client.event
#Function that is called everytime a user types something to the bot
async def on_message(message):

    # Makes sure that the author of the message isn't another bot or itself
    if message.author == client.user:
        return

    # Makes sure that the user types 'tweet:" before the message
    if not ('tweet:' or 'Tweet:') == message.content[:6]:
        pass
    else:
        # Tweets the message, but not "tweet:"
        Tweet(message.content[6:])
        await message.channel.send("Your message has been tweeted on @Bot_Dartmouth")

@client.event
# Function that is called every time a member joins
async def on_member_join(member):
    # Directs message the user
    await member.create_dm()

    # Teaches the user know how to tweet and where the tweet can be found
    await member.dm_channel.send(
        f'Hi {member.name}, you are able to tweet on the Twitter account @Bot_Dartmouth. (https://twitter.com/Bot_Dartmouth)'
        f' To tweet, type "tweet:" following whatever you want to tweet.'
    )

# Runs the client using a unique token from the bot
# Token comes from the discord developer website
client.run(discord_token)
