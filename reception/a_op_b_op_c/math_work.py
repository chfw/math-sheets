import yaml
import random

COUNT = 22
PLUS = '+'
MINUS = '-'
OPS = [PLUS, MINUS]


def main():
    rows = []
    for row in range(COUNT):
        index = random.randint(0, 1)
        index2 = random.randint(0, 1)
        a = random.randint(2, 7)
        b = random.randint(2, 7)
        c = random.randint(2, 7)
        op = OPS[index]
        op2 = OPS[index2]
        if op == MINUS:
            if a < b:
                a, b = b, a
        if op2 == MINUS:
            if op == MINUS:
                if (a-b) < c:
                    op2 = PLUS
            elif op == PLUS:
                if (a+b) < c:
                    op2 = PLUS
        rows.append({'a': a, 'b': b, 'op': op, 'c': c, 'op2': op2})

    content = yaml.dump({'rows': rows}, default_flow_style=False)
    with open('data.yml', 'w') as f:
        f.write(content)


if __name__ == '__main__':
    main()
