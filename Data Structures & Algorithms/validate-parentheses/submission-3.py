class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        stack = []

        for c in s:
            if c in pairs:
                stack.append(c)

            if c == pairs[stack[-1]]:
                stack.pop()

        return not stack

