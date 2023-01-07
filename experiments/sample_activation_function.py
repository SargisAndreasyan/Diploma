input_x = [0.4, 0.6, 0.8,.7,.5,.4,.3,.2, 0.9]
input_y = [0.4, 0.6, 0.5, 0.6]


def get_right_left(input_x):
    conv, sum1, sum2 = 0, 0, 0
    for i, x in enumerate(input_x):
        if i == 0:
            continue
        else:
            if input_x[i] > input_x[i - 1]:
                conv += 1
                sum1 += 1
            else:
                conv -= 1
                sum2 += 1
    try:
        mark = 1 - min(sum1, sum2) / len(input_x)
    except:
        mark = 1
    return conv, mark

print(get_right_left(input_x))
