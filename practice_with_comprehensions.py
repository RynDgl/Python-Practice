

"""
Practice with comprehensions
"""

nums = range(5,101)

halves = [num/2 for num in nums]

print(halves)

print([num for num in range(1, 101) if num % 3 == 0])

print([(letter, number) for number in range(1, 5) for letter in 'abc'])

print({number: letter for letter, number in zip('abcdefghijklmnopqrstuvwxyz', range(1, 27))})

total_nums = range(1, 101)

fizzbuzzes = {
    'fizz': [n for n in total_nums if n % 3 == 0],
    'buzz': [n for n in total_nums if n % 7 == 0]
}

print('first',fizzbuzzes)

#set practice {sets}

fizzbuzzes = {key: set(value) for key, value in fizzbuzzes.items()}

print('second',fizzbuzzes)

fizzbuzzes['fizzbuzz'] = {n for n in fizzbuzzes['fizz'].intersection(fizzbuzzes['buzz'])}
print('third',fizzbuzzes['fizzbuzz'])
