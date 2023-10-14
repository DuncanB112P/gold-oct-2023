# Define a list of monthly spendings.
spendings = [1346.0, 987.50, 1734.40, 2567.0, 3271.45, 2500.0, 2130.0, 2510.30, 2987.34, 3120.50, 4069.78, 1000.0]

# Initialize counters for low, normal, and high spendings.
low = 0
normal = 0
high = 0

# Iterate through each monthly spending in the list.
for month in spendings:
    # Check if the spending is less than 1000.0.
    if month < 1000.0:
        # If it is, increment the 'low' counter.
        low += 1
    # If the spending is not less than 1000.0, check if it is less than or equal to 2500.0.
    elif month <= 2500.0:
        # If it is, increment the 'normal' counter.
        normal += 1 
    # If the spending is neither low nor normal, it is considered high.
    else:
        # Increment the 'high' counter.
        high += 1

# Print the counts of low, normal, and high spendings.
print('Numbers of months with low spendings: ' + str(low) + ', normal spendings: ' + str(normal) + ', high spendings: ' + str(high) + '.')