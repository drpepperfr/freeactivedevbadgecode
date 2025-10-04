import discord
from discord import app_commands
from discord.ext import commands 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="?", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} commands.")

@bot.tree.command(name="activedevbadge", description="active dev badge claim")
async def hi(interaction: discord.Interaction):
    await interaction.response.send_message("free active dev badge: https://discord.com/developers/active-developer")

@bot.command()
async def activedevbadge(ctx):
    await ctx.send("Free active dev badge: https://discord.com/developers/active-developer")

bot.run("bot token here")
