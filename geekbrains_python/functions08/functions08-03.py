def calc_damage(player_a, player_d):
    return player_a['damage'] / player_d['armor']

def attack(player_a, player_d, func):
    player_d['health'] -= func(player_a, player_d)
    print(player_a, player_d)



name_player = input("Введите имя первого игрока: ")
name_enemy = input("Введите имя второго игрока: ")


player = {
    "name": name_player,
    "health": 100,
    "damage": 50,
    "armor": 1.2
}

enemy = {
    "name": name_enemy,
    "health": 100,
    "damage": 60,
    "armor": 1.5
}

attack(player, enemy, calc_damage)

