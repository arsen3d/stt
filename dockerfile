# Use a lightweight Linux image
FROM alpine:latest

# Set the working directory in the container
WORKDIR /app

# Create an output folder
RUN mkdir -p output

# Create a simple text file inside the output folder
RUN echo "Hello, Docker!" > output/output.txt

# Command to display the contents of the file
CMD ["cat", "output/output.txt"]