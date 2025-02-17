import discord
from discord.ext import commands
import json


def load_config():
    with open('config.json', 'r') as f:
        return json.load(f)

config = load_config()
intents = discord.Intents.default()

bot = commands.Bot(intents=intents)

async def set_status():
    await bot.change_presence(activity=discord.Game(name=config['status']))


@bot.event
async def on_ready():
    await set_status()
    print(f'Logged in as {bot.user.name}')


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass   

# Load cogs
cogs = [
    "cogs.neko"
]

 
if __name__ == "__main__":
    for extension in cogs:
        try:
            bot.load_extension(extension)
            name = extension.split(".")[1]
            print(
                f"Loaded cog: {name}"
            )
        except Exception as e:
            print(
                f"Failed to load cog {extension}"
            )
            print(e)



bot.run(config['token'])