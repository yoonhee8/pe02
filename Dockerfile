#refered based image from: https://hub.docker.com/_/python/tags
FROM python:3.9.16-bullseye

COPY requirements.txt ./requirements.txt
COPY train_and_test.py ./train_and_test.py
COPY flask_app.py ./flask_app.py

RUN pip install -r requirements.txt
#execute train and save model to joblib file
RUN python train_and_test.py

# runs application in the container
# Any Docker image must have an ENTRYPOINT or CMD declaration for a container to start.
# Default parameters that cannot be overridden when Docker Containers run with CLI parameters.
ENTRYPOINT ["python"]

# appends the list of parameters to the EntryPoint parameter
# to perform the command that runs the application.
# ex. python flask_app.py
CMD ["flask_app.py"]