import random as rd
import datetime
import time


# PLAYER 1 ATTACKING PLAYER 2 (CHECK BEFOREHAND THEY HAVE ENOUGH LIFE)
def combat(player1, player2):
    if player1.cannot_attack == True or player2.immune == True or player2.sneak == True:
        print('Player 1 cannot attack, so no combat!')
        return None

    # If a player is frozen, then they automatically lose a life and are unfrozen
    if player2.cannot_attack == True:
            player2.hp -= 1
            player2.cannot_attack = False
            print('Player 2 was frozen!')
            return True
    player1_combat = rd.randint(1, 20)
    player2_combat = rd.randint(1, 20)
    player1_combat += player1.attack_bonus
    player2_combat += player2.defense_bonus
    if player1_combat > player2_combat:
        player2.hp -= 1
        print('Player 1 wins!')
        return True
    elif player2_combat > player1_combat:
        player1.hp -= 1
        print('Player 2 wins!')
        return False
    else:
        print("It's a tie!")
        return None
    return None


class Player:
    # Initialize the player

    def __init__(self):
        self.hp = 20
        self.inventory = []

        # Keep track of capabilites for fighting
        self.cannot_attack = False
        self.cannot_attack_time = None

        # To keep track of immune
        self.immune = False
        self.time_of_immune = None

        self.attack_bonus = 0
        self.defense_bonus = 0


class Wizard(Player):
    def __init__(self):
        Player.__init__(self)
        self.cast_freeze = False
        self.sneak = False
        self.cast_freeze_date = None


    def fireball(self, player2):
        self.attack_bonus += 2
        combat(self, player2)
        self.attack_bonus -= 2


    def freeze(self, player2):
        if not self.cast_freeze:
            player2.cannot_attack = True
            player2.cannot_attack_time = time.time()
            self.cast_freeze = True
            self.cast_freeze_date = datetime.datetime.now().date()
        else:
            print("You cannot cast that again for another day.")

    def check(self):
        if self.immune == True:
            # Measures in seconds
            if self.time_of_immune <= time.time() - 1800:
                self.immune = False
                self.time_of_immune = None

        if self.cannot_attack == True:
            # Measures in seconds
            if self.cannot_attack_time <= time.time() - 1800:
                self.cannot_attack = False
                self.cannot_attack_time = None

        if self.cast_freeze == True:
            if datetime.datetime.now().date() != self.case_freeze_date:
                self.cast_freeze = False
                self.cast_freeze_date = None


class Warrior(Player):
    def __init__(self):
        Player.__init__(self)
        self.defensive_maneuver = False
        self.defensive_maneuver_time = None
        self.cast_defensive_maneuver = False
        self.defensive_maneuver_cast_time = None
        self.sneak = False

    def rend(self, player2):
        self.attack_bonus += 2
        combat(self, player2)
        self.attack_bonus -= 2

    def defensive_manuever(self):
        if self.cast_defensive_maneuver == False:
            self.defense_bonus += 2
            self.defensive_maneuver = True
            self.cast_defensive_maneuver = True
            self.defensive_maneuver_time = time.time()
            self.defensive_maneuver_cast_time = datetime.datetime.now().date()
        else:
            print("You cannot cast that again for another day.")

    def check(self):
        if self.immune == True:
            # Measures in seconds
            if self.time_of_immune <= time.time() - 1800:
                self.immune = False
                self.time_of_immune = None

        if self.cannot_attack == True:
            # Measures in seconds
            if self.cannot_attack_time <= time.time() - 1800:
                self.cannot_attack = False
                self.cannot_attack_time = None

        if self.defensive_maneuver == True:
            if self.defensive_maneuver_time <= time.time() - 1800:
                self.defnesive_maneuver = False
                self.defensive_maneuver_time = None
                self.defense_bonus -= 2

        if self.cast_defensive_maneuver == True:
            if self.defensive_maneuver_cast_time != datetime.datetime.now().date():
                self.cast_defensive_maneuver = False
                self.defensive_maneuver_cast_time = False

class Rogue(Player):
    def __init__(self):
        Player.__init__(self)
        self.sneak = False
        self.sneak_time = None
        self.sneak_cast = False
        self.sneak_cast_time = None

    def backstab(self, player2):
        x = player2.defense_bonus
        player2.defense_bonus = 0
        combat(self, player2)
        player2.defense_bonus = x

    def sneak(self):
        if self.sneak_cast == False:
            self.sneak = True
            self.sneak_time = time.time()
            self.sneak_cast = True
            self.sneak_cast_time = datetime.datetime.now().date()
        else:
            print("You cannot cast that again for another day.")

    def check(self):
        if self.immune == True:
            # Measures in seconds
            if self.time_of_immune <= time.time() - 1800:
                self.immune = False
                self.time_of_immune = None

        if self.cannot_attack == True:
            # Measures in seconds
            if self.cannot_attack_time <= time.time() - 1800:
                self.cannot_attack = False
                self.cannot_attack_time = None

        if self.sneak == True:
            if self.sneak_time <= time.time() - 1800:
                self.sneak = False
                self.sneak_time = None

        if self.sneak_cast == True:
            if self.sneak_cast_time != datetime.datetime.now().date():
                self.sneak_cast = False
                self.sneak_cast_time = False

x = Warrior()
y = Wizard()
print(x.hp)
print(y.hp)
x.rend(y)
print(x.hp)
print(y.hp)
y.fireball(x)
print(x.hp)
print(y.hp)
y.freeze(x)
combat(y,x)
print(x.hp)
print(y.hp)
