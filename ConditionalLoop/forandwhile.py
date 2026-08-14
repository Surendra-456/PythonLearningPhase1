#break immediately exits the loop.
for i in range(1, 11):
    if i == 5:
        break
    print(i)


#continue skips the current iteration and moves to the next one.
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


#break immediately exits the loop.

i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

#continue skips the current iteration and moves to the next one.
i = 0
while i < 10:
    i += 1

    if i == 5:
        continue

    print(i)