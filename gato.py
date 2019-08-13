from bot import recursion, combinations, argmax
from random import choice

class Gato:

    def __init__(self):
        self.player = []
        self.bot = []
        self.left = [i for i in range(1,10)]
        self.t = { i: "-" for i in range(1,10) }

    def reset(self):
        self.player = []
        self.bot = []
        self.left = [i for i in range(1,10)]
        self.t = { i: "-" for i in range(1,10) }

    def is_winner(self, p='player'):
        players = {'bot': self.bot, "player": self.player}
        if len(players[p]) > 2:
            trios = list(filter(lambda x : sum(x) == 15, combinations(players[p], 3)))
            if len(trios) > 0:
                return True
    
    def player_turn(self):
        while True:
            x = int(input("Position: "))
            if x in self.left: break
        self.left.remove(x)
        self.player.append(x)
        self.t[x] = 'O'

    def player_bot_turn(self):
        d = {'value': 0}
        recursion(self.player, self.bot, self.left, d)
        x = d['value']
        print(f"Bot eligio {x}")
        self.left.remove(x)
        self.player.append(x)
        self.t[x] = 'O'

    def dummy_turn(self):
        x = choice(self.left)
        self.left.remove(x)
        self.player.append(x)
        self.t[x] = 'O'

    def bot_turn(self):
        d = {'value': 0}
        recursion(self.player, self.bot, self.left, d)
        x = d['value']
        print(f"Bot eligio {x}")
        self.left.remove(x)
        self.bot.append(x)
        self.t[x] = 'X'

    def game(self):
        winner = False
        while not winner:
            self.print_tablero()
            print("Turno jugador")
            self.player_turn()

            if self.is_winner("player"):
                print("Gana jugador")
                self.bot_lose_report("Player")
                break

            if len(self.left) == 0:
                winner = True
                print("Empate")
                break

            self.print_tablero()
            print("Turno Bot")
            self.bot_turn()

            if self.is_winner('bot'):
                print("Gana robot") 
                break
        self.print_tablero()

    def game_2(self):            
        winner = False
        while not winner:
            self.print_tablero()
            print("Turno Bot")
            self.bot_turn()

            if self.is_winner('bot'):
                print("Gana robot") 
                break

            if len(self.left) == 0:
                winner = True
                print("Empate")
                break

            self.print_tablero()
            print("Turno jugador")
            self.player_turn()

            if self.is_winner("player"):
                print("Gana jugador")
                self.bot_lose_report("Bot parte")
                break
            
        self.print_tablero()

    def dummy_vs_bot(self):
        winner = False
        while not winner:
            self.print_tablero()
            print("Turno jugador")
            self.dummy_turn()

            if self.is_winner("player"):
                print("Gana jugador")
                self.bot_lose_report("Dummy")
                break

            if len(self.left) == 0:
                winner = True
                print("Empate")
                break

            self.print_tablero()
            print("Turno Bot")
            self.bot_turn()

            if self.is_winner('bot'):
                print("Gana robot") 
                break
        self.print_tablero()

    def bot_vs_bot(self):
        winner = False
        while not winner:
            self.print_tablero()
            print("Turno jugador")
            self.player_bot_turn()

            if self.is_winner("player"):
                print("Gana jugador")
                self.bot_lose_report("Player Bot")
                break

            if len(self.left) == 0:
                winner = True
                print("Empate")
                break

            self.print_tablero()
            print("Turno Bot")
            self.bot_turn()

            if self.is_winner('bot'):
                print("Gana robot") 
                break
        self.print_tablero()

    def bot_lose_report(self, who):
        with open("report.txt", 'a') as writer:
            writer.write("------{who}-----\n")
            writer.write(f"Player: {str(self.player)}\n")
            writer.write(f"Bot: {str(self.bot)}\n")
            writer.write(f"Left: {str(self.left)}\n")
            writer.write(f"|{self.t[8]}|{self.t[3]}|{self.t[4]}|      |8|3|4|\n")
            writer.write(f"|{self.t[1]}|{self.t[5]}|{self.t[9]}|      |1|5|9|\n")
            writer.write(f"|{self.t[6]}|{self.t[7]}|{self.t[2]}|      |6|7|2|\n")
            writer.write("-------------------\n")




    def print_tablero(self):
        t = self.t
        print(f"""
        |{t[8]}|{t[3]}|{t[4]}|      |8|3|4|
        |{t[1]}|{t[5]}|{t[9]}|      |1|5|9|
        |{t[6]}|{t[7]}|{t[2]}|      |6|7|2|
        """)

    def menu(self):
        while True:
            self.reset()
            print("""
            Quien juega?
            1) Jugador
            2) Bot 
            3) Dummy vs Bot
            4) Bot vs Bot (always the same)     
            """)
            options = {1: self.game, 2: self.game_2, 3: self.dummy_vs_bot, 4: self.bot_vs_bot}
            option = int(input("> "))
            try:
                options[option]()
                print(self.player, self.bot, self.left)
            except:
                pass

        
gato = Gato()
gato.menu()