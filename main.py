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
# Sukurkite Funkciją kuri priima du kintamuosius, skaičius.
# Juos susumuoja ir atspausdina.
def summ(a, b,):
    return a+b
result=summ(2,6)
print(result)
# -------------------------------------------
# Sukurkite Funkciją kuri vadinasi PISq.
# Funkcija gražina reikšmę. Reikšmė yra : 9.8596; Gautą reikšmę atspausdinkite.
def PISq():
    return 9.8596
result=PISq()
print(result)

# ----------------------------------------------
# Sukurkite Funkciją kuri priima du kintamuosius.
# Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.
def multiply (a,b):
    return a*b
result=multiply(3,5)
print(result)

# ---------------------------------------------
# Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina
# kiekvieną narį vienoje eilutėje.
def print_list (A,B,C,D):
    for letters in [A,B,C,D]:
        print(letters, end=' ')
    print()
    print(A,B,C,D)
print_list("A","B","C","D")

# ----------------------------------------------------
# Sukurkite Funkciją kuri priima du kintamuosius, min ir max reikšmėms nustatyti
# ir sugeneruoja random int skaičių ir jį gražintų.
def generate_random(min_value, max_value):
    return random.randint(min_value, max_value)
result = generate_random(2, 20)
print(result)

# ------------------------------------------------
# Sukurkite Funkciją kuri sugeneruotų random skaičių masyvą ir jį gražintų.
# Funkcija priima tris kintamuosius, min, max ir length reikšmėms nustatyti.
def generate_random_array(length, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(length)]
print(generate_random_array(5, 1, 10))


# ------------------------------------------------------
# Sukurkite Funkciją kuri panaudotų 6toje užduotyje sugeneruotą masyvą
# (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.
def generate_and_sum(min_value, max_value, length):
    array = [random.randint(min_value, max_value) for _ in range(length)]
    total = sum(array)
    print(array)
    return total
suma = generate_and_sum(1, 10, 5)
print(suma)
# ---------------------------------------------------------
# Sukurkite Funkciją kuri priimtų 6toje užduotyje sugeneruotą masyvą ir
# gražintų jos skaičių vidurkį.
def generate_and_avg(min_value, max_value, length):
    array = [random.randint(min_value, max_value)for _ in range(length)]
    return array
def average_of_array(array):
    if len(array) == 0:
        return 0
    return sum(array) / len(array)
# -------------------------------------------------------
# Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį
# užpildytą žvaigždutėmis. Pirmas skaičius- išoriniam ciklui, antras vidiniam
def rectangle(rows, columns):
    for i in range(rows):
        for j in range(columns):
            print("*", end="")
        print()
rectangle(3, 5)
# ---------------------------------------------------
# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek
# jame yra raidžių(simbolių) ir tarpų. Sakinys - “Šiandien labai graži diena”.
# (kodas turi veikti padavus bet kokį sakinį)
# (simboliu yra 23, tarpu yra 3)

def count_letters_and_gaps(sentence):
    letters=0
    gaps=0
    for char in sentence:
        if char == " ":
            gaps += 1
        else:
            letters += 1
    print("letters:", letters)
    print("gaps:", gaps)
count_letters_and_gaps("Šiandien labai graži diena")
#  here I say go through each symbol(char), if you find gap, count plus one gap,
#  as for others you plus 1 letter
# ---------------------------------------------------
def reverse_sentence(sentence):
    return sentence[::-1]
result= reverse_sentence ("Naglis")
print(result)

# double :: means to take the whole sentence and -1 means read from the back
# -------------------------------------------------
# Sukurti funkciją, kuri apsuka tik žodžius. “Labas rytas” -> “sabal satyr”
# ir atspausdina rezultatą

def reverse_sentence(sentence):
    return sentence[::-1]
result= reverse_sentence ("Labas rytas")
print(result)

# :: means to take the whole sentence, -1 from the end
# ---------------------------------------------------------------
# Sukurkite funkciją, kuri priimtų masyvą ir atspausdintų tik tuos
# elementus kurie yra skaičiai.

def only_numbers(lst):
    for item in lst:
        if isinstance(item, (int, float)):
            print(item)
data = [5, "hello", 3, 8 , "good", 10]
only_numbers(data)

# if isinstance(item, (int, float)):-checks the type of variable,
# If item is a number (either whole number or decimal), then do something."

# --------------------------------------------------------
# Sukurkite funkciją, kuri priima masyvą ir atspausdina tik
# sveikuosius skaičius. (jei pavyks, patobulinkite, kad funkcija priimtų
# antrą parametrą True/False kuris nuspręstų ar spausdins tik sveikuosius
# skaičius ar skaičius su kableliu.

def print_num(array, whole=True):
    for item in array:
        if whole and isinstance(item, int):
            print(item)
        elif not whole and isinstance(item,float):
            print(item)
data = [5, 2.34 , 3 , 8.4 , 9 , 10]
print("Only whole numbers:")
print_num(data, whole=True)

print("Only decimal numbers:")
print_num(data, whole=False)

# -----------------------------------------------------------
# Sukurkite funkciją word_count kuri priimtų textą ir
# gražintų kiek jame yra žodžių.

def word_count(text):
    words = text.split()
    return len(words)

# ---------------------------------------------------
# Sukurkite funkciją kuri priima du parametrus. Skaičių masyvą ir boolean.
# Funkcija gražina prafiltruotą masyvą. Kai antras parametras True/tik
# poriniais skaičiais, False/tik neporiniais skaičiais.

def add_func(numbers, even =True):
    result=[]
    for item in numbers:
        if even and item % 2 == 0:
            result.append(item)
        elif not even and item % 2 != 0:
            result.append(item)
    return result
data = [5, 6, 7, 8, 9, 4]
print(add_func(data,True))
print(add_func(data, False))
#
# -------------------------------------------------
# Sukurkite funkciją number_is_prime. Funkcija priima skaičių,
# gražina True/False ar skaičius pirminis.
# number_is_prime-is a natural number greater than 1 that has no
# divisors other than 1 and itself. In other words, it cannot be
# divided evenly by any other number.
# checks if number is higher than 1,for i in range(2, num):
# Tai reiškia: "Eik per visus skaičius nuo 2 iki num-1
# if num % i == 0:
# Čia tikriname, ar num dalijasi iš i be liekanos.

def numb_prime(number):
        if number < 2:
            return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
print(numb_prime(5))
print(numb_prime(4))

