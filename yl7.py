nimi = input("Sisesta oma nimi: ")
kodu = input("Tere, " + nimi + "! Kus sa elad?: ")

if kodu == "Saaremaa" or "saaremaa":
    print("Saaremaa on väga ilus koht.")
    
age = int(input("Kui vana sa oled? "))

if age < 18:
    print("Oled auto juhtimiseks veel liiga noor.")
elif age == 18:
    print("Palju õnne ametlikult täiskasvanuks saamise puhul!")
elif age > 18:
    print("Vau! Sa võid autot juhtida!")