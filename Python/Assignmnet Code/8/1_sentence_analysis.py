def analyze_sentence(text):
    vowels = consonants = digits = special = 0
    for ch in text:
        if ch.isalpha():
            if ch.lower() in "aeiou": vowels += 1
            else: consonants += 1
        elif ch.isdigit(): digits += 1
        elif not ch.isspace(): special += 1
    words = text.split()
    longest = max(words, key=len) if words else ""
    long_words = [word for word in words if len(word) > 5]
    clean = "".join(text.lower().split())
    return vowels, consonants, digits, special, longest, long_words, clean == clean[::-1]

def main():
    default = "Madam 123! programming"
    text = input(f"Enter a sentence: ").strip()
    v, c, d, s, longest, long_words, palindrome = analyze_sentence(text)
    print("Vowels:", v, "Consonants:", c)
    print("Digits:", d, "Special characters:", s)
    print("Longest word:", longest)
    print("Words longer than 5:", long_words)
    print("Palindrome:", palindrome)

main()
