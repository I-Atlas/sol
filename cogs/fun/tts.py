# Imports
from discord.ext import commands


# Main Command Class
class Tts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.desc = "Sends tts message."
        self.usage = "tts [text]"

    @commands.command(name='tts', aliases=['t'])
    @commands.has_permissions()
    async def tts(self, ctx, *, text):
        await ctx.message.delete()
        if not text:
            return await ctx.send("Please specify something to say.")
        try:
            return await ctx.send(text, tts=True)
        except:
            return await ctx.send("I don't have permission to send TTS messages.")


# Link to bot
def setup(bot):
    bot.add_cog(Tts(bot))