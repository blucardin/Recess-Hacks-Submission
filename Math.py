import random
import time 
from discord.ext import commands
import discord
import leaderboard

def run(bot): 

    class Mathcommands(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self.dict = dict()
            self.starttime = 0
            self.tries = 0

        @bot.command(name='Mathtest', help = "Meant for testing, should returen testingMath, testingMath, testingMath ")
        async def Mathtest(self, ctx):
            await ctx.send("testingMath, testingMath, testingMath")

        @bot.command(name='Math_Quiz', help = "A fun math subtration, addition, multiplicaiton, and division quiz. Structure: %Math_Quiz [lowest_number] [highest_number]      Where [lowest_number] is the lowest possible number and [highest_number] is the highest possible number.")
        async def Math_Quiz(self, ctx, startrange, endrange):

            uid = ctx.author.id

            def check(obj): 
                return uid == obj.author.id   

            signs = ["+", "-" , "*" ,"/"]
            x = str(random.randint(int(startrange), int(endrange)))
            y = str(random.randint(int(startrange), int(endrange)))

            self.dict[uid] = {
                "tries" : 0, 
                "starttime" : time.time() , 
                "equasion" : str(x) + " " + random.choice(signs) + " " + str(y), 
            }

            await ctx.send(f"Solve: " + self.dict[uid]["equasion"])

            while self.dict[uid]["tries"] <= 4:
                contract = await self.bot.wait_for('message', check=check)
                if contract.content == str(eval(self.dict[uid]["equasion"])):
                    timetaken = time.time() - self.dict[uid]["starttime"]  
                    await ctx.send("That is correct! \n You guessed it in %s seconds! \n It took you %s tries!"%(timetaken, self.dict[uid]["tries"]))
                    leaderboard.add_to_score(str(ctx.author), (500 - timetaken) - (self.dict[uid]["tries"] * 50) )
                    return

                else: 
                    await ctx.send("That is incorrect. You have %s tries left"% (4 - (self.dict[uid]["tries"])))
                    self.dict[uid]["tries"] += 1

            
            await ctx.send("Sorry, you ran out of tries. The answer we were looking for was: %s"%(eval(self.dict[uid]["equasion"])))





    bot.add_cog(Mathcommands(bot))