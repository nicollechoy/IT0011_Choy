def count_characters(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    spaces = 0
    other_chars = 0
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char == " ":
            spaces += 1
        else:
            other_chars += 1
    
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Spaces: {spaces}")
    print(f"Other Characters: {other_chars}")

input_str = input("Enter a string: ")
count_characters(input_str)