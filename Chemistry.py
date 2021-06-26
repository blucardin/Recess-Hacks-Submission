import random
import time 
from discord.ext import commands
import discord
import leaderboard

element_symboles = ["H", "He", "Li" , "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No"]
element_names = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron" , "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Terbium", "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Curium", "Berkelium", "Californium", "Ensteinium", "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson" ] 

def run(bot): 

    class ChemistryCommands(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self.starttime = 0
            self.index = 0
            self.tries = 0
            self.quiztype = None

        @bot.command(name='Chemtest', help = "Meant for testing, should returen \"testingChem, testingChem, testingChem\" ")
        async def Chemtest(self, ctx):
            await ctx.send("testingChem, testingChem, testingChem")

        @bot.command(name='Chemistry_symbols_quiz', help = "A fun Periodic table symbols quiz")
        async def Chemistry_symbols_quiz(self, ctx):
            self.tires = 0
            self.starttime = time.time()
            self.index  = random.randint(0, len(element_symboles) - 1)
            self.quiztype = 'Chemistry_symbols_quiz'
            await ctx.send(f"What is the element with this symbol? \n {element_symboles[self.index]} ")


        @bot.command(name='Chemistry_elements_quiz', help = "A fun Periodic table elements quiz")
        async def Chemistry_elements_quiz(self, ctx):
            self.tires = 0
            self.starttime = time.time()
            self.index = random.randint(0, len(element_symboles) - 1)
            self.quiztype = "Chemistry_elements_quiz"
            await ctx.send(f"What is the symbol for this element? \n {element_names[self.index]} ")
        

        @bot.command(name='Chemistry_answers', help = "Answer command for Chemistry quizzes")
        async def Chemistry_answers(self, ctx, message): 

            if self.quiztype == 'Chemistry_symbols_quiz':
                    if message == element_names[self.index]: 
                        timetaken = time.time() - self.starttime 
                        await ctx.send(f"That is correct! \n You guessed it in {timetaken} seconds! \n It took you {self.tries} tires!")
                        leaderboard.add_to_score(discord.Message.author.name, (500 - timetaken) - (self.tries * 100) )
                        print(ctx.message.author)
                        self.tries = 0
                    else: 
                        self.tries += 1 
                        await ctx.send(f"That was incorrect, try again. You have {(4 - self.tries) + 1} tries left")

            if self.quiztype == 'Chemistry_elements_quiz':
                if self.tries <= 4: 
                    if message == element_symboles[self.index]: 
                        await ctx.send(f"That is correct! \n You guessed it in {time.time() - self.starttime } seconds! \n It took you {self.tries} tires!")
                        self.tries = 0
                    else: 
                        self.tries += 1 
                        await ctx.send(f"That was incorrect, try again. You have {(4 - self.tries) + 1} tries left")

    bot.add_cog(ChemistryCommands(bot))

        




    



