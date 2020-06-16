starcorp = {
    '3': 'StarCorp',
    '5': 'IT',
    '15': 'StarCorpiano'
}

def get_label(num, div):
    if num % div == 0:
        return starcorp[str(div)]
    return None

for i in range(1, 101):
    n = get_label(i, 15) or get_label(i, 3) or get_label(i, 5) or i
    print(n)
