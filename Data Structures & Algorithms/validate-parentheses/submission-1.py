class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_brackets = ['}', ']', ')']
        bracket_map = {
            '{': '}',
            '[': ']',
            '(': ')',
        }

        for bracket in s:
            if bracket in bracket_map:
                stack.append(bracket)
            elif len(stack) == 0:
                return False
            else:
                opening_bracket = stack.pop()
                if bracket_map[opening_bracket] != bracket:
                    return False
            # if bracket in closing_brackets:
            #     if len(stack) == 0:
            #         return False
            #     opening_bracket = stack.pop()
            #     if bracket == "}" and opening_bracket != "{":
            #         return False
            #     if bracket == "]" and opening_bracket != "[":
            #         return False
            #     if bracket == ")" and opening_bracket != "(":
            #         return False
            # else:
            #     stack.append(bracket)
        return False if len(stack) else True