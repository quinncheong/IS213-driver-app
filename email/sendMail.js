const nodemailer = require("nodemailer");
const { nodeemailerUser, nodemailerPass } = require("./privateKey.json");

export default async function main(message) {
	// create reusable transporter object using the default SMTP transport
	let transporter = nodemailer.createTransport({
		host: "smtp-mail.outlook.com", // hostname
		// service: "hotmail",
		port: 587, // port for secure SMTP
		secure: false, // true for 465, false for other ports
		auth: {
			user: nodeemailerUser,
			pass: nodemailerPass,
		},
		tls: {
			ciphers: "SSLv3",
		},
		requireTLS: true,
	});
	
	const output = `
		<h3>Hello Admin Team ${email},</h3>
		<p>The Parcel for user ${} with ID: ${} has failed to deliver.</p>
		<p>Please look into this to resolve the parcel issue.</p>
		`;
	
	let mailOptions = {
		from: '"NinjaTruck" <ninjatruckESD@gmail.com>', // sender address
		to: email, // list of receivers in string form
		subject: `Failed Delivery for ID: ${}`, // Subject line
		// text: `Click on / go to the link to reset your password ${link}${id}`, // plain text body
		html: output, // html body
	};
	
	// send mail with defined transport object
	transporter.sendMail(mailOptions, (error, info) => {
		if (error) {
			throw error;
		}

		console.log(info)
		return
	});
	
}

