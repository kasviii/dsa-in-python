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
#this version i sobviously not memory efficient as it takes O(n^2)

#duplicates faster
def has_duplicates(numbers):
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False

numbers = [12, 23, 89, 77, 56, 34, 45, 12]
result = has_duplicates(numbers)
if result:
    print("has duplicate")
else:
    print("no duplicates")

##DATA STRUCTURE
#Array
marks = [88, 72, 95, 61, 79]
#Access O(1)
print(marks[1])
print(marks[-1])#prints last one

#add to end
marks.append(100)#O(1)
print(marks)

#specific position insert
marks.insert(2, 55)#O(n) as it shifts all the elements and therefore visits every element
print(marks)

#delete last element
marks.pop()#O(1)
print(marks)
#delete specific
marks.pop(2)#O(n) as it has to shift each following element
print(marks)
marks.remove(95)#O(n) same reason as before
print(marks)

#slicing, these operations take O(k)
print(marks[1:3])
print(marks[::2])#prints every second element
print(marks[::-1])#reverses the list

#Traversal
for mark in marks:
    print(mark)
for i in range(len(marks)):
    print(marks[i])

#reversing(in performing this operation we traverse the list)
for mark in reversed (marks):
    print(mark)
for mark in marks[::-1]:
    print(mark)
for i in range(len(marks)-1, -1, -1):
    print(marks[i])

#traversal using nested loop
classroom = [
    [33,45,55],
    [24,89,44],
    [45, 55,67]
    ]
for row in classroom:
    for student in row:
        print(student, end = " ")
    print()#moves to the next line
#but a nested loop is obviously not the most efficient since its O(n^2)
#a better way is 2 pointer technique used in place of nest loop in some use cases and is O(n)

# 2 pointer technique:
def find_two(numbers, target):
    numbers.sort()
    print(numbers)
    left = 0
    right = len(numbers)-1
    while left<right:
        total = numbers[left]+numbers[right]
        if total == target:
            return [numbers[left], numbers[right]]
        elif total<target:
            left+= 1
        else:
            right-=1
    return []
numbers = [12, 23, 89, 77, 56, 34, 45]
print(find_two(numbers, 57))

#2 pointer technique, same direction
def clean_list(names):
    left = 0
    for right in range(1, len(names)):
        if names[right] != names[left]:
            left = left + 1
            names[left] = names[right]
    return left+1#we return the final count by using present index + 1 coz it starts from zero
names=["amax","amax","neru","neru","gulu","zodi","zodi"]
k = clean_list(names)
print(k, names[:k])

#sliding window
