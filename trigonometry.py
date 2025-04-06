import math

# Γωνία σε μοίρες
degrees = int(input("Δώσε τη γωνία σε μοίρες \n Μοίρα: "))

# Μετατροπή σε ακτίνια
radians = math.radians(degrees)

# Υπολογισμός ημίτονου και συνημίτονου
sin_value = math.sin(radians)
cos_value = math.cos(radians)


# print(f"Ημίτονο: {sin_value}")
print(f"Συνημίτονο της γωνίας {degrees} μοιρών: {cos_value}")
print(f"Ημίτονο της γωνίας {degrees} μοιρών: {sin_value}")

# Στρογγυλοποίηση του συνημιτόνου και του ημίτονου σε 5 δεκαδικά ψηφία
cos_value = round(cos_value, 5)
sin_value = round(sin_value, 5)


# print(f"Ημίτονο: {sin_value}")
print(f"Συνημίτονο της γωνίας {degrees} μοιρών: {cos_value}")
print(f"Ημίτονο της γωνίας {degrees} μοιρών: {sin_value}")
