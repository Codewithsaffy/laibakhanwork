import random
import string
def generate_password(length, use_char, use_upprecase, use_number):
  characters = string.ascii_lowercase  #starts with lower case letters
  if use_upprecase:
    characters += string.ascii_uppercase
  if use_number:
    characters += string.digits
  if use_char:
    characters += string.punctuation

  password= ''.join(random.choice(characters) for _ in range(length))
  return password
def main():
  print("==== Random Password Generator ====")

  length = int(input("Enter the length of the password: "))
  use_char = input("Do you want to use special characters? (yes/no): ").lower() == "yes"
  use_upprecase = input("Do you want to use uppercase letters? (yes/no): ").lower() == "yes"
  use_number = input("Do you want to use numbers? (yes/no): ").lower() == "yes"

  password = generate_password(length, use_char, use_upprecase, use_number)

  print("\ngenerated password is:")
  print(password)
if __name__ == "__main__":
  main()  


  