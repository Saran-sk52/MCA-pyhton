def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

def replace_vowels(input_string):
    vowels = "aeiouAEIOU"
    result_string = ""
    for char in input_string:
        if char in vowels:
            result_string += "#"
        else:
            result_string += char
    return result_string

input_string =input ("Enter a string: ")
vowel_count = count_vowels(input_string)
replaced_string = replace_vowels(input_string)

print(f"Original String: {input_string}")
print(f"Number of Vowels: {vowel_count}")
print(f"String after Replacing Vowels: {replaced_string}")
