import os
import json

def load_questions():
    base_dir = os.path.dirname(__file__)  # Get current file's directory (day_30/)
    file_path = os.path.join(base_dir, "questions.json")
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def evaluate_answer(user_answer, keywords):
    user_answer = user_answer.lower()
    match_count = sum(1 for keyword in keywords if keyword.lower() in user_answer)
    total_keywords = len(keywords)
    return match_count, total_keywords