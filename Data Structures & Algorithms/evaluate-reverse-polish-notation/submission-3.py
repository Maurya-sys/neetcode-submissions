class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        op = ['+','-','*','/']
        
        tracker = []
        for i in tokens:
            if i not in op:
                tracker.append(int(i))
            else:
                b = tracker.pop()
                a = tracker.pop()
                res = eval(f"{a}{i}{b}")
                tracker.append(int(res))
        return tracker[0]
