import random

grid1 = ["a","b","c","d","e","f","g","h"]
grid2 = ["i","j","k","l","m","n","o","p"]
grid3 = ["q","r","s","t","u","v"]
grid4 = ["w","x","y","z"]

def GenCharacter():
    global row_1_item_1,row_1_item_2,row_1_item_3,row_1_item_4,row_2_item_1,row_2_item_2,row_2_item_3,row_2_item_4,row_3_item_1,row_3_item_2,row_3_item_3,row_3_item_4,row_4_item_1,row_4_item_2,row_4_item_3,row_4_item_4
    g1 = grid1.copy()
    g2 = grid2.copy()
    g3 = grid3.copy()
    g4 = grid4.copy()
    # ROW ONE
    row_1_item_1 = random.choice(g1)
    g1.remove(row_1_item_1)
    row_1_item_2 = random.choice(g1)
    g1.remove(row_1_item_2)
    row_1_item_3 = random.choice(g1)
    g1.remove(row_1_item_3)
    row_1_item_4 = random.choice(g1)
    # ROW TWO
    row_2_item_1 = random.choice(g2)
    g2.remove(row_2_item_1)
    row_2_item_2 = random.choice(g2)
    g2.remove(row_2_item_2)
    row_2_item_3 = random.choice(g2)
    g2.remove(row_2_item_3)
    row_2_item_4 = random.choice(g2)
    # ROW THREE
    row_3_item_1 = random.choice(g3)
    g3.remove(row_3_item_1)
    row_3_item_2 = random.choice(g3)
    g3.remove(row_3_item_2)
    row_3_item_3 = random.choice(g3)
    g3.remove(row_3_item_3)
    row_3_item_4 = random.choice(g3)
    # ROW FOUR
    row_4_item_1 = random.choice(g4)
    g4.remove(row_4_item_1)
    row_4_item_2 = random.choice(g4)
    g4.remove(row_4_item_2)
    row_4_item_3 = random.choice(g4)
    g4.remove(row_4_item_3)
    row_4_item_4 = random.choice(g4)
    print("        1   2   3   4 ")
    print()
    print(f" A      {row_1_item_1} | {row_1_item_2} | {row_1_item_3} | {row_1_item_4}")
    print(f" B      {row_2_item_1} | {row_2_item_2} | {row_2_item_3} | {row_2_item_4}")
    print(f" C      {row_3_item_1} | {row_3_item_2} | {row_3_item_3} | {row_3_item_4}")
    print(f" D      {row_4_item_1} | {row_4_item_2} | {row_4_item_3} | {row_4_item_4}")

while exit != "n":
    print()
    GenCharacter()
    exit = input("Do you want to re-roll? (Y-N) :").lower()

gen_words = []
words = []
valid_words = []

with open("4-letter-words.txt","r") as files:
    for line in files:
        new_line = line.replace("\n","").lower()
        words.append(new_line)


choice = input("Select your row (A-D)").lower()
# ROW ONE
if choice == "a":
    temp_list = []
    temp_list.append(row_1_item_1),temp_list.append(row_1_item_2),temp_list.append(row_1_item_3),temp_list.append(row_1_item_4)
    print(temp_list)

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
            print(gen_words[x],"----",words[index])
            if gen_words[x] == words[index]:
                valid_words.append(gen_words[x])
                print("GEN WORDS : ",gen_words[x])
                print("WORDS : ",words[index])
# ROW TWO 
elif choice == "b":
    temp_list = []
    temp_list.append(row_2_item_1),temp_list.append(row_2_item_2),temp_list.append(row_2_item_3),temp_list.append(row_2_item_4)
    print(temp_list)

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
            print(gen_words[x],"----",words[index])
            if gen_words[x] == words[index]:
                valid_words.append(gen_words[x])
                print("GEN WORDS : ",gen_words[x])
                print("WORDS : ",words[index])


print(valid_words)

