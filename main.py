import pandas as pd
import openai
import argparse
import matplotlib.pyplot as plt
from better_profanity import profanity
import os


openai.api_key = os.getenv("OPENAI_API_KEY")


def load_comments(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file type. Use .csv or .json")


def analyze_comment(text):
    prompt = f"""Analyze the following user comment:
\"{text}\"
Is it offensive? If yes, classify it as one of: hate speech, toxicity, profanity, harassment. Provide a short explanation."""

    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        reply = res['choices'][0]['message']['content'].lower()

        if "not offensive" in reply:
            return False, "", reply
        for cat in ["hate speech", "toxicity", "profanity", "harassment"]:
            if cat in reply:
                return True, cat, reply
        return True, "unknown", reply
    except Exception as e:
        return False, "", f"Error: {str(e)}"


def generate_report(df, output_path="flagged_comments.csv"):
    df.to_csv(output_path, index=False)
    print(f"\n🔍 Offensive Comments Summary:")
    offensive = df[df['is_offensive']]
    print("Total offensive comments:", len(offensive))
    print("\nOffense type breakdown:\n", offensive['offense_type'].value_counts())
    print("\nTop 5 Most Offensive Comments:\n", offensive[['comment_text', 'explanation']].head(5))


    offensive['offense_type'].value_counts().plot(kind='bar', title="Offense Type Distribution")
    plt.tight_layout()
    plt.savefig("offense_distribution.png")
    print("📊 Bar chart saved as offense_distribution.png")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help="Input file path (.csv or .json)")
    args = parser.parse_args()

    df = load_comments(args.input)
    print(f"✅ Loaded {len(df)} comments")

    profanity.load_censor_words()
    is_offensive_list = []
    offense_type_list = []
    explanation_list = []

    for comment in df['comment_text']:
        if profanity.contains_profanity(comment):
            is_offensive, offense_type, explanation = True, "profanity", "Detected using profanity filter"
        else:
            is_offensive, offense_type, explanation = analyze_comment(comment)
        is_offensive_list.append(is_offensive)
        offense_type_list.append(offense_type)
        explanation_list.append(explanation)

    df['is_offensive'] = is_offensive_list
    df['offense_type'] = offense_type_list
    df['explanation'] = explanation_list

    generate_report(df)

if __name__ == "__main__":
    main()
