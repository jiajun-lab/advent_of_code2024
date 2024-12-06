l = []

def check_row(i, j):
    s = ''
    for k in range(4):
        s += l[i][j+k]

    return s == 'XMAS' or s == 'SAMX'

def check_col(i, j):
    s = ''
    for k in range(4):
        s += l[i+k][j]

    return s == 'XMAS' or s == 'SAMX'

def check_diag(i, j):
    s = ''
    for k in range(4):
        s += l[i + k][j + k]

    return s == 'XMAS' or s == 'SAMX'

def check_asy_diag(i, j):
    s = ''
    for k in range(4):
        s += l[i + k][j - k]

    return s == 'XMAS' or s == 'SAMX'


def check_square(i, j):
    s1 = ''
    s2 = ''

    for k in range(3):
        s1 += l[i + k][j + k]
        s2 += l[i + k][j + 2 -k]

    return (s1 == 'MAS' or s1 == 'SAM') and (s2 == 'MAS' or s2 == 'SAM')

if __name__ == '__main__':

    with open("input/input_day4.txt", 'r') as f:
        for line in f:
            l.append(list(line.strip('\n')))

    res = 0
    res_mas = 0
    for i in range(0, len(l)):
        for j in range(0, len(l[i])):
            if j < len(l[i])-3 and check_row(i, j):
                res += 1
            if i < len(l)-3 and check_col(i, j):
                res += 1
            if j < len(l[i])-3 and i < len(l)-3 and check_diag(i, j):
                res += 1
            if j >= 3 and i < len(l)-3 and check_asy_diag(i, j):
                res += 1

            if i < len(l)-2 and j < len(l[i])-2 and check_square(i, j):
                res_mas += 1

    print(res)
    print(res_mas)

