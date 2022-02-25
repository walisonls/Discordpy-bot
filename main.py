import discord
import os
from discord.ext import commands, tasks
from datetime import datetime

## variables ##
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="$", case_insensitive = True, intents = intents)
point = 0

## crate client ##
@bot.event
async def on_ready():
  print(f"Estou pronto! Estou conectado como {bot.user}")
  current_time.start()

## time response ##
@tasks.loop(hours=24)
async def current_time():
  now = datetime.now()

  now = now.strftime("%d/%m/%Y às %H:%M:%S")

  channel = bot.get_channel(943122811747184720)

  await channel.send("Ping Retornado, data: " + now)

## message control ##
@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if "palavrão" in message.content:
    await message.channel.send(f"Por Favor, {message.author.name}, não ofenda os demais usuarios!")

    await message.delete()

  await bot.process_commands(message) #processar comandos.

  
## response command ##
@bot.command(name="oi")
async def send_hello(ctx):
  name = ctx.author.name
  response = "Olá, " + name

  await ctx.send(response)

## Seja Bem-Vindo(a) ##
@bot.event
async def on_member_join(member):
  canalboasvindas = bot.get_channel(942834048504561725)
  regras = bot.get_channel(942844806084845659)
  
  message = await canalboasvindas.send(f"Bem vindo(a) {member.mention}! Leia as regras em ")
  

## cargos por reação ##
@bot.event
async def on_reaction_add(reaction, user):
  if reaction.emoji == "🔴":
    role = user.guild.get_role(943859423959474197)
    await user.add_roles(role)
  elif reaction.emoji == "🟠":
    role = user.guild.get_role(943859422252384298)
    await user.add_roles(role)
  
## embed ##
@bot.command(name="foto")
async def get_random_image(ctx):
  url_image="https://picsum.photos/1920/1080"

  embed_image = discord.Embed(
    title = "Resultado da busca de imagens",
    description = "A busca é totalmente aleatoria",
    color = 0x0000FF,
  )

  embed_image.set_author(name=bot.user.name, icon_url="bot.user.avatar_url")
  embed_image.set_footer(text="Feito por " + bot.user.name, icon_url=bot.user.avatar_url)

  embed_image.add_field(name="API", value="Usamos a API do https://picsum.photos")
  embed_image.add_field(name="Parâmetros", value="{largura}/{altura}")

  embed_image.add_field(name="Exemplo", value=url_image, inline="False")

  embed_image.set_image(url=url_image)

  await ctx.send(embed=embed_image)


## recuperando TOKEN ##
bot.run(os.getenv('TOKEN'))