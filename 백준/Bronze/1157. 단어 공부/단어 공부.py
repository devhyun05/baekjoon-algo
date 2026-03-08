s = input()
word_dict = {}

for c in s.lower():
    word_dict[c] = word_dict.get(c, 0) + 1
    
max_count = 0

for c, char_count in word_dict.items():
    if char_count > max_count: 
        max_count = char_count 

occur_times = 0
ans = ""

for c, char_count in word_dict.items():
    if char_count == max_count: 
        occur_times += 1
        ans = c.upper()

if occur_times > 1: 
    print("?")
else:
    print(ans)
    