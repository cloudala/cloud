FROM node:20.12.1
WORKDIR /app
COPY app/. .
RUN npm install
EXPOSE 3000
CMD [ "node", "app.js" ]