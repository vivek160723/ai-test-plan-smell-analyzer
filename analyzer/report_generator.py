def generate_report(smells):
    print("\n🧪 Test Plan Smell Analysis Report\n")
    if not smells:
        print("✔ No smells detected. Test plan looks good.")
    else:
        for smell in smells:
            print(f"⚠ {smell}")
