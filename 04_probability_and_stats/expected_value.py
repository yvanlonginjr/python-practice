"""
Expected Value Problems
=======================
Collection of EV problems with full worked solutions.
All problems show: setup → formula → calculation → interpretation.
"""


def dice_game_ev():
    """
    Problem: Roll two fair dice.
    Win $10 if sum is 7.
    Win $4 if sum is even (not 7).
    Lose $3 if sum is odd (not 7).
    What is the EV of this game?
    """
    total_outcomes = 36

    # Count outcomes for sum = 7
    # (1,6),(2,5),(3,4),(4,3),(5,2),(6,1)
    sum_7 = 6

    # Count even sums (not 7): 2,4,6,8,10,12
    even_not_7 = 18  # 1+3+5+5+3+1

    # Remaining: odd and not 7
    odd_not_7 = total_outcomes - sum_7 - even_not_7  # = 12

    ev = (sum_7/total_outcomes)*10 + (even_not_7/total_outcomes)*4 + (odd_not_7/total_outcomes)*(-3)

    print(f"P(sum=7)={sum_7/total_outcomes:.4f}, payoff=$10")
    print(f"P(even, not 7)={even_not_7/total_outcomes:.4f}, payoff=$4")
    print(f"P(odd, not 7)={odd_not_7/total_outcomes:.4f}, payoff=-$3")
    print(f"EV = ${ev:.4f}")
    return ev


def coin_flip_game_ev():
    """
    Problem: Flip a fair coin 3 times.
    Win $8 if all heads.
    Win $2 if exactly 2 heads.
    Lose $3 if exactly 1 head.
    Lose $5 if 0 heads.
    What is the fair value?
    """
    import math
    total = 2**3  # 8 outcomes

    cases = [
        (math.comb(3, 3), 8),   # 3 heads
        (math.comb(3, 2), 2),   # 2 heads
        (math.comb(3, 1), -3),  # 1 head
        (math.comb(3, 0), -5),  # 0 heads
    ]

    ev = sum((count/total) * payoff for count, payoff in cases)
    print(f"Fair value: ${ev:.4f}")
    return ev


if __name__ == "__main__":
    print("=== Dice Game ===")
    dice_game_ev()
    print("\n=== Coin Flip Game ===")
    coin_flip_game_ev()
