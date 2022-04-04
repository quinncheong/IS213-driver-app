const config = require("./config");
const amqplib = require("amqplib/callback_api");
const nodemailer = require("nodemailer");
const sendMail = require("./sendMail").default;

const host = "127.0.0.1";
const port = "12345";
const amqp = "amqp://localhost";
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
		channel.assertQueue(
			queue,
			{
				// Ensure that the queue is not deleted when server restarts
				durable: true,
			},
			(err) => {
				if (err) {
					console.error(err.stack);
					return process.exit(1);
				}

				// Only request 1 unacked message from queue
				// This value indicates how many messages we want to process in parallel
				channel.prefetch(1);

				// Set up callback to handle messages received from the queue
				channel.consume(queue, (data) => {
					if (data === null) {
						return;
					}

					// Decode message contents
					let message = JSON.parse(data.content.toString());

                    console.log(message)

                    // await sendMail(message);
				});
			}
		);
	});
});
