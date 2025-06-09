
from collections import deque

class Stack:
    def __init__(self):
        # Using deque to store topics studied day-wise
        self.topic_by_day = deque()

    def mark_today_challenge_complete(self, topic):
        # Add today's topic to the stack
        self.topic_by_day.append(topic)

    def remove_and_revise_last(self):
        # Remove the most recent topic (for revision)
        return self.topic_by_day.pop()

    def get_yesterday_study_topic(self):
        # Peek the last topic studied without removing
        return self.topic_by_day[-1]
    
    def has_study_started(self):
        # Check if any topics have been covered yet
        return len(self.topic_by_day) != 0
    
    def study_streak_count(self):
        # Get the total number of days you've studied (streak)
        return len(self.topic_by_day)
    
    def show_topics_covered(self):
        # Display all covered topics
        for topics in list(self.topic_by_day):
            print(topics)
    

# Create an instance of the learner stack
learner_virat = Stack()

# ✅ Pre-filled: Add previously covered topics (Day 1 to Day 12)
learner_virat.topic_by_day.append({"Day_01": "Introduction to Python"})
learner_virat.topic_by_day.append({"Day_02": "Variables and Data Types"})
learner_virat.topic_by_day.append({"Day_03": "Lists, Tuples, and Dictionaries"})
learner_virat.topic_by_day.append({"Day_04": "Control Structures"})
learner_virat.topic_by_day.append({"Day_05": "Functions"})
learner_virat.topic_by_day.append({"Day_06": "Modules and Packages"})
learner_virat.topic_by_day.append({"Day_07": "File Handling"})
learner_virat.topic_by_day.append({"Day_08": "Object-Oriented Programming (Part 1)"})
learner_virat.topic_by_day.append({"Day_09": "Object-Oriented Programming (Part 2)"})
learner_virat.topic_by_day.append({"Day_10": "Exception Handling"})
learner_virat.topic_by_day.append({"Day_11": "Working with Dates and Times"})
learner_virat.topic_by_day.append({"Day_12": "Regular Expressions"})

# ✅ Check if study has started
if learner_virat.has_study_started():
    print(f"You have started the challenge and you are on a streak of {learner_virat.study_streak_count()} days")
else:
    print("Start the Challenge Now")

# ✅ Show all topics covered so far
print("\n📘 Already Covered Topics:")
learner_virat.show_topics_covered()

# ✅ Check the topic studied yesterday
print("\n📖 Last day you studied:")
print(learner_virat.get_yesterday_study_topic())

# ✅ Add today's topic (Day 13)
learner_virat.mark_today_challenge_complete({"Day_13": "Data Structures"})

# ✅ Suppose not confident, remove and revise again
print(f"\n❗Not confident in the topic. Let's remove and revise again: {learner_virat.remove_and_revise_last()}")

# ✅ Final check: Streak after revision
print(f'\n🔥 Great! You are on a streak of {learner_virat.study_streak_count()} days')

