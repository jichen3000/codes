class MyQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def remove_duplicates(the_list):
    result = []
    for item in the_list:
        if item not in result:
            result.append(item)
    return result

a = [1, 3, 7, 1, 2, 4, 7]
# print remove_duplicates(a)        

def remove_duplicates_without_new(the_list):
    for index in range(len(the_list))[::-1]:
        print index
        item = the_list[index]
        print item
        print the_list[index:len(the_list)]
        if item in the_list[index+1:len(the_list)]:
            the_list.pop(index)
    return the_list
print remove_duplicates_without_new(a)