AMBIGUOUS_WORDS = ["properly", "correctly", "etc", "normal flow"]
def analyze_smells(lines):
    smells = []
    seen = set()

    has_expected = False

    for idx, line in enumerate(lines, start=1):
        l = line.lower()

        if "expected" in l:
            has_expected = True

        # Duplicate detection
        if l in seen:
            smells.append(f"Duplicate step at line {idx}: {line}")
        seen.add(l)

        # Ambiguous wording
        ambiguous_words = ["properly", "correctly", "observe"]
        if any(word in l for word in ambiguous_words):
            smells.append(f"Ambiguous wording at line {idx}: {line}")

    if not has_expected:
        smells.append("Missing Expected Results section")

    return smells
