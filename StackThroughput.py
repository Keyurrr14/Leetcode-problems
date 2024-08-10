def stack_operations(n, x, y, t):
    elements = 0
    throughput = 0
    total_added = 0
    total_removed = 0

    for sec in range(1, t + 1):
        if sec % n == 0:
            elements += x
            throughput += x
            total_added += x
            elements -= y
            throughput += y
            total_removed += y
        else:
            throughput += y - x

    throughput = total_added + total_removed

    return elements, throughput, total_added, total_removed

# Example usage:
n = 5  # Alternate every 5 seconds
x = 3  # Add 3 elements every 5 seconds
y = 2  # Remove 2 elements every 5 seconds
t = 20  # Total number of seconds

num_elements, total_throughput, total_added, total_removed = stack_operations(n, x, y, t)
print("Number of elements in stack after {} seconds: {}".format(t, num_elements))
print("Total throughput in {} seconds: {}".format(t, total_throughput))
print("Total number of elements added after {} seconds: {}".format(t, total_added))
print("Total number of elements removed after {} seconds: {}".format(t, total_removed))
