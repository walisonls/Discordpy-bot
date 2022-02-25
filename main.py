import discord
import os
from discord.ext import commands, tasks
from datetime import datetime

## variables ##
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="$", case_insensitive = True, intents = intents)
point = 0

## Bot Connected ##
@bot.event
async def on_ready():
  now = datetime.now()#importando relogio.
  now = now.strftime(" %H:%M:%S de %d/%m/%Y")#configurando formato de horario.
  channel = bot.get_channel(942944936771346443)#canal de comunicação
  await channel.send(f"{bot.user} Conectada ao servidor as {now}")#menssagem


## Seja Bem-Vindo(a) ##
@bot.event
async def on_member_join(member):
  canalboasvindas = bot.get_channel(942834048504561725)
  url_image="https://picsum.photos/1920/1080"

  embed = discord.Embed(
    title = "Resultado da busca de imagens",
    description = "A busca é totalmente aleatoria",
    color = 0x0000FF,
  )

  embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
  embed.set_footer(text="ID do usuário " + bot.user.id)

  embed.add_field(name="API", value="Usamos a API do https://picsum.photos")
  embed.add_field(name="Parâmetros", value="{largura}/{altura}")

  embed.add_field(name="Exemplo", value=url_image, inline="False")

  embed.set_image(url=url_image)

  ##await ctx.send(embed=embed_image)
  message = await canalboasvindas.send(embed=embed)
  

## cargos por reação ##
@bot.event
async def on_reaction_add(reaction, user):
  if reaction.emoji == "🔴":
    role = user.guild.get_role(943859423959474197)
    await user.add_roles(role)
  elif reaction.emoji == "🟠":
    role = user.guild.get_role(943859422252384298)
    await user.add_roles(role)
  
## Reaction Roles ##
@bot.command(name="foto")
async def get_random_image(ctx):
  url_image="https://picsum.photos/1920/1080"

  embed = discord.Embed(
    title = "Resultado da busca de imagens",
    description = f"A busca é totalmente aleatoria",
    color = 0x0000FF,
  )

  embed.set_author(name=bot.user.name, icon_url=f"{bot.user.avatar_url}")
  embed.set_footer(text=f"Feito por {bot.user.name}")

  embed.add_field(name="API", value="Usamos a API do https://picsum.photos")
  embed.add_field(name="Parâmetros", value="{largura}/{altura}")

  embed.add_field(name="Exemplo", value=url_image, inline="False")

  embed.set_image(url=url_image)

  await ctx.send(embed=embed)


## recuperando TOKEN ##
bot.run(os.getenv('TOKEN'))