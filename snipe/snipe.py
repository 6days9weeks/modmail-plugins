P='{0.name}#{0.discriminator}'
O='There is nothing to snipe!'
N=str
J='id'
H='attachment'
G='channel'
F='guild'
E='author'
D='content'
A=None
import asyncio as K
from io import BytesIO as L
import discord as I
from discord.ext import commands as C
snipe={J:A,D:A,E:A,H:A,F:A,G:A}
B={E:A,D:A,F:A,G:A}
class M(C.Cog):
	def __init__(A,bot):A.bot=bot
	@C.Cog.listener()
	async def on_message_delete(self,message):
		B=message
		if B.author.bot:return
		global snipe;snipe[J]=B.id;snipe[E]=B.author;snipe[D]=B.content;snipe[F]=B.guild;snipe[G]=B.channel
		if B.attachments:snipe[H]=B.attachments[0].proxy_url
		await K.sleep(60)
		if B.id==snipe[J]:snipe[J]=A;snipe[E]=A;snipe[D]=A;snipe[H]=A;snipe[F]=A;snipe[G]=A
	@C.Cog.listener()
	async def on_message_edit(self,before,after):
		C=before;global B
		if C.author.bot:return
		B[E]=C.author;B[D]=C.content;B[F]=C.guild;B[G]=C.channel;await K.sleep(60)
		if C.id==after.id:B[E]=A;B[D]=A;B[F]=A;B[G]=A
	@C.command(aliases=['imagesnipe'])
	@C.cooldown(1,10,C.BucketType.member)
	async def snipe(self,ctx):
		B=ctx;global snipe
		if snipe[F]!=B.guild or snipe[G]!=B.channel or snipe[D]==A:K=I.Embed(color=16764365,description=O);M=await B.send(embed=K);return await M.delete(delay=4)
		C=I.Embed(description=N(snipe[D]),colour=16764365);C.set_author(name=P.format(snipe[E]),icon_url=snipe[E].avatar_url);C.set_footer(text=f"sniped by {B.author.name}#{B.author.discriminator}",icon_url=B.author.avatar_url)
		if snipe[H]is not A:
			async with self.bot.session.get(snipe[H])as Q:J=L(await Q.read())
			C.set_image(url='attachment://snipe.jpg');await B.send(embed=C,file=I.File(J,filename='snipe.jpg'));snipe[H]=A;J.close()
		else:await B.send(embed=C);snipe[H]=A
	@C.command(aliases=['esnipe'])
	@C.cooldown(1,10,C.BucketType.member)
	async def editsnipe(self,ctx):
		C=ctx
		if B[F]!=C.guild or B[G]!=C.channel or B[D]==A:J=I.Embed(color=16764365,description=O);K=await C.send(embed=J);return await K.delete(delay=4)
		H=I.Embed(description=N(B[D]),colour=16764365);H.set_footer(text=f"sniped by {C.author.name}#{C.author.discriminator}",icon_url=C.author.avatar_url);H.set_author(name=P.format(B[E]),icon_url=B[E].avatar_url);await C.send(embed=H)
def Q(bot):bot.add_cog(M(bot))
