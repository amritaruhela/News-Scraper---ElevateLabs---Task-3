
import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.bbc.com/news"

def fetch_headlines():
    headers={"User-Agent":"Mozilla/5.0"}
    response=requests.get(URL,headers=headers,timeout=10)
    response.raise_for_status()
    soup=BeautifulSoup(response.text,"html.parser")
    headlines=[]
    seen=set()
    for tag in soup.find_all(["h2","h3"]):
        text=tag.get_text(strip=True)
        if text and text not in seen and len(text)>20:
            seen.add(text)
            headlines.append(text)
    return headlines

def save_headlines(headlines, filename="headlines.txt"):
    with open(filename,"w",encoding="utf-8") as f:
        f.write(f"News Headlines\nGenerated: {datetime.now()}\n")
        f.write("="*60+"\n\n")
        for i,h in enumerate(headlines,1):
            f.write(f"{i}. {h}\n")

def main():
    try:
        headlines=fetch_headlines()
        if not headlines:
            print("No headlines found.")
            return
        save_headlines(headlines)
        print("Top Headlines:\n")
        for i,h in enumerate(headlines[:15],1):
            print(f"{i}. {h}")
        print("\nSaved to headlines.txt")
    except requests.RequestException as e:
        print("Network Error:",e)
    except Exception as e:
        print("Error:",e)

if __name__=="__main__":
    main()
