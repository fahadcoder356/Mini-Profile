print("\nWelcome to my MINIPROFILE")
print('*' * 30)
knowledge = input("Which year is running now? Please tell me. I think you would not mind. It is necessary for my short mini program. Tell me the four digit")
name = input("What is your name? ")
birth_year = input('what is your birth year?')
age = int(knowledge) -int(birth_year)
weight_lbs = input('Please tell me your weight')
weight_kgs = float(weight_lbs) * 0.45
years_to_70 = 70 - int(age) #it was just for fun
age_in_seventy = int(years_to_70) + int(knowledge)
cell_number = input(' Please tell me your cell number')
last_two_digit_of_cell_number = int(cell_number) % 100
print(f" This is your last two digit of your cell number, right? {last_two_digit_of_cell_number}")
name_title = name.title()
home_district = input('Where is your home town?')
print(f"Glad to hear that, you are from {home_district}")
popular_food_local_area = input("which is the most famous food in your home town?")
songs = input("Do you love to listen hindi songs? ")
print(f'I heard about this {popular_food_local_area}. but never tried it')
if songs.lower() == "yes":   # Fixed: added parentheses to call .lower()
    print("Oww, Me too")
else:
    print("Oh my bad")
print('\nHere is your form. You will able to see your little profile with answering all the question precisely')
print('-' * 15)
print('''\n
Our MINIPROFILE doesn not share your data with one another even we don't store it in our Server. 
So feel free to share your data. 
 ''')
print('-' * 30)
print("\nHi, " + name_title + " . I hope you will Enjoy")
print(f'your are now {age} years old')
print(f'You will be 70 years old by the year of {age_in_seventy}')
print('\nNow I will ask your present address. Tell me carefully')
house_number = input("House No.: ")
road_number = input("Road No.: ")
area = input("Name of the area you live in: ")
sub_district = input("Sub District: ")
district = input("District: ")
postal_code = int(input("Postal Code: "))
print(f"This is your full address: House-{house_number}, Road-{road_number}, {area}, {sub_district}, {district}-{postal_code}")





