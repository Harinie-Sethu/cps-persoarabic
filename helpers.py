def load_common_map(filepath):
    mappings = {}
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip() and not line.startswith("#"):
                parts = line.strip().split()
                if len(parts) >= 4:
                    cps, ar, fa, ur = parts[:4]
                    mappings[cps] = {"arabic": ar, "persian": fa, "urdu": ur}
    return mappings
