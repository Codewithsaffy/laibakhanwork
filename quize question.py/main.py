import time
def display_question(question ,options):
  print("\n" + question )
  for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
  while True:
    try:
      choice = int(input("Enter your choice (1/2/3/4) :"))
      if 1<= choice <= 4:
        return choice
      else:
        print("Invalid choice. Please enter a number between 1 and 4.")
    except ValueError:
      print("Invalid input. Please enter a number.")
def quize_question():
  quize_data=[
    {"question":"What is the national flower of Pakistan?",
    "options": ["Jasmine", "Rose"," Sunflower", "Tulip"],
    "answer":"1"
    },
    {"question":"What is the national language of Pakistan?",
    "options": ["Punjabi", "English","Sindhi", "Urdu"],
    "answer":"4"
    },
    {"question":"When did Pakistan become an independent country?",
    "options": ["15th August 1948", "14th August 1948","15th August 1947"," 14th August 1947"],
    "answer":"4" 
    },
    {"question":"Who is known as the founder of Pakistan?",
    "options": ["Allama Iqbal", "Liaquat Ali Khan","Muhammad Ali Jinnah", "Sir Syed Ahmed Khan"],
    "answer":"3"},
    {"question":"Which city is called the “City of Lights” in Pakistan?",
    "options": ["Lahore", "Islamabad","Karachi","Peshawar "],
    "answer":"3"},
    {"question":"What is the national animal of Pakistan?",
    "options": ["Markhor", "Snow Leopard","Lion", "Bengal Tiger"],
    "answer":"1"},
    {"question":"What is the capital city of Pakistan?",
    "options": ["Lahore", "Karachi","Islamabad", "Peshawar"],
    "answer":"3"}
  ]   
  print("Welcome to Pakistan Quize")
  print("Answer the following questions to test your knowledge about Pakistan.")
  score =0
  for question_data in quize_data:
    question = question_data["question"]
    options = question_data["options"]
    correct_answer = int(question_data["answer"])
    user_choice = display_question(question ,options)

    if user_choice == correct_answer:
      print("✅ Correct!")
      score += 1
    else:
      print(f"❌ Wrong! The correct answer is: {options[correct_answer - 1]}")
    time.sleep(1.5)

  print("\nQuiz Completed!")
  print(f"Your final score is: {score}/{len(quize_data)}")
  if score == len(quize_data):
        print("🎉 Perfect score! Well done!")
  elif score >= len(quize_data) // 2:
        print("👍 Good job!")
  else:
        print("💡 Keep practicing and try again!")  
if __name__ == "__main__":      
  quize_question()
  