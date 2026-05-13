class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_brackets = ['}', ']', ')']

        for bracket in s:
            if bracket in closing_brackets:
                if len(stack) == 0:
                    return False
                opening_bracket = stack.pop()
                if bracket == "}" and opening_bracket != "{":
                    return False
                if bracket == "]" and opening_bracket != "[":
                    return False
                if bracket == ")" and opening_bracket != "(":
                    return False
            else:
                stack.append(bracket)
        return False if len(stack) else True