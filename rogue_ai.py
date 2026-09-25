# ============================================================
# CMP 131 - ROGUE AI EMERGENCY DIAGNOSTIC SYSTEM
# Team members:
# ============================================================

print("========================================")
print("     ROGUE AI DIAGNOSTIC SYSTEM")
print("========================================")

# LEVEL 1 - TEMPERATURE DIAGNOSTIC
# Ask for the system temperature and make the required decision.
x=int(input("Enter AI System Temperature: " ))
if x>=100:
    print("WARNING: SYSTEM OVERHEATING")
else:
    print("SYSTEM TEMPERATURE: NORMAL")

# LEVEL 2 - POWER DIAGNOSTIC
# Ask for the battery percentage and make the required decision.
a=int(input("Enter System Battery Power Level: "))
if a<=20:   
    print("WARNING: LOW POWER LEVEL")
elif a>=9000:
    print('Nappa, "Whats the scouter say Vegita?"')
    print('Vegita,"ITS OVER 9,000!!!!"')
else:
    print("POWER NORMAL")


# LEVEL 3 - SECURITY DIAGNOSTIC
# Ask for the security status and make the required decision.
y=str(input("Enter the Security Status: "))
if y==("Danger") or y==("danger") or y==("DANGER"):
    print("SHUTDOWN REQUIRED")
else:   
    print("SYSTEM SECURE")


print("========================================")
print("Diagnostic complete.")
print("========================================")
