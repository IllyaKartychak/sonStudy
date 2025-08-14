def multiply_numbers(a: int, b: int) -> int:
    add_numbers_result = a + b
    return add_numbers_result


def greet_person(name: str = "Гість") -> str:
    return f"Привіт, {name}!"


def get_max_number(numbers: list[int]) -> int:
    return max(numbers)


print(get_max_number(numbers=[12, 25]))


def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


print(is_even(number=21))


def reverse_string(text: str) -> str:
    return text


reversed_string = reverse_string(text="somethings")[::-1]
print(reverse_string(text=reversed_string))


def calculate_average(numbers: list[float]) -> float:
    return numbers


print(calculate_average(numbers=[(2 + 2 + 2) / 3]))


def is_palindrome(text: str) -> bool:
    if text == text[::-1]:
        return True
    else:
        return False


print(is_palindrome(text="оно"))


def add_person_to_list(people: list[str], person: str) -> list[str]:
    people_list = people + [person]
    return people_list


print(add_person_to_list(people=["Max", "John"], person="Tolik").append("Vasiliy"))


def count_vowels(text: str) -> int:
    ukrainian_vowels = {"а", "е", "и", "і", "о", "у", "ю", "я", "є", "ї"}
    english_vowels = {"a", "e", "i", "o", "u"}
    ukrainian_count = 0
    english_count = 0
    text_lower = text.lower()

    for letter in text_lower:
        if letter in ukrainian_vowels:
            ukrainian_count += 1
        if letter in english_vowels:
            english_count += 1
    return ukrainian_count, english_count


some_text = "jghikhgjgchmnhnkguyikhryfgjhjikfyikdngkhbjolguрароаншевншолпрлбдшзщве7сшоегкансзднесгуенгревшангщн"
vowels = count_vowels(some_text)
print(vowels)

# °C = (°F - 32) / 1.8


def fahrenheit_to_celsius(f: float) -> float:
    C = (f - 32) / 1.8
    return C


print(fahrenheit_to_celsius(f=40))
