import time

def print_header():

    print("                 '*")
    print("            *          .")
    print("                   *       '")
    print("              *                *")
    print("")
    print("   -=||||| 1985: SPACE RACE |||||=-")
    print("       -=||| USA vs. USSR |||=-")
    print("")
    print("   *   '*")
    print("           *")
    print("                *")
    print("                       *")
    print("               *")
    print("                     *")
    print()


def game_intro():

    def print_statement():
        print("{} {}, prepare for launch!".format(title_name, player_name))
        launch_sequence()
        radio_message()

    def launch_sequence():
        count_down = 5
        while count_down:
            print(count_down)
            count_down -= 1
            time.sleep(1)
        print("Lift off!")

    def radio_message():

        print("{}: Captain {}, this is {}. Hope everything's going well up there.".format(ground_cap,
                                                                                          player_name, ground_name))
        print("There's just three things you have to keep in mind:")
        print()
        print("1. Oxygen: You'll need to mine space debris for more, should your supply run low.")
        print("Low oxygen can affect your ability to perform your mission.")
        print()
        print("2. Power: Your power level weakens with each hit. Power levels increase for each")
        print("successful battle. Keep in mind that power and oxygen levels influence your overall")
        print("success.")
        print()
        print("3. Finally, the details of your mission... You need to take out all three spacecraft.".format(alt_nation))
        print("Be careful though, those pesky {} can take you out with them.".format(ideo))
        print("Good luck and {}!".format(ideo_statement))
        print()

    nation = None
    while nation is None:
        nation = input("Are you a [S]oviet cosmonaut or an [A]merican astronaut? ").lower()
        if nation == "a":
            player_name = input("What is your name, patriot? ")
            title_name = "Patriot"
            ground_cap = "HOUSTON"
            ground_name = "Houston"
            alt_nation = "Soviet"
            ideo = "communists"
            ideo_statement = "God bless America"
            print_statement()
            return player_name, title_name
        elif nation == "s":
            player_name = input("What is your name, comrade? ")
            title_name = "Comrade"
            ground_cap = "MOSCOW"
            ground_name = "Moscow"
            alt_nation = "American"
            ideo = "capitalists"
            ideo_statement = "may the workers of the world unite"
            print_statement()
            return player_name, title_name
        else:
            print("I didn't understand that...")
            continue



