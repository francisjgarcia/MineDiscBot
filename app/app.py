import discord
from discord.ext import commands
from discord.ext import tasks
import requests
import asyncio
from settings import status_api_url, discord_bot_token, discord_play_game, discord_status_channel_id, discord_players_channel_id

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online, activity=discord.Game(discord_play_game))
  ping.start()

@tasks.loop(seconds=60)
async def ping():
  global status, status_channel, status_channel
  try:
    response = requests.get(status_api_url+'/status', timeout=5)
    if response.status_code == 200:
      status = response.json().get('status')
    else:
      print("La solicitud no fue exitosa. Código de estado:", response.status_code)
  except requests.exceptions.RequestException as e:
      print("Error al realizar la solicitud:", e)
  try:
    status_channel=str(bot.get_channel(discord_status_channel_id)).split(': ')[1]
  except AttributeError:
    print("Error al obtener el canal de estado.")
  try:
    if status != status_channel:
      canal = bot.get_channel(discord_status_channel_id)
      if isinstance(canal, discord.VoiceChannel):
        try:
          await canal.edit(name=f"Estado: {status}")
          print(f"Cambiando estado de Discord a {status}")
        except discord.Forbidden:
          print("No tengo permisos para cambiar el nombre del canal de voz.")
      else:
        print("No se encontró un canal de voz con ese ID0.")
      status_channel=str(bot.get_channel(discord_status_channel_id)).split(': ')[1]
  except AttributeError:
    print ('Ha sucedido un error al actualizar el estado del servidor de Minecraft en Discord.')
  try:
    if status == "Online":
      players = requests.get(status_api_url+'/players').json()
      players_channel=str(bot.get_channel(discord_players_channel_id)).split(': ')[1]
      current_players=(f"{players['players_online']}/{players['players_max']}")
      if current_players != players_channel:
        canal = bot.get_channel(discord_players_channel_id)
        if isinstance(canal, discord.VoiceChannel):
            try:
              await canal.edit(name=f"Jugadores: {players['players_online']}/{players['players_max']}")
              print(f"Cambiando número de jugadores del servidor de Minecraft en Discord a: {players['players_online']}/{players['players_max']}")
            except discord.Forbidden:
              print("No tengo permisos para cambiar el nombre del canal de voz.")
            else:
              print("No se encontró un canal de voz con ese ID1.")
    if status == "Offline" and status_channel == "Offline":
      players_channel=str(bot.get_channel(discord_players_channel_id)).split(': ')[1]
      if players_channel != "0/0":
        canal = bot.get_channel(discord_players_channel_id)
        if isinstance(canal, discord.VoiceChannel):
          try:
            await canal.edit(name=f"Jugadores: 0/0")
            print(f"Reseteando número de jugadores del servidor de Minecraft en Discord a 0.")
          except discord.Forbidden:
            print("No tengo permisos para cambiar el nombre del canal de voz.")
          else:
            print("No se encontró un canal de voz con ese ID2.")
  except AttributeError:
    print ('Ha sucedido un error al actualizar el estado de los canales en Discord.')

bot.run(discord_bot_token)
