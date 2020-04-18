import yaml
import random

COUNT = 4 * 25
PLUS = '+'
MINUS = '-'
OPS = [PLUS, MINUS]


def main():
    rows = []
    for row in range(COUNT):
        index = random.randint(0, 1)
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        op = OPS[index]
        if op == MINUS:
            if a < b:
                a, b = b, a
        rows.append({'a': a, 'b': b, 'op': op})

    content = yaml.dump({'rows': rows}, default_flow_style=False)
    with open('data.yml', 'w') as f:
        f.write(content)


if __name__ == '__main__':
    main()
