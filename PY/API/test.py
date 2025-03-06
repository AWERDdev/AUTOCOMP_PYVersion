import re
from spellchecker import SpellChecker

class WordCounter:
    def count_words(self, text):
        """Returns the total number of words in the given text."""
        words = re.findall(r'\b\w+\b', text)  # Extract words
        return len(words)

class TextCorrector:
    def __init__(self):
        self.spellchecker = SpellChecker()

    def check_word(self, word):
        """Returns True if the word is spelled correctly, False otherwise."""
        return word in self.spellchecker

    def fix_typos(self, word):
        """Returns the first suggested correct spelling or the original word if no suggestions exist."""
        if word in self.spellchecker:
            return word  # Word is already correct
        suggestions = self.spellchecker.candidates(word)
        return next(iter(suggestions), word)  # Return first suggestion or original word

# Example Usage:

# Initialize spell checker
spell_checker = TextCorrector()

# Test typo correction
print(spell_checker.fix_typos("welcme"))  # Output: "welcome" (or closest match)
print(spell_checker.fix_typos("hello"))   # Output: "hello" (unchanged)

# Initialize word counter
word_counter = WordCounter()
print(word_counter.count_words("Hello world! Hello ChatGPT."))  # Output: 4

















# # Path to the main API folder (where your script is running)
# api_folder = "H:/html/New folder/Auto_Complete_APP/PY/API"

# # Path to the dictionaries/en-AU folder
# en_au_path = os.path.join(api_folder, "dictionaries", "en-AU")

# # Check if the en-AU folder exists
# if os.path.exists(en_au_path):
#     # Define full paths to the index.aff and index.dic files
#     aff_file = os.path.join(en_au_path, "index.aff")
#     dic_file = os.path.join(en_au_path, "index.dic")

#     # Check if both files exist
#     if os.path.exists(aff_file) and os.path.exists(dic_file):
#         print("AFF File:", aff_file)
#         print("DIC File:", dic_file)
#     else:
#         print("Error: index.aff or index.dic not found in", en_au_path)
# else:
#     print("Error: en-AU folder not found in", en_au_path)

