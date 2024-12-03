import re


def f_day_3_1(string) -> int:
    pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)')
    l = pattern.findall(string)

    print(l)
    ans = 0
    for i in l:
        ans += mul(i)
    return ans


def f_day_3_2(string) -> int:
    pattern = re.compile(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)')
    l = pattern.findall(string)
    do_cal = True
    ans = 0
    for i in l:
        if i == 'do()':
            do_cal = True
            continue
        if i == 'don\'t()':
            do_cal = False
            continue
        ans += mul(i, do_cal)

    return ans


def mul(s, do_cal) -> int:
    if do_cal:
        sl = s.split(',')
        n1 = sl[0][4:]
        n2 = sl[1][:len(sl[1])-1]

        return int(n1)*int(n2)
    return 0


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        s = f.read()
    print(f_day_3_2(s))