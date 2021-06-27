from discord.ext import commands
import discord
import random
import time
import leaderboard


text_images_path = ["Images for typing Challenge/Screen Shot 2021-06-26 at 10.55.01 AM.png", "Images for typing Challenge/Screen Shot 2021-06-26 at 11.52.05 AM.png", "Images for typing Challenge/Capture1.PNG",                  "Images for typing Challenge/capture2.PNG",         "Images for typing Challenge/Capture.PNG", "Images for typing Challenge/Capture11.PNG",                                  "Images for typing Challenge/Capture2232e.PNG", "Images for typing Challenge/gyuhawdjik;l.PNG",                            "Images for typing Challenge/tfgyhawjok.PNG",  "Images for typing Challenge/fawgjio0kp.PNG",                            "Images for typing Challenge/ftaguwydjio.PNG",              "Images for typing Challenge/wuaijda-.PNG"]
text = ["The scientific term for brain freeze is \"sphenopalatine ganglioneuralgia\".", "The only letter that doesn\'t appear on the periodic table is J.",            "A single strand of Spaghetti is called a \"Spaghetto\".",   "At birth, a baby panda is smaller than a mouse.", "Iceland does not have a railway system.", "The tongue is the only muscle in one’s body that is attached from one end.", "Violin bows are commonly made from horse hair.", "The color red doesn’t really make bulls angry; they are color-blind.", "Lettuce is a member of the sunflower family.", "The average American child is given $3.70 per tooth that falls out.", "If you heat up a magnet, it will lose its magnetism.", "Videogames have been found to be more effective at battling depression than therapy.", "It is thought by Russians that eating ice cream will keep you warm." ]

def run(bot): 
    
    class Trypingcommands(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self.dict = dict()
            self.index = 0
            self.starttime = None
            self.tries = 0

        @bot.command(name='Typingtest', help = "Meant for testing, should returen \"testingTyping, testingTyping, testingTyping\" ")
        async def Typingtest(self, ctx):

            await ctx.send("testingTyping, testingTyping, testingTyping")

        @bot.command(name='Typing_Challenge', help = "A fun typing speed quiz!")
        async def Typing_Challenge(self, ctx):
            uid = ctx.author.id
            def check(obj): 
                return uid == obj.author.id  

            self.dict[uid] = {
                "tries" : 0, 
                "starttime" : time.time() , 
                "index" : self.index
            }
            await ctx.send("Print the following text in the chat",  file=discord.File(text_images_path[self.dict[uid]["index"]]))

            while self.dict[uid]["tries"] <= 4:
                contract = await self.bot.wait_for('message', check=check)
                if contract.content == text[self.dict[uid]["index"]]:
                    timetaken = time.time() - self.dict[uid]["starttime"]  
                    await ctx.send("That is correct! \n You guessed it in %s seconds! \n It took you %s tries!"%(timetaken, self.dict[uid]["tries"]))
                    leaderboard.add_to_score(str(ctx.author), (500 - timetaken) - (self.dict[uid]["tries"] * 50) )
                    self.index += 1
                    return

                else: 
                    await ctx.send("That is incorrect. You have %s tries left"% (4 - (self.dict[uid]["tries"])))
                    self.dict[uid]["tries"] += 1

            
            await ctx.send("Sorry, you ran out of tries. The answer we were looking for was: %s"%(text[self.dict[uid]["index"]]))
            self.index += 1
    
    bot.add_cog(Trypingcommands(bot))