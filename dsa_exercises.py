# creating stack using class for a list array
class Stack:
    def __init__(self):
        self.stack = []

    def push_stack(self, element):
        return self.stack.append(element)

    def pop_stack(self):
        return self.stack.pop()

    def peek_stack(self):
        return self.stack[-1]

    def is_emptystack(self):
        ck = not bool(self.stack)
        return ('Empty stack', ck)
    

    def size_stack(self):
        return len(self.stack)

user = Stack()

(user.push_stack('A'))
(user.push_stack('B'))
(user.push_stack('C'))
(user.push_stack('D'))

print('push: ', user.stack)
print('pop: ', user.pop_stack())
print('peek: ', user.peek_stack())
print('isEmpty', user.is_emptystack())
print('size: ', user.size_stack())
print('\n'*3)


# creating stack using class for a linked-list array
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_Node = Node(value)
        if self.head:
            new_Node.next = self.head
        self.head = new_Node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.head.value

    def stacksize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def transverseAndprint(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" <> ")
            currentNode = currentNode.next
        print()


user_trial = Stack()
user_trial.push('4')
user_trial.push('3')
user_trial.push('2')
user_trial.push('1')

print("LinkedList: ", end="")
user_trial.transverseAndprint()
print("Peek: ", user_trial.peek())
print("Pop: ", user_trial.pop())
print("LinkedList after Pop: ", end="")
user_trial.transverseAndprint()
print("isEmpty: ", user_trial.isEmpty())
print("Size: ", user_trial.stacksize())
print('\n'*3)


# creating queues using class for list arrays
class Queues:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        return self.queue.append(element)

    def dequeue(self):
        if self.queue == 0:
            return "Empty queue"
        return self.queue.pop(0)

    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        if self.queue == 0:
            return "Empty queue"
        x = not bool(self.queue)
        return x


    def size(self):
        return len(self.queue)

queue_manager = Queues()
queue_manager.enqueue('a'.upper())
queue_manager.enqueue('b'.upper())
queue_manager.enqueue('c'.upper())
queue_manager.enqueue('d'.upper())

print('queue: ', queue_manager.queue)
print('dequeue: ', queue_manager.dequeue())
print('after dequeue: ', queue_manager.queue)
print('peek: ', queue_manager.peek())
print('isempty: ', queue_manager.isEmpty())
print('size: ', queue_manager.size())
print('\n'*3)


#CREATING PYTHON BINARY TREE
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

# def inOrderTraversal(node):
#     if node is Node:
#         return
#     inOrderTraversal(node.left)
#     print(node.date, end=', ')
#     inOrderTraversal(node.right)

def searchTree(node, target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target < node.data:
        return searchTree(node.left, target)
    else:
        return searchTree(node.right, target)


root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

# root = Binary('R')
# nodeA = Binary('A')
# nodeB = Binary('B')
# nodeC = Binary('C')
# nodeD = Binary('D')
# nodeE = Binary('E')
# nodeF = Binary('F')
# nodeG = Binary('G')

# root.left = nodeA
# root.right = nodeB

# nodeA.left = nodeC
# nodeA.right = nodeD

# nodeB.left = nodeE
# nodeB.right = nodeF

# nodeF.left = nodeG

print("root.right.left.data:", root.right.left.data)

# inOrderTraversal(root)


result = searchTree(root, 13)
if result:
    print(f'Found our target at {result.data}')
else:
    print("Target doesn't exit")
print('\n'*3)


# BINARY SEARCH
def binary_search(arr, target_val):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right)//2

        if arr[mid] == target_val:
            return mid
        
        if arr[mid] < target_val:
            left = mid + 1
        else:
            right = mid - 1

    return -1 
        
       
arraylist = [1,2,3,4,5,6,7,8,9]
target = 6

result = binary_search(arraylist, target)
if result != -1:
    print(f"found at index {result}")
else:
    print("index not found")
print('\n'*3)


# BUBBLE SORT
bubble_array = [1, 14, 9, 15, 12, 5]
for outer_loop in range(len(bubble_array) - 1):
    for inner_loop in range(len( bubble_array )- outer_loop - 1):
        if bubble_array[inner_loop] > bubble_array[inner_loop + 1]:
            bubble_array[inner_loop], bubble_array[inner_loop+1] = bubble_array[inner_loop+1], bubble_array[inner_loop]
    
print(bubble_array)
print('\n'*3)


# QUICK SORT
