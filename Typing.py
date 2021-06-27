from discord.ext import commands
import discord
import random
import time
import leaderboard

def run(bot): 
    
    class Trypingcommands(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self.text_images_path = ["Images for typing Challenge/Screen Shot 2021-06-26 at 10.55.01 AM.png", "Images for typing Challenge/Screen Shot 2021-06-26 at 11.52.05 AM.png", "Images for typing Challenge/Capture1.PNG",                  "Images for typing Challenge/capture2.PNG",         "Images for typing Challenge/Capture.PNG", "Images for typing Challenge/Capture11.PNG",                                  "Images for typing Challenge/Capture2232e.PNG", "Images for typing Challenge/gyuhawdjik;l.PNG",                            "Images for typing Challenge/tfgyhawjok.PNG",  "Images for typing Challenge/fawgjio0kp.PNG",                            "Images for typing Challenge/ftaguwydjio.PNG",              "Images for typing Challenge/wuaijda-.PNG"]
            self.text = ["The scientific term for brain freeze is \"sphenopalatine ganglioneuralgia\".", "The only letter that doesn\'t appear on the periodic table is J.",            "A single strand of Spaghetti is called a \"Spaghetto\".",   "At birth, a baby panda is smaller than a mouse.", "Iceland does not have a railway system.", "The tongue is the only muscle in one’s body that is attached from one end.", "Violin bows are commonly made from horse hair.", "The color red doesn’t really make bulls angry; they are color-blind.", "Lettuce is a member of the sunflower family.", "The average American child is given $3.70 per tooth that falls out.", "If you heat up a magnet, it will lose its magnetism.", "Videogames have been found to be more effective at battling depression than therapy.", "It is thought by Russians that eating ice cream will keep you warm." ]
            self.index = None
            self.starttime = None
            self.tries = 0

        @bot.command(name='Typingtest', help = "Meant for testing, should returen \"testingTyping, testingTyping, testingTyping\" ")
        async def Typingtest(self, ctx):

            await ctx.send("testingTyping, testingTyping, testingTyping")

        @bot.command(name='Typing_Challenge', help = "A fun typing speed quiz!")
        async def Typing_Challenge(self, ctx):
            self.index = random.randint(0, (len(self.text_images_path) - 1))
            self.starttime = time.time()
            await ctx.send("Print the following text in the chat",  file=discord.File(self.text_images_path[self.index]))
            await ctx.send("Make sure to respond with %Type_answers")

        @bot.command(name='Type_answers', help = "Answer command for typing speed quiz!")
        async def Type_answers(self, ctx, *, args=None):
            hearts = (':heart:', ':orange_heart:', ':yellow_heart:',
              ':green_heart:', ':blue_heart:', ':purple_heart:')

            if args:
                if self.tries <= 4: 
                    if args == self.text[self.index]: 
                        timetaken = time.time() - self.starttime
                        await ctx.send(f"That is correct! \n You guessed it in {timetaken} seconds! \n It took you {self.tries} tries!")
                        self.tries = 0
                        leaderboard.add_to_score(str(ctx.author), (500 - timetaken) - (self.tries * 50))
                    else: 
                        self.tries += 1 
                        await ctx.send(f"That was incorrect, try again. You have {(4 - self.tries) + 1} tries left")

        

    
    bot.add_cog(Trypingcommands(bot))