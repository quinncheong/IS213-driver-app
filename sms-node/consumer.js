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

// Download the helper library from https://www.twilio.com/docs/node/install
// Find your Account SID and Auth Token at twilio.com/console
// and set the environment variables. See http://twil.io/secure
// const accountSid = process.env.TWILIO_ACCOUNT_SID;
// const authToken = process.env.TWILIO_AUTH_TOKEN;

// Hardcode for now
const {
	twilio_account_sid,
	twilio_auth_token,
} = require("../privateKey.json");
const client = require("twilio")(twilio_account_sid, twilio_auth_token);

const { Kafka } = require("kafkajs");
const kafka = new Kafka({
	clientId: "my-app",
	brokers: ["127.0.0.1:9093"],
});

const consumer = kafka.consumer({ groupId: "test-group" });

const run = async () => {
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

			client.messages
				.create({
					body: message.value.toString(),
					from: "+19402512615",
					to: "+6594573673",
				})
				.then((message) => console.log(message.sid));
		},
	});
};

run().catch(console.error);
