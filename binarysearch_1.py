# Linear search

def findposition(cards,query):
    for i in range(len(cards)):
        if cards[i]==query:
            return i
    return -1



test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}

result = findposition(test['input']['cards'], test['input']['query'])
if result==test['output']:
    print('Test case passed')
else:
    print('Test case failed')


# Binarysearch

def test_location(cards,query,mid):
    if cards[mid]==query:
        if mid-1>0 and cards[mid-1]==query:
            return 'left'
        else:
            return 'found'
    elif cards[mid]>query:
        return 'right'
    else:
        return 'left'
    

def binary_search(cards,query):
    low=0
    high=len(cards)-1
    while low<=high:
        mid=(low+high)//2
        result=test_location(cards,query,mid)
        if result=='found':
            return mid
        elif result=='right':
            low=mid+1
        else:
            high=mid-1
    return -1


test = {
    'input': { 
        'cards':[8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6
    },
    'output': 2
}

result=binary_search(test['input']['cards'], test['input']['query'])
print(result)
if result==test['output']:
    print('Test case passed')
else:
    print('Test case failed')



# finding starting and ending position of repeating elements
def findingposition(cards,query):
    i=0
    start=0
    while i<len(cards):
        if cards[i]==query:
            start=i
            while(cards[i+1]==query and i<len(cards)):
                i+=1
            end=i
            break
        i+=1          
    print('start',start)
    print('end',end)

cards=[8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]
query=6
findingposition(cards,query)











