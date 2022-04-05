const amqplib = require("amqplib/callback_api");

const sendMail = require("./sendMail").main;

// const host = "127.0.0.1";
// const port = "12345";
const amqp = "amqp://rabbitmq";
const queue = "nodemailer-amqp";

// Create connection to AMQP server
amqplib.connect(amqp, (err, connection) => {
	if (err) {
		console.error(err.stack);
		return process.exit(1);
	}
	// Create channel
	connection.createChannel((err, channel) => {
		if (err) {
			console.error(err.stack);
			return process.exit(1);
		}

		// Ensure queue for messages
		channel.assertQueue(queue, { durable: true }, (err) => {
			if (err) {
				console.error(err.stack);
				return process.exit(1);
			}

			// Only request 1 unacked message from queue
			// This value indicates how many messages we want to process in parallel
			channel.prefetch(1);

			// Set up callback to handle messages received from the queue
			channel.consume(
				queue,
				(data) => {
					if (data === null) {
						console.log("oops");
						// channel.reject(data, true);
						return;
					}
					// channel.ack(data);

					// Decode message contents
					let message = JSON.parse(data.content.toString());

					console.log(message);

					sendMail(message);
				},
				{ noAck: true }
			);
		});
	});
});
