import random


"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                THIS IS FOR NW_DATA2.TXT
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""


list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]



with open("nw_data2.txt", "w") as f:
    f.write(str(len(list)) + '\n')
    for name in list:
        f.write(name + '\t')

        for y in range(1, random.randint(1, 2)):
            a = random.randint(0, len(list) - 1)
            f.write(str(list[a]) + '\t')
        else:
            f.write('\n')




with open("nw_data2.txt", "r") as f:
    data = f.readlines()


    # remove the tabs and new lines
    for x in range(len(data)):
        data[x] = data[x].replace('\t', '')
        data[x] = data[x].replace('\n', '')
        # print(data[x])


    # check for duplicate characters, and remove them
    for x in range(1, len(data)):
        checker = data[x][0]
        if checker in data[x] and data[x].count(checker) > 1:
            data[x] = data[x][0] + data[x][1:].translate({ord(x): None for x in data[x][1:]})
        else:
            pass


    # find the missing friendships, and make sure they are in both of the characters' friendship lists
    for x in range(1, len(data)):

        firstChar = data[x][0]
        # print(firstChar)

        for y in range(1, len(data)):
            if firstChar in data[y]:
                if y == x:
                    pass
                newChar = data[y][0]
                if newChar in data[x]:
                    pass
                else:
                    data[x] += newChar
    
    
    # add the tabs and new lines back in
    for x in range(1, len(data)):
        for _ in range(1):
            data[x] = '\t'.join(data[x])
        else:
            data[x] += '\n'

    data[0] += '\n'
    

    # write them to file
    with open("nw_data2.txt", "w") as f:
        for x in range(len(data)):
            f.write(data[x])



"""
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                THIS IS FOR NW_DATA3.TXT
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
"""


list2 = []
for x in range(0, 50):
    string = ""
    for y in range(0, 2):
        string += random.choice(list)
    list2.append(string)


with open("nw_data3.txt", "w") as f:
    f.write(str(len(list2)) + '\n')
    for name in list2:
        f.write(name + '\t')

        for y in range(1, random.randint(1, 2)):
            a = random.randint(0, len(list2) - 1)
            f.write(str(list2[a]) + '\t')
        else:
            f.write('\n')




with open("nw_data3.txt", "r") as f:
    data = f.readlines()


    # remove the tabs and new lines    
    for x in range(len(data)):
        data[x] = data[x].replace('\t', '')
        data[x] = data[x].replace('\n', '')


    # check for duplicate characters, and remove them
    for x in range(1, len(data)):
        checker = data[x][0:2]
        if checker in data[x] and data[x].count(checker) > 1:
            data[x] = data[x][0:2] + data[x][2:].translate({ord(x): None for x in data[x][2:]})
        else:
            pass


    # find the missing friendships, and make sure they are in both of the characters' friendship lists
    for x in range(1, len(data)):

        firstChars = data[x][0:2]
        # print(firstChar)

        for y in range(1, len(data)):
            if firstChars in data[y]:
                if y == x:
                    pass
                newChar = data[y][0:2]
                if newChar in data[x]:
                    pass
                else:
                    data[x] += newChar
    
    
    
    # add the tabs and new lines back in
    for x in range(1, len(data)):
        for _ in range(1):
            data[x] = '\t'.join(data[x][i:i + 2] for i in range(0, len(data[x]), 2))
        else:
            data[x] += '\n'
    

    data[0] += '\n'

    
    # write them to file
    with open("nw_data3.txt", "w") as f:
        for x in range(len(data)):
            f.write(data[x])
    