 FROM python:3
 ENV PYTHONUNBUFFERED 1

# Setting up codebase directory
ENV APP_HOME /usr/src/app
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Install requirements
ADD requirements.txt $APP_HOME/
RUN pip install -r requirements.txt

# Add current codebase to container
ADD . $APP_HOME/

# Launch the server
CMD [ "python3", "main.py"]