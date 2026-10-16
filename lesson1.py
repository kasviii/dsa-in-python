# what we are trying to achieve we input card = [3,4,5,11,23] and query = 11
# and get an output of where the query is in card => output = 3

####====brute force====####
# def locate_card(cards, query):
#     position = 0#this is basically the index of the array/list
#     while True:
#         if cards[position] == query:
#             return position

#         position+=1#increment until you find the position corresponding to the query term
#         if position == len(cards):#this checks if we have reached the end of the array
#             return -1
# #simple way to test a testcase
# cards = [13, 11, 10, 7, 4, 3, 1, 0]
# query = 7

# print(locate_card(cards, query))

# #long healthy? way to test test cases
# tests = []
# tests.append({
#     'input': {
#         'cards':[13,11,10,7,4,3,1,0],
#         'query':7
#     },
#     'output': 3
# })

# test = tests[0]#in order to access tests you first have to get to starting point which is 0

# result = locate_card( test['input']['cards'], test['input']['query'])

# output = test['output']#we have to define output to use for comparison first

# print(result)
# print(result == output)

####====better solution working for more edge case====####
def locate_card(cards, query):
    position = 0
    while True:
        if cards[position] == query:
            return position

        position+=1
        if position == len(cards):
            return -1

tests = []
tests.append({
    'input': {
        'cards':[13,11,10,7,4,3,1,0],
        'query':1
    },
    'output': 6
})
tests.append({
    'input': {
        'cards':[4,2,1,-1],
        'query':4
    },
    'output': 0
})
tests.append({
    'input': {
        'cards':[3,-1,-9,-127],
        'query':-127
    },
    'output': 3
})
tests.append({
    'input': {
        'cards':[13],
        'query':13
    },
    'output': 0
})
tests.append({
    'input': {
        'cards':[13,11,10,7,4,3,1,0],
        'query':9
    },
    'output': -1
})
tests.append({#this edge case fails for the previous basic logic
    'input': {
        'cards':[],
        'query':1
    },
    'output': -1
})
tests.append({
    'input': {
        'cards':[13,11,11,11,11,10,7,4,3,3,3,3,1,0],
        'query':1
    },
    'output': 12
})
tests.append({
    'input': {
        'cards':[13,11,10,7,7,7,7,7,7,7,4,3,1,0],
        'query':7
    },
    'output': 3
})
# print(tests)

for test in tests:
    result = locate_card(test['input']['cards'], test['input']['query'])
    print("Expected:", test['output'], "| Got:", result, "| Passed:", result == test['output'])

