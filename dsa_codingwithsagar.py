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

#tiny thing to remember, f string in print
name = "Kasvi"
age = 21
#without f
print("My name is", name, "and I am", age)
#with f
print(f"My name is {name} and I am {age}")

#sliding window example
""" the example is that we have chocolates of different prizes, but we can only choose three consecutively laid out options
so we compare sums of each three group, to get the most expensive group possible"""
def best_sum(prices, window_size):
    current_total = sum ( prices[0 : window_size])
    best_total = current_total
    print(f"window 1: {prices[0:window_size]}={current_total}")

    for i in range(window_size, len(prices)):
        left_choco = prices[i-window_size]
        right_choco = prices[i]

        current_total = current_total-left_choco+right_choco
        window = prices[i - window_size + 1 : i + 1]#so this gives something like 3-3+1:3+1 which is prices[1:4]
        print(f"window : {window} = {current_total}")

        if current_total>best_total:
            best_total = current_total
    return best_total
        
prices = [2,4,6,1,7,3,5]
answer = best_sum(prices,3)
print("Best total", answer)

##Stack
#list way
stack = []

stack.append("a")
stack.append("b")
stack.append("c")
print(stack)
print("top item", stack[-1])
item = stack.pop()
print("popped", item)
print(stack)

print(len(stack) == 0)
"""when we accessed the top element, we could've just as easily written 2 or anything else
and recieved that element, so list can be used as a stack but isn't the right way always, as
in a stack one can only interact with last inserted item or the item on top, and not the rest"""

#class method, better way

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def display(self):
        print("Stack(top>bottom):", self.items[::-1])

s = Stack()
s.push(10)
s.push(24)
s.push(34)

print("After pushing")
s.display()

print("top element", s.peek())
print("popped element", s.pop())
print("After popping")
s.display()
print("stack size:", s.size())
print("Is stack empty:", s.is_empty())


##Queue
#way 1
queuee = []
#enqueue
queuee.append("R")
queuee.append("M")
queuee.append("H")
print(queuee)
#dequeue
first = queuee.pop(0)
print(first)
print(queuee)

#way 2
"""
double ended queue
o(1)
"""
from collections import deque
queue = deque()
queue.append("N")
queue.append("R")
queue.append("O")
queue.append("P")
print(queue)

first = queue.popleft()
print(first)
print(queue)

print("the new first element:", queue[0])#to look at the first element
print("size of queue:", len(queue))#to get size of queue
print("is queue empty?", len(queue)== 0)

#Priority queue



