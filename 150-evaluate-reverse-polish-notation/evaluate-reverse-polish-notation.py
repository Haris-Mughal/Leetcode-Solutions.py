class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        oper = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }

        for token in tokens:
            if token in oper:

                b = stack.pop()
                a = stack.pop()

                stack.append(oper[token](a, b))

            else: 
                stack.append(int(token))
        
        return stack[0]