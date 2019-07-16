import random
import time
from space_race_extra import print_header, game_intro

from actors import Naut, Extraterrestrial, SpaceDebris, Missile


def main():

    print_header()
    player_name, title_name = game_intro()
    game_loop(player_name)


def game_loop(intro_name):

    extraterrestrial = [
        Extraterrestrial('UFO', 1000),
        Missile('ICBM', 500, 2, True),
        Naut('Military Spacecraft', 2000, 1),
    ]

    space_debris = [
        SpaceDebris('Asteroid', 10),
        SpaceDebris('Satellite', 30)
    ]

    naut = Naut(intro_name, 75, 20)

    while True:

        active_et = random.choice(extraterrestrial)
        print('WARNING: Incoming {} of level {}...'
              .format(active_et.name, active_et.level))

        cmd = input('Do you [f]ire, [e]vade the threat, [c]heck vitals, [m]ine asteroids, or [l]ook around? ').lower()
        if cmd == 'f':
            if naut.attack(active_et):
                extraterrestrial.remove(active_et)
            else:
                print("Entering hyper-sleep...")
                time.sleep(5)
                print("You've taken a hit, but your defensive shields are at {}. Cabin oxygen levels at {}."
                      .format(naut.level, naut.oxygen))
        elif cmd == 'e':
            print('Engaging engines for evasive maneuver...')
        elif cmd == 'm':
            active_mine = random.choice(space_debris)
            print('A {} measuring {} meters is spotted.'
                  .format(active_mine.name, active_mine.level))
            mine_cmd = input('Would you like to mine? [Y/N] ').lower()
            while True:
                if mine_cmd == "y":
                    naut.oxygen_mine(active_mine)
                    break
                else:
                    break

        elif cmd == 'l':
            print('{} takes in the peaceful void of outer space and sees:'
                  .format(naut.name))
            for c in extraterrestrial:
                print(' * A {} of level {}'.format(c.name, c.level))
        elif cmd == 'c':
            naut.check_status()
            continue
        else:
            print("OK, exiting game... Bye!")
            break

        if not extraterrestrial:
            print("You've completed your mission. Well done!")
            break

        print()


if __name__ == '__main__':
    main()
