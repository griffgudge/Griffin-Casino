import random

money = 100

#Write your game of chance functions here

def wheel_maker():
    wheel_nums = []
    wheel_colors = []
    num_type = []
    for i in range(37):
        wheel_nums.append(i)

    for i in range(37):
        if i == 0:
            num_type.append("0")
        elif i % 2 != 0:
            num_type.append("Odd")
        else:
            num_type.append("Even")

    for i in range(37):
        if i > 28 and i % 2 != 0:
            wheel_colors.append("Black")
        if i > 28 and i % 2 == 0:
            wheel_colors.append("Red")
        elif i > 18 and i % 2 == 0:
            wheel_colors.append("Black")
        elif i > 18 and i % 2 != 0:
            wheel_colors.append("Red")
        elif i > 10 and i % 2 != 0:
            wheel_colors.append("Black")
        elif i > 10 and i % 2 == 0:
            wheel_colors.append("Red")
        elif i > 0 and i % 2 == 0:
            wheel_colors.append("Black")
        elif i > 0 and i % 2 != 0:
            wheel_colors.append("Red")
        else:
            wheel_colors.append("Green")

    wheel = list(zip(wheel_nums, num_type, wheel_colors))

    return wheel

def coin():
    num = random.randint(0, 1)
    side = None
    if num == 0:
        side = "Heads"
    else:
        side = "Tales"
    return side

def roulette():
    wheel = wheel_maker()
    index = random.randint(0, 35)
    landed = wheel[index]
    return landed

#############################################BLACK JACK##################################
def value_converter(value):
    if value > 10:
        value = 10
    return value

def hand_value_calc(hand):
    value = []
    for i in hand:
        value.append(value_converter(i[1]))
    value.sort()
    if 1 in value:
        value[0] = 11
    total = 0
    for i in value:
        total += i
    if total > 21 and value[0] == 11:
        value[0] = 1
        total = 0
        for i in value:
            total += i
    return total

def win(bet):
    with open("balance.txt", "r") as balance:
        money = int(balance.read())
    money += int(bet)
    with open("balance.txt", "w") as balance:
        balance.write(str(money))
    print("You won {} GriffCoins! Your new balance is {}!".format(bet, money))

def lose(bet):
    with open("balance.txt", "r") as balance:
        money = int(balance.read())
    money += -int(bet)
    with open("balance.txt", "w") as balance:
        balance.write(str(money))
    print("You lost {} GriffCoins! Your new balance is {}!".format(bet, money))
