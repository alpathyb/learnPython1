def isvalid(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack.pop() != bracket_map[char]:
                return False
        else:
            return False

    return not stack


input_str = "(){}[]"
result = isvalid(input_str)
if result:
    print("the input string valid")
else:
    print("the input not valid")
