FROM node:17.5.0
ENV NODE_ENV=production
WORKDIR /usr/src/app
COPY ["package.json", "package-lock.json*","privateKey.json", "./"]
RUN npm install --production
COPY . .
CMD [ "node", "consumer.js" ]