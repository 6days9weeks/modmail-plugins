import datetime

import discord
import humanize
import pytz
from discord.ext import commands, tasks


# Credits to https://github.com/Cog-Creators/Red-DiscordBot/blob/ded5aff08cfe443498770e7f27035db694e72c30/redbot/core/utils/chat_formatting.py#L86
def box(text: str, lang: str = "") -> str:
    """Get the given text in a code block.
    Parameters
    ----------
    text : str
        The text to be marked up.
    lang : `str`, optional
        The syntax highlighting language for the codeblock.
    Returns
    -------
    str
        The marked up text.
    """
    ret = "```{}\n{}```".format(lang, text)
    return ret


class Genshin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.coll = bot.plugin_db.get_partition(self)
        self._status_embed.start()
        self.channel = None
        self.message = None
        self.image = None
        self.bot.loop.create_task(self.cog_load())

    def cog_unload(self):
        """Cancel the loop when the cog is unloaded"""
        self._status_embed.cancel()

    async def cog_load(self):
        await self.obtain_shit()

    @tasks.loop(minutes=1)
    async def _status_embed(self):
        if self.message != None:
            await self.edit_embed()

    @staticmethod
    def natime():
        """Get time left for daily in NA till 4am their time."""
        now = datetime.datetime.now(pytz.timezone("America/Chicago"))
        utc_time_for_tz_loop: datetime.datetime = (
            datetime.datetime.combine(
                now.date() + datetime.timedelta(days=1), datetime.time(hour=4)
            )
            - now.utcoffset()
        )
        delta = utc_time_for_tz_loop - datetime.datetime.utcnow()
        return humanize.time.precisedelta(delta, minimum_unit="minutes", format="%0.f")

    @staticmethod
    def natimew():
        """Get time left for weekly in NA till 4am their time."""
        now = datetime.datetime.now(pytz.timezone("America/Chicago"))
        utc_time_for_tz_loop: datetime.datetime = (
            datetime.datetime.combine(
                now.date() + datetime.timedelta(days=7 - now.weekday()), datetime.time(hour=4)
            )
            - now.utcoffset()
        )
        delta = utc_time_for_tz_loop - datetime.datetime.utcnow()
        return humanize.time.precisedelta(delta, minimum_unit="minutes", format="%0.f")

    @staticmethod
    def asartime():
        """Get time left for daily in Asia/SAR till 4am their time."""
        now = datetime.datetime.now(pytz.timezone("Asia/Hong_Kong"))
        utc_time_for_tz_loop: datetime.datetime = (
            datetime.datetime.combine(
                now.date() + datetime.timedelta(days=1), datetime.time(hour=4)
            )
            - now.utcoffset()
        )
        delta = utc_time_for_tz_loop - datetime.datetime.utcnow()
        return humanize.time.precisedelta(delta, minimum_unit="minutes", format="%0.f")

    @staticmethod
    def asartimew():
        """Get time left for weekly in Asia/SAR till 4am their time."""
        now = datetime.datetime.now(pytz.timezone("Asia/Hong_Kong"))
        utc_time_for_tz_loop: datetime.datetime = (
            datetime.datetime.combine(
                now.date() + datetime.timedelta(days=7 - now.weekday()), datetime.time(hour=4)
            )
            - now.utcoffset()
        )
        delta = utc_time_for_tz_loop - datetime.datetime.utcnow()
        return humanize.time.precisedelta(delta, minimum_unit="minutes", format="%0.f")

    @staticmethod
    def eutime():
        """Get time left for daily in EU till 4am their time."""
        now = datetime.datetime.now(pytz.timezone("Europe/Dublin"))
        time_for_4_am: datetime.datetime = (
            datetime.datetime.combine(
                now.date() + datetime.timedelta(days=0), datetime.time(hour=4)
            )
        )
        delta = pytz.timezone("Europe/Dublin").localize(time_for_4_am) - datetime.datetime.now(pytz.timezone("Europe/Dublin"))
        return humanize.time.precisedelta(delta, minimum_unit="minutes", format="%0.f")

    @staticmethod
    def eutimew():
        """Get time left for weekly in EU till 4am their time."""
        now = datetime.datetime.now(pytz.timezone("Europe/Dublin"))
        utc_time_for_tz_loop: datetime.datetime = (
            datetime.datetime.combine(
                now.date() + datetime.timedelta(days=7 - now.weekday()), datetime.time(hour=4)
            )
            - now.utcoffset()
        )
        delta = utc_time_for_tz_loop - datetime.datetime.utcnow()
        return humanize.time.precisedelta(delta, minimum_unit="minutes", format="%0.f")

    @staticmethod
    async def status_embed(self):
        """The status embed or smth"""
        embed = discord.Embed(
            title="Server Status",
            description="Members: {}".format(self.bot.modmail_guild.member_count),
            timestamp=datetime.datetime.utcnow(),
        )
        embed.add_field(
            name="Server Time:",
            value="{NA}• Daily reset in {NADaily}\n• Weekly reset in {NAWeekly}\n{EU}• Daily reset in {EUDaily}\n• Weekly reset in {EUWeekly}\n{ASI}• Daily reset in {ASIDaily}\n• Weekly reset in {ASIWeekly}\n{SAR}• Daily reset in {SARDaily}\n• Weekly reset in {SARWeekly}".format(
                NA=box(
                    "# NA "
                    + datetime.datetime.now(pytz.timezone("America/Chicago")).strftime("%I:%M %p"),
                    "md",
                ),
                NADaily=self.natime(),
                NAWeekly=self.natimew(),
                EU=box(
                    "# EU "
                    + datetime.datetime.now(pytz.timezone("Europe/Dublin")).strftime("%I:%M %p")
                ),
                EUDaily=self.eutime(),
                EUWeekly=self.eutimew(),
                ASI=box(
                    "# ASIA "
                    + datetime.datetime.now(pytz.timezone("Asia/Hong_Kong")).strftime("%I:%M %p"),
                    "glsl",
                ),
                ASIDaily=self.asartime(),
                ASIWeekly=self.asartimew(),
                SAR=box(
                    "# SAR "
                    + datetime.datetime.now(pytz.timezone("Asia/Hong_Kong")).strftime("%I:%M %p"),
                    "fix",
                ),
                SARDaily=self.asartime(),
                SARWeekly=self.asartimew(),
            ),
        )
        if self.image != None:
            url = self.image + "?size=4096"
        else:
            url = "https://cdn.discordapp.com/banners/522681957373575168/e5ff2cb0b8c102ee4f2e1f02b728bc99.webp?size=2048"
        embed.set_image(url=url)
        return embed

    async def edit_embed(self):
        chan = self.bot.get_channel(self.channel)
        msg = await chan.fetch_message(self.message)
        await msg.edit(embed=await self.status_embed(self))

    async def obtain_shit(self):
        config = await self.coll.find_one({"_id": "config"})
        try:
            self.channel = int(config["status-channel"]["channel"]) or None
            self.message = int(config["status-embed"]["message"]) or None
            self.image = config["image-url"]["url"] or None
        except Exception:
            pass

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def setstatuschan(self, ctx, *, channel: discord.TextChannel):
        """Set status channel."""
        message = await self.bot.get_channel(channel.id).send(
            embed=discord.Embed(
                title="This is a test embed which will be gone in few minutes. Please don't delete it. This will be the status embed.",
                color=0xFFCDCD,
            )
        )
        await self.coll.find_one_and_update(
            {"_id": "config"},
            {"$set": {"status-channel": {"channel": str(channel.id)}}},
            upsert=True,
        )
        await self.coll.find_one_and_update(
            {"_id": "config"},
            {"$set": {"status-embed": {"message": str(message.id)}}},
            upsert=True,
        )
        embed = discord.Embed(
            title=f"The status channel has been set to #{channel}.\nThe status function will auto-start now.",
            color=0xFFCDCD,
        )
        embed.set_footer(text="you're amazing~!!")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def seturl(self, ctx, url):
        """Provide an image url for the status embed"""
        if (
            url.endswith(".png")
            or url.endswith(".jpeg")
            or url.endswith(".gif")
            or url.endswith(".jpg")
            or url.endswith(".webp")
        ):
            await self.coll.find_one_and_update(
                {"_id": "config"},
                {"$set": {"image-url": {"url": str(url)}}},
                upsert=True,
            )
            embed = discord.Embed(title=f"The image url has been set.", color=0xFFCDCD)
            embed.set_image(url=url)
            embed.set_footer(text="you're amazing~!!")
            await ctx.send(embed=embed)
        else:
            await ctx.reply("Give an valid url and it should be `png/jpeg/gif/jpg/webp`.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def imessedup(self, ctx):
        await self.obtain_shit()
        await ctx.reply("Should work.")

def setup(bot):
    cog = Genshin(bot)
    bot.add_cog(cog)
