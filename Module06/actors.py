import random
import time

class Extraterrestrial:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} of {}".format(
            self.name, self.level
        )

    def get_defensive_role(self):
        return random.randint(1, 12) * self.level

    def level_up(self):
        self.level += 5

    def level_down(self):
        self.level -= 10


class Naut(Extraterrestrial):

    def get_defensive_role(self):
        return random.randint(1, 6) * self.level * self.oxygen

    def __init__(self, name, level, oxygen):
        super().__init__(name, level)
        self.oxygen = oxygen

    def oxygen_up(self):
        self.oxygen += 5

    def oxygen_down(self):
        self.oxygen -= 5

    def check_status(self):
        print("SYSTEM: Commander {}, your defense shields are at {}. Cabin oxygen levels are currently at {}."
              .format(self.name, self.level, self.oxygen))
        time.sleep(3)
        print()

    def oxygen_mine(self, extraterrestrial):
        print("WARNING: Mining can be dangerous with larger space debris.")
        print("The space commander {} locks coordinates on the {} to gather oxygen!".format(
            self.name, extraterrestrial.name
        ))

        my_roll = self.get_defensive_role()
        et_roll = extraterrestrial.get_defensive_role()

        print("Your equipment is measured to handle {}...".format(my_roll))
        print("The {}'s size is measured at {}...".format(extraterrestrial.name, et_roll))

        if my_roll >= et_roll:
            print("ALERT: Oxygen collected. {} no longer detected on radar.".format(extraterrestrial.name))
            self.oxygen_up()

            return True
        else:
            print("WARNING: Critical damage sustained.")
            self.level_down()
            if self.level == 0:
                print("SYSTEM FAILURE. MISSION ABORTED.")
            return False

    def attack(self, extraterrestrial):
        print("The heroic space commander {} attacks {}!".format(
            self.name, extraterrestrial.name
        ))

        my_roll = self.get_defensive_role()
        et_roll = extraterrestrial.get_defensive_role()

        print("Your attack measures {}...".format(my_roll))
        print("The {}'s counter attack measured {}...".format(extraterrestrial.name, et_roll))

        if my_roll >= et_roll:
            print("ALERT: Systems stable. {} no longer detected on radar.".format(extraterrestrial.name))
            self.level_up()

            return True
        else:
            print("WARNING: Critical damage sustained.")
            self.level_down()
            self.oxygen_down()
            if self.level == 0:
                print("SYSTEM FAILURE. MISSION ABORTED.")
                quit()
            elif self.oxygen == 0:
                print("SYSTEM FAILURE. MISSION ABORTED.")
                quit()
            return False


class SpaceDebris(Extraterrestrial):
    def get_defensive_role(self):
        base_roll = super().get_defensive_role()
        return base_roll


class Missile(Extraterrestrial):
    def __init__(self, name, level, size, nuclear):
        super().__init__(name, level)
        self.nuclear = nuclear
        self.size = size
        
    def get_defensive_role(self):
        base_roll = super().get_defensive_role()
        nuclear_modifier = 5 if self.nuclear else 1
        size_modifier = self.size / 10

        return base_roll * nuclear_modifier * size_modifier
