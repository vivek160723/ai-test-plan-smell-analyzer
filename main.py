from analyzer.doc_reader import read_doc
from analyzer.smell_rules import analyze_smells
from analyzer.report_generator import generate_report
from analyzer.ai_analyzer import ai_analysis
from analyzer.excel_reader import read_excel
from analyzer.pdf_reader import read_pdf

FILE_PATH = "sample_docs/sample_test_plan.docx"

lines = read_doc(FILE_PATH)
smells = analyze_smells(lines)
generate_report(smells)

print("\n🤖 AI Suggestions:\n")

text = "\n".join(lines)
ai_output = ai_analysis(text)

print(ai_output)

FILE_PATH = "sample_docs/sample_test_plan.xlsx"

if FILE_PATH.endswith(".docx"):
    from analyzer.doc_reader import read_doc
    lines = read_doc(FILE_PATH)

elif FILE_PATH.endswith(".xlsx"):
    lines = read_excel(FILE_PATH)

elif FILE_PATH.endswith(".pdf"):
    lines = read_pdf(FILE_PATH)

else:
    print("Unsupported file format")
    exit()
