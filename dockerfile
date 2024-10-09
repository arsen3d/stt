# Use a lightweight Linux image
FROM alpine:latest

# Set the working directory in the container
WORKDIR /app

# Create a simple text file
RUN echo "Hello, Docker!" > output.txt

# Command to display the contents of the file
CMD ["cat", "output.txt"]