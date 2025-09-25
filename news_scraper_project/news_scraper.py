import requests
from bs4 import BeautifulSoup

def fetch_headlines(url="https://www.bbc.com/news", output_file="headlines.txt"):
    try:
        # Step 1: Fetch HTML content
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print(f"❌ Failed to fetch page. Status code: {response.status_code}")
            return

        # Step 2: Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Step 3: Extract headlines (BBC often uses <h2>)
        headlines = soup.find_all("h2")

        # Step 4: Save to a text file
        with open(output_file, "w", encoding="utf-8") as file:
            for idx, headline in enumerate(headlines, start=1):
                text = headline.get_text(strip=True)
                if text:  # skip empty headlines
                    file.write(f"{idx}. {text}\n")

        print(f"✅ Headlines saved successfully to {output_file}")

    except Exception as e:
        print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    fetch_headlines()
