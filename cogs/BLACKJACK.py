# Blackjack gambaling game with controls for discord. 

#--------- Libaries ---------#

import discord, random, asyncio, sys
from discord.ext import commands
sys.path.append("../")
from tools.logging import ABLog
from tools.embeds import *
from settings import *

#--------- Variables ---------#

h_emoji = '\U0001f1ed'
p_emoji = '\U0001f1f5'

#--------- Code ---------#

class BlackJack(commands.Cog):

    #--------- Setup ---------#

    def __init__(self, client):
        self.client = client

    @commands.command(name='blackjack', aliases=['jack', 'black', 'cards']) # Initiates the game.
    async def blackjack(self, context):

        ABLog("Cards Delt.")

        class Deck(): #Allows for pulling of cards at random while also implimenting the cards.

            deck_cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2'] * 4

            def pick(self, num): #Pulls cards that haven't already been pulled. 
                picked = []

                for _ in range(num):
                    CHOSEN = random.randint(0, len(self.deck_cards) - 1)
                    picked.append(self.deck_cards[CHOSEN])
                    self.deck_cards.pop(CHOSEN)
                return picked

        class Player(Deck): #Simple player class allows for gambling and playing.
            cards = []
            burst = False

            def __init__(self):
                self.money = 500 #TODO add money!


        class Dealer(Deck): #Simple dealer class that allows for playing and checking it player has won.
            cards = []
            burst = False

        async def print_cards(cards): #Allows for showing of cards to be much easier.
            pcards = []
            for i in range(len(cards)):
                pcards.append(cards[i])
            return pcards

        async def print_board(PLAYERSCARDS, DEALERSCARDS):
            Playerscards = await print_cards(PLAYERSCARDS)
            DealersCards = await print_cards(DEALERSCARDS)
            Playerscards = ', '.join(str(x) for x in Playerscards)
            DealersCards = ', '.join(str(x) for x in DealersCards)
            await context.send(embed=TwoFieldEmbed(BlackJackName, ("Your Cards:", Playerscards), ("Dealer's Cards:", DealersCards),
                                    FooterText=f"Invoked by {context.author.name}", FooterIconURL=context.author.avatar_url), delete_after=8)
            

        def hCheck(reaction, user): #I don't know why I added this, I'm just too scared to remove it.
            return user == context.author

        def find_value(cards): #Finds and returns value of given hand of cards.
            card_value = []
            total = 0
            ace = False
            value_dict = {'A': 11, 'K': 10, 'Q': 10, 'J': 10, '10': 10,
            '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, }

            for i in range(len(cards)):
                card_value.append(value_dict[cards[i]])
                if cards[i] == 'A':
                    ace = True

            for i in range(len(card_value)):
                total += card_value[i]

            if total > 21 and ace:
                total -= 10

            return total

    #--------- Logic ---------#

        p1 = Player()
        d1 = Dealer()

        while True:
            
            p1.cards = p1.pick(2)
            d1.cards = d1.pick(1)

            dealer_won = False

            await print_board(p1.cards, d1.cards) #First board print.

            
            while True: #Player turns continues till he passes or bursts

                while True: #Asks player choice for action till a valid choice is put
                    MSG = await context.send("Do you want to hit or pass?", delete_after=8) #Add easy to use emoji controls. 
                    await MSG.add_reaction(h_emoji)
                    await MSG.add_reaction(p_emoji)
                    try:
                        reaction, user = await context.bot.wait_for('reaction_add', timeout=7.0, check=hCheck) #Waits for user input, if not given, closes games. 
                        break
                    except asyncio.TimeoutError:
                        ABLog("Player didn't respond in time, closing game.")
                        break

                if reaction.emoji == h_emoji: #Hits if player choses hit, passes and plays through the reset of the games if not.
                    p1.cards += p1.pick(1)
                    await print_board(p1.cards, d1.cards)
                else:
                    break

                if find_value(p1.cards) > 21: # Checks if player went over 21.
                    p1.burst = True
                    dealer_won = True
                    break

            
            if not dealer_won: #Dealer only plays if the player is not bursted yet
                while True:
                    d1.cards += d1.pick(1)
                    if find_value(d1.cards) > 21:
                        d1.burst = True
                        break

                    if find_value(d1.cards) > find_value(p1.cards):
                        dealer_won = True
                        break


            
            if dealer_won: #Winner determination and result printing 
                if p1.burst:
                    await context.channel.send(f"{context.author.name}, Your cards value exceeded 21")
                else:
                    await context.channel.send(f"{context.author.name}, Dealer won this time...")
            else:
                if d1.burst:
                    await context.channel.send(f"You won {context.author.name}! Congrats") #TODO add money

            break

def setup(client):
	client.add_cog(BlackJack(client))
