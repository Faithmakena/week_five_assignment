# File Creation
try:
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Line 3 with some special characters: !@#$%^&*\n")
except Exception as e:
    print("An error occurred while creating the file:", e)
else:
    print("File 'my_file.txt' created successfully.")

# File Reading and Display
try:
    with open("my_file.txt", "r") as file:
        print("Contents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to read the file.")
except Exception as e:
    print("An error occurred while reading the file:", e)

# File Appending
try:
    with open("my_file.txt", "a") as file:
        file.write("This is line 4 added through append mode.\n")
        file.write("67890\n")
        file.write("Appending line 6.\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to append to the file.")
except Exception as e:
    print("An error occurred while appending to the file:", e)
finally:
    print("Appending completed.")

