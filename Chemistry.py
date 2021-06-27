import random
import time 
from discord.ext import commands
import discord
import leaderboard

element_symboles = ["H",       "He",     "Li" ,     "Be",       "B",         "C",       "N",    "O",        "F",      "Ne",     "Na",    "Mg",       "Al",      "Si",       "P",            "S",     "Cl",      "Ar",   "K",            "Ca",   "Sc",       "Ti",           "V",        "Cr",   "Mn",           "Fe", "Co",     "Ni",       "Cu",   "Zn",   "Ga",       "Ge",       "As",       "Se",       "Br",       "Kr",   "Rb",       "Sr",           "Y",        "Zr",       "Nb",       "Mo",       "Tc",       "Ru",       "Rh",       "Pd",           "Ag",     "Cd",    "In",     "Sn",    "Sb",      "Te",         "I",      "Xe",    "Cs",     "Ba",    "Lu",       "Hf",      "Ta",     "W",          "Re",     "Os",     "Ir",       "Pt",       "Au",   "Hg",       "Tl",       "Pb",   "Bi",       "Po",     "At",       "Rn",     "Fr",       "Ra",       "Lr",       "Rf",           "Db",       "Sg",       "Bh",       "Hs",        "Mt",      "Ds",           "Rg",           "Cn",           "Nh",       "Fl",       "Mc",       "Lv",           "Ts",       "Og",       ]
element_names = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron" , "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Plantinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Framcium", "Radium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"]

def run(bot): 

    class ChemistryCommands(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self.dict = dict()
            self.starttime = 0
            self.index = 0
            self.tries = 0
            self.quiztype = None

        @bot.command(name='Chemtest', help = "Meant for testing, should returen \"testingChem, testingChem, testingChem\" ")
        async def Chemtest(self, ctx):
            await ctx.send("testingChem, testingChem, testingChem")

        @bot.command(name='Chemistry_symbols_quiz', aliases=["csquiz"], help = "A fun Periodic table symbols quiz. Find the right symbol to match the given element.")
        async def Chemistry_symbols_quiz(self, ctx):
            uid = ctx.author.id
            def check(obj): 
                return uid == obj.author.id


            localindex = random.randint(0, len(element_symboles) - 1)        
            self.dict[uid] = {
                "tries" : 0, 
                "starttime" : time.time() , 
                "index" : localindex, 
            }
            await ctx.send("What is the symbol for this element? \n %s "%element_names[self.dict[uid]["index"]])

            while self.dict[uid]["tries"] <= 4:
                contract = await self.bot.wait_for('message', check=check)
                if contract.content == element_symboles[self.dict[uid]["index"]]:
                    timetaken = time.time() - self.dict[uid]["starttime"]  
                    await ctx.send("That is correct! \n You guessed it in %s seconds! \n It took you %s tries!"%(timetaken, self.dict[uid]["tries"]))
                    leaderboard.add_to_score(str(ctx.author), (500 - timetaken) - (self.tries * 50) )
                    return
                else: 
                    await ctx.send("That is incorrect. You have %s tries left"% (4 - (self.dict[uid]["tries"])))
                    self.dict[uid]["tries"] += 1

            await ctx.send("Sorry, you ran out of tries. The answer we were looking for was: %s"%(element_symboles[self.dict[uid]["index"]]))


        @bot.command(name='Chemistry_elements_quiz', aliases=["cequiz"], help = "A fun Periodic table elements quiz. Find the right element to match the given symbol")
        async def Chemistry_elements_quiz(self, ctx):
            uid = ctx.author.id
            def check(obj): 
                return uid == obj.author.id


            localindex = random.randint(0, len(element_symboles) - 1)        
            self.dict[uid] = {
                "tries" : 0, 
                "starttime" : time.time() , 
                "index" : localindex, 
            }
            await ctx.send("What is the element with this symbol? \n %s "%element_symboles[self.dict[uid]["index"]])

            while self.dict[uid]["tries"] <= 4:
                contract = await self.bot.wait_for('message', check=check)
                if contract.content == element_names[self.dict[uid]["index"]]:
                    timetaken = time.time() - self.dict[uid]["starttime"]  
                    await ctx.send("That is correct! \n You guessed it in %s seconds! \n It took you %s tries!"%(timetaken, self.dict[uid]["tries"]))
                    leaderboard.add_to_score(str(ctx.author), (500 - timetaken) - (self.dict[uid]["tries"] * 50) )
                    return
                else: 
                    await ctx.send("That is incorrect. You have %s tries left"% (4 - (self.dict[uid]["tries"])))
                    self.dict[uid]["tries"] += 1

           
            await ctx.send("Sorry, you ran out of tries. The answer we were looking for was: %s"%(element_names[self.dict[uid]["index"]]))
        

    bot.add_cog(ChemistryCommands(bot))

        




    



