letters = ["c", "f", "j"]
target = "k"


letters_to_nums = []

for i in letters:
    letters_to_nums.append(ord(i))

target_to_nums = ord(target)


flag = False
for j in letters_to_nums:
    if j > target_to_nums:
        flag = True
        print(chr(j))
        break

if not flag:
    print(chr(min(letters_to_nums)))