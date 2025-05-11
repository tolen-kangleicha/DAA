class Interval:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

def interval_scheduling(intervals):
    # Step 1: Sort intervals by finish time
    intervals.sort(key=lambda interval: interval.finish)

    selected_intervals = []
    last_finish_time = -float("inf")

    # Step 2: Iterate and select non-overlapping intervals
    for interval in intervals:
        if interval.start >= last_finish_time:
            selected_intervals.append(interval)
            last_finish_time = interval.finish  # Update last finish time

    return selected_intervals

# Example Usage
intervals = [Interval(1, 3), Interval(2, 5), Interval(3, 9), Interval(6, 8), Interval(8, 11)]
selected = interval_scheduling(intervals)

print("Selected Intervals:")
for interval in selected:
    print(f"({interval.start}, {interval.finish})")
