
#file = "demo.txt"
file = "live.txt"

ordering_rules, page_numbers_to_update =  open(file).read().split("\n\n")

def sort_page_number(page_number):
    for rule in ordering_rules.split("\n"):
        first_page, second_page = map(int, rule.split("|"))
        if not (first_page in page_number and second_page in page_number):
            continue
        is_valid_rule = page_number.index(first_page) < page_number.index(second_page)
        if not is_valid_rule:
            # swap the pages
            new_page_number = page_number.copy()
            new_page_number[page_number.index(second_page)] = first_page
            new_page_number[page_number.index(first_page)] = second_page
            page_number = sort_page_number(new_page_number)
    return page_number

def is_valid_page_number(page_number):
    for rule in ordering_rules.split("\n"):
        first_page, second_page = map(int, rule.split("|"))
        if first_page in page_number and second_page in page_number:
            is_valid_rule = page_number.index(first_page) < page_number.index(second_page)
            if not is_valid_rule:
                return False
    return True

sorted_pages = []
for page_number_list in page_numbers_to_update.split("\n"):
    page_number = list(map(int, page_number_list.split(",")))
    is_valid = is_valid_page_number(page_number)
    if not is_valid:
        sorted_page_number = sort_page_number(page_number)
        sorted_pages.append(sorted_page_number)

total_pages_middles = 0
for sorted_page in sorted_pages:
    middle = len(sorted_page) // 2
    total_pages_middles += sorted_page[middle]

print("Total number is ",total_pages_middles)
