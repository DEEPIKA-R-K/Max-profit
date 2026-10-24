
def max_profit(n):
    buildings = {

        "T": (5, 1500),  
        "P": (4, 1000),  
        "C": (10, 2000) 
    }

    dp = [None] * (n + 1)
    dp[0] = (0, {"T": 0, "P": 0, "C": 0})

    for time in range(n + 1):
        if dp[time] is None:
            continue

        profit, counts = dp[time]

        for building, (construction, earning) in buildings.items():
            finish = time + construction

            if finish >= n:
                continue

            new_profit = profit + (n - finish) * earning
            new_counts = counts.copy()
            new_counts[building] += 1

            if dp[finish] is None or new_profit > dp[finish][0]:
                dp[finish] = (new_profit, new_counts)

    
    best_profit = 0
    best_counts = {"T": 0, "P": 0, "C": 0}

    for result in dp:
        if result is not None and result[0] > best_profit:
            best_profit, best_counts = result

    print(f"Earnings: ${best_profit}")
    print(f"T: {best_counts['T']} "
          f"P: {best_counts['P']} "
          f"C: {best_counts['C']}")


# Test cases
n=int(input("Enter input"))
max_profit(n)

