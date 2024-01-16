

def combine(number: str):
    keyboard = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}
    i = 0
    result = ['']  
    if not number:
        return []

    number = list(number)
    number = list(map(int, number))
    while i < len(number):
        if number[i] in keyboard:
            apoio = []
            b = keyboard[number[i]]
            j = 0
            while j < len(b):
                k = 0
                while k < len(result):
                    apoio.append(result[k] + b[j])
                    k += 1
                j += 1
            result = apoio
        i += 1
    result.sort()
    return result

