FROM python:3.8-slim
RUN apt-get update && apt-get install -y procps less
RUN pip install flask
# Set the working directory to /app
WORKDIR /home/almogr/World_Of_Games/Docker 

# Copy the current directory contents into the container as /app
COPY . /home/almogr/World_Of_Games/Docker

# Adding the Score.txt file
ADD /Scores.txt /home/almogr/World_Of_Games/Docker/Scores.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD python Docker-Flask.py
