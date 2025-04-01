import string
# List of A–Z

letters = list(string.ascii_uppercase)  # ['A', 'B', 'C', ..., 'Z']
# List of 0–9

digits = [str(i) for i in range(10)]   # ['0', '1', '2', ..., '9']
# Combine them into a single list

combined_list = letters + digits
print(combined_list)


for c in string.ascii_uppercase:
    print("\t","\'",ord(c)-55,"\'",":",c)