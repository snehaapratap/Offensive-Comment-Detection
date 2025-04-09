# 🛡️ Offensive Comment Detection using Generative AI

It is a **Python-based CLI tool** that analyzes user-generated comments to detect and classify offensive content, generate summary reports, and visualize insights with charts.

---

## 🚀 Features

- 🔍 Detects offensive/inappropriate comments
- 📦 Classifies comments into:
  - Hate Speech
  - Profanity
  - Toxicity
  - Insults
- 📊 Generates summary reports
- 📈 Creates bar and pie charts for offense distribution
- 🧠 Uses `better-profanity` for pre-filtering
- 🧪 Simple CLI interface

---

## 📁 File Structure

```
├── comments.csv               
├── flagged_comments.csv             
├── offense_distribution.png              
├── main.py                    
├── report.png
├── requirements.txt          
├── README.md                  
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/snehaapratap/offensive-comment-detection.git
cd offensive-comment-detection
```

### 2. Install Requirements

Make sure you're using Python 3.9+ and run:

```bash
pip install -r requirements.txt
```

---

## 📥 Input Format

The script expects a `.csv` file with the following columns:

```csv
comment_id,username,comment_text
1,alice,"You are such an idiot!"
2,bob,"Great job on your work!"
...
```

> ⚠️ NOTE: Make sure comments with commas are **wrapped in double quotes**. A flawed `comments.csv` is included to demonstrate error handling.

---

## 🧠 How It Works

The script classifies comments into offense types based on keywords and profanity:

| Offense Type | Example Phrase                          | Severity |
|--------------|------------------------------------------|----------|
| Profanity    | "f***", "s**t", "clown"                  | 3        |
| Insult       | "idiot", "dumb", "loser"                 | 4        |
| Toxicity     | "trash", "garbage", "you suck"           | 5        |
| Hate Speech  | "shut up", "worthless", "get lost"       | 6        |
| Clean        | —                                        | 0        |

---

## ▶️ Usage

Run the script using:

```bash
python main.py --input comments.csv
```

### 📌 Output:

- 📜 Prints:
  - Number of offensive comments
  - Offense type breakdown
  - Top 5 most severe offensive comments

- 📂 Generates:
  - `offense_distribution.png`
  - a report (stored as `report.png`)

---

## 🖼️ Output

### Offense Distribution
![offense_distribution](https://github.com/user-attachments/assets/af4a9671-dec8-4c7c-9492-948d6d0eddcd)


### Report
<img width="739" alt="report" src="https://github.com/user-attachments/assets/74a8d49c-8394-424f-b062-ad862e55d4a2" />

---

## ✅ Bonus Features

- ✅ Simple CLI with `argparse`
- ✅ Chart generation with `matplotlib`
- ✅ Profanity pre-filtering with `better-profanity`
- 🚧 Error handling for flawed CSV input

---
## 📬 Contact

📧 For any queries or collaboration, reach out at [sneha.prem918@gmail.com](mailto:sneha.prem918@gmail.com)
