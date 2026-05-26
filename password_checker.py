import re
from datetime import datetime
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

# Load common passwords
with open("common_passwords.txt", "r") as file:
    common_passwords = file.read().splitlines()

# User input
password = input("Enter Your Password: ")

score = 0
recommendations = []

print("\n========== PASSWORD ANALYSIS ==========\n")

# Length Check
if len(password) >= 8:
    print(Fore.GREEN + "[+] Length Check Passed")
    score += 1
else:
    print(Fore.RED + "[-] Password should be at least 8 characters")
    recommendations.append("Use at least 8 characters")

# Uppercase Check
if re.search(r"[A-Z]", password):
    print(Fore.GREEN + "[+] Uppercase Check Passed")
    score += 1
else:
    print(Fore.RED + "[-] Add uppercase letters")
    recommendations.append("Add uppercase letters")

# Lowercase Check
if re.search(r"[a-z]", password):
    print(Fore.GREEN + "[+] Lowercase Check Passed")
    score += 1
else:
    print(Fore.RED + "[-] Add lowercase letters")
    recommendations.append("Add lowercase letters")

# Number Check
if re.search(r"[0-9]", password):
    print(Fore.GREEN + "[+] Number Check Passed")
    score += 1
else:
    print(Fore.RED + "[-] Add numbers")
    recommendations.append("Include numbers")

# Special Character Check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print(Fore.GREEN + "[+] Special Character Check Passed")
    score += 1
else:
    print(Fore.RED + "[-] Add special characters")
    recommendations.append("Add special characters")

# Common Password Check
if password.lower() in common_passwords:
    print(Fore.RED + "[-] Common password detected!")
    recommendations.append("Avoid common passwords")
else:
    print(Fore.GREEN + "[+] Not a common password")

# Repeated Characters Check
if re.search(r"(.)\1\1", password):
    print(Fore.RED + "[-] Repeated characters detected")
    recommendations.append("Avoid repeated characters")

# Sequential Pattern Check
sequences = ["1234", "abcd", "qwerty"]

for seq in sequences:
    if seq in password.lower():
        print(Fore.RED + "[-] Sequential pattern detected")
        recommendations.append("Avoid sequential patterns")
        break

# Password Score
print(f"\nPassword Score: {score}/5")

# Determine Strength
if score == 5:
    strength = "Strong Password"
    print(Fore.GREEN + "[+] Strong Password")

elif score >= 3:
    strength = "Medium Password"
    print(Fore.YELLOW + "[*] Medium Password")

else:
    strength = "Weak Password"
    print(Fore.RED + "[-] Weak Password")

# Recommendations
print("\n========== RECOMMENDATIONS ==========\n")

if recommendations:
    for rec in recommendations:
        print(f"[*] {rec}")
else:
    print(Fore.GREEN + "[+] No recommendations needed")

# Save Report
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

filename = f"reports/password_report_{timestamp}.txt"

with open(filename, "w") as report:

    report.write("===== PASSWORD STRENGTH REPORT =====\n\n")

    report.write(f"Date & Time : {timestamp}\n")
    report.write(f"Entered Password : {password}\n\n")

    report.write("========== RESULT ==========\n")
    report.write(f"Password Score : {score}/5\n")
    report.write(f"Strength Level : {strength}\n\n")

    report.write("========== RECOMMENDATIONS ==========\n")

    if recommendations:
        for rec in recommendations:
            report.write(f"[*] {rec}\n")
    else:
        report.write("[+] No recommendations needed\n")

print(Fore.CYAN + f"\nReport saved successfully: {filename}")
