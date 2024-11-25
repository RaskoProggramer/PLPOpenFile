def read_and_modify_file(input_filename, output_filename):
    try:
        # Try to open the input file for reading
        with open(input_filename, 'r') as file:
            # Read the contents of the file
            content = file.read()
        
        # Modify the content (e.g., convert text to uppercase)
        modified_content = content.upper()  # Example modification: making all text uppercase

        # Write the modified content to a new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"File modified successfully. The modified content has been written to {output_filename}.")

    except FileNotFoundError:
        # Handle the case where the file doesn't exist
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        # Handle any IO errors (like permission issues)
        print(f"Error: Could not read or write the file '{input_filename}' or '{output_filename}'.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

def main():
    # Ask the user for the input and output filenames
    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name of the file to write to: ")

    # Call the function to read, modify, and write the file
    read_and_modify_file(input_filename, output_filename)

if __name__ == "__main__":
    main()
