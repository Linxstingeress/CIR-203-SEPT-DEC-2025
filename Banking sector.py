import numpy as np
transactions = np.array([
    [1200, 1500, 1600, 1400, 1700, 1800],  
    [2000, 2100, 1900, 2200, 2300, 2500],  
    [1700, 1600, 1800, 1750, 1900, 2000],  
    [1000, 1200, 1100, 1300, 1250, 1350]   
])
print("Transaction Volumes (4x6):")
print(transactions)
total_per_branch = np.sum(transactions, axis=1)
print("\nTotal Transactions Per Branch:")
print(total_per_branch)
highest_branch = np.argmax(total_per_branch) + 1  
print("\nBranch with Highest Transactions:")
print(f"Branch {highest_branch} with {total_per_branch[highest_branch-1]} transactions")
average_monthly = np.mean(transactions, axis=0)
print("\nAverage Monthly Transaction Volume:")
print(average_monthly)
reshaped_array = transactions.reshape(3, 8)
print("\nReshaped Array (3x8):")
print(reshaped_array)