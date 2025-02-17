import discord
from discord.ext import commands
import json
import aiohttp

with open('config.json', 'r') as settings_file:
    settings = json.load(settings_file)

embed_color = int(settings['embed_color'], 16)

class CatGirlSender(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="neko", description="Sends a random neko image",
                            integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    })
    async def catgirl(self, ctx):
        api_url = f"https://nekos.best/api/v2/neko"

        async with aiohttp.ClientSession() as session:
            async with session.get(api_url) as response:
                data = await response.json()
                image_url = data['results'][0]['url']

                embed = discord.Embed(
                    color=embed_color
                )
                embed.set_image(url=image_url)
                await ctx.respond(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(CatGirlSender(bot))
