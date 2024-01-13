# print("Hello world")
# ################ 1 ####################
#
# string = input("Введіть рядок: ")
#
# letter_count = 0
# digit_count = 0
# for char in string:
#    if char.isalpha():
#        letter_count += 1
#    elif char.isdigit():
#        digit_count += 1
#
# print("Кількість букв:", letter_count)
# print("Кількість цифр:", digit_count)

############## 2 ################

# num1 = list(map(int,input("Введіть ряд чисел через пробіл: ").split()))
# num2 = int(input("Введіть число для пошуку: "))
#
# num3 = 0
# for i in num1:
#    if i==num2:
#        num3+=1
# print(f"Число {num2} зустрічається {num3} разів")

################# 3 ###################

string = input("Введіть рядок: ")
search_word = input("Введіть слово для пошуку: ")
replace_word = input("Введіть слово, щоб замінити його на: ")
words = string.split()
modified_words = []
for word in words:
   if word == search_word:
       modified_words.append(replace_word)
   else:
       modified_words.append(word)
modified_string = " ".join(modified_words)
print(modified_string)

################### 4 #################