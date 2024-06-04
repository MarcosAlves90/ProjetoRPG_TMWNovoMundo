import math
from config import color, line, clear_screen, line_down, line_up, exit_game, pause, invalid, print_text, force_exit


class Player:
    def __init__(self,
                 name=None,
                 race=None,
                 race_bonus=None,
                 race_bonus1=None,
                 race_bonus2=None,
                 race_desc=None,
                 combat=None,
                 combat_type=None,
                 combat_desc=None,
                 origin=None,
                 origin_name=None,
                 origin_desc=None,
                 life=None,
                 defense=None,
                 attack=None,
                 energy=None,
                 darkness=0.00,
                 armors_quantity=1,
                 armor_id='A1'
                 ):
        self.name = name
        # --------------------------
        # RACE
        self.race = race
        self.race_bonus = race_bonus
        self.race_bonus1 = race_bonus1
        self.race_bonus2 = race_bonus2
        self.race_desc = race_desc
        # --------------------------
        # COMBAT
        self.combat = combat
        self.combat_type = combat_type
        self.combat_desc = combat_desc
        # --------------------------
        # ORIGIN
        self.origin = origin
        self.origin_name = origin_name
        self.origin_desc = origin_desc
        # --------------------------
        # STATUS
        self.life = life
        self.defense = defense
        self.attack = attack
        self.energy = energy
        self.darkness = darkness
        # --------------------------
        # STORE
        self.armors_quantity = armors_quantity
        self.armor_id = armor_id


# -----------------------------------------------

def choose_area(area, player):
    def areas():
        game_areas = {
            'bedroom': {1: mirror, 2: wardrobe, 3: bed, 4: door},
            'house': {1: work, 2: mission, 3: status}
        }
        selected_area = game_areas[area]
        print()
        for AREA, VALUE in selected_area.items():
            print(f"[{AREA}] {VALUE.__name__.capitalize()}") \
                if VALUE != bed else print(f"[{AREA}] {VALUE.__name__.capitalize() + " [Save/Exit]"}")
        print()
        return selected_area

    x = areas()

    resp1 = int(input("Choose an option and press ENTER: "))

    for i, value in x.items():
        if i == resp1:
            value(player)
            return True

    invalid()
    return False


def armors():
    armors_list = {
        '1': {'ID': 'A1', 'name': 'Sevastopol Suit', 'DEF': 5,
              'Desc': 'A common suit for Sevastopol soldiers.'
                      'Usually used as a means of defense in '
                      'combat against ultra-humans, can protect '
                      'from a few attacks. ',
              'acquired': True},
        '2': {'ID': 'A2', 'name': 'Exo-suit', 'DEF': 10, 'Desc': '', 'acquired': False},
        '3': {'ID': 'A3', 'name': 'Nanotech Armor', 'DEF': 15, 'Desc': '', 'acquired': False},
    }
    return armors_list


# -----------------------------------------------

def salvar(player):
    clear_screen()


def sair(player):
    phrases_list = []
    exit_game()


# -----------------------------------------------

def bed(player):
    while True:
        clear_screen()
        options = {
            '1': {'name': salvar, 'desc': 'Do you want to save your progress? [Y/N]'},
            '2': {'name': sair, 'desc': 'Do you want to quit the game? [Y/N]'}
        }

        print('Sleeping might not be the best option right now...\n'
              'you know, the world won\'t change because of it.\n'
              'Enough running away from problems.\n')
        for i, VALUE in options.items():
            print(f"[{i}] {VALUE['name'].__name__.capitalize()}")
        print()
        resp1 = input("Choose an option and press ENTER: ")

        if resp1 in options:
            clear_screen()
            print(options[resp1]['desc'] + '\nAre you sure of your choice? [Y/N]')
            resp2 = input("Choose an option and press ENTER: ")
            if resp2.lower() == 'y':
                options[resp1]['name'](player)
            elif resp2.lower() == 'n':
                pass
            else:
                invalid()
        else:
            invalid()


def mirror(player):
    clear_screen()
    common_lines = {
        'Common': {1: 'The mirror shows the image of someone tired.'},
    }
    lines = {
        'Human': {1: f'{common_lines["Common"][1]}\nYou should take care of those dark circles.'},
        'Android': {1: f'{common_lines["Common"][1]}\nIt\'s time to recharge your batteries.'},
        'Cyborg': {1: f'{common_lines["Common"][1]}\nMaybe using so many implants is not good for you.'},
        'Ultra-Human': {1: f'{common_lines["Common"][1]}\nYour energy is failing again.'}
    }
    darkness_level = math.floor(player.darkness)
    print(lines[player.race][1 if darkness_level < 1 else darkness_level])
    pause()
    bedroom(player)


def wardrobe(player):
    while True:
        clear_screen()
        common_lines = {
            'Common': {1: 'It\'s been a while since you bought new clothes.'
                          '\nThe remaining rags are dirty and torn.'}
        }
        lines = {
            'Human': {1: f'{common_lines["Common"][1]}'},
            'Android': {1: f'{common_lines['Common'][1]}'},
            'Cyborg': {1: f'{common_lines['Common'][1]}'},
            'Ultra-Human': {1: f'{common_lines['Common'][1]}'}
        }
        print(lines[player.race][player.armors_quantity] + '\n')
        for i, value in armors().items():
            if value['ID'] == player.armor_id:
                print(f'Selected Armor: {value['name']}\n')
            if value['acquired']:
                print(f"[{i}] {value['name']}")
        print()
        resp1 = input("Choose an option and press ENTER: ")
        if resp1 in armors() and armors()[resp1]['acquired']:
            while True:
                clear_screen()
                print(f'{armors()[resp1]['name']}:\n')
                print(f'{armors()[resp1]['Desc']}\nSelect armor? [Y/N]')
                resp2 = input('Choose an option and press ENTER: ')
                if resp2.lower() == 'y':
                    player.armor_id = armors()[resp1]['ID']
                    player.defense = armors()[resp1]['DEF']
                    bedroom(player)
                elif resp2.lower() == 'n':
                    break
                else:
                    invalid()
        else:
            invalid()


def work(player):
    clear_screen()
    pause()


def mission(player):
    clear_screen()
    pause()


def door(player):
    clear_screen()
    house(player)
    pause()


def status(player):
    clear_screen()
    pause()


def house(player):
    print('a')


def bedroom(player):
    while True:
        clear_screen()
        line("BEDROOM")
        x = choose_area('bedroom', player)
        if x:
            break
        else:
            pass


# -----------------------------------------------

def choose_race():
    while True:
        clear_screen()
        line("Choose your race")
        print()
        races = {
            "1": {"name": "Human", "bonus": "+5 HP -5 DEF", "bonus1": 5, "bonus2": 5,
                  "description": "Humans are beings made of fluids, flesh, and bones.\nTheir composition is 99%% "
                                 "oxygen, carbon, hydrogen, calcium, and phosphorus.\nThey have eyes, ears, nostrils, "
                                 "and a mouth, in addition to a brain for thinking and feeling.\nTheir brain is "
                                 "composed of interconnected neurons, capable of processing information and "
                                 "thoughts.\nTheir limbs are formed by tissues and bones, allowing various categories "
                                 "of movement.\nThey are born from a biological mother and father, through sexual "
                                 "reproduction."},
            "2": {"name": "Android", "bonus": "+5 DEF -5 HP", "bonus1": 5, "bonus2": 5,
                  "description": "Androids are beings made of vandal titanium, detroid iron, and nano chrome-barium "
                                 "alloy.\nTheir composition is 99%% silicon, chrome-barium, copper, iron, "
                                 "and titanium.\nThey do not have eyes, ears, nostrils, or a mouth. Not even a brain "
                                 "to think or feel.\nTheir processor is composed of interconnected circuits, "
                                 "capable of processing data and variables.\nTheir limbs are formed by metal alloys "
                                 "and rubberized tissues, allowing various categories of movement.\nThey are built by "
                                 "a factory, being incapable of reproducing."},
            "3": {"name": "Cyborg", "bonus": "+5 ATK -5 NRG", "bonus1": 5, "bonus2": 5,
                  "description": "Cyborgs are beings made of fluids, flesh, bones, rubber, and metals.\nTheir "
                                 "composition is imprecise and variable, depending heavily on the degree of "
                                 "modification.\nThey may or may not have eyes, ears, nostrils, and a mouth, "
                                 "in addition to a brain or processor.\nTheir mechanical limbs are known as "
                                 "'Chromes', allowing for the enhancement of physical and/or mental "
                                 "capabilities.\nThey are born in the same way as humans, but are modified through "
                                 "surgeries and implants.\nThey can modify themselves to the limit of their "
                                 "biological bodies."},
            "4": {"name": "Ultra-Human", "bonus": "+5 NRG -5 ATK", "bonus1": 5, "bonus2": 5,
                  "description": "Ultra-Humans are beings made of fluids, flesh, and bones.\nTheir composition is 99% "
                                 "oxygen, carbon, hydrogen, calcium, and phosphorus.\nThey have eyes, ears, nostrils, "
                                 "and a mouth, in addition to a brain for thinking and feeling.\nTheir brain is "
                                 "composed of interconnected neurons, capable of processing information and "
                                 "thoughts.\nTheir limbs are formed by tissues and bones, allowing various categories "
                                 "of movement.\nThey are born from a biological mother and father, through sexual "
                                 "reproduction.\nThe difference between them and humans is the ability to manipulate "
                                 "energy, allowing the use of special abilities."}
        }

        for key, value in races.items():
            print(f"[{key}] {value['name']}")
        print()

        resp1 = input("Choose an option and press ENTER: ")
        if resp1 in races:
            race = races[resp1]['name']
            race_bonus = races[resp1]['bonus']
            race_bonus1 = races[resp1]['bonus1']
            race_bonus2 = races[resp1]['bonus2']
            race_desc = races[resp1]['description']
            clear_screen()
            print(
                f"You are a {race}.\n\n{race_desc}\n\nYour bonus is {race_bonus}\n\nAre you sure of your choice? [Y/N]")
            resp2 = input("Choose an option and press ENTER: ")
            if resp2.lower() == 'y':
                player = Player(None, race, race_bonus, race_bonus1, race_bonus2, race_desc)
                class_definition(*choose_class(player))
                return
            elif resp2.lower() == 'n':
                pass
            else:
                invalid()
        else:
            invalid()


def class_definition(player, c, ct, cd):
    player.combat = c
    player.combat_type = ct
    player.combat_desc = cd
    origin_definition(*choose_origin(player))


def choose_class(player):
    while True:
        clear_screen()
        line("Choose your combat style")
        print()
        combat_types = {
            '1': {
                'combat': 'melee combat',
                'combat_type': 'physical1',
                'desc': '"Melee combat" is a combat style that involves the use of unarmed fighting techniques.\nIt '
                        'is based on physical strikes, such as punches, kicks, elbow strikes, and knee strikes.\nIt '
                        'is a style that requires strength, agility, and physical endurance.\nExamples of weapons: '
                        'Gloves, boots, armors, etc.'
            },
            '2': {
                'combat': 'melee weapons',
                'combat_type': 'physical2',
                'desc': '"Melee weapons" is a combat style that involves the use of melee weapons.\nIt is based on '
                        'short-range attacks, such as cuts, thrusts, and dodges.\nIt is a style that requires '
                        'strength, agility, and physical endurance.\nExamples of weapons: Swords, axes, spears, etc.'
            },
            '3': {
                'combat': 'arcane magic',
                'combat_type': 'magic',
                'desc': '"Arcane magic" is a combat style that involves the use of energy and enchantments.\nIt is '
                        'based on energetic "skills", such as fireballs, rays, and spectral shields.\nIt can be used '
                        'at short and long range, depending on the user\'s choice.\nIt is a style that requires '
                        'concentration, wisdom, and mental endurance.\nExamples of weapons: Amulets, artifacts, '
                        'scrolls, etc.'
            },
            '4': {
                'combat': 'firearms',
                'combat_type': 'firearms',
                'desc': '"Firearms" is a combat style that involves the use of firearms.\nIt is based on long-range '
                        'attacks, such as shots, grenades, and explosions.\nIt is a style that requires precision, '
                        'agility, and wisdom.\nExamples of weapons: Pistols, rifles, machine guns, etc.'
            },
            '5': {
                'combat': 'chromes',
                'combat_type': 'chromes',
                'desc': '"Chromes" is a combat style that involves the use of cybernetic implants.\nIt is based on '
                        'short and long-range attacks, such as punches, shots, and explosions.\nIt is a style that '
                        'requires strength, concentration, and agility.\nExamples of weapons: Mechanical arms, '
                        'mechanical legs, cybernetic eyes, etc.'
            }
        }

        for key, value in combat_types.items():
            print(f"[{key}] {value['combat']}")

        print()
        resp1 = input("Choose an option and press ENTER: ")
        if resp1 in combat_types:
            combat = combat_types[resp1]['combat']
            combat_type = combat_types[resp1]['combat_type']
            combat_desc = combat_types[resp1]['desc']
            clear_screen()
            print(
                f"You are a {player.race} who fights using {combat}.\n\n{combat_desc}\n\n"
                f"Are you sure of your choice? [Y/N]")
            resp2 = input("Choose an option and press ENTER: ")
            if resp2.lower() == 'y':
                return player, combat, combat_type, combat_desc
            elif resp2.lower() == 'n':
                pass
            else:
                invalid()
        else:
            invalid()


def origin_definition(player, o, on, od):
    player.origin = o
    player.origin_name = on
    player.origin_desc = od
    choose_name(player)


def choose_origin(player):
    while True:
        clear_screen()
        line("Choose your origin")
        print()
        origins = {
            "1": {
                "name": "Forest",
                "origin": "FR",
                "desc": "You were born and raised in a quiet city called 'Mydensgate'.\nIt is known for its gloomy "
                        "and polluted atmosphere, where sunlight is rarely seen.\nThe population is made up of humans "
                        "and cyborgs living between two worlds, wealth and poverty.\nThe city is governed by a "
                        "corporation called 'Infinity', which controls the economy and politics.\n\nLike any other "
                        "citizen, your dream has always been to become a professional hero.\nYou trained and studied "
                        "for years, but something prevented you from achieving your goal..."
            },
            "2": {"name": "City", "origin": "CT",
                  "desc": "You were born and raised in a quiet city called 'Mydensgate'.\nIt is known for its gloomy "
                          "and polluted atmosphere, where sunlight is rarely seen.\nThe population is made up of "
                          "humans and cyborgs living between two worlds, wealth and poverty.\nThe city is governed by "
                          "a corporation called 'Infinity', which controls the economy and politics.\n\nLike any "
                          "other citizen, your dream has always been to become a professional hero.\nYou trained and "
                          "studied for years, but something prevented you from achieving your goal..."},
            "3": {"name": "Mountain", "origin": "MT",
                  "desc": "You were born and raised in a high and dangerous mountain called 'Pinnacle of "
                          "Ascension'.\nIt is known for its cold and windy atmosphere, where sunlight shines between "
                          "the peaks of the mountains.\nThe population is made up of humans and cyborgs who live in "
                          "search of achieving inner peace.\nThe mountain is ruled by the 'Eremites', who teach about "
                          "the arts of hermitism.\n\nAs a member of the Eremites, your duty has always been to "
                          "achieve inner peace and spiritual enlightenment.\nYou trained and studied for years, "
                          "but something prevented you from achieving your goal..."},
            "4": {"name": "Desert", "origin": "DS",
                  "desc": "You were born and raised in a vast and inhospitable desert called 'Pharr Canyon'.\nIt is "
                          "known for its hot and dry atmosphere, where sunlight burns the skin and eyes.\nThe "
                          "population consists of humans and animals living in search of water and food.\nThe desert "
                          "is ruled by the 'Kobra', who controls trade and religion.\n\nLike any other inhabitant of "
                          "the wilderness, your dream has always been to lift your family out of poverty.\nYou "
                          "trained and studied for years, but something prevented you from achieving your goal..."},
            "5": {"name": "Sea", "origin": "SE",
                  "desc": "You were born and raised in a turbulent sea mistakenly called the 'Silver Ocean'.\nIt is "
                          "known for its humid and stormy atmosphere, where sunlight doesn't always shine.\nThe "
                          "population is made up of human and cyborg pirates who live off what they can steal.\nThe "
                          "sea is ruled by the 'Corsairs', who control trade and piracy.\n\nWith life as it is, "
                          "your dream has always been to find a legendary treasure and become rich.\nYou trained and "
                          "stole for years, but something prevented you from achieving your goal..."}
        }

        for key, value in origins.items():
            print(f"[{key}] {value['name']}")
        print()

        resp1 = input("Choose an option and press ENTER: ")
        if resp1 in origins:
            origin = origins[resp1]["origin"]
            origin_name = origins[resp1]["name"]
            origin_desc = origins[resp1]["desc"]
            clear_screen()
            print(
                f"You are a {player.race} who fights using {player.combat} and comes from the {origin_name}.\n\n"
                f"{origin_desc}\n\nAre you sure of your choice? [Y/N]")
            resp2 = input("Choose an option and press ENTER: ")
            if resp2.lower() == 'y':
                return player, origin, origin_name, origin_desc
            elif resp2.lower() == 'n':
                pass
            else:
                invalid()
        else:
            invalid()


def named(player, n):
    player.name = n
    return player


def choose_name(player):
    while True:
        clear_screen()
        line("Enter your first name")
        print()
        resp1 = input("Name: ")
        if isinstance(resp1, str):
            name = resp1
            print()
            print("Are you sure of your choice? [Y/N]")
            resp2 = input("Choose an option and press ENTER: ")
            if resp2.lower() == 'y':
                return final_definition(named(player, name))
            elif resp2.lower() == 'n':
                pass
            else:
                invalid()
        else:
            invalid()


def final_definition(player):
    clear_screen()
    print(
        f"You are a {player.race} who fights using {player.combat} and comes from the {player.origin_name}. "
        f"Your name is {player.name}.\n")
    color("MAGENTA")
    print_text([
        "In the current world, the concept of gender and sexuality is outdated and seen as prejudiced.",
        "Therefore, it is not necessary to choose a gender or sexuality that defines you.",
        "You are free to be whoever you want, without judgment or limitations.",
        "Your body is your temple, your mind is your sanctuary, and your soul is your refuge.",
        "Everyone is considered equal under the law and society, without exceptions or privileges.\n\n"
        "However, without the existence of differences, life has become monotonous and meaningless."
    ])
    pause()
    clear_screen()
    print_text([
        "There have always been rumors circulating about the unknown ideals of the Infinity Corporation.",
        "It has always been seen as a benevolent and just organization, too perfect.",
        "But, like any other organization, it has secrets and mysteries that no one knows.",
        "Some say that it is responsible for the destruction of individuality and personality.",
        "Others say that it seeks absolute control over humanity, without exceptions or limits.\n",
        "Who knows if these whispers are true...",
        "In that case, we would be mere extras in a gigantic theater."
    ])
    pause()
    clear_screen()
    print_text([
        "Things start to change when we realize that Infinity is not the only one pulling the strings.",
        "Secret organizations around the globe are moving, trying to achieve their goals.",
        "Soon, a third world war will begin among all countries.",
        "And, as always, the population will be the most affected by this war."
    ])
    pause()
    clear_screen()
    print_text([
        "There is no one who can stop this from happening.",
        "The future is already completely compromised."
    ])
    pause()
    start_definition(player)


def start_definition(player):
    clear_screen()
    color("YELLOW")
    print_text([
        "You wake up after a restless night of sleep.",
        "The sun shines through the window, illuminating your face with a soft light.\n",
        "You get out of bed and stretch, feeling sore and tired.",
        "Yesterday was long and stressful, but forgettable, like every other day."
    ])
    pause()
    player.life = 15
    player.defense, player.attack, player.energy = 5, 5, 5
    if player.race == 'Human':
        player.life = player.life + player.race_bonus1
        player.defense = player.defense - player.race_bonus2
    elif player.race == 'Android':
        player.defense = player.defense + player.race_bonus1
        player.life = player.life - player.race_bonus2
    elif player.race == 'Cyborg':
        player.attack = player.attack + player.race_bonus1
        player.energy = player.energy - player.race_bonus2
    elif player.race == 'Ultra-Human':
        player.energy = player.energy + player.race_bonus1
        player.attack = player.attack - player.race_bonus2
    else:
        print('Error: player.race has not been defined.')
        force_exit()
    bedroom(player)


def play():
    clear_screen()
    print_text([
        "There was a time when the existence of energy was not known.",
        "When that changed, humanity was taken over by arrogant organizations and individuals.",
        "The influence they had on society caused unimaginable effects.",
        "Little did they know the destiny they would be forced to face."
    ])
    pause()

    clear_screen()
    print_text([
        "This was the end of times.",
        "There was no chance of survival."
    ])
    pause()

    clear_screen()
    color("RED")
    print_text([
        "And that's how you died."
    ])
    pause()

    clear_screen()
    print_text([
        "You awaken in a world that doesn't belong to you.",
        "The ground beneath your feet screams and trembles endlessly.",
        "The sky above pulls you violently.",
        "And the air around you presses you down,",
        "trying to find its way inside."
    ])
    pause()

    color("BLUE")
    clear_screen()
    print_text([
        "This is planet Earth.",
        "A cruel world that should have never existed.",
        "The year is 2052, a dystopian future where technology",
        "has become one with humanity."
    ])
    pause()
    color("GREEN")
    choose_race()


def menu():
    color("GREEN")
    print()
    line_up("┏┳┓┓┏┏┓  ┳┳┓┏┓┳┓┏┳┓┏┓┓   ┓ ┏┏┓┳┓┓ ┳┓")
    print("  ┃ ┣┫┣   ┃┃┃┣ ┃┃ ┃ ┣┫┃   ┃┃┃┃┃┣┫┃ ┃┃ ")
    line_down(" ┻ ┛┗┗┛  ┛ ┗┗┛┛┗ ┻ ┛┗┗┛  ┗┻┛┗┛┛┗┗┛┻┛")
    print()
    print("[1] Start the Game")
    print("[2] Quit")
    print()
    response = input("Choose an option and press ENTER: ")
    if response == "1":
        play()
    elif response == "2":
        exit_game()


menu()
