def count_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else: 
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["count"]

def sort_characters(char_counts):
    sorted_counts = []

    for char in char_counts:
        if char.isalpha():
            char_dict = {"char": char, "count": char_counts[char]}
            sorted_counts.append(char_dict)
    
    sorted_counts.sort(key=sort_on, reverse=True)
    return sorted_counts
