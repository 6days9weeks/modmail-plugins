import discord
from discord.ext import commands
import nekos
from core import checks
from core.models import PermissionLevel


class Action(commands.Cog):
    """
    Some action commands
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def kiss(self, ctx, *, user: discord.Member):
        """Kiss a user!"""

        author = ctx.message.author
        kisses = nekos.img('kiss')

        # Building Embed
        embed = discord.Embed(color=self.bot.main_color)
        embed.description = f"**{author.mention} kisses {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=kisses)
        await ctx.send(embed=embed)
        
   
    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def pat(self, ctx, *, user: discord.Member):
        """Pat a user!"""

        author = ctx.message.author
        pats = nekos.img('pat')

        # Building Embed
        embed = discord.Embed(color=self.bot.main_color)
        embed.description = f"**{author.mention} pats {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=pats)
        await ctx.send(embed=embed)     

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def hug(self, ctx, *, user: discord.Member):
        """Hug a user!"""

        author = ctx.message.author
        hugs = nekos.img('hug')

        # Building The Embed
        embed = discord.Embed(color=self.bot.main_color)
        embed.description = f"**{author.mention} hugs {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=hugs)
        await ctx.send(embed=embed)

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def slap(self, ctx, *, user: discord.Member):
        """Slap a user!"""

        author = ctx.message.author
        slaps = nekos.img('slap')

        # Building The Embed
        embed = discord.Embed(color=self.bot.main_color)
        embed.description = f"**{author.mention} slap {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=slaps)
        await ctx.send(embed=embed)        

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def baka(self, ctx, *, user: discord.Member):
        """Call a user baka!"""

        author = ctx.message.author
        bakas = nekos.img('baka')

        # Building The Embed
        embed = discord.Embed(color=self.bot.main_color)
        embed.description = f"**{author.mention} calls {user.mention} baka**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=bakas)
        await ctx.send(embed=embed)  


    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def tickle(self, ctx, *, user: discord.Member):
        """Tickles a user!"""

        author = ctx.message.author
        tickles = nekos.img('tickle')

        # Building The Embed
        embed = discord.Embed(color=self.bot.main_color)
        embed.description = f"**{author.mention} tickles {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=tickles)
        await ctx.send(embed=embed)

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def smug(self, ctx, *, user: discord.Member):
        """Smug at a user!"""

        author = ctx.message.author
        smugs = nekos.img('smug')

        # Building The Embed
        embed = discord.Embed(color=self.bot.main_color)
        embed.description = f"**{author.name} smugs at {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=smugs)
        await ctx.send(embed=embed)        

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def cuddle(self, ctx, *, user: discord.Member):
        """Cuddle a user!"""

        author = ctx.message.author
        cuddles = nekos.img('cuddle')

        # Building The Embed
        embed = discord.Embed(color=self.bot.main_color)
        embed.description = f"**{author.mention} cuddles {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=cuddles)
        await ctx.send(embed=embed)   

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def poke(self, ctx, *, user: discord.Member):
        """Poke a user!"""

        author = ctx.message.author
        pokes = nekos.img('poke')

        # Building The Embed
        embed = discord.Embed(color=self.bot.main_color)
        embed.description = f"**{author.mention} pokes {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=pokes)
        await ctx.send(embed=embed)        

    @commands.command()
    @checks.has_permissions(PermissionLevel.REGULAR)
    async def feed(self, ctx, *, user: discord.Member):
        """Feed a user!"""

        author = ctx.message.author
        feeds = nekos.img('feed')

        # Building The Embed
        embed = discord.Embed(color=self.bot.main_color)
        embed.description = f"**{author.mention} feeds {user.mention}**"
        embed.set_footer(text="Made with the help of nekos.life")
        embed.set_image(url=feeds)
        await ctx.send(embed=embed)        
        
def setup(bot):
    bot.add_cog(Action(bot))     
