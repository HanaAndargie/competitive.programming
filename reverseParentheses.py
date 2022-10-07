class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack1 = []
        stack2 = []
        for i in range(len(s)):
            if s[i] == ")":
                while stack2 and stack2[-1] != "(":
                    stack1.append(stack2[-1])
                    stack2.pop()

                stack2.pop()

                for j in stack1:
                    stack2.append(j)

                stack1 = []

            else:
                stack2.append(s[i])

        return "".join(stack2)
