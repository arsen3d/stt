# Use a lightweight Python image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Create the /outputs directory and set permissions
RUN mkdir /outputs && chmod 777 /outputs

# Copy the Python script into the container
COPY output_script.py .

# Run the Python script when the container launches
CMD ["python", "output_script.py"]