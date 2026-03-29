def write_email(client):
    print("\n--- AI Email Writer ---")
    recipient = input("Who is this email to? (e.g. my manager, a client): ").strip()
    purpose = input("What is the purpose of the email? ").strip()
    tone = input("Tone? (formal / friendly / assertive): ").strip()

    if not purpose:
        print("No purpose provided.")
        return

    print("\nWriting your email...")
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": (
                    f"Write a {tone} email to {recipient}.\n"
                    f"Purpose: {purpose}\n"
                    f"Include a subject line, greeting, body, and sign-off."
                )
            }
        ]
    )
    print("\n✅ Your Email:")
    print(message.content[0].text)
