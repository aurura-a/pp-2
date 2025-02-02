
import math


class TextHandler:
    def __init__(self):
        self.data = ""

    def retrieve_text(self):
        self.data = input()

    def display_text(self):
        print(self.data.upper())


class GeometricShape:
    def __init__(self):
        pass

    def compute_area(self):
        return 0


class Cube(GeometricShape):
    def __init__(self, edge):
        self.edge = edge

    def compute_area(self):
        return self.edge ** 2


class Box(GeometricShape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def compute_area(self):
        return self.length * self.breadth


class CoordinatePoint:
    def __init__(self, axis_x, axis_y):
        self.axis_x = axis_x
        self.axis_y = axis_y

    def reveal(self):
        print(f"Coordinate({self.axis_x}, {self.axis_y})")

    def relocate(self, new_x, new_y):
        self.axis_x = new_x
        self.axis_y = new_y
        print(f"Moved to position: ({self.axis_x}, {self.axis_y})")

    def compute_distance(self, another_point):
        return math.sqrt((another_point.axis_x - self.axis_x) ** 2 + (another_point.axis_y - self.axis_y) ** 2)


class BankAccount:
    def __init__(self, account_holder, account_balance):
        self.account_holder = account_holder
        self.account_balance = account_balance

    def add_funds(self, amount):
        if amount > 0:
            self.account_balance += amount

    def withdraw_funds(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount


def is_prime_check(num): return num > 1 and all(
    num % i != 0 for i in range(2, int(num ** 0.5) + 1))


num_list = [10, 23, 4, 11, 12, 17, 15, 18, 13, 5]

prime_filtered = list(filter(is_prime_check, num_list))

print("Prime numbers in the list:", prime_filtered)


def grams_to_ounces(weight):
    return 28.3495231 * weight


def fahrenheit_to_celsius(temp_f):
    return (5 / 9) * (temp_f - 32)


def farm_animals(head_count, leg_count):
    rabbits = (leg_count - 2 * head_count) // 2
    chickens = head_count - rabbits
    return chickens, rabbits


def prime_filter(numbers):
    return [num for num in numbers if is_prime_check(num)]


def word_permutations(word, perm=""):
    if not word:
        print(perm)
        return
    for i in range(len(word)):
        word_permutations(word[:i] + word[i+1:], perm + word[i])


def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])


def check_adjacent_threes(lst):
    return any(lst[i] == 3 and lst[i+1] == 3 for i in range(len(lst) - 1))


def detect_007(lst):
    return '007' in ''.join(map(str, lst))


def sphere_volume(r):
    return (4/3) * math.pi * (r ** 3)


def unique_elements(lst):
    return list(dict.fromkeys(lst))


def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]


def draw_histogram(lst):
    for val in lst:
        print('*' * val)


def number_guessing_game():
    name = input("Hello! What is your name? ")
    target = random.randint(1, 20)
    guesses = 0
    while True:
        guess = int(input("Take a guess: "))
        guesses += 1
        if guess < target:
            print("Your guess is too low.")
        elif guess > target:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {
                  guesses} tries!")
            break
