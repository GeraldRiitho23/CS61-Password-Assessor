import string

def evaluate_password(password):
    score = 0
    strength = ""
    details = []

    if len(password) >= 8:
        score += 1
    else:
        details.append("Must be at least 8 characters")
        
    if any(char.isdigit() for char in password):
        score += 1
    else:
        details.append("Must include at least one number")
        
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        details.append("Must include at least one symbol")

    compromised_passwords = ["password", "qwerty", "password123"]

    if password.lower() in compromised_passwords:
        return "Compromised", 0, ["This password is known to be compromised."]
    
    if score <= 1:
        strength = "Weak"
    elif score == 2:
        strength = "Medium"
    elif score == 3:
        strength = "Strong"

    return strength, score, details
