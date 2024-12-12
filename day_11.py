
dp = {}

def replace_principle(word, time):
    if (word, time) in dp:
        return dp[(word, time)]
    if time == 0:
        ret = 1
    elif word == 0:
        ret = replace_principle(1, time-1)
    elif len(str(word)) % 2 == 0:
        length = len(str(word)) // 2
        left = str(word)[0:length]
        right = str(word)[length:]
        ret = replace_principle(int(left), time-1) + replace_principle(int(right), time-1)
    else:
        ret = replace_principle(word*2024, time-1)

    dp[(word, time)] = ret
    return ret


if __name__ == '__main__':
    with open('input/input_day11.txt') as f:
        words = [int(x) for x in f.read().split(" ")]
    t = 75
    print(sum(replace_principle(x, t) for x in words))
