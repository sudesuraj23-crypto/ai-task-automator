import os

def organize_files(client):
    print("\n--- AI File Organizer ---")
    folder_path = input("Enter the folder path to organize: ").strip()

    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    files = os.listdir(folder_path)
    if not files:
        print("Folder is empty.")
        return

    file_list = "\n".join(files)
    print(f"\nFound {len(files)} files. Asking AI for suggestions...")

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": (
                    f"I have the following files in a folder:\n\n{file_list}\n\n"
                    f"Suggest how to organize them into subfolders by category "
                    f"(e.g. Images, Documents, Videos, Code, etc.). "
                    f"List each file and which subfolder it should go into."
                )
            }
        ]
    )
    print("\n✅ AI Organization Suggestions:")
    print(message.content[0].text)
