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
size=25
symbol='*'
for i in range(size):
    print(symbol * size)
# -----------------------------------------------

while True:
    result = random.randint(0, 1)
    if result == 0:
        print("H")
        break
    else:
        print("S")

# ------------------------------------------------------
emblem=0
while emblem < 3:
    throw = random.randint(0, 1)
    if throw == 0:
        print("H")  # Herbas
        emblem += 1
    else:
        print("S")
# ----------------------------------------------

emblem_in_row = 0

while emblem_in_row < 3:
    throw = random.randint(0, 1)
    if throw == 0:
        print("H")
        emblem_in_row += 1
    else:
        print("S")
        emblem_in_row = 0
# -------------------------------------------


petras_points = 0
kazys_points = 0

while petras_points < 222 and kazys_points < 222:
    petras = random.randint(10, 20)
    kazys = random.randint(5, 25)

    petras_points += petras
    kazys_points += kazys

    print(f"Petras: {petras_points} taškai, Kazys: {kazys_points} taškai.")

    if petras > kazys:
        print("Partiją laimėjo: Petras\n")
    elif kazys > petras:
        print("Partiją laimėjo: Kazys\n")
    else:
        print("Partija baigėsi lygiosiomis\n")

if petras_points >= 222 and kazys_points >= 222:
    print("Abu pasiekė 222 taškus – lygiosios!")
elif petras_points >= 222:
    print("Žaidimą laimėjo: Petras!")
else:
    print("Žaidimą laimėjo: Kazys!")
# -----------------------------------------------------

total_hits = 0

for i in range(5):
    length = 0
    hits = 0

    while length < 85:
        length += random.randint(5, 20)
        hits += 1

    print(f"Vinis {i+1} įkalta per {hits} smūgius.")
    total_hits += hits

print(f"Viso smūgių: {total_hits}")

# --------------------------------------------------------

total_hits = 0

for i in range(5):
    length = 0
    hits = 0

    while length < 85:
        length += random.randint(20, 30)
        hits += 1

    if random.randint(0, 1) == 1:
        length += random.randint(20, 30)
        print(f"  Smūgis {hits}: pataikė, įkala {length} mm")
    else:
        print(f"  Smūgis {hits}: nepataikė")
        print(f"{i + 1}-oji vinis įkalta per {hits} smūgius")
        total_hits += hits

    print(f"\nViso smūgių: {total_hits}")

# ------------------------------------------------

numbers = random.sample(range(1, 201), 50)
result = " ".join(str(num) for num in numbers)
print(result)

# -------------------------------------------
random_array = [random.randint(5, 25) for _ in range(30)]
print(random_array)
# --------------------------------------------------------

array = [random.randint(5, 25) for _ in range(30)]
count_greater_than_10 = sum(1 for value in array if value > 10)
print("Array:", array)
print("Count of values greater than 10:", count_greater_than_10)

# -----------------------------------------------------------
random_array = [random.randint(5, 25) for _ in range(30)]
numb= max(random_array)
print(random_array)
print(numb)
# ----------------------------------------------------------
random_array = sum([random.randint(5, 25) for _ in range(30)])
print(random_array)
# ------------------------------------------------------
random_array =[random.randint(5, 25) for _ in range(30)]
new_array = [value - index for index, value in enumerate(random_array)]
print(random_array)
print(new_array)

# -------------------------------------------------

random_array =[random.randint(5, 25) for _ in range(30)]
random_array.extend([random.randint(5, 25) for _ in range(10)])
print(random_array)

# ------------------------------------------------------------
num=0
random_array =[random.randint(5, 25) for _ in range(30)]

even_array = [random_array[i] for i in range(0, 30, 2)]
odd_array  = [random_array[i] for i in range(1, 30, 2)]
print(even_array)
print(odd_array)

# --------------------------------------------------------------
random_array =[random.randint(5, 25) for _ in range(30)]
for i in range(0, len(array), 2):
    if array[i] > 15:
        array[i] = 0
        print(array)
# ---------------------------------------------------

array =[random.randint(5, 25) for _ in range(30)]
for i in range(len(array)):
    if array[i] > 10:
        print(f"\nFirst index with value > 10: {i} (value = {array[i]})")
        break
# ------------------------------------------------------

letters= [random.choice(['A', 'B', 'C', 'D']) for _ in range(200)]
print(random_array)
A_sk = letters.count('A')
B_sk = letters.count('B')
C_sk = letters.count('C')
D_sk = letters.count('D')

print("letters.count:")
print("A =", A_sk)
print("B =", B_sk)
print("C =", C_sk)
print("D =", D_sk)

letters.sort()

#----------------------------------------------------
def generate_array():
    return [random.choice(['A', 'B', 'C', 'D']) for _ in range(200)]

array1 = generate_array()
array2 = generate_array()
array3 = generate_array()

combined = [array1[i] + array2[i] + array3[i] for i in range(200)]
# -------------------------------------------------------
def say_hi_to(name):
    print("hi", name)
say_hi_to("Jonas")
say_hi_to("Petras")

def sim_pi():
    return 3.14
print(sim_pi())
sp = sim_pi()
print(sp)
# ------------------------------------

def summ(a, b,):
    return a+b
result=summ(2,6)
print(result)
# -------------------------------------------


