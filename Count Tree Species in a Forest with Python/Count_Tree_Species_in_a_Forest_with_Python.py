trees = ["oak", "pine", "maple", "oak", "birch", "pine", "oak"]

# Step 2: Count occurrences using a dictionary
tree_counts = {}
for tree in trees:
    tree_counts[tree] = tree_counts.get(tree, 0) + 1

# Step 3: Display the results
for tree, count in tree_counts.items():
    print(f"{tree}: {count}")

