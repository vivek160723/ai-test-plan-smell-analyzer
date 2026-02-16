AMBIGUOUS_WORDS = ["properly", "correctly", "etc", "normal flow"]

def analyze_smells(lines):
    smells = []
    seen = set()

    for idx, line in enumerate(lines, start=1):
        l = line.lower()

        if l in seen:
            smells.append(f"Duplicate test step at line {idx}: {line}")
        seen.add(l)

        if any(word in l for word in AMBIGUOUS_WORDS):
            smells.append(f"Ambiguous wording at line {idx}: {line}")

        if len(line) < 15:
            smells.append(f"Very short step at line {idx}: {line}")

    return smells
