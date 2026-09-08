class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # use to track opening parenthesis
        pairs = ["[]" ,"()" , "{}"]  # used to check if closing parenthesis makes a valid pair
        for p in s:
            # add opening parenthesis
            if p in ["[", "{", "("]:
                stack.append(p)
                continue

            # for closing parenthesis, first check if stack is empty
            if stack:
                # if not empty, now check if last item in stack is matching opening parenthesis
                if stack[-1] + p in pairs:
                    # if pair is good, pop opener and move to next iteration
                    stack.pop()
                else:
                    # if no good pair, return False
                    return False
            else:
                # if empty, theres an extra closing, so return False
                return False
        
        return not stack
            
        
        