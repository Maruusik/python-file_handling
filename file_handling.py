# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1\n")
        file.write("12345\n")
        file.write("Another line here with some numbers: 9876\n")
        print("File created and written successfully.")
except PermissionError:
    print("Permission denied. Couldn't create the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("Content of my_file.txt:\n", content)
except FileNotFoundError:
    print("File not found. Couldn't read the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File reading process completed.\n")

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1\n")
        file.write("Appending line 2\n")
        file.write("Appending line 3\n")
    print("Content appended to my_file.txt successfully.")
except PermissionError:
    print("Permission denied. Couldn't append to the file.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print("File appending process completed.")
