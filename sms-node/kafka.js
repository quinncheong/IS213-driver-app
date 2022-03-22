// const { Kafka } = require("kafkajs");

// const { KAFKA_USERNAME: username, KAFKA_PASSWORD: password } = process.env;
// const sasl =
// 	username && password ? { username, password, mechanism: "plain" } : null;
// const ssl = !!sasl;

// // This creates a client instance that is configured to connect to the Kafka broker provided by
// // the environment variable KAFKA_BOOTSTRAP_SERVER
// const kafka = new Kafka({
// 	clientId: "npm-slack-notifier",
// 	brokers: [process.env.KAFKA_BOOTSTRAP_SERVER],
// 	ssl,
// 	sasl,
// });

// module.exports = kafka;

const { Kafka } = require("kafkajs");

const kafka = new Kafka({
	clientId: "my-app",
	brokers: ["127.0.0.1:9093"],
});

const producer = kafka.producer();
const consumer = kafka.consumer({ groupId: "test-group" });

const run = async () => {
	// Producing
	console.log("awaiting producer");
	console.log(producer);
	await producer.connect();
	await producer.send({
		topic: "test-topic",
		messages: [{ value: "Hello another KafkaJS user!" }],
	});

	console.log("producer end");

	// Consuming
	await consumer.connect();
	await consumer.subscribe({ topic: "test-topic", fromBeginning: true });

	await consumer.run({
		eachMessage: async ({ topic, partition, message }) => {
			console.log(topic);
			console.log({
				partition,
				offset: message.offset,
				value: message.value.toString(),
			});
		},
	});
};

run().catch(console.error);
