#Weather report
#Importing Beautifulsoup Library
import requests
from bs4 import BeautifulSoup
#importing requests module

def Main():
    print("Hi, this is a program that switches temperature between Fahrenheit and Celsius", end = "\n\n")
    input_user = input("Enter the name of the town where you want to know the weather: ")
    #city = "Meadville"

    url = "https://www.google.com/search?q="+"weather"+ input_user
    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    data = str.split('\n')
    time = data[0]
    sky = data[1]

    pos = str.find('Wind')
    other_data = str[pos:]
    
    # printing all data
    print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)
    print(other_data)

if __name__ == "__main__":
    Main()




