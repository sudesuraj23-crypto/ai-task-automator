import anthropic
import sys

def get_client():
    api_key = input("Enter your Claude API key: ").strip()
    return anthropic.Anthropic(api_key=api_key)

def main():
    print("=" * 40)
    print("   AI Task Automator — Powered by Claude")
    print("=" * 40)
    print("\nSelect a task:")
    print("1. Summarize a document")
    print("2. Write an email")
    print("3. Organize file names")
    print("4. Scrape & summarize a webpage")
    print("0. Exit")

    choice = input("\nEnter your choice: ").strip()
    client = get_client()

    if choice == "1":
        from tasks.summarizer import summarize
        summarize(client)
    elif choice == "2":
        from tasks.email_writer import write_email
        write_email(client)
    elif choice == "3":
        from tasks.file_organizer import organize_files
        organize_files(client)
    elif choice == "4":
        from tasks.web_scraper import scrape_and_summarize
        scrape_and_summarize(client)
    elif choice == "0":
        print("Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()
