# from uparser import UnifiedParser
# from globals import GLOBALS
# import json

# def run_and_save(lang):
#     parser = UnifiedParser(lang)
#     input_file = f"words/{lang}.txt"
#     output_file = f"{lang}_parsed.json"

#     parsed_data = parser.parse_words_from_file(input_file)
    
#     with open(output_file, 'w', encoding='utf-8') as outfile:
#         json.dump(parsed_data, outfile, ensure_ascii=False, indent=4)

#     print(f"Parsed phonemes saved in {output_file}")

# if __name__ == "__main__":
#     for lang in [GLOBALS.ARABIC, GLOBALS.PERSIAN, GLOBALS.URDU]:
#         run_and_save(lang)
from uparser import UnifiedParser
from globals import GLOBALS
import json

def run_and_save(lang_code, lang_name):
    parser = UnifiedParser(lang_code)
    input_file = f"words/{lang_name}.txt"
    output_file = f"{lang_name}_parsed.json"

    # Read words explicitly to debug tokenization issues
    with open(input_file, 'r', encoding='utf-8') as infile:
        words = infile.read().splitlines()

    parsed_data = {}
    for word in words:
        phonemes = parser.parse_word(word)
        parsed_data[word] = phonemes

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(parsed_data, outfile, ensure_ascii=False, indent=4)

    print(f"Parsed phonemes saved in {output_file}")

if __name__ == "__main__":
    # Ensure you use correct language codes as defined in your globals.py
    language_details = [
        (GLOBALS.ARABIC, 'arabic'),
        (GLOBALS.PERSIAN, 'persian'),
        (GLOBALS.URDU, 'urdu')
    ]
    for lang_code, lang_name in language_details:
        run_and_save(lang_code, lang_name)
