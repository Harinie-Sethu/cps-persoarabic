def load_words(language):
    filepath = f"Words/{language}.txt"
    with open(filepath, 'r', encoding='utf-8') as file:
        words = [line.strip() for line in file if line.strip()]
    return words
