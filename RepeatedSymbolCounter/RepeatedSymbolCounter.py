# Write a Python program to count the number of duplicates
# characters in string s. The program should print the total number of repeated characters
# and in the next line - repeated characters separated by a space and sorted alphabetically.
# If there are no repeated characters in the string,
# print 0 as the total and on the next line - None.

s = input("Enter string: ")
repeated = []
sortedStr = sorted(s)

# Shows sorted string's characters by ascending
print('Sorted string: ', sortedStr)

for x in range(len(sortedStr)):
    if x > 0:
        if sortedStr[x] == sortedStr[x-1]:
            if len(repeated) > 0:
               if repeated[-1] != sortedStr[x]:
                   repeated.append(sortedStr[x])
            else:
                repeated.append(sortedStr[x])

print('Amount: ', len(repeated))
if len(repeated) == 0:
    print('Repeated: NONE')
else:
    print('Repeated: ', end="")
    for ch in repeated:
        print(ch, end=" ")
    print()
