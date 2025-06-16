import random

for i in range(10):
    print("labas")
# -------------------------------------
nums=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums)

# ------------------------------------------

plants=["rose", "ivy", "lily", "daisy", "violet", "poppy", "corn", "moss", "lotus", "cactus"]
print(plants)

for plant in plants:
    print(plant)

 # ------------------------------

plants=["rose", "ivy", "lily", "daisy", "violet", "poppy", "corn", "moss", "lotus", "cactus"]
print(plants)
for plant in reversed(plants):
    print(plant)

 # -----------------------------------------

for number in range(10, 51, 2):
    print(number)

# -------------------------------
for number in range(10, 51):
    if i % 2 == 0:
        continue
        print(i)
# --------------------------------------

for number in range(10, 51, 2):
    if number % 10 == 0:
        continue
    print(number)

 # ----------------------------------
count=0
for i in range(0, 21):
    if i % 2 == 0:
        count += 1
        print(count)

# ------------------------------
plants=["rose", "ivy", "lily", "daisy", "violet", "poppy", "corn", "moss", "lotus", "cactus"]
print(plants)

short_count=0
long_count=0

for plant in plants:
    length=len(plant)
    if length >= 7:
        long_count +=1
    if length <= 5:
        short_count +=1
print("shorter_words", short_count)
print("longer_words", long_count)

# -----------------------------------------------

plants=["rose", "ivy", "lily", "daisy", "violet", "poppy", "corn", "moss", "lotus", "cactus"]
print(plants)

count=0

for plant in plants:
    length = len(plant)
    if length > 5 and length < 10:
        count += 1
print("middle_words:", count)

# ---------------------------------


numbers = [random.randint(0, 300) for _ in range(300)]

output = []
for num in numbers:
    if num > 275:
        output.append(f"[{num}]")
    else:
        output.append(str(num))
print(output)
count = sum(1 for num in numbers if num > 150)
print("amount of numbers", count)

# -------------------------------------------------------

first = True
for num in range(1, 3001):
    if num % 77 == 0:
        if not first:
            print(", ", end="")
        print(num, end="")
        first = False
print()
# ---------------------------------------------------------

print(", ".join(str(num) for num in range(1, 3001) if num % 77 == 0))

# -------------------------------------------------------






