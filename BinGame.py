import random
import time



gen_words = []
words = []
valid_words = []
entered_words = []
score = 0

grid1 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#grid2 = ["i","j","k","l","m","n","o","p"]
#grid3 = ["q","r","s","t","u","v"]
#grid4 = ["w","x","y","z"]
def GenCharacter():
    global row_1_item_1,row_1_item_2,row_1_item_3,row_1_item_4,row_2_item_1,row_2_item_2,row_2_item_3,row_2_item_4,row_3_item_1,row_3_item_2,row_3_item_3,row_3_item_4,row_4_item_1,row_4_item_2,row_4_item_3,row_4_item_4
    g1 = grid1.copy()
    #g2 = grid2.copy()
    #g3 = grid3.copy()
    #g4 = grid4.copy()
    # ROW ONE
    row_1_item_1 = random.choice(g1)
    g1.remove(row_1_item_1)
    row_1_item_2 = random.choice(g1)
    g1.remove(row_1_item_2)
    row_1_item_3 = random.choice(g1)
    g1.remove(row_1_item_3)
    row_1_item_4 = random.choice(g1)
    # ROW TWO
    row_2_item_1 = random.choice(g1)
    g1.remove(row_2_item_1)
    row_2_item_2 = random.choice(g1)
    g1.remove(row_2_item_2)
    row_2_item_3 = random.choice(g1)
    g1.remove(row_2_item_3)
    row_2_item_4 = random.choice(g1)
    # ROW THREE
    row_3_item_1 = random.choice(g1)
    g1.remove(row_3_item_1)
    row_3_item_2 = random.choice(g1)
    g1.remove(row_3_item_2)
    row_3_item_3 = random.choice(g1)
    g1.remove(row_3_item_3)
    row_3_item_4 = random.choice(g1)
    # ROW FOUR
    row_4_item_1 = random.choice(g1)
    g1.remove(row_4_item_1)
    row_4_item_2 = random.choice(g1)
    g1.remove(row_4_item_2)
    row_4_item_3 = random.choice(g1)
    g1.remove(row_4_item_3)
    row_4_item_4 = random.choice(g1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("----------------------------------------------------------------------------------------")
    print()
    print("       1   2   3   4 ")
    print("       |   |   |   | ")
    print()
    print(f" A  -  {row_1_item_1} | {row_1_item_2} | {row_1_item_3} | {row_1_item_4}")
    print(f" B  -  {row_2_item_1} | {row_2_item_2} | {row_2_item_3} | {row_2_item_4}")
    print(f" C  -  {row_3_item_1} | {row_3_item_2} | {row_3_item_3} | {row_3_item_4}")
    print(f" D  -  {row_4_item_1} | {row_4_item_2} | {row_4_item_3} | {row_4_item_4}")
    print()
    print("----------------------------------------------------------------------------------------")
    print()
    print("\n\n\n\n\n\n\n\n")

while exit != "n":
    print()
    GenCharacter()
    print()
    exit = input("Do you want to re-roll? (Y-N) :").lower()


with open("4-letter-words.txt","r") as files:
    for line in files:
        new_line = line.replace("\n","").lower()
        words.append(new_line)


print("Select what adjacent line you will use")
print()
print(" 1 - Horizontal")
print(" 2 - Vertical")

option = int(input("Enter (1-2) :"))



if option == 1:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("----------------------------------------------------------------------------------------")
    print()
    print("       1   2   3   4 ")
    print("       |   |   |   | ")
    print()
    print(f" A  -  {row_1_item_1} | {row_1_item_2} | {row_1_item_3} | {row_1_item_4}")
    print(f" B  -  {row_2_item_1} | {row_2_item_2} | {row_2_item_3} | {row_2_item_4}")
    print(f" C  -  {row_3_item_1} | {row_3_item_2} | {row_3_item_3} | {row_3_item_4}")
    print(f" D  -  {row_4_item_1} | {row_4_item_2} | {row_4_item_3} | {row_4_item_4}")
    print()
    print("----------------------------------------------------------------------------------------")
    print()
    print("\n\n\n\n\n\n\n\n")

    choice = input("Select your row (A-D)").lower()
    #-----------------------ROW-----------------------
    # ROW ONE
    if choice == "a":
        temp_list = []
        temp_list.append(row_1_item_1),temp_list.append(row_1_item_2),temp_list.append(row_1_item_3),temp_list.append(row_1_item_4)

        for i in range(0,4):
            l1 = temp_list[i]
            for n in range(0,4):
                l2 = temp_list[n]
                for b in range(0,4):
                    l3 = temp_list[b]
                    for m in range(0,4):
                        l4 = temp_list[m]
                        gen_words.append(l1+l2+l3+l4)

        len_words = len(words)
        len_genwords = len(gen_words)

        for x in range(0,len_genwords):
            for index in range(0,len_words):
                #print(gen_words[x],"----",words[index])
                if gen_words[x] == words[index]:
                    valid_words.append(gen_words[x])
                    #print("GEN WORDS : ",gen_words[x])
                    #print("WORDS : ",words[index])
    # ROW TWO 
    elif choice == "b":
        temp_list = []
        temp_list.append(row_2_item_1),temp_list.append(row_2_item_2),temp_list.append(row_2_item_3),temp_list.append(row_2_item_4)

        for i in range(0,4):
            l1 = temp_list[i]
            for n in range(0,4):
                l2 = temp_list[n]
                for b in range(0,4):
                    l3 = temp_list[b]
                    for m in range(0,4):
                        l4 = temp_list[m]
                        gen_words.append(l1+l2+l3+l4)

        len_words = len(words)
        len_genwords = len(gen_words)

        for x in range(0,len_genwords):
            for index in range(0,len_words):
                #print(gen_words[x],"----",words[index])
                if gen_words[x] == words[index]:
                    valid_words.append(gen_words[x])
                    #print("GEN WORDS : ",gen_words[x])
                    #print("WORDS : ",words[index])
    # ROW THREE
    elif choice == "c":
        temp_list = []
        temp_list.append(row_3_item_1),temp_list.append(row_3_item_2),temp_list.append(row_3_item_3),temp_list.append(row_3_item_4)

        for i in range(0,4):
            l1 = temp_list[i]
            for n in range(0,4):
                l2 = temp_list[n]
                for b in range(0,4):
                    l3 = temp_list[b]
                    for m in range(0,4):
                        l4 = temp_list[m]
                        gen_words.append(l1+l2+l3+l4)

        len_words = len(words)
        len_genwords = len(gen_words)

        for x in range(0,len_genwords):
            for index in range(0,len_words):
                #print(gen_words[x],"----",words[index])
                if gen_words[x] == words[index]:
                    valid_words.append(gen_words[x])
                    #print("GEN WORDS : ",gen_words[x])
                    #print("WORDS : ",words[index])
    # ROW FOUR
    elif choice == "d":
        temp_list = []
        temp_list.append(row_4_item_1),temp_list.append(row_4_item_2),temp_list.append(row_4_item_3),temp_list.append(row_4_item_4)

        for i in range(0,4):
            l1 = temp_list[i]
            for n in range(0,4):
                l2 = temp_list[n]
                for b in range(0,4):
                    l3 = temp_list[b]
                    for m in range(0,4):
                        l4 = temp_list[m]
                        gen_words.append(l1+l2+l3+l4)

        len_words = len(words)
        len_genwords = len(gen_words)

        for x in range(0,len_genwords):
            for index in range(0,len_words):
                #print(gen_words[x],"----",words[index])
                if gen_words[x] == words[index]:
                    valid_words.append(gen_words[x])
                    #print("GEN WORDS : ",gen_words[x])
                    #print("WORDS : ",words[index])

elif option == 2:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("----------------------------------------------------------------------------------------")
    print()
    print("       1   2   3   4 ")
    print("       |   |   |   | ")
    print()
    print(f" A  -  {row_1_item_1} | {row_1_item_2} | {row_1_item_3} | {row_1_item_4}")
    print(f" B  -  {row_2_item_1} | {row_2_item_2} | {row_2_item_3} | {row_2_item_4}")
    print(f" C  -  {row_3_item_1} | {row_3_item_2} | {row_3_item_3} | {row_3_item_4}")
    print(f" D  -  {row_4_item_1} | {row_4_item_2} | {row_4_item_3} | {row_4_item_4}")
    print()
    print("----------------------------------------------------------------------------------------")
    print()
    print("\n\n\n\n\n\n\n\n")

    choice = input("Select your row (1-4) :").lower()
    #-----------------------COLUM-----------------------
    # COLUM ONE
    if choice == "1":
        temp_list = []
        temp_list.append(row_1_item_1),temp_list.append(row_2_item_1),temp_list.append(row_3_item_1),temp_list.append(row_4_item_1)

        for i in range(0,4):
            l1 = temp_list[i]
            for n in range(0,4):
                l2 = temp_list[n]
                for b in range(0,4):
                    l3 = temp_list[b]
                    for m in range(0,4):
                        l4 = temp_list[m]
                        gen_words.append(l1+l2+l3+l4)

        len_words = len(words)
        len_genwords = len(gen_words)

        for x in range(0,len_genwords):
            for index in range(0,len_words):
                #print(gen_words[x],"----",words[index])
                if gen_words[x] == words[index]:
                    valid_words.append(gen_words[x])
                    #print("GEN WORDS : ",gen_words[x])
                    #print("WORDS : ",words[index])
    # COLUM TWO 
    elif choice == "2":
        temp_list = []
        temp_list.append(row_1_item_2),temp_list.append(row_2_item_2),temp_list.append(row_3_item_2),temp_list.append(row_4_item_2)

        for i in range(0,4):
            l1 = temp_list[i]
            for n in range(0,4):
                l2 = temp_list[n]
                for b in range(0,4):
                    l3 = temp_list[b]
                    for m in range(0,4):
                        l4 = temp_list[m]
                        gen_words.append(l1+l2+l3+l4)

        len_words = len(words)
        len_genwords = len(gen_words)

        for x in range(0,len_genwords):
            for index in range(0,len_words):
                #print(gen_words[x],"----",words[index])
                if gen_words[x] == words[index]:
                    valid_words.append(gen_words[x])
                    #print("GEN WORDS : ",gen_words[x])
                    #print("WORDS : ",words[index])
    # COLUM THREE
    elif choice == "3":
        temp_list = []
        temp_list.append(row_1_item_3),temp_list.append(row_2_item_3),temp_list.append(row_3_item_3),temp_list.append(row_4_item_3)

        for i in range(0,4):
            l1 = temp_list[i]
            for n in range(0,4):
                l2 = temp_list[n]
                for b in range(0,4):
                    l3 = temp_list[b]
                    for m in range(0,4):
                        l4 = temp_list[m]
                        gen_words.append(l1+l2+l3+l4)

        len_words = len(words)
        len_genwords = len(gen_words)

        for x in range(0,len_genwords):
            for index in range(0,len_words):
                #print(gen_words[x],"----",words[index])
                if gen_words[x] == words[index]:
                    valid_words.append(gen_words[x])
                    #print("GEN WORDS : ",gen_words[x])
                    #print("WORDS : ",words[index])
    # COLUM FOUR
    elif choice == "4":
        temp_list = []
        temp_list.append(row_1_item_4),temp_list.append(row_2_item_4),temp_list.append(row_3_item_4),temp_list.append(row_3_item_4)

        for i in range(0,4):
            l1 = temp_list[i]
            for n in range(0,4):
                l2 = temp_list[n]
                for b in range(0,4):
                    l3 = temp_list[b]
                    for m in range(0,4):
                        l4 = temp_list[m]
                        gen_words.append(l1+l2+l3+l4)

        len_words = len(words)
        len_genwords = len(gen_words)

        for x in range(0,len_genwords):
            for index in range(0,len_words):
                #print(gen_words[x],"----",words[index])
                if gen_words[x] == words[index]:
                    valid_words.append(gen_words[x])
                    #print("GEN WORDS : ",gen_words[x])
                    #print("WORDS : ",words[index])
        
else:
    print("ERROR: 259")

print(valid_words)

user_input = ""
while user_input != "5":
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("----------------------------------------------------------------------------------------")
    print()
    print("       1   2   3   4 ")
    print("       |   |   |   | ")
    print()
    print(f" A  -  {row_1_item_1} | {row_1_item_2} | {row_1_item_3} | {row_1_item_4}")
    print(f" B  -  {row_2_item_1} | {row_2_item_2} | {row_2_item_3} | {row_2_item_4}")
    print(f" C  -  {row_3_item_1} | {row_3_item_2} | {row_3_item_3} | {row_3_item_4}")
    print(f" D  -  {row_4_item_1} | {row_4_item_2} | {row_4_item_3} | {row_4_item_4}")
    print()
    print("----------------------------------------------------------------------------------------")
    print()
    print("\n\n\n\n\n\n\n\n")
    user_input = str(input("INPUT a 4 letter word (5 - exit) :")).lower()
    print(f" Words entered - {entered_words}")
    entered_words.append(user_input)

entered_words.remove("5")
range_entered_words = len(entered_words)
range_valid_words = len(valid_words)

for h in range(0,range_entered_words):
    for t in range(0,range_valid_words):
        if entered_words[h] == valid_words[t]:
            score += 1
        else:
            pass
print("--------------------------------------------------------------------------------")
print(f" ACHIEVABLE SCORE - {range_valid_words}")
print(f" Your score: {score}")
print(f" Possible words: {valid_words}")    
print(f" Words entered - {entered_words}")
print("--------------------------------------------------------------------------------")
