const nodemailer = require("nodemailer");
const { nodemailerUser, nodemailerPass } = require("./privateKey.json");

// https://accounts.google.com/b/0/DisplayUnlockCaptcha might have to do this

async function main(message) {
	console.log(message);
	// create reusable transporter object using the default SMTP transport
	let transporter = nodemailer.createTransport({
		// host: "smtp-mail.gmail.com", // hostname
		service: "gmail",
		port: 587, // port for secure SMTP
		secure: false, // true for 465, false for other ports
		auth: {
			user: nodemailerUser,
			pass: nodemailerPass,
		},
		tls: {
			ciphers: "SSLv3",
		},
		requireTLS: true,
	});

	const output = `
		<h3>Hello Admin Team,</h3>
		<p>The Parcel with ID: ${message.parcelId} for user ${message.customerName} has failed to deliver.</p>
		<p>Please look into this to resolve the parcel issue.</p>
		`;

	const emailStr = message.emails.join(",")

	let mailOptions = {
		from: '"NinjaTruck" <ninjatruckESD@gmail.com>', // sender address
		to: emailStr, // list of receivers in string form
		subject: `Failed Delivery for Parcel: ${message.parcelId}`, // Subject line
		// text: `Click on / go to the link to reset your password ${link}${id}`, // plain text body
		html: output, // html body
	};

	// send mail with defined transport object
	transporter.sendMail(mailOptions, (error, info) => {
		if (error) {
			console.log("hitting the error");
			throw error;
		}

		console.log(info);
		return;
	});
}

module.exports = {
	main,
};
