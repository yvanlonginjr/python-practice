"""
Update Release Scheduler
========================
Problem: Given n updates with planned_date[i] and alternate_date[i],
release updates in order of increasing planned date.
Each update must be released on its planned or alternate date.
Release days must be non-decreasing.
Return the minimum possible final day.

Approach: Sort by planned date, greedily pick earliest valid date
that maintains non-decreasing order.

Time complexity: O(n log n) — dominated by sort
Space complexity: O(n)
"""


def get_min_days(planned_date, alternate_date):
    n = len(planned_date)

    # Pair each update with both its dates, then sort by planned date
    updates = sorted(zip(planned_date, alternate_date), key=lambda x: x[0])

    last_day = 0  # track the last release day used

    for planned, alternate in updates:
        # Greedy choice: pick the earliest valid date
        # A date is valid if it's >= last_day (non-decreasing constraint)
        if planned >= last_day:
            last_day = planned          # use planned date if valid
        elif alternate >= last_day:
            last_day = alternate        # use alternate if planned is too early
        else:
            # Neither date works — return -1 or handle as infeasible
            return -1

    return last_day


if __name__ == "__main__":
    # Example from assessment
    planned = [3, 7, 4, 9]
    alternate = [1, 5, 2, 3]
    print(f"Minimum days: {get_min_days(planned, alternate)}")  # Expected: 9
