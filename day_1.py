def f_day1_1():
    l1 = []
    l2 = []
    with open("input/input_day1.txt", "r") as f:
        for line in f:
            pair = line.strip().split("   ")
            l1.append(int(pair[0]))
            l2.append(int(pair[1]))

    l1.sort()
    l2.sort()
    s = 0
    for i in range(len(l1)):
        s += abs(l1[i] - l2[i])

    print(s)


def f_day1_2():
    s = {}
    l = []
    with open("input/input_day1.txt", "r") as f:
        for line in f:
            pair = line.strip().split("   ")
            l.append([int(pair[0]), int(pair[1])])
    for i in range(len(l)):
        s[l[i][0]] = 0

    for i in range(len(l)):
        if(l[i][1] in s):
            s[l[i][1]] += 1

    res = 0
    for k,v in s.items():
        res += v*k

    return res





if __name__ == '__main__':
    print(f_day1_2())