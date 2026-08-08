weather = (1, 0, 0, 0, 1, 1, 0)
print(weather)

rainy = weather.count(1)
sunny = weather.count(0)

if rainy > sunny:
    print("Rainy weather is predicted")
else:
    print("sunny weather is predicted")