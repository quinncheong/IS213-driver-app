FROM python:3-slim
WORKDIR /usr/src/app
COPY requirements.txt privateKey.json ./
RUN python -m pip install --no-cache-dir -r requirements.txt
COPY ./LoadDashboard.py ./invokes.py ./
CMD [ "python", "./LoadDashboard.py" ]