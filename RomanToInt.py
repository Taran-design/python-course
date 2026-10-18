def romanToInt(roman):
    values = {'I':1,'V':5,'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0

    roman = roman.upper()
    for i in range(len(roman)):
        if roman[i] not in values:
            return None
        current_value = values[roman[i]]
        if i + 1 < len(roman):
            next_value = values.get(roman[i + 1],0)
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            total += current_value
    return total
roman_input = input("Enter a roman numeral: ").strip()
result = romanToInt(roman_input)
if result is None or roman_input == "":
    print("Invalid roman numeral input")
else:
    print("Integer value:", result)