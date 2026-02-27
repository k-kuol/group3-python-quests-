# Goblin's gold and friends
total_gold = 27
friends = 4

# Calculate gold per friend and remainder
gold_per_friend = total_gold // friends   # integer division
gold_leftover = total_gold % friends      # remainder

print(f"Each friend gets {gold_per_friend} gold pieces, and the goblin keeps {gold_leftover}.")