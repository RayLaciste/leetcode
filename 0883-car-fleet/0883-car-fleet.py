class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(cars)[::-1]: # position, speed in reverse order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)
        