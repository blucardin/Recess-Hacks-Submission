
def run(bot): 
    
    @bot.command(name='Typingtest', help = "Meant for testing, should returen \"testingTyping, testingTyping, testingTyping\" ")
    async def Typingtest(ctx):

        await ctx.send("testingTyping, testingTyping, testingTyping")