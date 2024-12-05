import random

def rock_paper_scissors():
  print("Welcome to Rock, Paper, Scissors Game")
  print("==== Rock, Paper, Scissors Game ====")
  while True:
    try:
      user_choice = input("\n chose Rock, Paper, Scissors (or quit) :").lower()
      if user_choice == "quit":
        print("Thanks for playing! Goodbye!")
        break
      elif user_choice not in ["rock", "paper", "scissors"]:
        print("Please a valid choice")
        continue
      computer_choice = random.choice(["rock", "paper", "scissors"])
      print(f"computer chose {computer_choice}")

      if user_choice == computer_choice:
        print("It's a tie!")
      elif user_choice == "rock" and computer_choice == "scissors":  
        print("You win!")
      elif user_choice == "paper" and computer_choice == "scissors": 
        print("You lose!")
      elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
      elif user_choice == "rock" and computer_choice == "paper":
        print("You lose!")  
      elif user_choice == "scissors" and computer_choice == "rock": 
        print("You lose!")
      elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
      else:
        print("Something went wrong")  

    except Exception as e:
      print(f"An error occurred: {e}")

if __name__ == "__main__" :
  rock_paper_scissors()


