import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting script execution")
    
    # Create the output directory
    output_dir = "/outputs"
    os.makedirs(output_dir, exist_ok=True)
    logging.info(f"Created output directory: {output_dir}")
    
    # Create a text file with the message
    output_path = os.path.join(output_dir, "hello.txt")
    with open(output_path, "w") as f:
        f.write("Hello from Lilypad")
    logging.info(f"Text file created and saved as {output_path}")
    
    # List contents of the output directory
    logging.info(f"Contents of {output_dir}:")
    logging.info(os.listdir(output_dir))

    # Print current working directory
    logging.info(f"Current working directory: {os.getcwd()}")

if __name__ == "__main__":
    main()