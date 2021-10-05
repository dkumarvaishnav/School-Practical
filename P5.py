sen = input("enter a sentance = ")
count = 1
alp = 0
for j in sen :
    if j == " " :
        count += 1
    elif j.isalnum() :
        alp += 1
print("number of word is ",count)
print("number of characters ",len(sen))
print("percentage of alpha numeric = ", (alp / len(sen)) * 100)