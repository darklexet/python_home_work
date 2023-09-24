input_strings = input("Введите строки через запятую: ").split(",")

result_strings = []

for string in input_strings:
    if len(string.strip()) <= 3:
        result_strings.append(string.strip())

print(result_strings)