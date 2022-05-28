value = float(input("숫자를 입력해 주십시오. "))

if value - int(value) == 0:
    value = int(value)

print(f"{value} lb = {0.453592 * value} kg")
print("{} lb = {} kg".format(value, 0.453592 * value))
print(f"{value} kg = {2.204623 * value} lb")