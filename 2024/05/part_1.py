
#file = "demo.txt"
file = "live.txt"

ordering_rules, page_numbers_to_update =  open(file).read().split("\n\n")
#print(ordering_rules)
#print(page_numbers_to_update)

def is_valid_page_number(page_number):
    #print(page_number)
    for rule in ordering_rules.split("\n"):
        first_page, second_page = map(int, rule.split("|"))
        if first_page in page_number and second_page in page_number:
            #print(first_page, second_page)
            is_valid_rule = page_number.index(first_page) < page_number.index(second_page)
            #print(rule)
            if not is_valid_rule:
                print("Not valid rule: ", rule, "for page number: ", page_number)
                return False
    return True


valid_page_numbers = []
for page_number_list in page_numbers_to_update.split("\n"):
    #print(page_number_list)
    page_number = list(map(int, page_number_list.split(",")))
    is_valid = is_valid_page_number(page_number)
    if is_valid:
        valid_page_numbers.append(page_number)

total_pages_middles = 0
for page_number in valid_page_numbers:
    middle = len(page_number) // 2
    total_pages_middles += page_number[middle]

print("Total number is ",total_pages_middles)
