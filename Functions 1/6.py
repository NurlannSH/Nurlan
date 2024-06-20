def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Example usage:
sentence = "We are ready"
print(reverse_words('We are ready'))