from getpass import getpass

# Common passwords for basic security awareness checks
common_passwords = [
    "password",
    "12345678",
    "123456789",
    "qwerty",
    "admin",
    "welcome",
    "letmein"
]


# Function to check password character types
def check_character_types(password):
    results = {
        "length": len(password) >= 8,
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "number": any(char.isdigit() for char in password),
        "special": any(not char.isalnum() for char in password)
    }

    return results


# Program heading
print("=" * 50)
print("        🔐 PASSWORD SECURITY AUDITOR")
print("=" * 50)
print("Analyze your password security instantly")
print("-" * 50)


# Get password securely
password = getpass("Enter your password: ")

# Check password characteristics
results = check_character_types(password)


# ---------------- SECURITY ANALYSIS ----------------

print("\n--- Security Analysis ---")

if results["length"]:
    print("✓ Length: Good")
else:
    print("✗ Length: Too short")

if results["uppercase"]:
    print("✓ Uppercase letter: Found")
else:
    print("✗ Uppercase letter: Missing")

if results["lowercase"]:
    print("✓ Lowercase letter: Found")
else:
    print("✗ Lowercase letter: Missing")

if results["number"]:
    print("✓ Number: Found")
else:
    print("✗ Number: Missing")

if results["special"]:
    print("✓ Special character: Found")
else:
    print("✗ Special character: Missing")


# ---------------- SECURITY SCORE ----------------

score = 0

if results["length"]:
    score += 20

if results["uppercase"]:
    score += 20

if results["lowercase"]:
    score += 20

if results["number"]:
    score += 20

if results["special"]:
    score += 20


print("\n--- Security Score ---")
print("Score:", score, "/ 100")


# ---------------- SECURITY METER ----------------

filled = score // 10
empty = 10 - filled

meter = "█" * filled + "░" * empty

print("Security Meter:", meter)


# ---------------- RECOMMENDATIONS ----------------

print("\n--- Recommendations ---")

if not results["length"]:
    print("→ Use at least 8 characters.")

if not results["uppercase"]:
    print("→ Add at least one uppercase letter.")

if not results["lowercase"]:
    print("→ Add at least one lowercase letter.")

if not results["number"]:
    print("→ Add at least one number.")

if not results["special"]:
    print("→ Add at least one special character.")


# ---------------- COMMON PASSWORD CHECK ----------------

if password.lower() in common_passwords:
    print("\n⚠ Warning: This is a commonly used password.")
    print("→ Choose a more unique password.")
else:
    print("\n✓ No common-password match detected.")


# ---------------- REPEATED CHARACTER CHECK ----------------

repeated_character = False

for i in range(len(password) - 2):
    if password[i] == password[i + 1] == password[i + 2]:
        repeated_character = True
        break

if repeated_character:
    print("\n⚠ Warning: Repeated characters detected.")
    print("→ Avoid using the same character repeatedly.")
else:
    print("\n✓ No excessive repeated characters detected.")


# ---------------- SEQUENTIAL PATTERN CHECK ----------------

sequences = [
    "1234",
    "2345",
    "3456",
    "abcd",
    "bcde",
    "cdef",
    "qwer"
]

sequence_found = False

for sequence in sequences:
    if sequence in password.lower():
        sequence_found = True
        break

if sequence_found:
    print("\n⚠ Warning: Simple sequential pattern detected.")
    print("→ Avoid predictable sequences such as 1234 or abcd.")
else:
    print("\n✓ No simple sequential pattern detected.")


# ---------------- RISK DEDUCTION ----------------

risk_deduction = 0

if password.lower() in common_passwords:
    risk_deduction += 20

if repeated_character:
    risk_deduction += 10

if sequence_found:
    risk_deduction += 10


# ---------------- FINAL SCORE ----------------

final_score = max(0, score - risk_deduction)

print("\n--- Final Security Assessment ---")
print("Base Score:", score, "/ 100")
print("Risk Deduction:", risk_deduction)
print("Final Score:", final_score, "/ 100")


# ---------------- FINAL SECURITY MESSAGE ----------------

if final_score == 100:
    print("\n✓ Excellent! Your password meets all security requirements.")

elif final_score >= 80:
    print("\n✓ Good password, but there is still room for improvement.")

elif final_score >= 60:
    print("\n⚠ Your password is moderately secure. Consider improving it.")

else:
    print("\n⚠ Your password needs significant improvement.")


# ---------------- FINAL SECURITY LEVEL ----------------

if final_score <= 40:
    final_level = "WEAK"

elif final_score <= 70:
    final_level = "MODERATE"

else:
    final_level = "STRONG"


print("Final Security Level:", final_level)

print("\n" + "=" * 50)
print("          AUDIT COMPLETED")
print("=" * 50)