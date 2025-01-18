# class StringChallenge:
#     def __init__(self, n, m, strings, costs, contradictions, budget):
#         self.n = n
#         self.m = m
#         self.strings = strings
#         self.costs = costs
#         self.budget = budget
#         self.worths = [self.calculate_worth(s) for s in strings]
        
#         # Map each string to its index
#         self.string_to_index = {s: i for i, s in enumerate(strings)}
        
#         # Build contradiction map
#         self.contradiction_map = [0] * n
#         for a, b in contradictions:
#             a_idx = self.string_to_index[a]
#             b_idx = self.string_to_index[b]
#             self.contradiction_map[a_idx] |= (1 << b_idx)
#             self.contradiction_map[b_idx] |= (1 << a_idx)

#     def calculate_worth(self, string):
#         return sum(ord(char) - ord('a') + 1 for char in string)

#     def solve(self):
#         dp = [0] * (self.budget + 1)  # DP array for the maximum worth achievable at each budget level

#         for mask in range(1 << self.n):  # Iterate over all subsets of strings
#             total_cost = 0
#             total_worth = 0
#             valid = True

#             # Check if the current subset is valid and calculate its total cost and worth
#             for i in range(self.n):
#                 if mask & (1 << i):  # If the i-th string is in the current subset
#                     # Check for contradictions
#                     if self.contradiction_map[i] & mask:
#                         valid = False
#                         break
#                     total_cost += self.costs[i]
#                     total_worth += self.worths[i]

#             # If valid and within budget, update the dp array
#             if valid and total_cost <= self.budget:
#                 dp[total_cost] = max(dp[total_cost], total_worth)

#         # Find the maximum worth over all possible budgets
#         return max(dp)

# # Input Parsing
# def main():
#     n, m = map(int, input().split())
#     strings = input().split()
#     costs = list(map(int, input().split()))
#     contradictions = [input().split() for _ in range(m)]
#     budget = int(input())

#     # Solve the problem
#     challenge = StringChallenge(n, m, strings, costs, contradictions, budget)
#     result = challenge.solve()
    
#     # Print the result without any extra formatting
#     print(result)

# if __name__ == "__main__":
#     main()


class StringChallenge:
    def __init__(self, n, m, strings, costs, contradictions, budget):
        self.n = n
        self.m = m
        self.strings = strings
        self.costs = costs
        self.budget = budget
        self.worths = [sum(ord(c) - ord('a') + 1 for c in s) for s in strings]
        self.string_to_index = {s: i for i, s in enumerate(strings)}
        self.contradiction_map = [0] * n
        for a, b in contradictions:
            a_idx, b_idx = self.string_to_index[a], self.string_to_index[b]
            self.contradiction_map[a_idx] |= (1 << b_idx)
            self.contradiction_map[b_idx] |= (1 << a_idx)

    def solve(self):
        dp = [0] * (self.budget + 1)
        for mask in range(1 << self.n):
            total_cost, total_worth, valid = 0, 0, True
            for i in range(self.n):
                if mask & (1 << i):
                    if self.contradiction_map[i] & mask:
                        valid = False
                        break
                    total_cost += self.costs[i]
                    total_worth += self.worths[i]
            if valid and total_cost <= self.budget:
                dp[total_cost] = max(dp[total_cost], total_worth)
        return max(dp)

def main():
    n, m = map(int, input().split())
    strings = input().split()
    costs = list(map(int, input().split()))
    contradictions = [input().split() for _ in range(m)]
    budget = int(input())
    challenge = StringChallenge(n, m, strings, costs, contradictions, budget)
    print(challenge.solve())

if __name__ == "__main__":
    main()
