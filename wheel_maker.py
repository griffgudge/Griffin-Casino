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
