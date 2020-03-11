# take test case
case = int(input())
# make two list and then combine them
even_list = []
odd_list = []
for i in range(0, case):
    number = int(input())
    if(number % 2 == 0):
        even_list.append(number)
    else:
        odd_list.append(number)

even_list.sort()                # sort by asc
odd_list.sort(reverse = True)   # sort by desc
final = even_list + odd_list    # combine them

for i in final:
    print(i)
