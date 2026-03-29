import urllib.request
import re

def scrape_and_summarize(client):
    print("\n--- Web Scraper & Summarizer ---")
    url = input("Enter the webpage URL: ").strip()

    print("\nFetching webpage...")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"Failed to fetch URL: {e}")
        return

    clean_text = re.sub(r"<[^>]+>", " ", html)
    clean_text = re.sub(r"\s+", " ", clean_text).strip()
    clean_text = clean_text[:4000]

    print("Summarizing content...")
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": (
                    f"The following is raw text extracted from a webpage.\n\n"
                    f"{clean_text}\n\n"
                    f"Please summarize the key information from this page clearly."
                )
            }
        ]
    )
    print("\n✅ Webpage Summary:")
    print(message.content[0].text)
