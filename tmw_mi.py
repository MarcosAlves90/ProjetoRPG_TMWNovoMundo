import collections
import math
import random
import pickle
import os

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
                 life=15,
                 max_life=0,
                 defense=5,
                 attack=5,
                 energy=10,
                 max_energy=0,
                 darkness=0.00,
                 armors_quantity=1,
                 armor_id='A1',
                 money=0,
                 level=1,
                 experience=0,
                 days=1,
                 bedroom_color="YELLOW"):
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
        self.enemy_ai = []
        # --------------------------
        # ORIGIN
        self.origin = origin
        self.origin_name = origin_name
        self.origin_desc = origin_desc
        # --------------------------
        # LIFE
        self.life = life
        self.max_life = max_life
        # --------------------------
        # DEFENSE AND ATTACK
        self.defense = defense
        self.attack = attack
        # ENERGY
        self.energy = energy
        self.max_energy = max_energy
        # --------------------------
        # DARKNESS
        self.darkness = darkness
        # --------------------------
        # STORE AND WARDROBE
        self.armors_quantity = armors_quantity
        self.armor_id = armor_id
        self.armors = {
            '1': {'ID': 'A1', 'name': 'Sevastopol Suit', 'DEF': 5, 'acquired': True, 'value': 0},
            '2': {'ID': 'A2', 'name': 'Exo-suit', 'DEF': 10, 'acquired': False, 'value': 100},
            '3': {'ID': 'A3', 'name': 'Nano Tech Armor', 'DEF': 15, 'acquired': False, 'value': 500},
        }
        for i, value in self.armors.items():
            value['Desc'] = armors_desc(value['name'])
        self.money = money
        # --------------------------
        # LEVEL
        self.level = level
        self.experience = experience
        self.experience_cap = level * 100
        # --------------------------
        # AGE
        self.days = days
        # --------------------------
        # AREAS
        self.bedroom_color = bedroom_color

    def verify_level_up(self):
        if self.experience >= self.experience_cap:
            self.level += 1
            self.experience -= self.experience_cap
            self.experience_cap = self.level * 100
            self.max_life = self.life + 5
            self.defense = self.defense + 5
            self.attack = self.defense + 5
            self.max_energy = self.energy + 5
            clear_screen()
            print('Humiliation made him superior...\n'
                  'You have reached a new level.')
            pause()


# -----------------------------------------------
# MISSIONS

def mission(player) -> None:
    clear_screen()
    line("MISSION")
    print()
    print(f'A blinding voice occupies your mind...\n"{player.name}, the hourglass is almost empty. Your time is up'
          f'finishing."\n')
    print(f'[1] Accept mission\n[X] Exit\n')
    resp1 = input("Choose an option and press ENTER: ")
    if resp1 == '1':
        tower_combat(player)
    elif resp1.lower() == 'x':
        house(player)
    else:
        invalid()


def enemy_reactions(enemy_infos, reaction_type, reaction_category):
    reactions_dict = {
        'm': {
            'attack': [
                f'{enemy_infos["enemy"]} attacks you without showing any remorse.\n',
                f'{enemy_infos["enemy"]} launches a fierce attack towards you.\n',
                f'{enemy_infos["enemy"]} attacks with a savage roar.\n'
            ],
            'defense': [
                f'{enemy_infos["enemy"]} defends himself, believes you will never be able to hit him.\n',
                f'{enemy_infos["enemy"]} raises its guard, preparing for its attack.\n',
                f'{enemy_infos["enemy"]} deftly dodges your attacks.\n'
            ],
            'energy': [
                f'{enemy_infos["enemy"]} uses energy, preventing you from escaping the tower.\n',
                f'{enemy_infos["enemy"]} channels his energy, creating a barrier around him.\n',
                f'{enemy_infos["enemy"]} releases a wave of energy towards you.\n'
            ],
            'run': [
                f'{enemy_infos["enemy"]} tries to run away, but fails.\n',
                f'{enemy_infos["enemy"]} attempts to escape, but stumbles.\n',
                f'{enemy_infos["enemy"]} fails to flee the battle.\n'
            ],
            'wait': [
                f'{enemy_infos["enemy"]} waits, watching your every move.\n',
                f'{enemy_infos["enemy"]} remains silent, studying his actions.\n',
                f'{enemy_infos["enemy"]} does nothing, just watches you cautiously.\n'
            ]
        },
        'p': {
            'attack': [
                f'You attack {enemy_infos["enemy"]} without showing any remorse.\n',
                f'You launch a fierce attack towards {enemy_infos["enemy"]}.\n',
                f'You attack {enemy_infos["enemy"]} with a savage roar.\n'
            ],
            'defense': [
                f'You defend yourself, believing that {enemy_infos["enemy"]} will never be able to reach you.\n',
                f'You raise your guard, preparing for {enemy_infos["enemy"]}\'s attack.\n',
                f'You skillfully dodge {enemy_infos["enemy"]}\'s attacks.\n'
            ],
            'energy': [
                f'You use energy, preventing {enemy_infos["enemy"]} from escaping the tower.\n',
                f'You channel your energy, creating a barrier around you.\n',
                f'You release a wave of energy towards {enemy_infos["enemy"]}.\n'
            ],
            'run': [
                f'You try to run away, but fail.\n',
                f'You attempt to escape, but stumble.\n',
                f'You fail to flee the battle.\n'
            ],
            'wait': [
                f'You wait, watching {enemy_infos["enemy"]}\'s every move.\n',
                f'You remain silent, studying the actions of {enemy_infos["enemy"]}.\n',
                f'You do nothing, just watch {enemy_infos["enemy"]} cautiously.\n'
            ]
        }
    }
    return random.choice(reactions_dict[reaction_type][reaction_category])


# def enemy_ai_learning(player, n):
#     if len(player.enemy_ai) >= 10:
#         player.enemy_ai.insert(0, random.randint(1, n))
#         player.enemy_ai.pop()
#     else:
#         player.enemy_ai.insert(0, random.randint(1, n))


def enemy_ai_reaction(monster, player):
    # reaction_mapping = {1: 2, 2: 3, 3: 4, 4: 1, 5: 5}
    #
    # random_action = random.randint(1, 5)
    # most_common_action = int(collections.Counter(player.enemy_ai).most_common(1)[0][0])
    # chosen_action = random.choice([random_action, most_common_action])

    if monster['energy'] == 0:
        return 4  # Wait

    if player.energy == 0:
        return 1  # Attack

    if monster['life'] >= monster['max_life'] * 0.5:
        return 1  # Attack

    if monster['life'] <= monster['max_life'] * 0.5:
        if monster['energy'] > 5:
            return 5  # Run
        else:
            return 2  # Defend

    if player.life <= player.max_life * 0.2:
        if player.energy >= 5:
            return 3  # Energy
        else:
            return 1  # Attack

    if player.life <= player.max_life * 0.5:
        return 1  # Attack

    # return reaction_mapping[chosen_action]


# -----------------------------------------------

def get_user_input():
    return input("Choose an option and press ENTER: ")


def handle_user_input(monster, player, input):
    action_mapping = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        's': 's'
    }

    if input.lower() in action_mapping:
        if action_mapping[input.lower()] == 's':
            clear_screen()
            print(f"Level: {player.level} | Experience: {player.experience}/{player.experience_cap}\n"
                  f"Life: {player.life}\n"
                  f"Defense: {player.defense}\n"
                  f"Attack: {player.attack}\n"
                  f"Energy: {player.energy}")
            pause()
        else:
            # enemy_ai_learning(player, action_mapping[input.lower()])
            return action_mapping[input.lower()], enemy_ai_reaction(monster, player)
    else:
        invalid()


# -----------------------------------------------


def tower_combat(player):
    color("RED")
    attack = 1
    defense = 2
    energy_y = 3
    wait = 4
    run = 5

    def check_death(entity):
        if isinstance(entity, dict):  # Se a entidade for um dicionário (inimigo)
            return entity['life'] <= 0
        else:  # Se a entidade for um objeto Player
            return entity.life <= 0

    def handle_death():
        if check_death(player) and check_death(enemy_infos):
            print_message_and_lose(f'You and {enemy_infos["enemy"]} were defeated.')
        elif check_death(player):
            print_message_and_lose(f'You were defeated by {enemy_infos["enemy"]}.')
        elif check_death(enemy_infos):
            player.experience += enemy_infos['XP'] + random.randint(1, 20)
            player.days += 2
            print_message_and_win(f'You defeated {enemy_infos["enemy"]}.')

    def print_message_and_run(entity):
        clear_screen()
        if entity == 'player':
            print_text(["You successfully escaped from the tower."])
        elif entity == 'enemy':
            print_text([f"{entity['enemy']} successfully escaped from the tower."])
        pause()
        player.days += 2
        house(player)

    def print_message_and_win(message):
        clear_screen()
        print_text([message])
        pause()
        house(player)

    def print_message_and_lose(message):
        clear_screen()
        print_text([message])
        pause()
        force_exit()

    def calculate_damage(attacker, defender, is_player, player_a, enemy_a):
        if is_player:
            damage = (attacker.attack / 2) - defender['defense'] if enemy_a == 2 else (attacker.attack / 2)
        else:
            damage = (attacker['attack'] / 2) - defender.defense if player_a == 2 else (attacker['attack'] / 2)
        return max(0, damage)  # Garante que o dano mínimo seja 0

    def handle_action(player_a, enemy_a, action_type):
        action_mapping = {1: 'attack', 2: 'defense', 3: 'energy', 4: 'wait', 5: 'run'}

        if player_a == action_type:
            player_a = enemy_reactions(enemy_infos, 'p', action_mapping[action_type])
            if action_type == wait:
                player.energy += 1
            elif (action_type == attack or action_type == energy_y or action_type == defense) and player.energy >= 1:
                player.energy -= 1
                if action_type == attack:
                    enemy_infos['life'] -= calculate_damage(player, enemy_infos, True, player_a, enemy_a)
            elif (action_type == attack or action_type == energy_y or action_type == defense) and player.energy == 0:
                player_a = f'You do not have enough energy to complete your action.\n'
        if enemy_a == action_type:
            enemy_a = enemy_reactions(enemy_infos, 'm', action_mapping[action_type])
            if action_type == wait:
                enemy_infos['energy'] += 1
            elif ((action_type == attack or action_type == energy_y or action_type == defense)
                  and enemy_infos['energy'] >= 1):
                enemy_infos['energy'] -= 1
                if action_type == attack:
                    player.life -= calculate_damage(enemy_infos, player, False, player_a, enemy_a)
            elif (action_type == attack or action_type == energy_y) and enemy_infos['energy'] == 0:
                enemy_a = f'{enemy_infos["enemy"]} does not have enough energy to complete its action.\n'

        return player_a, enemy_a

    def status_modify(player_a, enemy_a):
        mutual_a = None

        if player_a == enemy_a:
            if player_a == run:
                mutual_a = f'You and {enemy_infos["enemy"]} try to run away, but the tower won\'t let you.'
                player_a, enemy_a = None, None
            elif player_a == wait:
                mutual_a = f'You and {enemy_infos["enemy"]} wait, observing each other.'
                player_a, enemy_a = None, None

        player_a, enemy_a = handle_action(player_a, enemy_a, attack)
        player_a, enemy_a = handle_action(player_a, enemy_a, defense)
        player_a, enemy_a = handle_action(player_a, enemy_a, energy_y)
        player_a, enemy_a = handle_action(player_a, enemy_a, wait)
        player_a, enemy_a = handle_action(player_a, enemy_a, run)

        return mutual_a, player_a, enemy_a

    def try_to_run(entity, entity_type):
        energy_needed_to_run = 5

        if entity_type == "player" or entity_type == "both":
            if entity.energy >= energy_needed_to_run:
                entity.energy -= energy_needed_to_run
                return True
        if entity_type == "enemy" or entity_type == "both":
            if entity['energy'] >= energy_needed_to_run:
                entity['energy'] -= energy_needed_to_run
                return True
        return False

    clear_screen()
    enemy_infos = decide_mission(player)
    enemy_action_code, enemy_action = None, None
    player_action_code, player_action = None, None
    mutual_actions, dont_show_hourglass = None, None

    print(enemy_infos['desc_highlight'])
    pause()

    while True:

        if player_action and not dont_show_hourglass:
            clear_screen()
            print('You spin the hourglass...')
            pause()

        clear_screen()
        handle_death()
        dont_show_hourglass = False

        if player_action_code == run and enemy_action_code == run:
            pass
        elif player_action_code == run:
            if try_to_run(player, "player"):
                print_message_and_run('player')
        elif enemy_action_code == run:
            if try_to_run(enemy_infos, "enemy"):
                print_message_and_run('enemy')

        if not player_action:
            print(f'You are facing {enemy_infos["enemy"]}.\n')

        print(f'Your life: {player.life} | Enemy\'s Life: {enemy_infos["life"]}')
        print(f'Your energy: {player.energy} | Enemy\'s Energy: {enemy_infos["energy"]}')
        if mutual_actions:
            print(f'\n{mutual_actions}')
        print(f'\n{player_action}{enemy_action}') if player_action and enemy_action else print()
        mutual_actions = None
        print(f'[1] Attack | [2] Defend\n[3] Energy | [4] Wait\n[5] Run | [S] Status\n')
        try:
            player_action, enemy_action = handle_user_input(enemy_infos, player, get_user_input())
        except TypeError:
            dont_show_hourglass = True
            pass
        player_action_code = player_action
        enemy_action_code = enemy_action
        if player_action is not None and enemy_action is not None:
            mutual_actions, player_action, enemy_action = status_modify(player_action, enemy_action)


def decide_mission(player):
    clear_screen()

    def common_modify():
        var_common_modify = random.randint(0, 5)
        return var_common_modify

    missions_dict = {
        1: {
            'enemy': 'The Rat King',
            'desc_highlight': 'The sound of heavy footsteps echoes throughout the tower.\n'
                              'As usual, something creeps through the shadows.\n'
                              'A great putrid shadow approaches...',
            'XP': 25
        },
        2: {
            'enemy': 'The Persecutor God',
            'desc_highlight': 'A slender figure steals through the mist.\n'
                              'His white eyes shine with a sinister light.\n'
                              'He approaches, hiding his true identity...',
            'XP': 30
        },
        3: {
            'enemy': 'The Shadow Beast',
            'desc_highlight': 'A chilling howl echoes through the darkness.\n'
                              'A creature of nightmares emerges, its eyes glowing with malice.\n'
                              'It approaches, demonstrating his colossal size...',
            'XP': 30
        },
        4: {
            'enemy': 'The Forgotten One',
            'desc_highlight': 'An ancient being, lost to time, stirs from its slumber.\n'
                              'Its power is immense, dwarfing anything you have faced before.\n'
                              'He pursues you, with no memory of who he once was...',
            'XP': 30
        },
        5: {
            'enemy': 'The Taken King',
            'desc_highlight': 'A chilling silence falls over the tower.\n'
                              'A figure of regal stature emerges, his presence commanding and intimidating.\n'
                              'He approaches, his eyes filled with a determination that'
                              '\nsends shivers down your spine...',
            'XP': 50
        }
    }
    enemy_type = random.randint(1, 5)
    mi_di = missions_dict[enemy_type]
    xp = mi_di['XP']
    mi_di['life'] = player.life + common_modify() + xp // 5
    mi_di['attack'] = player.attack - common_modify() + xp // 10
    mi_di['defense'] = player.defense + common_modify() + xp // 10
    mi_di['energy'] = player.energy - common_modify() + xp // 10
    # MAX STATUS
    mi_di['max_life'] = mi_di['life']
    mi_di['max_energy'] = mi_di['energy']
    return mi_di


# -----------------------------------------------


def choose_area(area, player):
    def areas():
        game_areas = {
            'bedroom': {'1': mirror, '2': wardrobe, '3': bed, '4': window, '5': door},
            'house': {'1': work, '2': mission, '3': status, '4': store, '5': bedroom}
        }
        selected_area = game_areas[area]
        print()
        for AREA, VALUE in selected_area.items():
            print(f"[{AREA}] {VALUE.__name__.capitalize()}") \
                if VALUE != bed else print(f"[{AREA}] {VALUE.__name__.capitalize() + " [Save/Exit]"}")
        print()
        return selected_area

    x = areas()

    resp1 = input("Choose an option and press ENTER: ")

    for i, value in x.items():
        if i == resp1:
            value(player)
            return True

    return False


# -----------------------------------------------
# ARMORS LIST


def armors_desc(item):
    armors_desc_info = {
        'Sevastopol Suit': 'A common suit for Sevastopol soldiers.\n'
                           'Usually used as a means of defense in '
                           'combat against ultra-humans,\ncan protect '
                           'from a few attacks.',
        'Exo-suit': 'An advanced suit equipped with exoskeleton technology.\n'
                    'It provides enhanced strength and durability,\nmaking it '
                    'ideal for heavy combat situations.',
        'Nano Tech Armor': 'A state-of-the-art armor infused with nanotechnology.\n'
                           'It can self-repair and adapt to various types of damage,\n'
                           'offering superior protection on the battlefield.'
    }
    return armors_desc_info[item]


# -----------------------------------------------
# BED

# save_game_bedroom(player) is a function that is called when the player decides to save the game.
def save_game_bedroom(player) -> None:
    clear_screen()
    with open('tmw_save_game.dat', 'wb') as file:
        pickle.dump(player, file)
    print('Game saved successfully.')
    pause()
    return bedroom(player)


# exit_game_bedroom(player) is a function that is called when the player decides to quit the game.
def exit_game_bedroom(player=None) -> None:
    phrases_list = ['And once again you running away from problems...',
                    'Nightmares won\'t go away if you don\'t face them.',
                    'Do you think this is really going to help you?',
                    'The world won\'t change just because you\'re tired.',
                    'You should feel sorry for yourself.']
    return exit_game(random.choice(phrases_list))


# -----------------------------------------------
# STORE

def store(player) -> None:
    while True:
        clear_screen()
        line("STORE")
        print(f'\n"Welcome back {player.name}. How can I help you?"\n'
              f'Says the old salesman with a malicious smile on his face.\n'
              f'He knows you don\'t have many options.\n')
        print(f"Money: {player.money}\n")
        for i, value in player.armors.items():
            if not value['acquired']:
                print(f"[{i}] {value['name']} |  Price: {value['value']}")
        print(f'[X] Exit\n')
        resp1 = input("Choose an option and press ENTER: ")
        if resp1.lower() == 'x':
            house(player)
        elif resp1 in player.armors and not player.armors[resp1]['acquired']:
            while True:
                clear_screen()
                print(f'{player.armors[resp1]['name']}:\n')
                print(f'Price: {player.armors[resp1]["value"]}\n')
                print(f'{player.armors[resp1]['Desc']}\n\nBuy armor? [Y/N]')
                resp2 = input('Choose an option and press ENTER: ')
                if resp2.lower() == 'y':
                    if player.money >= player.armors[resp1]['value']:
                        player.money -= player.armors[resp1]['value']
                        player.armors_quantity += 1
                        player.armors[resp1]['acquired'] = True
                        store(player)
                    else:
                        print('\nYou don\'t have enough money.')
                        pause()
                        store(player)
                elif resp2.lower() == 'n':
                    store(player)
                else:
                    invalid()
        else:
            invalid()


# -----------------------------------------------

def window(player) -> None:
    while True:
        clear_screen()
        print(f'The window with a yellowish white frame appears to open by itself\n'
              f'at night. You know this is a lie.\n')
        window_events = {
            '1': {'name': 'Close the window', 'desc': 'You close the window and the room becomes dark again.',
                  'state': "YELLOW"},
            '2': {'name': 'Look outside', 'desc': 'The window shows the image of a world in ruins.'
                                                  '\nThe sky is red and the ground is covered with debris.'
                                                  '\nThe sun is hidden behind the clouds as if it were afraid of the '
                                                  'world.'
                                                  '\nThe wind blows cold and strong as if it were trying to take '
                                                  'everything with it.',
                  'state': "YELLOW"},
            '3': {'name': 'Open the window', 'desc': 'You open the window and the room becomes bright.'
                                                     '\nThe light shines through the window, illuminating the room.',
                  'state': "BLUE"},
        }
        for i, value in window_events.items():
            if value['state'] == player.bedroom_color:
                print(f"[{i}] {value['name']}")
        print(f'[X] Exit\n')
        resp1 = input("Choose an option and press ENTER: ")
        if resp1.lower() == 'x':
            bedroom(player)
        elif resp1 in window_events and window_events[resp1]['state'] == player.bedroom_color:
            clear_screen()
            if window_events[resp1]['name'] == 'Close the window':
                color("BLUE")
                player.bedroom_color = "BLUE"
            elif window_events[resp1]['name'] == 'Open the window':
                color("YELLOW")
                player.bedroom_color = "YELLOW"
            print(window_events[resp1]['desc'])
            pause()
            window(player)
        else:
            invalid()


def bed(player) -> None:
    while True:
        clear_screen()
        options = {
            '1': {'name': save_game_bedroom, 'desc': 'Do you want to save your progress? [Y/N]'},
            '2': {'name': exit_game_bedroom, 'desc': 'Do you want to quit the game? [Y/N]'}
        }

        print('Sleeping might not be the best option right now...\n'
              'you know, the world won\'t change because of it.\n'
              'Enough running away from problems.\n')
        for i, VALUE in options.items():
            print(f"[{i}] {'Save Game' if VALUE['name'] == save_game_bedroom else 'Exit Game'}")
        print("[X] Exit\n")
        resp1 = input("Choose an option and press ENTER: ")

        if resp1.lower() == 'x':
            return bedroom(player)
        elif resp1 in options:
            print("\n" + options[resp1]['desc'])
            resp2 = input("Choose an option and press ENTER: ")
            if resp2.lower() == 'y':
                options[resp1]['name'](player)
            elif resp2.lower() == 'n':
                pass
            else:
                invalid()
        else:
            invalid()


def mirror(player) -> None:
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
    return bedroom(player)


def wardrobe(player) -> None:
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
        for i, value in player.armors.items():  # Use player.armors directly
            if value['ID'] == player.armor_id:
                print(f'Selected Armor: {value['name']}\n')
            if value['acquired']:
                print(f"[{i}] {value['name']}")
        print(f'[X] Exit\n')
        resp1 = input("Choose an option and press ENTER: ")
        if resp1.lower() == 'x':
            return bedroom(player)
        elif resp1 in player.armors and player.armors[resp1]['acquired']:
            while True:
                clear_screen()
                print(f'{player.armors[resp1]['name']}:\n')
                print(f'{player.armors[resp1]['Desc']}\n\nSelect armor? [Y/N]')
                resp2 = input('Choose an option and press ENTER: ')
                if resp2.lower() == 'y':
                    player.armor_id = player.armors[resp1]['ID']
                    player.defense = player.armors[resp1]['DEF']
                    return bedroom(player)
                elif resp2.lower() == 'n':
                    break
                else:
                    invalid()
        else:
            invalid()


# Preciso fazer pelo menos 5 eventos de trabalho.
def work(player) -> None:
    clear_screen()
    player.money += random.randint(8, 15)
    darkness_level = max(1, math.floor(player.darkness))
    work_events = {
        1: {
            'event': 'Your superior requests you to stay beyond working hours.\n'
                     'He insists the reports are overdue, but you distinctly\n'
                     'remember completing them a few days prior. You communicate this, but\n'
                     'he insists on new ones.',
            1: 'Concerned about job security, you comply and redo all your work.'
        },
        2: {
            'event': 'A colleague invites you for a private discussion.\n'
                     'He accuses you of involvement in pagan rituals in secluded places and structures.\n'
                     'His only evidence is a photograph of you exiting an abandoned tower.\n'
                     'While the photo is accurate, he seems to have misconstrued the true nature\n'
                     'of your activities.',
            1: 'To circumvent complications, you convince him of the cult idea.\n'
               'He agrees to leave you alone if you cover his shifts for the rest of the week.\n'
               'There seems to be no better alternative.'
        }
    }
    if player.days == 1:
        print(f'One day or another your lies will no longer be enough.\n'
              f'When others find out what you did, no one will stand by you.\n'
              f'Even the worst monster is most trustworthy.')
        pause()
        clear_screen()
    temp = random.randint(1, 2)
    print(f'{work_events[temp]['event']}\n{work_events[temp][darkness_level]}')
    pause()
    player.days += 1
    return house(player)


def door(player) -> None:
    clear_screen()
    return house(player)


def status(player) -> None:
    clear_screen()
    print(
        f"You are a {player.race} who fights using {player.combat}\nand comes from the {player.origin_name}. "
        f"Your name is {player.name}.\n")
    print(f"Level: {player.level} | Experience: {player.experience}/{player.experience_cap}\n"
          f"Life: {player.life} | "
          f"Defense: {player.defense}\n"
          f"Attack: {player.attack} | "
          f"Energy: {player.energy}\n")
    print(f"Day: {player.days}")
    # print(f'It must be strange to use this voltage meter to measure your power...'
    #       f'well, whatever.')
    pause()
    house(player)


def basic_choose_area(player, bc_area) -> None:
    while True:
        clear_screen()
        line(bc_area.upper())
        x = choose_area(bc_area, player)
        if x:
            break
        else:
            invalid()


def house(player) -> None:
    player.verify_level_up()
    player.life = player.max_life
    player.energy = player.max_energy
    color("YELLOW")
    return basic_choose_area(player, 'house')


def bedroom(player) -> None:
    player.verify_level_up()
    color(player.bedroom_color)
    return basic_choose_area(player, 'bedroom')


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


def class_definition(player, c, ct, cd) -> None:
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
            combat_name = combat_types[resp1]['combat']
            combat_type = combat_types[resp1]['combat_type']
            combat_desc = combat_types[resp1]['desc']
            clear_screen()
            print(
                f"You are a {player.race} who fights using {combat_name}.\n\n{combat_desc}\n\n"
                f"Are you sure of your choice? [Y/N]")
            resp2 = input("Choose an option and press ENTER: ")
            if resp2.lower() == 'y':
                return player, combat_name, combat_type, combat_desc
            elif resp2.lower() == 'n':
                pass
            else:
                invalid()
        else:
            invalid()


def origin_definition(player, o, on, od) -> None:
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


def final_definition(player) -> None:
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


def start_definition(player) -> None:
    clear_screen()
    color("YELLOW")
    print_text([
        "You wake up after a restless night of sleep.",
        "The sun shines through the window, illuminating your face with a soft light.\n",
        "You get out of bed and stretch, feeling sore and tired.",
        "Yesterday was long and stressful, but forgettable, like every other day."
    ])
    pause()
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
    player.max_life = player.life
    player.max_energy = player.energy
    bedroom(player)


def play() -> None:
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


def menu() -> None:
    color("GREEN")
    print()
    line_up("┏┳┓┓┏┏┓  ┳┳┓┏┓┳┓┏┳┓┏┓┓   ┓ ┏┏┓┳┓┓ ┳┓")
    print("  ┃ ┣┫┣   ┃┃┃┣ ┃┃ ┃ ┣┫┃   ┃┃┃┃┃┣┫┃ ┃┃ ")
    line_down(" ┻ ┛┗┗┛  ┛ ┗┗┛┛┗ ┻ ┛┗┗┛  ┗┻┛┗┛┛┗┗┛┻┛")
    print()
    print("[1] Start the Game")
    if os.path.exists('tmw_save_game.dat'):
        print('[2] Load Game')
        print("[3] Quit")
    else:
        print("[2] Quit")
    print()
    response = input("Choose an option and press ENTER: ")
    if response == "1":
        play()
    elif response == "2" and os.path.exists('tmw_save_game.dat'):
        with open('tmw_save_game.dat', 'rb') as file:
            player = pickle.load(file)
        bedroom(player)
    elif response == "2":
        force_exit()
    elif response == "3" and os.path.exists('tmw_save_game.dat'):
        force_exit()
    else:
        invalid()


menu()
