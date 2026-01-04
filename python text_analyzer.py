import re
from collections import Counter

def analyze_text(file_path):
    """
    Analyzes a text file to count sentences, words, and frequent vocabulary.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            
        # --- 1. Calculate Sentence Count ---
        # We split by common sentence terminators: . ! ?
        # We filter out empty strings to avoid counting trailing whitespace as sentences.
        sentences = re.split(r'[.!?]+', text)
        sentence_count = len([s for s in sentences if s.strip()])

        # --- 2. Process Words (Case-insensitive & Ignore Punctuation) ---
        # re.findall(r'\b\w+\b', ...) finds all alphanumeric words ignoring punctuation.
        # .lower() ensures "AI" and "ai" are treated as the same word.
        words = re.findall(r'\b\w+\b', text.lower())

        # --- 3. Calculate Total Word Count ---
        word_count = len(words)

        # --- 4. Identify Top 10 Most Frequent Words ---
        # Counter creates a dictionary-like object mapping words to their frequency.
        word_counts = Counter(words)
        top_10_words = word_counts.most_common(10)

        # --- Display Results ---
        print("-" * 30)
        print(f"Analysis for file: {file_path}")
        print("-" * 30)
        print(f"Total Sentences: {sentence_count}")
        print(f"Total Words:     {word_count}")
        print("\nTop 10 Most Frequent Words:")
        print(f"{'Word':<15} {'Count'}")
        print("-" * 25)
        
        for word, count in top_10_words:
            print(f"{word:<15} {count}")
            
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    analyze_text("C:\\Users\\DELL\\Downloads\\Text-Analyzer\\sample_text.txt")

