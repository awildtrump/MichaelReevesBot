import discord
import random
import inspect
import os
import ffmpeg

version = "1.0"



client = discord.Client()
#n
#i
#g
#h
#t
#m
#a
#r
#e

#client.change_presence(activity=ActivityType.Listening(name="$reeves help"))
#nightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmarenightmare

#I am in great pain, juje made me do python
#-juji 2020


quotes = [
    ["https://www.youtube.com/watch?v=c2gq4IwIc_s&t=51s", "2019", "I'm Elon Musk of bad ideas", 0x11cc11],
         ["https://www.youtube.com/watch?v=Hu3p5ZR_i5s&t=5s", "2018", "Here's a drone video. Eat shit!", 0xbbbbbb], 
         ["https://www.youtube.com/watch?v=Q8QlNuTUe4M&t=3s", "2018", "Facial detection? Nah. I prefer racial detection.", 0xaa1111], 
         ["https://www.youtube.com/watch?v=5QYpD428hAQ&t=6s", "2018", "I went over to the cemetery and urinated on the old man's grave.", 0xe8dc31], 
         ["https://www.youtube.com/watch?v=B1dWbiXnz_s&t=105s", "2019", "Eat my brown ass Will!", 0x8b4513], 
         ["https://www.youtube.com/watch?v=mPbtR4vorgY&t=1s", "2018", "It's 2018 we're living in the goddamn future.", 0x6fe8e2], 
         ["https://www.youtube.com/watch?v=mPbtR4vorgY&t=8s", "2018", "GOD I drink so much cafeine!", 0x806340], 
         ["https://www.youtube.com/watch?v=pE39KdptM40&t=59s", "2019", "As long as it takes to make it perfect just so I can show you that it's your idea that's bad. Whatever it is days, weeks, months...", 0xaa2222],
         ["https://www.youtube.com/watch?v=pE39KdptM40&t=76s", "2019", "I've got everyone's favourite food, tin foil...", 0xd9d9d9], 
         ["https://www.youtube.com/watch?v=A_BlNA7bBxo&t=115s", "2020", "I forgot to record all the sound effects, OK? Give me a fucking break.", 0x11cc11], 
         ["https://www.youtube.com/watch?v=D75ZuaSR8nQ&t=362s", "2019", "Python can do *anything*. Just badly.", 0xfff700], 
         ["https://www.youtube.com/watch?v=B0eSPogdaHs&t=101s", "2019", "I'm gonna be slamming my head against the keyboard trying to figure out how I'm gonna run a website off of a goddamn cup I built, my blood is gonna become redbull...", 0xff4800], 
         ["https://www.youtube.com/watch?v=A_BlNA7bBxo&t=91s", "2020", "NO! Ur stupid and I hate you.", 0x11cc11], 
         ["https://www.youtube.com/watch?v=ZIxaGgTY8UM&t=55s", "2020", "That is a fucking alarm clock!", 0x11cc11], 
         ["https://www.youtube.com/watch?v=ZIxaGgTY8UM&t=200s", "2020", "I am Iron Man.", 0xff4800], 
         ["https://www.youtube.com/watch?v=ZIxaGgTY8UM&t=366s", "2020", "Have a seat ~~in my electric~~ in my pneumatic chair.", 0x11cc11], 
         ["https://www.youtube.com/watch?v=D75ZuaSR8nQ&t=565s", "2018", "Let's do with random people because my real friends are too busy... ...being imaginary.", 0x11cc11], 
         ["https://www.youtube.com/watch?v=d5d02U5YYfk&t=67s", "2018", "Hitler ruins everything.", 0x11cc11]
         ]




def quote():
    s = random.choice(quotes)
    return(s)

@client.event
async def on_ready():
    print("gej si {0.user}".format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$reeves help"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$reeves quote"):
        #RANDOM QUOTE EMBED

        #govno index
        #0: url
        #1: year
        #2: quote
        #3: color



        govno = quote()

        #print(inspect.getmembers(client, lambda a:not(inspect.isroutine(a))))
        embedVar = discord.Embed(title=govno[2], color=govno[3])
        embedVar.add_field(name="On video:", value=govno[0], inline=False)
        #embedVar.add_field(name=quote(), value="Mihael Reeves -i have no clue which year", inline=False)
        embedVar.set_footer(text="Michael Reeves -" + govno[1], icon_url="https://vignette.wikia.nocookie.net/youtube/images/d/d1/Michaelreevesicon.jpeg/revision/latest?cb=20200216070831")
        await message.channel.send(embed=embedVar)

    elif message.content.startswith("$reeves about"):
        govno = quote()
        embedVar = discord.Embed(title="About MichaelReevesBot", color=0xFFFF00)
        embedVar.add_field(name="About", value="MichaelReevesBot was meticulously created by PotaTronics in 2020. It's purpose is to make Discord communities less depressed by providing quotes by our beloved YouTuber Michael Reeves.", inline=False)
        embedVar.add_field(name="Version", value="MichaelReevesBot v" + version, inline=False)
        await message.channel.send(embed=embedVar)

    elif message.content.startswith("$reeves crackhead"):
        embedVar = discord.Embed(title="Crackhead mode: ```ON```", color=0xFFFF00)
        await message.channel.send(embed=embedVar)
        user=message.author
        voice_channel=user.voice.channel
        vc = await voice_channel.connect()
        print(vc)
        vc.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source="stvar.mp3"))
    elif message.content.startswith("$reeves nightmare"):

        embedVar = discord.Embed(title="Nightmare mode: ```ON```", color=0xFFFF00)
        await message.channel.send(embed=embedVar)
        voice_channel = message.author.voice.voice_channel
        await bot.join_voice_channel(voice_channel)
        voice = await message.author.voice.channel.connect()
        voice.play(discord.FFmpegPCMAudio("stvar.wav"))

client.run("")