import re

minion = 'minion'
minion_1 = 'Bob'
minions = 'minion miNYon mIneYon MinYoN Bob Minion Minion Minion Bob ManYon minYON Minion MinioN Bob MinioN'
minions_1 = 'Bob minion miNYon mIneYon MinYoN Minion Minion Bob Minion ManYon minYON Minion MinioN MinioN'
minions_2 = 'minion miNYon mIneYon MinYoN Minion Minion Minion ManYon minYON Minion MinioN MinioN'

# создается регулярное выражение
Bob = re.compile('Bob')

# поиск (находит только первое совпадение)
match = Bob.search(minion)
print(match)
matches = Bob.search(minions)
print(matches)

# находит все совпадения (выдает позицию)
match_1 = Bob.finditer(minions_1)
for _ in match_1:
    print(f'match_1 – {_}')
match_2 = Bob.finditer(minions_2)
for _ in match_2:
    print(f'match_2 – {_}')

# выдает значения
match_3 = Bob.findall(minions_1)
match_4 = Bob.findall(minions_2)
print(match_3)
print(match_4)

# производится замена
minions_with_Kevin_1 = Bob.sub('Kevin', minions)
print(minions_with_Kevin_1)

split = Bob.split(minions)  # аналогично с тем, что используется в строке
print(split)

full_match_1 = Bob.fullmatch(minion_1)  # возвращает объект Match в случае полного совпадения со строкой
full_match = Bob.fullmatch(minions)  # в ином случае возвращается None
print(full_match_1)
print(full_match)
