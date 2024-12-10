from googlesearch import search
import time
import random

# Define the query template
query = "examtopics.com exam-sc-100-topic-{}-question-{}-discussion"

# Enter the topic number manually
topic = int(input("Enter the topic number: "))
question_start=int(input("Enter the start question number:  "))
max_questions = int(input("Enter the maximum number of questions: "))

# Open a file to write results
with open(f"sc-100-questions-topic-{topic}.txt", "w") as file:
    topic_has_results = False  # Flag to track if the topic has any results
    j=0
    for question in range(question_start, max_questions + 1):  # Loop through the specified number of questions
        try:
            # Perform Google search for the current topic and question
            formatted_query = query.format(topic, question)
            top_results = list(search(formatted_query, num_results=10))

            # Check if any result matches the expected format
            expected_format = f"exam-sc-100-topic-{topic}-question-{question}-discussion"
            top_selected_result = None
            for result in top_results:
                if expected_format in result:
                    top_selected_result = result
                    break

            if top_selected_result:
                # If a matching result is found, write it to the file
                print(f"Topic {topic}, Question {question}: {top_selected_result}")
                file.write(top_selected_result + '\n')
                topic_has_results = True  # Indicate that this topic has results
            else:
                print(f"Topic {topic}, Question {question}: No result")

            # Wait a random amount of time to avoid detection
            time.sleep(random.uniform(15, 30))
        except Exception as e:
            j+=1
            print(f"Error occurred for Topic {topic}, Question {question}: {e}")
            time.sleep(500*j)
            continue

    if not topic_has_results:
        print(f"No results for Topic {topic}.")
    else:
        print(f"Search completed for Topic {topic}.")