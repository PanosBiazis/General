from mpmath import mp

# Ρύθμισε τον αριθμό των ψηφίων
mp.dps = 1000

# Υπολόγισε το π
pi_value = str(mp.pi)

# Αποθήκευσε το αποτέλεσμα σε αρχείο
with open("pi_digits.txt", "w") as file:
    file.write(pi_value)
