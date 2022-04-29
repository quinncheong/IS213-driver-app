FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./UpdateParcelStatus.py ./invokes.py ./send_message.py ./send_email.py ./amqp_setup.py ./
CMD [ "python", "./UpdateParcelStatus.py" ]