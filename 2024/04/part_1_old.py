import regex as re

file = "demo.txt"
#file = "live.txt"

words =  open(file).read()
line_size = len(words.split("\n")[0])
all_words = words.replace("\n","")
print(all_words)

# Get horizontal words
horizontal = re.findall(r"(XMAS|SAMX)", all_words, overlapped=True)
horizontal_count = len(horizontal)

# Get vertical words
string_to_find = "X.{%d}M.{%d}A.{%d}S" %(line_size -1, line_size -1, line_size -1)
string_backwords = "S.{%d}A.{%d}M.{%d}X" %(line_size -1, line_size -1, line_size -1)

final_match_string = "(%s|%s)" %(string_to_find, string_backwords)

vertical = re.findall(final_match_string, all_words, overlapped=True)
vertical_count = len(vertical)

# get oblque words
string_to_find = "X.{%d}M.{%d}A.{%d}S" %(line_size, line_size, line_size)
string_backwords = "S.{%d}A.{%d}M.{%d}X" %(line_size, line_size, line_size)

string_to_find_reverse = "X.{%d}M.{%d}A.{%d}S" %(line_size-2, line_size-2, line_size-2)
string_backwords_reverse = "S.{%d}A.{%d}M.{%d}X" %(line_size-2, line_size-2, line_size-2)

final_match_string = "(%s|%s|%s|%s)" %(string_to_find, string_backwords, string_to_find_reverse, string_backwords_reverse)
oblque1 = re.findall(string_to_find, all_words, overlapped=True)
oblque2 = re.findall(string_backwords, all_words, overlapped=True)
oblque3 = re.findall(string_to_find_reverse, all_words, overlapped=True)
oblque4 = re.findall(string_backwords_reverse, all_words, overlapped=True)
oblque_count1 = len(oblque1)
oblque_count2 = len(oblque2)
oblque_count3 = len(oblque3)
oblque_count4 = len(oblque4)

oblque_count = oblque_count1 + oblque_count2 + oblque_count3 + oblque_count4

total = horizontal_count + vertical_count + oblque_count
print("horizontal=", horizontal_count)
print("vertical=", vertical_count)
print("oblque=", oblque_count)
print("total=", total)