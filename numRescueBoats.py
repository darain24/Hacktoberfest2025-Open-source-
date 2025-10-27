class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        while people:
            if people[-1] + people[0] <= limit:
                ans += 1
                people = people[1:-1]
            else:
                ans += 1
                people.pop()
        
        return ans

        
