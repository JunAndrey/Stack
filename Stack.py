class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def full_size(self):
        return self.stack


def check_components(string):
    stack = Stack()
    in_item, out_item = "<({[", ">)}]"
    for item in string:
        if item in in_item:
            stack.push(item)
        elif item in out_item:
            if stack.isEmpty():
                return False
            else:
                stack_pop = stack.pop()
                balancing_components = in_item[out_item.index(item)]
                if stack_pop != balancing_components:
                    return False
        else:
            return False
    return stack.isEmpty()


if __name__ == "__main__":
    my_stack = Stack()
    print('Stack state', my_stack.full_size())
    print('Stack empty!!', my_stack.isEmpty())
    my_stack.push(4)
    my_stack.push('Stack not empty')
    my_stack.push(777)
    my_stack.push(999)
    print(my_stack.size())
    print(my_stack.peek())
    print('Popped item', my_stack.pop())
    print('Stack state', my_stack.full_size())


components = '(({[]}))'
print('Result: ', check_components(components))
