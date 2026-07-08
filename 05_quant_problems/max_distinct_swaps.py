"""
Maximum Distinct Elements After Swaps
======================================
Problem: Given arrays A and B, perform at most k swaps
(swap A[i] with B[j]). Maximize distinct elements in A.

Approach: Greedy — swap duplicates in A for new elements from B.

Time complexity: O(n log n)
Space complexity: O(n)
"""

from collections import Counter


def max_distinct(a, b, k):
    count_a = Counter(a)
    unique_in_a = set(a)

    # Elements in B not already in A — these are useful
    new_from_b = [x for x in b if x not in unique_in_a]

    # Duplicate slots in A — these can be swapped out
    duplicates = []
    for val, cnt in count_a.items():
        if cnt > 1:
            duplicates.extend([val] * (cnt - 1))

    # Greedy: swap a duplicate for a new element
    swaps = 0
    for new_val in new_from_b:
        if swaps >= k or not duplicates:
            break
        duplicates.pop()
        unique_in_a.add(new_val)
        swaps += 1

    return len(unique_in_a)


if __name__ == "__main__":
    a = [2, 3, 3, 2, 2]
    b = [1, 3, 2, 4, 1]
    k = 2
    print(f"Max distinct: {max_distinct(a, b, k)}")  # Expected: 4
