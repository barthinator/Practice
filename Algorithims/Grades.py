grades = [73, 67, 38, 33]

for i in range(len(grades)):
    if grades[i] > 37 and grades[i] % 5 is not 5:
        if (5 - grades[i] % 5) < 3:
            grades[i] = grades[i] + (5 - grades[i] % 5)
    print(grades[i])
