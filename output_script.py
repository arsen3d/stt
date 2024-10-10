import os

def main():
    print("Starting script execution")
    
    # Create the output directory
    output_dir = "output"
    print(f"Attempting to create directory: {output_dir}")
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a text file with the message
    file_path = os.path.join(output_dir, "hello.txt")
    print(f"Attempting to create file: {file_path}")
    with open(file_path, "w") as f:
        f.write("Hello from Lilypad")
    
    print(f"File creation attempted. Checking if file exists: {os.path.exists(file_path)}")
    
    # List contents of the output directory
    print(f"Contents of {output_dir}:")
    print(os.listdir(output_dir))

    # Print current working directory
    print(f"Current working directory: {os.getcwd()}")

if __name__ == "__main__":
    main()