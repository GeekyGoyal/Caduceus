import discord
import os
import requests ####
import json #### 
import random
import emoji



#--------------------------------------#
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
worry_gifs = ["Everything will be OK; just relax and take a deep breath.  https://media.giphy.com/media/3o6vXJZlfNfAYysryo/giphy.gif " , "Good things are coming down the road, just don’t stop walking. https://media.giphy.com/media/3o7TKKx1y98UPBkaLC/giphy.gif " , "You can’t calm the storm, so stop trying. What you can do is calm yourself, the storm will pass. https://media.giphy.com/media/45Lg3ECIw25Fe/giphy.gif " , "Tides don’t last forever and when they go, they leave behind beautiful seashells." , "Take a deep breath, and relax, it’s all going to turn out better than you expected. https://media.giphy.com/media/EvYHHSntaIl5m/giphy.gif " , "https://media.giphy.com/media/3M4NpbLCTxBqU/giphy.gif " , "Everything is going to be alright. https://media.giphy.com/media/jMGxhWR7rtTNu/giphy.gif ", "Calm Down! https://media.giphy.com/media/TZJHBCDlsCFYA/giphy.gif" ,"You are one in a MILLION(MINION) :red_heart: https://i.pinimg.com/originals/b1/33/6c/b1336cd2e18a0a2fe89c005667b0ecc6.jpg"] #!!!ADD!!!!!!!!!!!!

jokes = ["Why can't a bicycle stand on its own?\nIt's two tired😴🚲", "If we weigh 100 Kgs on Earth, we'll weigh 38 Kgs on Mars, and just 16.6 Kgs on the Moon! It goes to prove, we're not overweight, just on the wrong planet.", "What movie should you watch on a dinner date? 🍴\nKabhi Sushi Kabhi Rum🍣🍹"]

memes = ["https://i.redd.it/ic2zu18uuw851.png", "https://i.pinimg.com/originals/94/5b/fb/945bfb6804e920b298848d73dce2a0e1.jpg", "https://www.thehealthy.com/wp-content/uploads/2020/10/xp1iwnvph2q51.jpg?w=800", "https://i.imgflip.com/59nra7.jpg", "https://the-breakdown.co.uk/wp-content/uploads/2020/12/mental.healthmemes_.png"] #!ADD!!!!!!!!!!!

twisters = ["How much wood would a woodchuck\nchuck\nIf a woodchuck would chuck wood? A woodchuck would chuck all the\nwood he could chuck\nIf a woodchuck would chuck wood", "A big black bug bit a big black bear and made the big black bear bleed blood" , "Shy Shelly says she shall sew sheets💪", "Sheela sat slowly sewing some silk salwars👖", "Pinky's papa picked a pink papaya to pickle", "I thought a thought.\nBut the thought I thought wasn't the thought I thought I thought.\nIf the thought I thought I thought had been the thought I thought,I wouldn't have thought so much."]

gifs = ["https://cdn.discordapp.com/attachments/805132413146759170/805461686479093780/giphy_24.gif" , "https://media.giphy.com/media/diAhf8bYer76E/giphy.gif ", "https://media.giphy.com/media/3oEdv4hwWTzBhWvaU0/giphy.gif " , " https://media.giphy.com/media/QbkL9WuorOlgI/giphy.gif" , " https://media.giphy.com/media/2GnS81AihShS8/giphy.gif " , "It will be okayyy! https://media.giphy.com/media/KztT2c4u8mYYUiMKdJ/giphy.gif " , " https://media.giphy.com/media/U2AH7M3nag85Ko4wVl/giphy.gif" , " https://media.giphy.com/media/l0HU2sYgCZh3HiKnS/giphy.gif " , " https://media.giphy.com/media/l4pTdcifPZLpDjL1e/giphy.gif " " https://media.giphy.com/media/l2QDYGQQKKNGq6mhq/giphy.gif " , " https://media.giphy.com/media/3o7abm56qOKRf3tl04/giphy.gif " , "https://media.giphy.com/media/9JnRMIFMYAKpaHRXRF/giphy.gif" , "https://media.giphy.com/media/l0HU2sYgCZh3HiKnS/giphy.gif " , " https://media.giphy.com/media/9Pv9okDwcVjvWK8vYg/giphy.gif", " https://media.giphy.com/media/M90mJvfWfd5mbUuULX/giphy.gif" , "https://media.giphy.com/media/VEj30DuFKtXE0o5MBS/giphy.gif"]   #!!!!!!!!!Add more care gifs!!!!!!!!!!!!!!
starter_inspirations = ["Cheer up! Everything will be alright. Try having something delicious? https://media.giphy.com/media/xT3i1drOzJ19adRkVW/giphy.gif " , "You are amazing! https://media.giphy.com/media/26n6yBeeXFU8C5j8c/giphy.gif ", "Smile, you look beautiful!" ,"Be Happy! https://media.giphy.com/media/3oxHQjb3brk6dOWBGg/giphy.gif "  , "To fall in love with yourself is the first secret to happiness. -Robert Morely", "Be gentle with yourself, learn to love yourself, to forgive yourself, for only as we have the right attitude toward ourselves can we have the right attitude toward others. -Wilfred Peterson" ,"Love yourself!", "Try doing nothips://media.giphy.com/media/3oxHQjb3brk6dOWBGg/giphy.gif "  , "To fall in love with yourself is the first secret to happiness. -Robert Morely", "Be gentle with yourself, learn to love yourself, to forgive yourself, for only as we have the right attitude toward ourselves can we have the right attitude toward others. -Wilfred Peterson" ,"Love yourself!", "Try doing nothing for 15 seconds https://cdn.lowgif.com/full/65353ed76bf13aa5-digital-icon-pack-clock-gif-by-seth-eckert-motion.gif " , "If you’re searching for that one person that will change your life, take a look in the mirror."]
songs = ["https://youtu.be/I0czvJ_jikg" , "https://youtu.be/Xn676-fLq7I", "https://youtu.be/_Yhyp-_hX2s" , "https://youtu.be/G-UnzRM24IM" , "https://youtu.be/nkqVm5aiC28" , "https://youtu.be/1k8craCGpgs"] #!!!Add songs!!!!!!!!!!!

cheer_up = ['Do you know, you are the most perfect you there is. \N{smiling face with halo}','Do you know, you are one of the smartest people I know. \N{smiling face with halo}', 'Do you know, you have the best smile. \N{smiling face with halo}', "You are the best ever, even better than a chocolate!🍫", "The word legend was coined in your praise!😎", "You are the rising sun on a cloudy day✨"] 

books = ["https://1lib.in/book/3408539/b1502b" , "https://1lib.in/book/737677/96de75" , "https://1lib.in/book/2884726/51cc4b" , "https://1lib.in/book/2765386/3121a6"]

movies = [" https://www.youtube.com/watch?v=reRcVxAWT1g  " , " https://www.youtube.com/watch?v=xroy2VFphi4 " , " https://www.youtube.com/watch?v=lTxn2BuqyzU " , " https://www.youtube.com/watch?v=XZHim74k7CA" ,"https://www.youtube.com/watch?v=sAea71tH8Zc"]  #biscuit #piper watermelon , night before math exam , camera 

#---------------------------------#
lazy_words = ["lazy", "boring", "bored"] 
relationship_words = ['romantic', 'partner', 'special someone', 'friend', 'boyfriend', 'girlfriend', 'relationship']
bodyshame_words = ["obesity", "overweight" , " fat" , "chubby"]

exercises=['Go for a walk! https://media.giphy.com/media/omHPYZttAVAAw/giphy.gif ',
           "How about a run? Don't forget to stretch! https://media.giphy.com/media/3oKIPavRPgJYaNI97W/giphy.gif ",
           'Stand up, walk around, and streeeeetch! https://media.giphy.com/media/8mvV5eUXkM18iCm5Eg/giphy.gif ',
           'Try some yoga! https://media.giphy.com/media/H3SYd8rWzFXQrAWLNc/giphy.gif ',
           'Head outside and explore! The world is your oyster.',
           'Try some pushups. Down, up 1! https://media.giphy.com/media/3ohhwElB92YQv0igda/giphy.gif ',
           'Find some friends and throw a frisbee','Lets do some exercise! https://media.giphy.com/media/Y3wnbT1OLWur4th15c/giphy.gif']
#---------------------------#


def contains_depression_traces(message):
  depression_keywords = ["kill myself", "cut myself", "I want to die", "hate myself", "end my life", "self harm", "i don't want to live", "harm", "die"]
  sentiment_analyze = SentimentIntensityAnalyzer()
  sentiment_dict = sentiment_analyze.polarity_scores(message)
  if sentiment_dict['neg'] >= 0.95:   #if score is lesser tha -0.95 , message may be serious
    return True
  is_depressing = sentiment_dict['neg'] > .75 or (sentiment_dict['neg'] > .5 and sentiment_dict['pos'] < .5)
  
  for word in depression_keywords: #rechecking if message includes harmful keywords
    if word in message:
       return  is_depressing
  return False


def depression_response():
  intro = "Hey, Are you okay? If you're struggling with anything, you're not alone and help is available. Here are some resources:"
  r1 = "  -  National Suicide Prevention Lifeline: call 9152987821 or visit http://www.aasra.info/"   
  r2 = "  -  Please remember you are always loved: " + random.choice(gifs)

  return "{intro}\n\n{r1}\n{r2}".format(intro = intro, r1 = r1, r2 = r2)


def contains_stress_traces(message):
  stress_keywords = ['stress','anxiety','anxious','stressed', 'scared', 'afraid', 'fear','need help','need support']
  sentiment_analyze = SentimentIntensityAnalyzer()
  sentiment_dict = sentiment_analyze.polarity_scores(message)
  if sentiment_dict['compound'] >= -0.85 and sentiment_dict['compound'] < -0.55:   # if score between -0.85 and -0.55
    return True
  is_stressed =sentiment_dict['neg'] > .75 or (sentiment_dict['neg'] > .5 and sentiment_dict['pos']  < .5)  
  for word in stress_keywords: #rechecking if message includes stress keywords
    if word in message:
      return is_stressed
  return False

def stress_response():
  intro = "Hey, you sound stressed"
  r2 = "\nWould you like to listen to some songs?"
  r3 = "\nCheck this out"
  r4 = random.choice(songs) 
  return "{intro}\n{r2}\n{r3}\n{r4}".format(intro = intro, r2 = r2, r3 = r3, r4 = r4) 

def contains_worry_traces(message):
  worry_keywords = ["sad", "depressed" , "stress", "stressed", "unhappy","miserable", "angry", "depressing", "cry", "crying", "worry", "worried", "tensed " , "trouble" , "distress" , "strain" , "upset " , "anxiety " , "irritated" , "irritation" ,"pressure " ,"difficulty ","suffering","burden ", "afraid" , "tired"]
  sentiment_analyze = SentimentIntensityAnalyzer()
  sentiment_dict = sentiment_analyze.polarity_scores(message)
  is_worried = sentiment_dict['neg']  > .75 or (sentiment_dict['neg']  > .5 and sentiment_dict['pos']  < .5) 
  for word in worry_keywords: #rechecking if message includes worry keywords
    if word in message:
       return is_worried
  return False


def worry_response():
  intro = "Hey, it's okay life happens sometimes"
  r1 = random.choice(worry_gifs)
  return "{intro}\n{r1}".format(intro = intro, r1 = r1)

def contains_happy_traces(message):
  happy_words = ["happy", "joy", "yohooo", "yay!","yay", "cheerful", "cheers","nice" , "cool" ,"helpful" ,"great" ,"wow"] 
  sentiment_analyze = SentimentIntensityAnalyzer()
  sentiment_dict = sentiment_analyze.polarity_scores(message)
  is_happy = sentiment_dict['pos']  > .75 or (sentiment_dict['pos']  > .5 and sentiment_dict['neg']  < .5)
  for word in happy_words:
    if word in message:
      return is_happy
  return False

def happy_response():
  intro = "I am glad you are happieeeeeee!"
  gif = "https://media.giphy.com/media/10UeedrT5MIfPG/giphy.gif"
  r1 = "Try typing $joy for hapieeer suggestions"
  return "\n{intro}\n{gif}\n{r1}".format(intro = intro, gif = gif, r1 = r1)


#---------------------------------------#


def get_quote(): ####
  response = requests.get("https://zenquotes.io/api/random") #get response from api
  json_data = json.loads(response.text) #converts response to json #response.text --> from api documentation
  quote = json_data[0]['q'] + "\n-" + json_data[0]['a']
  return(quote)



client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:  #should trigger only when it is clients message and not ours
    return
  
  TheMsg = message.content.lower()
#JUST SAY $hello TO ACTIVATE BOT
  hello_words = ["hello", "$hello", "hi", "heya", "hola", "hey","bonjour"]
  for word in hello_words:
    if TheMsg.startswith(word): 
        await message.channel.send('Hello! How are you, lovely person \N{smiling face with halo}')

  if TheMsg.startswith("$inspire"): 
    quote = get_quote()
    await message.channel.send(quote)

  elif TheMsg.startswith('$joy'): 
        quote = get_quote()
        joy_list = [random.choice(songs), random.choice(memes), random.choice(gifs), quote, random.choice(cheer_up), random.choice(exercises), random.choice(books), random.choice(movies), random.choice(jokes), random.choice(twisters)]
        response = "Try this:\n" + random.choice(joy_list)
        await message.channel.send(response)
  
  elif ("bye" in TheMsg) or ("goodbye" in TheMsg):
    await message.channel.send("Byeeeee. See you soon ❤️")
  
  elif "no friends" in TheMsg or ("no friend" in TheMsg) or ("lonely" in TheMsg):
    response = emoji.emojize("Hey Sunshine, I am your friend. I'm always here for you :red_heart:")
    await message.channel.send(response)

  elif any(word in TheMsg for word in lazy_words): #iterates over lazy_words to check if there is any word in message that is also in lazy_words
    response = random.choice(exercises)
    await message.channel.send(response) #gives a random excercise suggestion
  
  elif ("compliment" in TheMsg) or ("compliments" in TheMsg):
    compliments = ['You are more fun than bubble wrap <3',
    'You are the most perfect you there is. <3',
    'You are enough. <3',
    'You are one of the smartest people I know. <3',
    'You look great today <3',
    'You have the best smile <3',
    'You light up the whole server <3']
    response = random.choice(compliments)
    await message.channel.send(response)

  elif ("movie" in TheMsg) or ("movies" in TheMsg):
    response = "Try this movie:\n" + random.choice(movies)
    await message.channel.send(response)

  elif ("book" in TheMsg) or ("books" in TheMsg):
    response = "Try this book:\n" + random.choice(books)
    await message.channel.send(response)

  elif ("song" in TheMsg) or ("song" in TheMsg):
    response = "Try this song:\n" + random.choice(songs)
    await message.channel.send(response)
  
  elif ("meme" in TheMsg) or ("memes" in TheMsg):
    await message.channel.send(random.choice(memes))

  elif ("exercise" in TheMsg) or ("overweight" in TheMsg.lower()):
    await message.channel.send(random.choice(exercises))

  elif ("be my friend" in TheMsg) or ("i love you" in TheMsg):
    r1 = emoji.emojize("Aww, You are the idli to my chutney :red_heart: https://i.pinimg.com/474x/a3/2e/32/a32e32592fde3bafe8349c75f397da09.jpg")
    r2 = emoji.emojize("Aww, You are the aloo to my samosa :red_heart: https://i.pinimg.com/originals/5b/cd/04/5bcd0476568792ec8e7c07f851769828.jpg" 
    )
    r3 = emoji.emojize("Aww, You are the paneer to my pakora :red_heart:")
    r4 = emoji.emojize("Aww , You are the sambhar to my dosa :red_heart: https://i.pinimg.com/originals/2f/b1/07/2fb1073c4851ebdd27453c35e286a556.jpg ")
    r5 = emoji.emojize("Can we be friends? :red_heart: https://sm.mashable.com/mashable_sea/photo/default/54518851-2145886505490834-5209910250487939072-n_52be.jpg") 
    responses = [r1, r2, r3,r4,r5]
    await message.channel.send(random.choice(responses))
  elif ("bad joke" in TheMsg):
    response = "My sense of humor is stil in alpha, hopefully soon it'll get beta"
    await message.channel.send(response)

  elif ("sleep" in TheMsg):
    response = ["https://youtu.be/JEoxUG898qY", "https://youtu.be/cI4ryatVkKw"]
    await message.channel.send(random.choice(response))

  elif ("cheer" in TheMsg):
    await message.channel.send(random.choice(cheer_up))

  elif ("joke" in TheMsg) or ("jokes" in TheMsg) or ("make me laugh" in TheMsg):
    response = "Try this:\n" + random.choice(jokes)
    await message.channel.send(response)

  elif ("tongue twister" in TheMsg):
    response = "Try this:\n" + random.choice(twisters)
    await message.channel.send(response)

  elif any(word in TheMsg for word in relationship_words):
    await message.channel.send("Relationships are complicated and are very precious. We might not be able to understand but ask for advice in the safespace discord server of therapists and kind folks: https://discord.gg/9g98gZ9H%22")

  elif any(word in TheMsg for word in bodyshame_words):
    await message.channel.send(random.choice(cheer_up))

  elif contains_happy_traces(TheMsg):
    response = happy_response()
    await message.channel.send(response)

  elif  ("no" in TheMsg) and ("not" not in TheMsg) and ("now" not in TheMsg):
    await message.channel.send("Try typing $joy for some other cool stuff ") 

  elif contains_depression_traces(TheMsg):
        response = depression_response()
        await message.channel.send(response)
  elif contains_stress_traces(TheMsg):
        response = stress_response()
        await message.channel.send(response)
  elif contains_worry_traces(TheMsg):
        response = worry_response()
        await message.channel.send(response)
  elif contains_happy_traces(TheMsg):
    response = happy_response()
    await message.channel.send(response)
  elif ("thank you" in TheMsg) or ("thank u" in TheMsg) or ("thank you!" in TheMsg) or ("thanks" in TheMsg):
    await message.channel.send("My Pleasure \N{smiling face with halo}")
  else:
    response = emoji.emojize("Try typing $joy for memes, songs, gifs, books, short movies and more :smiling_face_with_3_hearts:")
    await message.channel.send(response) 
  


#run discord bot
client.run(os.getenv("TOKEN"))

