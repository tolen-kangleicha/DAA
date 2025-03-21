from itertools import combinations

class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def is_valid_schedule(subset):
    # Check if all jobs in the subset can be scheduled before deadlines
    subset = sorted(subset, key=lambda job: job.deadline)  # Sort by deadline
    time_slots = set()
    
    for job in subset:
        for t in range(job.deadline, 0, -1):
            if t not in time_slots:  # Assign job to the latest available time slot
                time_slots.add(t)
                break
        else:
            return False  # If no valid slot is found, subset is invalid
    
    return True

def brute_force_job_scheduling(jobs):
    max_profit = 0
    best_schedule = []

    # Generate all possible subsets of jobs
    for r in range(1, len(jobs) + 1):
        for subset in combinations(jobs, r):  # Generate all job subsets
            if is_valid_schedule(subset):  # Check if it can be scheduled
                total_profit = sum(job.profit for job in subset)
                if total_profit > max_profit:
                    max_profit = total_profit
                    best_schedule = subset

    return max_profit, [job.id for job in best_schedule]

# Example Usage
jobs = [Job("A", 2, 100), Job("B", 1, 50), Job("C", 2, 10), Job("D", 1, 20), Job("E", 3, 30)]
max_profit, job_order = brute_force_job_scheduling(jobs)

print(f"Maximum Profit: {max_profit}")
print(f"Job Execution Order: {job_order}")
