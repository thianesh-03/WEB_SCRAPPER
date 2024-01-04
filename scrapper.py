import requests
from bs4 import BeautifulSoup
import csv 

url = "https://www.swiggy.com/city/bangalore/best-restaurants"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

try: 
    response = requests.get('https://www.swiggy.com/city/bangalore/best-restaurants', headers=headers)
    response.raise_for_status() 


    if response.status_code == 200: 
        print("Success!")
        
        csv_file = open('csv/Bangalore_2.csv', 'w')
        writer = csv.writer(csv_file)
        writer.writerow(['Restaurant Name'])
        
        soup = BeautifulSoup(response.text, 'html.parser')
        restaurants = soup.find_all('div', class_="styled__StyledRestaurantGridCard-sc-fcg6mi-0 lgOeYp")

        for restaurant in restaurants: 
            name = restaurant.find('div', class_='sc-beySbM cwvucc').text.strip()
            writer.writerow([name]) 
            print(name)
    else:
        print("Error")
            
except requests.exceptions.HTTPError as errh:
    print(f"HTTP Error: {errh}")
except Exception as e:
    print(f"An error occurred: {e}")
