secret_code = 42
attempts = 0

while attempts < 3:
    guess = int(input("Enter the secret code: "))
    attempts += 1
    
    if guess == secret_code:
        print("Code cracked!")
        break
    else:
        print(f"Wrong! {3 - attempts} attempts remaining.")
else:
    print("Out of attempts. Access denied!") 
