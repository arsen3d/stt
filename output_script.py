import os

def main():
    # Create the output directory
    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Create a text file with the message
    file_path = os.path.join(output_dir, "output.txt")
    with open(file_path, "w") as f:
        f.write("Hello from Lilypad")
    
    print(f"Created file: {file_path}")

if __name__ == "__main__":
    main()