// const express = require('express')
// const app = express()
// const port = 3000

// app.get('/', (req, res) => {
//   res.send('Hello World!')
// })

// app.listen(port, () => {
//   console.log(`Example app listening on port ${port}`)
// })

const { Kafka } = require("kafkajs");

const kafka = new Kafka({
	clientId: "my-app",
	brokers: ["127.0.0.1:9093"],
});

const producer = kafka.producer();

const run = async () => {
	// Producing
	console.log("awaiting producer");
	console.log(producer);
	await producer.connect();
	await producer.send({
		topic: "test-topic",
		messages: [{ value: "Hello ian KafkaJS user!" }],
	});

	console.log("producer end");
};

run().catch(console.error);
