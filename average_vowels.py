def average_vowels(words):
    vowels = "aeiou"
    total_vowels = 0
    
    for word in words:
        for letter in word.lower():
            if letter in vowels:
                total_vowels += 1
    
    return total_vowels / len(words)


if __name__ == "__main__":
    sample = ["hello", "world", "python"]
    print(average_vowels(sample))
