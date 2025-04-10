def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        # Attempt to open and read the original file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content (convert to uppercase as an example)
        modified_content = content.upper()

        # Write the modified content to a new file
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"✅ File was read and written successfully to '{new_filename}'.")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except IOError:
        print(f"❌ Error: Could not read or write to the file '{filename}'.")

# Run the function
read_and_modify_file()

