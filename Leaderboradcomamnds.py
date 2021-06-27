from discord.ext import commands
import discord
import leaderboard

def run(bot): 

    class Leaderboard(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @bot.command(name='Leadertest', help = "Meant for testing, should return \"testingleader, testingleader, testingleader\" ", pass_context=True)
        async def Leadertest(self, ctx):
            await ctx.send("testingleader, testingleader, testingleader")

        @bot.command(name='retrivescore', help = "Retrive a player's score. Your score goes up the more correct answers you get on the quizzes.")
        async def retrivescore(self, ctx, user):
            score = leaderboard.retrivescore(user)
            if score == "Player not in database": 
                await ctx.send("Sorry, that player is not in the database. Play some games and earn some points to be added.")
            else: 
                await ctx.send(leaderboard.retrivescore(user))

        @bot.command(name='show_all_scores', help = "Retrive all players scores")
        async def show_all_scores(self, ctx):
            for x in range(0, (len(leaderboard.listplayers))):
                await ctx.send(leaderboard.printrow(x))

    bot.add_cog(Leaderboard(bot))

            

            