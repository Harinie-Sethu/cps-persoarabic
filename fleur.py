from datasets import load_dataset
import os

def extract_words_from_fleurs_arabic():
    # Load the Arabic split of FLEURS
    dataset = load_dataset("google/fleurs", "ar_eg", split='train+validation+test')

    # Collect words from transcriptions
    word_set = set()
    for example in dataset:
        transcription = example['transcription']
        words = transcription.strip().split()
        for word in words:
            # Optional: filter punctuation or normalize here if needed
            word_set.add(word)

    # Sort the words
    sorted_words = sorted(word_set)

    # Create directory if not exists
    os.makedirs("Words", exist_ok=True)

    # Save to file
    with open("Words/arabic.txt", "w", encoding="utf-8") as f:
        for word in sorted_words:
            f.write(f"{word}\n")

    print(f"Extracted {len(sorted_words)} unique words to Words/arabic.txt")

# Run the function
extract_words_from_fleurs_arabic()
