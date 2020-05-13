import yaml
import random

COUNT = 4 * 12
PLUS = '+'
MINUS = '-'
OPS = [PLUS, MINUS]


def main():
    rows = []
    for row in range(COUNT):
        index = random.randint(0, 1)
        a = random.randint(1, 5)
        b = random.randint(1, 5)
        op = OPS[index]
        if op == MINUS:
            if a < b:
                a, b = b, a
            c = a - b
        else:
            c = a + b
        rows.append({'a': a, 'c': c, 'op': op})

    content = yaml.dump({'rows': rows}, default_flow_style=False)
    with open('data.yml', 'w') as f:
        f.write(content)


if __name__ == '__main__':
    main()
