#first page of code



# from urllib import response
import pyaztro
import random
import requests




print("________________________________________________________________")
print("1. Aries (March 21 – April 19)")
print("2. Taurus (April 20 – May 20)")
print("3. Gemini (May 21 – June 20)")
print("4. Cancer (June 21 – July 22)")
print("5. Leo (July 23 – August 22)")
print("6. Virgo (August 23 – September 22)")
print("7. Libra (September 23 – October 22)")
print("8. Scorpio (October 23 – November 21)")
print("9. Sagittarius (November 22 – December 21)")
print("10. Capricorn (December 22 – January 19)")
print("11.Aquarius (January 20 – February 18)")
print("12. Pisces (February 19 – March 20)")
print("________________________________________________________________")
# z=int(input("Select Your Zodiac sign(1-12):- "))

first = ["Today is perfect for new endeavors. ", 
"The tensions of this week will feel heavier today than yesterday. ", 
"Today is the day to cherish and embrace others. ", 
"Making yourself useful is a main component of a successful day. ", 
"Today, exercise caution when crossing the street. ",
"Money will come in as word about your skills gets around",
"You will need to curb your tendency to indulge in excesses to remain healthy",
"Travelling overseas in an official capacity is indicated for some",
""]


second = ["Remember that good things come to those who work hard. ", 
"Don’t let the circumstances bring you down. ", 
"Patience is key, but sometimes a little push can get the job done. ", 
"A smile can get you a long way. ",
"Those worried about their financial situation can rest easy.",
"Taking time off to visit friends and relations is possible for some.",
"Someone close can suggest some changes in a plan.",
"Money may come to you from a most unexpected quarte"]


third = ["Looking ahead may seem like a waste of time, but it pays off in the end. ", 
"Luck favors those who mind the risks and take them. ", 
"Today is the day for that thing you always wanted to do. ", 
"Luck is on your side today, so seize it! ", 
"Things are looking up for you! ",
" A new arrival is set to bring joy and happiness in the family.",
" Much fun awaits some in a journey.",
" Your efforts are likely to bring cohesiveness in the team on the work front.",
"You will manage to tie up all the loose ends at work"]
z = int(input("Pick your sign by typing a number and pressing Enter: "))


if z==1:
    sign="Aries"
if z==2:
    sign="Taurus"
if z==3:
    sign="Gemini"
if z==4:
    sign="Cancer"
if z==5:
    sign="Leo"
if z==6:
    sign="Virgo"
if z==7:
    sign="Libra"
if z==8:
    sign="Scorpious"
if z==9:
    sign="Sagittarius"
if z==10:
    sign="Capricornus"
if z==11:
    sign="Aquarius"
if z==12:
    sign="Pisces"

day=input("Please enter the horoscope day(today,tomorrow,or yesterday):")
if 0 < z < 13:
	print(random.choice(first), random.choice(second), random.choice(second), random.choice(third))
else:
	print("This does not correspond to a zodiac sign")
horoscope = pyaztro.Aztro(sign)

print("_____________________________________________________________________________")

print("Your Zodiac is",sign)

print("_____________________________________________________________________________")

# # Mood
print("Current Mood:-",horoscope.mood)
# 'Relaxed'
print("_____________________________________________________________________________")

# # Lucky time
print("Lucky Time:-",horoscope.lucky_time)
# '2pm'
print("_____________________________________________________________________________")

# # Description
print("Description:-",horoscope.description)
# 'If you don't have big plans, you can rest assured that you will soon. A surprise missive is waiting. Enjoy. It's spontaneity, not variety, that's the spice of life.'
print("_____________________________________________________________________________")

# # Sun sign date range
print("Sun Sign Date Range:-",horoscope.date_range)
# [datetime.datetime(2019, 3, 21, 0, 0), datetime.datetime(2019, 4, 20, 0, 0)]
print("_____________________________________________________________________________")

# # Lucky Color
print("Lucky Colour:-",horoscope.color)
# 'Spring Green'
print("_____________________________________________________________________________")

# # Sign compatibility
print("Sign Compatibility:-",horoscope.compatibility)
# 'Aquarius'
print("_____________________________________________________________________________")


# # Horoscope date for which the info is valid for
print("Valid For:-",horoscope.current_date)
# datetime.date(2019, 6, 2)
print("_____________________________________________________________________________")

# # Lucky number
print("Lucky Number:-",horoscope.lucky_number)
# 85

