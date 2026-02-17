# 🤖 AI Test Plan Smell Analyzer

An AI-powered QA tool that analyzes manual test plans before client submission.  
It detects unclear steps, duplicate test cases, missing edge cases, and provides intelligent suggestions using a local AI model.

---

## 🚀 Features

✅ Supports Word (.docx), Excel (.xlsx), and PDF test plans  
✅ Detects ambiguous or unclear test steps  
✅ Identifies duplicate test cases  
✅ Highlights short or weak test steps  
✅ AI-powered improvement suggestions (local AI – Ollama Llama model)  
✅ Helps QA teams improve documentation quality before client delivery  

---

## 🧠 Why This Tool?

Manual test plans often contain:

- Unclear test steps  
- Duplicate scenarios  
- Missing validations  
- Poor documentation quality  

This tool helps QA teams:

✔ Improve test quality  
✔ Reduce missed bugs  
✔ Deliver better documentation to clients  
✔ Save review time  

---

## ⚙️ Installation Steps

### 1️⃣ Clone the repository

```bash
git clone https://github.com/vivek160723/ai-test-plan-smell-analyzer.git
cd ai-test-plan-smell-analyzer
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Install Local AI Model (Important)
Install Ollama first:
👉 https://ollama.com/download

Then run:

ollama pull llama3.2
5️⃣ Run the project
python main.py
📂 Supported Test Plan Formats
Word Documents (.docx)
Excel Test Cases (.xlsx)
PDF Test Plans (.pdf)
Place your test plan inside:
sample_docs/
Then update the file path in main.py.
🧪 Example Output
Duplicate test steps detected
Ambiguous wording flagged
AI suggestions for better test coverage
🔐 Data Privacy
This tool uses local AI models, ensuring:
✔ No client data exposure
✔ Secure QA analysis
✔ Offline capability

👨‍💻 Tech Stack
Python
Pandas
PyPDF2
Python-docx
Ollama (Local AI Model)
📈 Future Enhancements
Web UI dashboard
Automated test case improvement suggestions
Jira/TestRail integration
Advanced QA analytics
🙌 Contribution
Feel free to fork, improve, and contribute.
⭐ Author
Developed as an AI QA innovation project to enhance manual testing documentation quality.
