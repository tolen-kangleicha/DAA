class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_scheduling(jobs):
    # Step 1: Sort jobs by profit in descending order
    jobs.sort(key=lambda job: job.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)  # Find max deadline
    schedule = [-1] * max_deadline  # Slots for jobs (-1 means empty)

    total_profit = 0

    # Step 2: Assign jobs to the latest available slot before deadline
    for job in jobs:
        for t in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if schedule[t] == -1:  # Slot is empty
                schedule[t] = job.id  # Schedule job
                total_profit += job.profit
                break

    return total_profit, [job for job in schedule if job != -1]

# Example Usage
jobs = [Job("A", 2, 100), Job("B", 1, 50), Job("C", 2, 10), Job("D", 1, 20), Job("E", 3, 30)]
max_profit, job_order = job_scheduling(jobs)

print(f"Maximum Profit: {max_profit}")
print(f"Job Execution Order: {job_order}")
