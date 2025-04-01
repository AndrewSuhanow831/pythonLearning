# example: 
# lambda x : x > 0

result = filter(lambda x : x > 0, [1, 5, 6, -10, 0, -1])
result = map(lambda x : x ** 2, [1, 5, 6, -10, 0, -1])
# print(", ".join(str(x) for x in result))

lines = ["afss", "ab", "ba", "xfgdgt35gdg"]
# print(sorted(lines, key=lambda line: (-len(line), line))) # len(line) - критерий по длине, len - критерий по алфавиту
print(min(lines, key=lambda line: (len(line), line))) 