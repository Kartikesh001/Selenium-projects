from bs4 import BeautifulSoup
import os
import pandas as pd  


d = {'title': [], 'price': [], 'link': []}

for file in os.listdir("data"):
    try:
        
        with open(f"data/{file}", encoding='utf-8') as f:
            html_doc = f.read()

       
        soup = BeautifulSoup(html_doc, 'html.parser')

        
        t = soup.find("h2")
        if t:
            title = t.get_text().strip()
            d['title'].append(title)
        else:
            d['title'].append("N/A")

        
        l = t.find("a") if t else None
        if l:
            link = "https://amazon.in/" + l['href']
            d['link'].append(link)
        else:
            d['link'].append("N/A")

        
        p = soup.find("span", attrs={"class": 'a-price-whole'})
        if p:
            price = p.get_text().strip()
            d['price'].append(price)
        else:
            d['price'].append("N/A")

        
        print(f"Title: {title}, Price: {price}, Link: {link}")

    except Exception as e:
        print(f"Error processing file {file}: {e}")

df = pd.DataFrame(data=d)
df.to_csv("data.csv", index=False)
print("Data saved to data.csv")
