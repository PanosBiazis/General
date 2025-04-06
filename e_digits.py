from mpmath import mp

# Ρύθμισε τον αριθμό των ψηφίων
mp.dps = 100

# Υπολόγισε το e
e_value = str(mp.e)

# Αποθήκευσε το αποτέλεσμα σε αρχείο
with open("e_digits.txt", "w") as file:
    file.write(e_value)
