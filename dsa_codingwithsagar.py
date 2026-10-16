#for O(1)
marks = [88,72,95,61,79]
first_m = marks[0]
print(first_m)#the list can be even longer but the effort will be the same

#for O(logn)
def find_name(names, target):
    left = 0
    right = len(names)-1
    while left<=right:
        middle = (left+right)//2

        if names[middle] == target:
            return middle
        elif names[middle]<target:
            left = middle+1
        else:
            right = middle-1
    return -1

names = ["aa","bh","cc","dee"]
target_name = "cc"
result = find_name(names, target_name)
if result != -1:
    print("found at", result)
else:
    print("not found")

#for O(n)
def find_paper(papers, name):
    for paper in papers:
        if paper == name:
            return True
    return False

papers = ["az","sx","er","qw"]
search_name = "az"
result = find_paper(papers, search_name)
if result:
    print("paper found")
else:
    print("paper not found")

#O(n^2)
def find_duplicates(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return True
    return False

numbers = [12, 23, 34, 45, 12]
result = find_duplicates(numbers)
if result:
    print("duplicate found")
else:
    print("no duplicates")