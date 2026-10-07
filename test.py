import string
import random
import re

def generate_password(length, include_uppercase, include_numbers, include_special):
  if length < (include_uppercase + include_numbers + include_special):
    raise ValueError("Password length is too short for the specified criteria.")

  password = ''

  if include_uppercase:
    password += random.choice(string.ascii_uppercase)
  if include_numbers:
    password += random.choice(string.digits)
  if include_special:
    password += random.choice(string.punctuation)

  characters = string.ascii_lowercase
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_numbers:
    characters += string.digits
  if include_special:
    characters += string.punctuation

  for _ in range(length - len(password)):
    password += random.choice(characters)

  password_list = list(password)
  random.shuffle(password_list)
  return ''.join(password_list)

def check_password_strength(password):
  strength = 0
  if len(password) >= 8:
    strength += 1
  if re.search('[a-z]', password):
    strength += 1
  if re.search('[A-Z]', password):
    strength += 1
  if re.search('[0-9]', password):
    strength += 1
  if re.search('[@#$%+=!]', password):
    strength += 1
  return strength

def get_strength_label(strength):
  labels = {
      5: "Very Strong",
      4: "Strong",
      3: "Medium",
      2: "Weak",
      1: "Very Weak"
  }
  return labels.get(strength, "Extremely Weak")

def main():
  try:
    count = int(input('How many passwords do you want to generate?: '))
    length = int(input('Enter password length: '))
    include_uppercase = input('Include uppercase letters?  (y/n): ').lower() == 'y'
    include_numbers = input('Include numbers?   (y/n): ').lower() == 'y'
    include_special = input('Include special characters?   (y/n): ').lower() == 'y'
    
    print('\nGenerated Passwords & Strength Analysis:')
    for i in range(count):
      password = generate_password(length, include_uppercase, include_numbers, include_special)
      strength_score = check_password_strength(password)
      strength_label = get_strength_label(strength_score)
      print(f'{i+1}. {password:<{length + 4}} | Strength: {strength_label} (Score: {strength_score}/5)')
  except ValueError as e:
    print(f'Error: {e}')

if __name__ == '__main__':
  main()