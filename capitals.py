from ast import In
from random import *
import time

capitals = [
    ("Afghanistan", "Kabul"),
    ("Armenia", "Yerevan"),
    ("Azerbaijan", "Baku"),
    ("Bahrain", "Manama"),
    ("Bangladesh", "Dhaka"),
    ("Bhutan", "Thimphu"),
    ("Brunei", "Bandar Seri Begawan"),
    ("Cambodia", "Phnom Penh"),
    ("China", "Beijing"),
    ("Cyprus", "Nicosia"),
    ("Georgia", "Tblisi"),
    ("India", "New Delhi"),
    ("Indonesia", "Jakarta"),
    ("Iran", "Tehran"),
    ("Iraq", "Baghdad"),
    ("Israel", "Jerusalem"),
    ("Japan", "Tokyo"),
    ("Jordan", "Amman"),
    ("Kazakhstan", "Astana"),
    ("North Korea", "Pyongyang"),
    ("South Korea", "Seoul"),
    ("Kuwait", "Kuwait City"),
    ("Kyrgyzstan", "Bishkek"),
    ("Laos", "Vientiane"),
    ("Lebanon", "Beirut"),
    ("Malaysia", "Kuala Lumpur"),
    ("Maldives", "Malé"),
    ("Mongolia", "Ulaanbaatar"),
    ("Myanmar", "Nay Pyi Taw"),
    ("Nepal", "Kathmandu"),
    ("Oman", "Muscat"),
    ("Pakistan", "Islamabad"),
    ("Palestine", "Jerusalem"),
    ("Philippines", "Manila"),
    ("Qatar", "Doha"),
    ("Russia", "Moscow"),
    ("Saudi Arabia", "Riyadh"),
    ("Singapore", "Singapore"),
    ("Sri Lanka", "Sri Jayawardendpura Kotte"),
    ("Syria", "Damascus"),
    ("Tajikistan", "Dushanbe"),
    ("Thailand", "Bangkok"),
    ("East Timor", "Dili"),
    ("Turkmenistan", "Ashgabat"),
    ("United Arab Emirates", "Abu Dhabi"),
    ("Uzbekistan", "Tashkent"),
    ("Vietnam", "Hanoi"),
    ("Yemen", "Sana’a"),
    ("Algeria", "Algiers"),
    ("Angola", "Luanda"),
    ("Benin", "Porto Novo"),
    ("Botswana", "Gaborone"),
    ("Burkina Faso", "Ouagadougou"),
    ("Burundi", "Bujumbura"),
    ("Cameroon", "Yaoundé"),
    ("Cape Verde", "Praia"),
    ("Central African Republic", "Bangui"),
    ("Chad", "N’Djamena"),
    ("Comoros", "Moroni"),
    ("Côte d’Ivoire", "Yamoussoukro"),
    ("Democratic Republic of Congo", "Kinshasa"),
    ("Djibouti", "Djibouti"),
    ("Egypt", "Cairo"),
    ("Equatorial Guinea", "Malabo"),
    ("Eritrea", "Asmara"),
    ("Ethiopia", "Addis Ababa"),
    ("Gabon", "Libreville"),
    ("Gambia", "Banjul"),
    ("Ghana", "Accra"),
    ("Guinea", "Conakry"),
    ("Guinea-Bissau", "Bissau"),
    ("Kenya", "Nairobi"),
    ("Lesotho", "Maseru"),
    ("Liberia", "Monrovia"),
    ("Libya", "Tripoli"),
    ("Madagascar", "Antananarivo"),
    ("Malawi", "Lilongwe"),
    ("Mali", "Bamako"),
    ("Mauritania", "Nouakchott"),
    ("Mauritius", "Port Louis "),
    ("Morocco", "Rabat"),
    ("Mozambique", "Maputo"),
    ("Namibia", "Windhoek"),
    ("Niger", "Niamey"),
    ("Nigeria", "Abuja"),
    ("Republic of Congo", "Brazzaville"),
    ("Rwanda", "Kigali"),
    ("Sāo Tomé and Principe", "Sāo Tomé"),
    ("Senegal", "Dakar"),
    ("Seychelles", "Victoria"),
    ("Sierra Leone ", "Freetown"),
    ("Somalia", "Mogadishu"),
    ("South Africa", "Cape Town"),
    ("South Sudan", "Juba"),
    ("Sudan", "Khartoum"),
    ("Swaziland", "Lobamba and Mbabane"),
    ("Tanzania", "Dodoma"),
    ("Togo", "Lomé"),
    ("Tunisia", "Tunis"),
    ("Uganda", "Kampala"),
    ("Zambia", "Lusaka"),
    ("Zimbabwe", "Harare"),
    ("Antigua and Barbuda", "St John’s"),
    ("Bahamas", "Nassau"),
    ("Barbados", "Bridgetown"),
    ("Belize", "Belmopan"),
    ("Canada", "Ottawa"),
    ("Costa Rica", "San José"),
    ("Cuba", "Havana"),
    ("Dominica", "Roseau"),
    ("Dominican Republic", "Santo Domingo"),
    ("El Salvador", "San Salvador"),
    ("Grenada", "St George’s"),
    ("Guatemala", "Guatemala City"),
    ("Haiti", "Port-au-prince"),
    ("Honduras", "Tegucigalpa"),
    ("Jamaica", "Kingston"),
    ("Mexico", "Mexico City"),
    ("Nicaragua", "Managua"),
    ("Panama", "Panama City"),
    ("Saint Kitts and Necis", "Basseterre"),
    ("Saint Lucia", "Castries"),
    ("Saint Vincent and the Grenadines", "Kingstown"),
    ("Trinidad and Tobago", "Port of Spain"),
    ("United States", "Washington, DC"),
    ("Argentina", "Buenos Aires"),
    ("Bolivia", "Sucre and La Paz"),
    ("Brazil", "Brasilia"),
    ("Chile", "Santiago"),
    ("Colombia", "Bogotá"),
    ("Ecuador", "Quito"),
    ("Guyana", "Georgetown"),
    ("Paraguay", "Asunción"),
    ("Peru", "Lima"),
    ("Suriname", "Paramaribo"),
    ("Trinidad and Tobago", "Port of Spain"),
    ("Uruguay", "Montevideo"),
    ("Venezuela", "Caracas"),
    ("Australia", "Canberra"),
    ("Fiji", "Suva"),
    ("Kiribati", "Tarawa and Bairiki"),
    ("Marshall Islands", "Majuro"),
    ("Federated States of Micronesia", "Palikir"),
    ("New Zealand", "Wellington"),
    ("Palau", "Melekeok"),
    ("Papua New Guinea", "Port Moresby"),
    ("Samoa", "Apia"),
    ("Solomon Islands", "Honiara"),
    ("Tonga", "Nuku’alofa"),
    ("Tuvalu", "Funafuti"),
    ("Vanuatu", "Port Vila"),
    ("Albania", "Tirana"),
    ("Andorra", "Andorra La Vella"),
    ("Armenia", "Yerevan"),
    ("Austria", "Vienna"),
    ("Azerbaijan", "Baku"),
    ("Belarus", "Minsk"),
    ("Belgium", "Brussels"),
    ("Bosnia and Herzegovina", "Sarajevo"),
    ("Bulgaria", "Sofia"),
    ("Croatia", "Zagreb"),
    ("Cyprus", "Nicosia"),
    ("Czech Republic", "Prague"),
    ("Denmark", "Copenhagen"),
    ("Estonia", "Tallinn"),
    ("Finland", "Helsinki"),
    ("France", "Paris"),
    ("Georgia", "Tblisi"),
    ("Germany", "Berlin"),
    ("Hungary", "Budapest"),
    ("Iceland", "Reykjavik"),
    ("Ireland", "Dublin"),
    ("Italy", "Rome"),
    ("Kazakhstan", "Astana"),
    ("Latvia", "Riga"),
    ("Liechtenstein", "Vaduz"),
    ("Lithuania", "Vilnius"),
    ("Luxembourg", "Luxembourg"),
    ("Macedonia", "Skopje"),
    ("Malta", "Valletta"),
    ("Moldova", "Chişinău"),
    ("Monaco", "Monaco"),
    ("Montenegro", "Podgorica"),
    ("Netherlands", "Amsterdam"),
    ("Norway", "Oslo"),
    ("Poland", "Warsaw"),
    ("Portugal", "Lisbon"),
    ("Romania", "Bucharest"),
    ("Russia", "Moscow"),
    ("San Marino", "San Marino"),
    ("Serbia", "Belgrade"),
    ("Slovakia", "Bratislava"),
    ("Slovenia", "Ljubljana"),
    ("Spain", "Madrid"),
    ("Sweden", "Stockholm"),
    ("Switzerland", "Bern"),
    ("Turkey", "Ankara"),
    ("Ukraine", "Kiev"),
    ("United Kingdom", "London"),
    ("Vatican City", "Vatican City")
]

how_many_countries = len(capitals)
points = 0
selected_country = None
random_int = 0 
asked_countries_id = []
country = 0

# Header of the game
print("----------------------------------")
print("-- \U0001F30D WORLD'S CAPITALS QUIZ! \U0001F30D --")
print("----------------------------------")
print()
print()

def gameStarter():
    global points
    # Choosing a country to ask
    random_int = randint(0,how_many_countries-1)
    if (random_int not in asked_countries_id):
        selected_country = capitals[random_int][0]
        asked_countries_id.append(random_int)
        country = selected_country
    else:
        random_int = randint(0,how_many_countries-1)
        selected_country = capitals[random_int][0]
        asked_countries_id.append(random_int)
        country = selected_country

    true_answer_str = capitals[random_int][1]
    print()
    print("What is the capital of the " + country + "?")
    print()
    
    # generating wrong answers
    wrong_answers = []
    while(True):
        if len(wrong_answers) != 3:
            random_capital_chooser = randint(0,how_many_countries-1)
            if capitals[random_capital_chooser][1] not in wrong_answers and capitals[random_capital_chooser][1] != capitals[random_int][1]:
                wrong_answers.append(capitals[random_capital_chooser][1])
        else:
            break
            
    # generating random answers' order
    true_answer_int = randint(1,4)
    if true_answer_int == 1:
        print("1. " + str(true_answer_str))
        print("2. " + str(wrong_answers[0]))
        print("3. " + str(wrong_answers[1]))
        print("4. " + str(wrong_answers[2]))
    elif true_answer_int == 2:
        print("1. " + str(wrong_answers[0]))
        print("2. " + str(true_answer_str))
        print("3. " + str(wrong_answers[1]))
        print("4. " + str(wrong_answers[2]))
    elif true_answer_int == 3:
        print("1. " + str(wrong_answers[0]))
        print("2. " + str(wrong_answers[1]))
        print("3. " + str(true_answer_str))
        print("4. " + str(wrong_answers[2]))
    elif true_answer_int == 4:
        print("1. " + str(wrong_answers[0]))
        print("2. " + str(wrong_answers[1]))
        print("3. " + str(wrong_answers[2]))
        print("4. " + str(true_answer_str))

    print()

    # Checking the answer if it is true or not
    true_inputs = ["1","2","3","4"]
    entered_answer = input("Your answer: ")
    if entered_answer in true_inputs:
        user_answer = int(entered_answer)
        if user_answer == true_answer_int:
            print()
            print()
            print("\U00002705 CORRECT \U0001F929 You got 10 points!")
            print()
            print()
            points += 10
        else:
            print()
            print()
            if points > 5:
                print("\U0000274C INCORRECT \U0001F915 You lost 5 points!")
                print()
                points -= 5
            else:
                print("\U0000274C INCORRECT \U0001F915 You already have 0 points")
                print()
                points = 0
    else:
        print("You entered an invalid string, next question is preparing..")

# Start the game
while (True):
    time.sleep(0.5)
    print("--------------------------------")
    print("----- \U0001F30D Your points : " + str(points) + " ------")
    print("--------------------------------")
    print()
    time.sleep(1)
    gameStarter()