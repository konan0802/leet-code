# https://leetcode.com/problems/number-of-recent-calls/

"""
知見
・popleft()の計算量はO(1)
・スライスは内部でO(n)のコピー操作が発生する
"""

class RecentCounter:

    def __init__(self):
        self.current = []

    def ping(self, t: int) -> int:
        self.current.append(t)
        for i in reversed(range(len(self.current))):
            if self.current[i] < t-3000:
                self.current = self.current[i+1:]
                break
        return len(self.current)


class CorrectSolution:
    
    def __init__(self):
        self.q = collections.deque()
    
    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)