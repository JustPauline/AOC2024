total = 0


def makecombinations(n):
    if n == 0:
        return [[]]
    combinations = makecombinations(n-1)
    return [combo + ["+"] for combo in combinations] + [combo + ["*"] for combo in combinations] + [combo + ["|"] for combo in combinations]


with open('data.txt') as f:
    for line in f:
        line = line.strip().split(' ')
        line[0] = line[0].strip(':')
        operators = makecombinations(len(line)-2)
        for ops in operators:
            result = int(line[1])
            for number, op in zip(line[2:], ops):
                if op == '+':
                    result += int(number)
                elif op == '*':
                    result *= int(number)
                elif op == '|':
                    result = int(str(result)+str(number))
            if int(result) == int(line[0]):
                total += result
                break
print(total)