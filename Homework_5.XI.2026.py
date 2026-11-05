# #სავარჯიშო 1
# def demo_o_1(data):
#     operations = 0
#     for item in data[:1]:
#         operations += 1
#     print(f"O(1) -> მონაცემთა ზომა: {len(data)}, ოპერაციების რაოდენობა: {operations}")
#
# def demo_o_n(data):
#     operations = 0
#     for item in data:
#         operations += 1
#     print(f"O(n) -> მონაცემთა ზომა: {len(data)}, ოპერაციების რაოდენობა: {operations}")
#
# def demo_o_n_kvdrt(data):
#     operations = 0
#     for i in data:
#         for j in data:
#             operations += 1
#     print(f"O(n^2) -> მონაცემთა ზომა: {len(data)}, ოპერაციების რაოდენობა: {operations}")
#
# sample_data = [10, 20, 30, 40, 50]
# demo_o_1(sample_data)
# demo_o_n(sample_data)
# demo_o_n_kvdrt(sample_data)
#
#სავარჯიშო 2
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def reverse_text(text):
    stack = Stack()
    for char in text:
        stack.push(char)
    reversed_str = ""
    while not stack.is_empty():
        reversed_str += stack.pop()
    return reversed_str

def pALINDROME(text):
    cleaned = ""
    for char in text.lower():
        if char != " ":
            cleaned += char

    stack = Stack()
    for char in cleaned:
        stack.push(char)

    reversed_cleaned = ""
    while not stack.is_empty():
        reversed_cleaned += stack.pop()

    return cleaned == reversed_cleaned


print(reverse_text("Python"))
print(reverse_text("გამარჯობა"))

print(pALINDROME("Python"))
print(pALINDROME("ababa"))
print(pALINDROME("heheheha"))