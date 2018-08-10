# DataScience

import matplotlib.pyplot as plt
import billionaires
list_of_billionaire = billionaires.get_billionaires()

gender = []
age = []
wealth = []


male = []
female = []

maleTotal = 0
femaleTotal = 0

maleAge = []
femaleAge = []

maleWealth = []
femaleWealth = []


# for i in list_of_billionaire:
#    gender = i["demographics"]["gender"]
#    print("Gender of billionaire " + gender)
#    wealth = i["wealth"]["worth in billions"]
#    print("Wealth of billionaire " + str(wealth))
#    age = i["demographics"]["age"]
#    print("Age of billionaire " + str(age))


#print(list_of_billionaire[1]["demographics"]["gender"])
#for i in list_of_billionaire:
#    male = i["demograph"]

#female = []

if gender == "male":
    maleTotal += 1
    if age == i["demographics"]["age"]:
        maleAge.append(age)
    if wealth == i["wealth"]["worth in billions"]:
        maleWealth.append(wealth)

if gender == "female":
    femaleTotal += 1
    if age == i["demographics"]["age"]:
        femaleAge.append(age)
    if wealth == i["wealth"]["worth in billions"]:
        femaleWealth.append(wealth)





plt.plot(maleAge, maleWealth, color='red')
plt.plot(femaleAge, maleWealth, color='blue')
plt.xlabel('Age of Billionaire')
plt.ylabel('Wealth of Billionaire')
plt.title("Age vs. Wealth of Male and Female Billionaires")
plt.show()
