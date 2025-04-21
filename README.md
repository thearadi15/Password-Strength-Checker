![image](https://github.com/user-attachments/assets/bef426e2-0c36-4926-9385-5e7c8d1a4032)# Password-Strength-Checker
# 🔒 ARHACX Stealth Analyzer v3.0




A sophisticated password security analysis tool with military-grade evaluation and toggleable visibility, designed for cybersecurity professionals and privacy-conscious users.

## 🚀 Features

- **Password Strength Evaluation**  
  - Length analysis (12+ characters recommended)
  - Character diversity check (uppercase, lowercase, numbers, special chars)
  - Common password detection

- **Secure Input Options**  
  - Toggle between visible text and bullet points
  - Automatic hiding after analysis
  - Shoulder-surfing protection

- **Detailed Security Report**  
  - Color-coded strength meter
  - Criteria breakdown with recommendations
  - Strength percentage score

- **Enterprise-Grade Security**  
  - No password storage or transmission
  - Local analysis only
  - Common password blacklist

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Tkinter (usually included with Python)

bash
# Clone the repository
git clone https://github.com/yourusername/arhacx-password-analyzer.git

# Navigate to project directory
cd arhacx-password-analyzer

# Install dependencies
pip install -r requirements.txt
🖥️ Usage
bash
python arhacx_analyzer.py


## 🖥️ How to Use

1. **Enter Password**  
   ```bash
   [Password Input Field]
Type your password (shows as ••••• by default)

Toggle Visibility


[Press 👁️] to show/hide password
Initiate Analysis

[Press ANALYZE] or hit [Enter]
View Results


===== SECURITY REPORT =====
• Length: 14 chars ✓
• Complexity: ★★★☆ (3/4)
• Status: STRONG (78%)
📊 How We Calculate Strength

┌──────────────────────┬─────────┐
│      Criteria        │ Weight  │
├──────────────────────┼─────────┤
│ Length ≥12 chars     │   25%   │
│ Uppercase letters    │   15%   │
│ Lowercase letters    │   15%   │
│ Numbers              │   20%   │
│ Special characters   │   25%   │
│ Common password      │  -30%   │
└──────────────────────┴─────────┘
🏆 Strength Ratings

┌─────────────┬─────────────┬───────────────┐
│   Strength  │ Score Range │    Visual     │
├─────────────┼─────────────┼───────────────┤
│  Critical   │   0-39%     │ 🔴 RED        │
│  Moderate   │  40-59%     │ 🟡 YELLOW     │
│  Strong     │  60-79%     │ 🟢 GREEN      │
│  Maximum    │  80-100%    │ 💎 BLUE       │
└─────────────┴─────────────┴───────────────┘
⚠️ Important Security Notes

▸ NEVER stores passwords
▸ 100% local analysis
▸ For optimal security:
  - Use offline
  - Toggle visibility only in private
  - Close after use
📜 License & Contribution

MIT Licensed | © 2025 ARHACX

Want to contribute?
1. Fork repo
2. Create branch
3. Submit PR
4. Discuss in Issues first for major changes
