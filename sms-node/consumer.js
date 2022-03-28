// Download the helper library from https://www.twilio.com/docs/node/install
// Find your Account SID and Auth Token at twilio.com/console
// and set the environment variables. See http://twil.io/secure
// const accountSid = process.env.TWILIO_ACCOUNT_SID;
// const authToken = process.env.TWILIO_AUTH_TOKEN;

// Hardcode for now
const { twilio_account_sid, twilio_auth_token } = require("./privateKey.json");
const client = require("twilio")(twilio_account_sid, twilio_auth_token);

const clientId = "my-app";
const groupId = "test-group";
const topic = "test-topic";

const broker = "127.0.0.1:9093";
const phoneNumber = "+19402512615";

const { Kafka } = require("kafkajs");
const kafka = new Kafka({
	clientId: clientId,
	brokers: [broker],
});

const consumer = kafka.consumer({ groupId: groupId });

const run = async () => {
	// Consuming
	await consumer.connect();
	await consumer.subscribe({ topic: topic, fromBeginning: true });

	await consumer.run({
		eachMessage: async ({ topic, partition, message }) => {
			console.log(topic);
			console.log(partition);
			console.log(message.value);
			console.log({
				partition,
				offset: message.offset,
				value: JSON.parse(message.value.toString()),
			});

			let { phoneNumber: numberToSend, body } = JSON.parse(
				message.value.toString()
			);

			// client.messages
			// 	.create({
			// 		body: body,
			// 		from: phoneNumber,
			// 		to: numberToSend, // It must start with +65
			// 	})
			// 	.then((message) => console.log(message.sid))
			// 	.catch((err) => console.log(err));
		},
	});
};

run().catch(console.error);
