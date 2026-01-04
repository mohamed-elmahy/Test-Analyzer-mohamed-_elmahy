# Python Text Analyzer

A efficient Python script that reads a text file and generates a statistical summary, including word count, sentence count, and a frequency analysis of the top vocabulary. This tool is designed to handle punctuation and case sensitivity automatically.

## Features

* **File Processing:** Reads text data securely from external files.
* **Sentence Counting:** Uses Regular Expressions to accurately split sentences based on punctuation (`.`, `!`, `?`).
* **Word Tokenization:** Extracts words while ignoring special characters and punctuation.
* **Case Insensitivity:** Treats "AI", "Ai", and "ai" as the same word for accurate counting.
* **Frequency Analysis:** Identifies and displays the top 10 most frequent words using `collections.Counter`.

## Technologies Used

* **Language:** Python 3.x
* **Libraries:**
    * `re` (Regular Expressions for pattern matching)
    * `collections` (For high-performance counting)

## Project Structure

```text
├── text_analyzer.py    # The main Python script
├── sample_text.txt     # Input text file
├── requirements.txt    # (Not needed/Empty as no external libs used)
└── README.md           # Project documentation
