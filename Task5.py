import random

random_numbers = [random.randint(100, 500) for _ in range(50)]
unique_numbers = set(random_numbers)
count_unique = len(unique_numbers)

print(f"רשימת המספרים: {random_numbers}")
print(f"מספרים ייחודיים: {unique_numbers}")
print(f"מספר המספרים הייחודיים: {count_unique}")
