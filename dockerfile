# Use a lightweight Python image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the Python script into the container
COPY output_script.py .

# Print contents of the script and list directory
RUN cat output_script.py && echo "\n\nCurrent directory:" && ls -la

# Run the Python script when the container launches
CMD ["python", "output_script.py"]