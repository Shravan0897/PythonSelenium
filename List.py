Values = [1, 3, "Shravan", 6, 8.999]
print(Values[1]) # 3
print(Values[3]) # 6
print(Values[-1]) # 8.999
Values.insert(3,"Tomar")
print(Values) # [1, 3, 'Shravan', 'Tomar', 6, 8.999]
print(Values[2:4]) # ['Shravan', 'Tomar']
Values.append("Selenium")
print(Values[-1]) # Selenium
print(Values) # [1, 3, 'Shravan', 'Tomar', 6, 8.999, 'Selenium']
Values[2] = "SHRAVAN"
print(Values) # [1, 3, 'SHRAVAN', 'Tomar', 6, 8.999, 'Selenium']
del Values[0]
print(Values) # [3, 'SHRAVAN', 'Tomar', 6, 8.999, 'Selenium']