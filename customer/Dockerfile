FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt privateKey.json ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./Customer.py ./
CMD [ "python", "./Customer.py" ]



