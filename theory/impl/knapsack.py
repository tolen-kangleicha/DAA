class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def fractional_knapsack(capacity, items):
    items.sort(key=lambda item: item.profit / item.weight, reverse=True)
    total_profit = 0.0

    for item in items:
        if capacity == 0:
            break
        if item.weight <= capacity:
            total_profit += item.profit
            capacity -= item.weight
        else:
            total_profit += (item.profit / item.weight) * capacity
            capacity = 0    # knapsack is full
    return total_profit

if __name__ == "__main__":
    items = [Item(11, 20), Item(16, 100), Item(10, 100)]
    capacity = 1000
    max_profit = fractional_knapsack(capacity, items)
    print(f"Maximum profit in knapsack = {max_profit:.2f}")
