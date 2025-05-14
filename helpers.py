# def load_common_map(filepath):
#     mappings = {}
#     with open(filepath, 'r', encoding='utf-8') as file:
#         for line in file:
#             if line.strip() and not line.startswith("#"):
#                 parts = line.strip().split()
#                 if len(parts) >= 4:
#                     cps, ar, fa, ur = parts[:4]
#                     mappings[cps] = {"arabic": ar, "persian": fa, "urdu": ur}
#     return mappings
def load_common_map(filepath):
    mappings = {}
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")  # Explicitly splitting by tabs for accuracy
            if len(parts) == 5:
                _, cps, arabic_char, persian_char, urdu_char = parts
                mappings[cps] = {
                    "arabic": arabic_char,
                    "persian": persian_char,
                    "urdu": urdu_char
                }
    return mappings
