def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[1], reverse=True)

    n = len(jobs)
    # Find the maximum deadline
    max_deadline = max(job[2] for job in jobs)

    # Initialize time slots (0 means empty)
    slot = [0] * (max_deadline + 1)

    total_profit = 0
    job_order = []

    for i in range(n):
        job_id, profit, deadline = jobs[i]

        # Find a free slot before or on the deadline
        for j in range(deadline, 0, -1):
            if slot[j] == 0:
                slot[j] = job_id
                total_profit += profit
                job_order.append(job_id)
                break

    return job_order, total_profit

print("Job Sequencing with Deadlines Problem")

n = int(input("Enter number of jobs: "))
jobs = []

for i in range(n):
    j,p,d=map(int,input().split())
    jobs.append((j,p,d))
job_order, total_profit = job_sequencing(jobs)

print("\nJobs selected to maximize profit:", job_order)
print("Total profit:", total_profit)

