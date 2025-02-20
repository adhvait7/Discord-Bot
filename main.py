import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord import Member
import random
import os
import typing
import asyncio
import aiohttp
import imghdr
  

from keep_alive import keep_alive
my_secret = os.environ['TOKEN']
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '!',intents = intents)
client.remove_command("help")

#Printing the logged in thingy

@client.event
async def on_ready( ):
  print('We have logged in as {0.user}'.format(client))
  # Setting `Playing ` status 
  await client.change_presence(activity=discord.Game("with Thundy's feelings <3"))
  #await client.user.edit(avatar=pfp)

from discord.ext import commands


#@client.event
#async def on_command_error(ctx, error):
#  if ctx.message.content == ("!d bump"):
#    return
#  elif isinstance(error, commands.CommandNotFound):
#    embed= discord.Embed(
#    color=discord.Color.teal(),
#    title=('Invalid Command'),
#    description = ('Type !help to see list of commands.')
#    )
#    await ctx.reply(embed=embed)


  
  
  
#on_member_leave
@client.event
async def on_member_remove(member):
  guild = member.guild
  icon = str(guild.icon_url)
  channel = discord.utils.get(guild.channels, name='general') #searches for a channel in the guild called channel
  if channel:
    embed = discord.Embed(color = discord.Color.from_rgb(170,164,255), description=f'{member} just left the server.')
    embed.set_thumbnail(url=icon)
    await channel.send(embed=embed)



#Welcome command
@client.event
async def on_member_join(member):
  guild = member.guild
  memcount = guild.member_count
  lastdigit = (memcount%10)
  if (lastdigit == 1):
    icon = str(guild.icon_url)
    embed = discord.Embed(color = discord.Color.from_rgb(170,164,255), title=f'Welcome {member}, You are our {guild.member_count}ˢᵗ member.')
    
  elif (lastdigit == 2):
    icon = str(guild.icon_url)
    embed = discord.Embed(color = discord.Color.from_rgb(170,164,255), title=f'Welcome {member}, You are our {guild.member_count}ⁿᵈ member.')
  elif (lastdigit == 3):
    icon = str(guild.icon_url)
    embed = discord.Embed(color = discord.Color.from_rgb(170,164,255), title=f'Welcome {member}, You are our {guild.member_count}ʳᵈ member.')
  elif (lastdigit == 4 or 5 or 6 or 7 or 8 or 9 or 0):
    icon = str(guild.icon_url)
    embed = discord.Embed(color = discord.Color.from_rgb(170,164,255), title=f'Welcome {member}, You are our {guild.member_count}ᵗʰ member.  Enjoy your stay :)')


      

  embed.set_thumbnail(url=icon)
  embed.add_field(name = chr(173), value = chr(173))

  embed.add_field(name=f"Like this bot?", value=" [Add this bot to your server!](https://discord.com/api/oauth2/authorize?client_id=837675924035731466&permissions=8&scope=bot)")

  

  await member.send(embed=embed)



#async def(welcomer):
#  await ctx.reply("What is the server id?"):
#  msg = await client.wait_for("message", check=check)
#  id = int(msg.content)




#administrative commands

#kick
@client.command()
#@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  if ctx.author.guild_permissions.kick_members:
    embed= discord.Embed(
    color = discord.Color.from_rgb(170,164,255),
    description = (f'You have been kicked from {ctx.guild.name}. Reason = {reason}.')
    )
    await member.send(embed=embed)
    await member.kick(reason=reason)
    embed= discord.Embed(
    color = discord.Color.from_rgb(170,164,255),
    description = (f'{member.mention} has been kicked.')
    )
    await ctx.reply(embed=embed)
  elif member.guild_permissions.kick_members:
    embed= discord.Embed(
    color = discord.Color.from_rgb(170,164,255),
    description = (f'{member.mention} is a mod/admin, I cannot do that.')
    )
    await ctx.reply(embed=embed)
  else:
    embed= discord.Embed(
    color = discord.Color.from_rgb(170,164,255),
    description = (f"You don't have the permissions to do that, pleb. {ctx.author.mention}")
    )
    await ctx.reply(embed=embed)
 

#ban
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
  if ctx.author.guild_permissions.ban_members:
    await member.ban(reason=reason)
    embed= discord.Embed(
    color = discord.Color.from_rgb(170,164,255),
    title=('Member Banned'),
    description = (f'{member.mention} has been banned.')
    )
    await ctx.reply(embed=embed)
    embed= discord.Embed(
    color = discord.Color.from_rgb(170,164,255),
    description = (f'You have been banned from {ctx.guild}. Reason: {reason}')
    )
    await member.send(embed=embed)

  elif member.guild_permissions.ban_members:
    embed= discord.Embed(
    color = discord.Color.from_rgb(170,164,255),
    title=('Command Failed'),
    description = (f'{member.mention} is a mod/admin, I cannot do that.')
    )
  
  else:
    embed= discord.Embed(
    color = discord.Color.from_rgb(170,164,255),
    title = ('Command Failed'),
    description = (f"You don't have the permissions to do that, pleb. {ctx.author.mention}")
    )
    await ctx.reply(embed=embed)

  

#unban doesnt work for now.
#unban
@client.command()
async def unban(ctx, member : discord.Member, *, reason=None):
  if ctx.author.guild_permissions.ban_members:
    await member.unban(reason=reason)
    await ctx.reply(f'{member.mention} has been unbanned.')
  else:
    await ctx.reply(f"You don't have the permissions to do that, pleb. {ctx.author.mention}")

#leave 
@client.command()
async def leave(ctx):
  if ctx.author.id == 407064079904276480: 
    await ctx.reply("aight, leaving the server.")
    await ctx.guild.leave()
#numbers
@client.command()
async def infinity(ctx):
  number = 1
  #for i in range(1,10000000000000):
    #await ctx.send(i)
  while True:
    await ctx.send(number)
    number += 1


#7 spammer
@client.command()
async def seven(ctx):
  number = 7
  while True:
    await ctx.send(number)

#status
@client.command()
async def status(ctx, member : discord.Member=None):
  if member is None:
    member = ctx.author
  embed=discord.Embed(title=f"{member.name} your current status is", description= f'{member.activities[0].name}', color=0xcd32a7)
  await ctx.send(embed=embed)


#dm
@client.command()
async def dm(ctx, user:discord.Member=None, *,message=None):
  if user is None or message is None:
    message = "Invalid Command Usage"
    embed = discord.Embed(title=message)
    embed.add_field(name="Try using it like:", value="`!dm [user] <message>`",inline=True)
    await ctx.reply(embed=embed)
  else:
    embed = discord.Embed(title=message)
    embed.set_footer(text=f"Message from: {ctx.message.author}")
    await user.send(embed=embed)
    
  

#remind command
@client.command()
async def r(ctx, amt:int=290,msg:str=None):
  if msg is None:
    mesg = await ctx.channel.send(f"reminding you in {amt} seconds.")
    await asyncio.sleep(amt)
    await mesg.delete()
    await ctx.reply(f"reminder!")
  else:
    mesg = await ctx.channel.send(f"reminding you in {amt} seconds.")
    await asyncio.sleep(amt)
    await mesg.delete()
    await ctx.reply(f"reminder!\nMessage: {msg}")
  

#remind command
@client.command()
async def remind(ctx, amt:int=5):
  await ctx.channel.send(f"reminding you in {amt} minutes.")
  await asyncio.sleep(amt*60)
  await ctx.reply("reminder!")
  

#say
@client.command()
async def say(ctx,*, message=None):
  member = client.get_user(407064079904276480)
  url = ctx.message.jump_url
  embed= discord.Embed(
    title=f"!say command used by: {ctx.author}",
    description=f"**Content:** {message}",
    color = discord.Color.from_rgb(170,164,255)
  )
  embed.add_field(name="Server:", value=f'{ctx.guild}', inline=True)
  embed.add_field(name=f"Channel:",value=f"[Jump to message]({url})", inline=False)
  await member.send(embed=embed)
  
  await ctx.message.delete()
  async with ctx.typing():
    await asyncio.sleep(1)    
    await ctx.send(message)
    await ctx.message.delete()


#emoji
@client.command(name = "emoji")
async def emoji(ctx, emoji : discord.Emoji, message_id):
  message = await ctx.fetch_message(message_id)
  await message.add_reaction(emoji)

#embedsay
@client.command(aliases = ['esay'])
async def embedsay(ctx,*, message=None):
  ctx.message.delete()
  member = client.get_user(407064079904276480)
  url = ctx.message.jump_url
  embed= discord.Embed(
    title=f"!esay command used by: {ctx.author}",
    description=f"**Content:** {message}",
    color = discord.Color.from_rgb(170,164,255)
  )
  embed.add_field(name="Server:", value=f'{ctx.guild}', inline=True)
  embed.add_field(name=f"Channel:",value=f"[Jump to message]({url})", inline=False)
  await member.send(embed=embed)
  embed=discord.Embed(
    description = message,
    color = discord.Color.from_rgb(170,164,255)
  )
  await ctx.message.delete()
  await ctx.send(embed=embed)


#clear
@client.command(aliases = ['purge','delete'])
async def clear(ctx, amount:int=5):
  if ctx.author.guild_permissions.manage_messages or ctx.author.id == 407064079904276480:
    await ctx.channel.purge(limit=amount, check=lambda m:m.id!=ctx.message.id)
    response = f"Deleted {amount} messages"
    msg = await ctx.reply(response)
    await asyncio.sleep(1)
    await msg.delete()
    await ctx.message.delete()
  else:
    response = f"You don't have permissions to do that."
    msg = await ctx.reply(response)
    await asyncio.sleep(1)
    await msg.delete()
    await ctx.message.delete()
    
  #fun stuff
first = ["hey","hi","hello","heya","hii","hiii",'hiiii']
wordlist = ["bored"]
responses = ["type !burshuvasu to see fun commands"]




dababy = ["lets go","less go","let's go","LETS GOO","dababy","Letssss gooo","lesgo","lessgo"]
dababyr = ["https://tenor.com/view/daceegee-dacg-dababy-less-go-gif-20851407","https://tenor.com/view/dababy-rapper-hip-hop-rap-digibyte-gif-17582117","https://tenor.com/view/dababy-convertable-gif-20206040","LESS GOOOOOOO:point_right::sunglasses::point_left:",":point_right::sunglasses::point_left:","https://media.discordapp.net/attachments/837220945705304106/839020488557985892/tenor.gif"]


waifureplies = ["Hii baby :relaxed:","hi bae :heart_eyes:","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder","hi thunder"]
waifureplies2 = ["I have a boyfriend :expressionless:","Bye","ew stay away from me",'hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)','hi :)']
avinas = ["avinash","avinas"]
tea = [" tea "," chai "," coffee "," tea"," chai"," coffee","tea ","chai ","coffee "]
k=["k","k"]
tea2 = ["tea","coffee","chai"]


reacts = ['🖐️','🍆','✊','🍑','👀','😏','☺️','😚','😝','🤩','😳','🤯','🥰','😎','🥳','😋','😕','☹️','😐','😶']
lolxdreacts = ['<:grape:923432696401776700>','😹',]
#sixnine = [nice emoji]
#clown 
#future plan
@client.listen('on_message')
async def on_message(message):

  if message.author == client.user:
      return
#useful stuff
  if message.content.lower() in first:
    if message.author.id == 407064079904276480:
      async with message.channel.typing():
        await asyncio.sleep(1)
      await message.channel.send(f"hi master {message.author.mention}")
    else:
      await message.channel.send(f"hi {message.author.mention}")
      
  if message.content.lower() in k:
    nomber = random.randint(0,100)
    if nomber < 30:
      await message.channel.send('k')
  if any(word in message.content.lower() for word in dababy):
    await message.add_reaction("👉")
    await message.add_reaction("😎")
    await message.add_reaction("👈")
    nomber = random.randint(0,100)
    print(f'Number for dababy is {nomber}.')
    if nomber < 30:
      await message.channel.send(random.choice(dababyr))
    

  if message.content.lower() == "boobs":
    await message.delete()
    await message.channel.send("boobs!")


    
  if message.content.lower() in avinas:
    nomber = random.randint(0,100)
    print(f'Number for avinas is {nomber}.')
    if nomber < 11:
      await message.channel.send(f'DuE tO OvErThinKingS i DiDnT gO to KoLLejH')
  

  if any(word in message.content.lower() for word in tea):
    embed = discord.Embed(color=discord.Color.dark_theme())
    embed.set_image(url = "https://i.redd.it/6iz6kj2s0ce51.jpg")
    await message.channel.send(embed = embed)
    
  if message.content.lower() in tea2:
    embed = discord.Embed(color=discord.Color.dark_theme())
    embed.set_image(url = "https://i.redd.it/6iz6kj2s0ce51.jpg")
    await message.channel.send(embed = embed)   
      
  if any(word in message.content.lower() for word in wordlist):
    nomber = random.randint(0,100)
    print(f'Number for easter egg is {nomber}.')
    if nomber < 10:
    
      await message.channel.send(random.choice(responses),delete_after=5)
      await asyncio.sleep(5)
      await message.delete()

  
  if client.user.mentioned_in(message):
    if message.mention_everyone:
        return    
    if message.author.id == 407064079904276480:
      await message.reply(random.choice(waifureplies))
    else:
      await message.reply(random.choice(waifureplies2))
  if message.content.lower() == ("hand workout"):
    for i in reacts:
      await message.add_reaction(i)

      
 
  





    for i in reacts:
      await message.add_reaction(i)

  if message.content == ("!d bump"):
    await message.channel.send("Thanks for bumping. Will remind you again in 2 hrs")
    await asyncio.sleep(7200)
    await message.channel.send(f"{message.author.mention}, Time to bump")

#@client.listen('on_message')
#@client.event
#async def on_message(message):
  #await message.add_reaction(":UWU:839831330681782302")
  #if message.author.id == 407064079904276480:

    #await message.add_reaction("👁️")
  #await message.channel.send(f"haha")
  #return
  #await message.add_reaction(":UWU:839831330681782302")
  #await client.process_commands(message)


  

#bump reminded
@client.command()
async def dbump(ctx):
  await ctx.send("Thanks for bumping")

#mass ping
@client.command()
async def massupingu(ctx):
  memberlist = ctx.guild.members
  for i in memberlist:
    await ctx.channel.send((i).mention)


@client.command()
async def masspingeveryone(ctx, amount:int=None):
  if amount is None:
    await ctx.channel.send("Enter no. of times to ping.\n Example: `!masspingeveryone 10`")
  else:
    while amount > 0:
      await ctx.channel.send('@everyone')
      amount -= 1









#meme commands
memesubs = ['https://www.reddit.com/r/dankmemes/hot.json','https://www.reddit.com/r/dankmemes/new.json','https://www.reddit.com/r/memes/hot.json','https://www.reddit.com/r/memes/new.json','https://www.reddit.com/r/ksi/hot.json','https://www.reddit.com/r/Animemes/new.json','https://www.reddit.com/r/Animemes/hot.json','https://www.reddit.com/r/virginvschad/new.json','https://www.reddit.com/r/virginvschad/hot.sjon']

@client.command()
async def meme(ctx, amount:int=1):
  nomber = 0
  while nomber < amount:
    promonum = random.randint(0,100)
    print(promonum)
    if promonum < 95:
      async with aiohttp.ClientSession() as cs:
        async with cs.get(random.choice(memesubs)) as r:
          data = await r.json()
          data = data['data']
          children = data['children']
          post = random.choice(children)['data']
          title = post["title"]
          sub = post["subreddit"]
          embed = discord.Embed(
          color = discord.Color.default(),
          title=title
          )
          
          embed.set_image(url=post["url_overridden_by_dest"])
          embed.set_footer(text=f"Powered by r/{sub} | Meme requested by {ctx.author}")
          await ctx.send(embed=embed)
          nomber +=1
          print(nomber)
          await asyncio.sleep(1)
      
    else:
      async with aiohttp.ClientSession() as cs:
        async with cs.get(random.choice(memesubs)) as r:
          data = await r.json()
          data = data['data']
          children = data['children']
          post = random.choice(children)['data']
          
          sub = post["subreddit"]
          embed = discord.Embed(
          color = discord.Color.default(),
          )
          embed.add_field(name="Support Us!",value="[Click here to add this bot to your server!](https://discord.com/api/oauth2/authorize?client_id=837675924035731466&permissions=8&scope=bot)", inline=False)
          embed.set_image(url=("https://i.imgflip.com/5hgqva.jpg"))
          embed.set_footer(text=f"Support the developer! | type !invite to add this bot to  your server.")
          await ctx.send(embed=embed)
          nomber +=1
          print(nomber)
          await asyncio.sleep(1)


@client.command()
@commands.cooldown(1, 7777777, commands.BucketType.guild)
async def automeme(ctx):
  while True:
    
    async with aiohttp.ClientSession() as cs:
      async with cs.get(random.choice(memesubs)) as r:
        data = await r.json()
        data = data['data']
        children = data['children']
        post = random.choice(children)['data']
        title = post["title"]
        sub = post["subreddit"]
        embed = discord.Embed(
        color = discord.Color.default(),
        title=title
        )
        embed.set_image(url=post["url_overridden_by_dest"])
        embed.set_footer(text=f"Powered by r/{sub} | Meme requested by {ctx.author}")
        await ctx.send(embed=embed)
        await asyncio.sleep(300)  

@automeme.error
async def automeme_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = await ctx.reply('This command can only be used once.')
        await asyncio.sleep(2)
        await ctx.message.delete()
        await msg.delete()
    else:
        raise error




#serverinfo cmd
@client.command(aliases=['servinfo','sewer'])
async def serverinfo(ctx):
  name = str(ctx.guild.name)
  description = "Description: " + str(ctx.guild.description)

  owner = str(ctx.guild.owner)
  id = str(ctx.guild.id)
  region = str(ctx.guild.region)
  memberCount = str(ctx.guild.member_count)

  icon = str(ctx.guild.icon_url)
  
  embed = discord.Embed(
      title=name,
      description=description,
      color=discord.Color.gold()
    )
  icon2 = str(ctx.author.avatar_url)
  embed.set_author(name=ctx.author, icon_url=icon2)
  embed.set_thumbnail(url=icon)
  embed.add_field(name="Owner", value=owner, inline=True)
  embed.add_field(name="Region", value=region[0].upper()+region[1:], inline=True)
  embed.add_field(name="Member Count", value=memberCount, inline=True)
  #embed.add_field(name="Created at", value=ctx.guild.created_at.strftime("%d/%m/%y,  %H:%M:%S"), inline=True)
  embed.set_footer(text="Created at: "+str(ctx.guild.created_at.strftime("%d/%m/%y,  %-I:%M:%S %p")))

  await ctx.send(embed=embed)



#userinfo
@client.command(aliases = ['ui'])
async def userinfo(ctx, *, user: discord.Member = None):
    if user is None:  
        user = ctx.author      
    await ctx.send(ctx.author.mention)    
    date_format = "%a, %d %b %Y %I:%M:%S %p"
    embed = discord.Embed(color=0x38ffca, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    #if len(user.roles) > 1:
        #role_string = ' '.join([r.mention for r in user.roles][1:])
        #embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    #perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    #embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)


#avatar
@client.command(aliases = ['av'])
async def avatar(ctx, user: discord.Member = None):
  if user is None:
    user = ctx.author
  embed = discord.Embed(color=discord.Color.dark_theme())
  embed.set_author(name=str(user), icon_url=user.avatar_url)
  embed.set_image(url = user.avatar_url)
  embed.set_footer(text=ctx.author,icon_url=ctx.author.avatar_url)
  await ctx.reply(embed = embed)  
  



    


#<!-----------------HELP COMMAND-------------------------------
@client.command(aliases = ['cmds','commands'], pass_context=True)
async def help(ctx):
  await ctx.message.add_reaction('✅')
  

  embed= discord.Embed(
    title="Commands List",
    description="A list of all commands",
    color = discord.Color.from_rgb(170,164,255)
  )
  icon = str(ctx.guild.icon_url)
  icon2 = str(ctx.author.avatar_url)
  embed.set_author(name=ctx.author, icon_url=icon2)
  embed.set_thumbnail(url=icon)
  embed.add_field(name="**:shield:Administrative Commands**", value="Commands for administrative purposes.", inline=False)
  embed.add_field(name="!kick `username`", value="Kicks the specified user from the server.", inline=True)
  embed.add_field(name="!ban `username`", value="Bans the specified user from the server.", inline=True)
  embed.add_field(name="!clear `*amount of messages*`", value="Deletes the specified number of messages from the chat.", inline=True)
  embed.add_field(name="!userinfo `member`", value="Shows info about the specified user.", inline=True)
  embed.add_field(name="!serverinfo", value="Shows information about the server.", inline=True)
  embed.add_field(name="!avatar `username`", value="Shows the profile picture of the user if mentioned.")
  embed.add_field(name="**:smiling_face_with_3_hearts:Fun Commands**", value="Commands for entertainment purposes.", inline=False)
  embed.add_field(name="!say `stuff`", value="Makes the bot say stuff.", inline=True)
  embed.add_field(name="!esay `stuff`", value="Makes the bot say stuff in embedded form.", inline=True)
  embed.add_field(name="!meme", value="Sends a meme.", inline=True)
  embed.add_field(name=f"Support Us", value="[Add this bot to your server!](https://discord.com/api/oauth2/authorize?client_id=837675924035731466&permissions=8&scope=bot)", inline=False)
  await ctx.author.send(embed=embed)
  await ctx.send(embed=embed)



#<!-----------------invite bot command-------------------------------
@client.command()
async def invite(ctx):
  embed = discord.Embed(
        title = "Invite this bot to your server!",
        description = "[Click here to add this bot to your server!](https://discord.com/api/oauth2/authorize?client_id=837675924035731466&permissions=8&scope=bot)",
        color = discord.Color.blue()
  )
  
  await ctx.send(embed=embed)

#<!-----------------BURSHUVASU COMMAND-------------------------------
@client.command(pass_context=True)
async def burshuvasu(ctx):
  await ctx.message.add_reaction('😉')

  embed= discord.Embed(
    title="Easter Eggs",
    description="Fun stuff to try.",
    color = discord.Color.from_rgb(255,192,203)
  )
  icon = str(ctx.guild.icon_url)
  icon2 = str(ctx.author.avatar_url)
  embed.set_author(name=ctx.author, icon_url=icon2)
  embed.set_thumbnail(url=icon)
  embed.add_field(name="**:smiling_face_with_3_hearts:Fun Commands**", value="Commands for entertainment purposes.", inline=False)
  embed.add_field(name="`dababy`", value="Less goo.", inline=True)
  embed.add_field(name="`tea`", value="Sends an image of waifu making tea.", inline=True)
  embed.add_field(name="!say `stuff`", value="Makes the bot say stuff.", inline=True)
  embed.add_field(name="!esay `stuff`", value="Makes the bot say stuff in embedded form.", inline=True)
  await ctx.author.send(embed=embed,delete_after=3)
  await ctx.send(embed=embed, delete_after=3)
  await asyncio.sleep(3)
  await ctx.message.delete()
  await client.message.delete()



#list of servers
@client.command()
async def servers(ctx):
  servers = list(client.guilds)
  await ctx.send(f"Connected on {str(len(servers))} servers:")
  await ctx.send('\n'.join(guild.name for guild in servers))










  
keep_alive()
client.run(os.getenv('TOKEN'))  
