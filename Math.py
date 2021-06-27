import random
import time 
from discord.ext import commands
import discord
import leaderboard

def run(bot): 

    class Mathcommands(commands.Cog):
        def init(self, bot):
            self.bot = bot
            self.dict = dict()
            self.starttime = 0
            self.index = 0
            self.tries = 0
            self.quiztype = None

        @bot.command(name='Mathtest', help = "Meant for testing, should returen testingMath, testingMath, testingMath ")
        async def Mathtest(self, ctx):
            await ctx.send("testingMath, testingMath, testingMath")

        @bot.command(name='Math_Quiz', help = "A fun math subtration and addition quiz")
        async def Math_Quiz(self, ctx, startrange, endrange):
            signs = ["+", "-" , "*" ,"/"]
            x = str(random.randint(int(startrange), int(endrange)))
            y = str(random.randint(int(startrange), int(endrange)))
            self.equasion = str(x) + " " + random.choice(signs) + " " + str(y)
            print(self.equasion)
            print(eval(self.equasion))
            self.starttime = time.time()
            await ctx.send(f"Solve: " +  self.equasion)
            self.tries = 0


        @bot.command(name='Math_answers', help = "Answers for math quiz")
        async def Math_answers(self, ctx, message): 
                if self.tries <= 4:
                    print(int(message))
                    if int(message) == eval(self.equasion): 
                        timetaken = time.time() - self.starttime 
                        
                        await ctx.send(f"That is correct! \n You guessed it in {timetaken} seconds! \n It took you {self.tries} tires!")
                        leaderboard.add_to_score(str(ctx.author), (500 - timetaken) - (self.tries * 100)) 
                        self.tries = "no quesiton"
                    else: 
                        self.tries += 1 
                        await ctx.send(f"That was incorrect, try again. You have {(4 - self.tries) + 1} tries left")

                elif self.tries == "no quesiton": 
                    await ctx.send("No quesiton has been requested, request a question with %Math_Quiz")

                else:
                    await ctx.send("Sorry, you ran out of tries")
                    self.tries = "no quesiton"


    bot.add_cog(Mathcommands(bot))