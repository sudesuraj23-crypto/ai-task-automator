def summarize(client):
    print("\n--- Document Summarizer ---")
    print("Paste your text below (press Enter twice when done):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    text = "\n".join(lines)
    if not text.strip():
        print("No text provided.")
        return

    print("\nSummarizing...")
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"Please summarize the following text clearly and concisely:\n\n{text}"
            }
        ]
    )
    print("\n✅ Summary:")
    print(message.content[0].text)
