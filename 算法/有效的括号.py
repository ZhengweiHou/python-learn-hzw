

class Solution:
    sol_dict={')':'(',']':'[','}':'{'}
    def isValid(self,s:str) -> bool:
        stack = []
        for c in s:
            if self.sol_dict.__contains__(c):
                tempc = '$' if len(stack) < 1 else stack.pop()
                if tempc != self.sol_dict[c]:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0


class Solution2:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

s1 = Solution();

print(s1.isValid(s='({[1]})'))
