import random 

num_playes = int(input("enter players count: "))
steps = int(input("enter number of stages: "))
players = [{'can play': 1, 'step': 0, 'lifes': 3} for i in range(num_playes)]

while sum(p['can play'] for p in players) > 1:  
    player1 = player2 = 0
    while player1 == player2 or players[player1]['can play'] != 1 or players[player2]['can play'] != 1:
        player1 = random.randint(0, len(players)-1)
        player2 = random.randint(0, len(players)-1)

    if random.randint(1, 2) == 1:
        players[player1]['step'] += 1
        players[player2]['lifes'] -= 1
    else:
        players[player2]['step'] += 1
        players[player1]['lifes'] -= 1

    if players[player1]['lifes'] <= 0 or players[player1]['step'] >= steps:
        players[player1]['can play'] = 0
    if players[player2]['lifes'] <= 0 or players[player2]['step'] >= steps:
        players[player2]['can play'] = 0
result=sum(1 for unit in players if unit['step'] == steps)
print(f"Only {result} players out of {num_playes} players reached the {steps}th stage .")
