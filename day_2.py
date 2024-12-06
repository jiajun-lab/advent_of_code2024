def f_day2_1():
    l = []
    with open("input/input_day2.txt", "r") as f:
        for line in f:
            l.append([int(item) for item in list(line.strip().split(" "))])
    result = 0
    for i in range(len(l)):
        if check_safe(l[i]):
            result += 1

    return result

def check_safe(list) -> bool:
    is_increase = list[0] < list[1]
    is_decrease = list[0] > list[1]

    for i in range(len(list)-1):
        if list[i] > list[i+1] and is_increase is True:
            return False
        if list[i] < list[i+1] and is_decrease is True:
            return False
        if abs(list[i] - list[i+1]) > 3 or abs(list[i] - list[i+1]) == 0:
            return False

    return True

def check_more_safe(list) -> bool:
    if check_safe(list):
        return True

    for i in range(len(list)):
        l = [item for item in list]
        l.pop(i)
        if check_safe(l):
            return True
    return False


def f_day2_2():
    l = []
    with open("input/input_day2.txt", "r") as f:
        for line in f:
            l.append([int(item) for item in list(line.strip().split(" "))])
    result = 0
    for i in range(len(l)):
        if check_more_safe(l[i]):
            result += 1

    return result

if __name__ == '__main__':
    print(f_day2_1())
    print(f_day2_2())