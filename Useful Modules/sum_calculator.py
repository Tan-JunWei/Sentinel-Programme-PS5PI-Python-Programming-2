import sys

sum = 0
for i in range(1, len(sys.argv)):
    # accepts all numbers and floats, positive and negative
    if sys.argv[i].replace(".", "").replace("-", "").isnumeric():
        sum += float(sys.argv[i])
    else:
        print(f"WarningL '{sys.argv[i]}' is not a number and will be ignored.")

print(f"Total sum: {sum}")