import numpy as np

INPUT = 'input.txt'

divisors_lcm = 1

class Monkey():
    def __init__(self, starting_items, operation, test_divisor, target_if_test_true, target_if_test_false):
        self.items = starting_items
        exec(f'self.operation = {operation}')
        self.relief               = lambda worry_level: worry_level//3
        self.test_divisor         = test_divisor
        self.target_if_test_true  = target_if_test_true
        self.target_if_test_false = target_if_test_false
        self.inspect_counter      = 0

    def inspect_items(self, monkeys, part=1):
        for _ in range(len(self.items)):
            self.inspect_counter += 1
            item = self.items.pop(0)
            item = self.operation(item)
            item %= divisors_lcm #crucial for part 2
            if part==1:
                item //= 3
            target_monkey = self.target_if_test_true if item%self.test_divisor==0 else self.target_if_test_false
            self.throw_item(item, monkeys[target_monkey])

    def throw_item(self, item, other_monkey):
        other_monkey.items += [item]


def parse_input(input_file):
    monkeys = []
    with open(input_file) as input_data:
        for line in input_data.readlines():
            line = line.strip()
            if line:
                if line.startswith('Monkey'):
                    monkey_attributes = {}
                elif line.startswith('Starting items'):
                    items_str = line.replace('Starting items: ','').split(', ')
                    monkey_attributes['starting_items'] = list(map(int, items_str))
                elif line.startswith('Operation'):
                    monkey_attributes['operation'] = line.replace('Operation: new =', 'lambda old:')
                elif line.startswith('Test'):
                    monkey_attributes['test_divisor'] = int(line.split(' ')[-1])
                elif line.startswith('If true'):
                    monkey_attributes['target_if_test_true'] = int(line.split(' ')[-1])
                elif line.startswith('If false'):
                    monkey_attributes['target_if_test_false'] = int(line.split(' ')[-1])
                    monkeys += [Monkey(**monkey_attributes)]
    return monkeys


def main():
    rounds = (20, 10000)
    for part, n_rounds in enumerate(rounds, start=1):
        monkeys = parse_input(INPUT)
        global divisors_lcm
        divisors_lcm = np.lcm.reduce([monkey.test_divisor for monkey in monkeys])
        for _ in range(n_rounds):
            for monkey in monkeys:
                monkey.inspect_items(monkeys, part)
        n_inspections = [m.inspect_counter for m in monkeys]
        n_inspections.sort()
        monkey_business = n_inspections[-1]*n_inspections[-2]
        print(f'Part {part}: {monkey_business = }')

if __name__=='__main__':
    main()
