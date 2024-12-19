# This program was provided by ChatGPT and solves part 2 correctly. I gave ChatGPT my solution to part 1 and told it
# what I was trying to do, how python couldn't keep track of such a long list, and asked it to use a caching method.
# This is what is spit out, and it works. I added the timing mechanism because it was so freaking fast I wanted to know
# how fast. 75 iterations in 65 ms. Crazy.

import time

def simulate_stone_transformations_optimized(initial_stones, iterations):
    from collections import defaultdict

    # Start with a count of the initial stones
    stone_counts = defaultdict(int)
    for stone in initial_stones:
        stone_counts[stone] += 1

    for x in range(iterations):
        new_counts = defaultdict(int)

        # Process each stone type and its count
        for stone, count in stone_counts.items():
            if stone == 0:
                # Transformations for a 0 stone
                new_counts[1] += count
            elif len(str(stone)) // 2 == len(str(stone)) / 2:
                # Split into two stones
                length = len(str(stone))
                half = int(length / 2)
                first = str(stone)[:half]
                second = str(stone)[half:].lstrip("0")
                if len(second) == 0:
                    second = 0
                new_counts[int(first)] += count
                new_counts[int(second)] += count
            else:
                # Multiply by 2024
                new_counts[stone * 2024] += count

        # Update the stone counts for the next iteration
        stone_counts = new_counts

    # Sum up all the counts to get the total number of stones
    total_stones = sum(stone_counts.values())
    total_keys = 0
    for key in stone_counts:
        total_keys += 1
    print(f"There are {total_keys} unique values in the cache.")
    return total_stones

start = time.time()
initial_stones = [0, 5601550, 3914, 852, 50706, 68, 6, 645371]
iterations = 500
result = simulate_stone_transformations_optimized(initial_stones, iterations)
print(f"Total stones after {iterations} iterations: {result}")
print(f"Total time: {time.time() - start}")