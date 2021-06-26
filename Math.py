

def run(bot): 
    
    @bot.command(name='Mathtest', help = "Meant for testing, should returen \"testingMath, testingMath, testingMath\" ")
    async def Mathtest(ctx):

        await ctx.send("testingMath, testingMath, testingMath")