<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">NinjaTruck</h3>

  <p align="center">
    This outlines the project codebase for IS213 ESD - G5 Group7 - AY2021/2022 Semester 2
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

NinjaTruck aims to be the last mile delivery management solution for delivery drivers. The application covers the most essential features a delivery driver will need when carrying out their day to day responsibilities of delivering a parcel to customers. 

<p align="right">(<a href="#top">back to top</a>)</p>



## Built With

### Frontend
* [Vue.js](https://nextjs.org/)
* [Quasar](https://reactjs.org/)

### API Gateway
* [KONG](https://laravel.com)

### Backend
* [Python](https://vuejs.org/)
* [Node.js](https://angular.io/)
* [Java Spring Boot](https://svelte.dev/)
* [Docker](https://laravel.com)

### Message Brokers
* [RabbitMQ](https://laravel.com)
* [Apache Kafka](https://laravel.com)

### External APIs used
* [Weather API](https://laravel.com)
* [Google Maps API](https://laravel.com)
* [Twilio API](https://laravel.com)
* [Nodemailer API](https://laravel.com)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
### Backend
Make sure you have a clean environment with no other containers as it can possibly conflict with this project’s ports mapping, image or container naming/labeling. Make sure that the Kong container and image is also deleted along with its network to set up a new kong configuration.
1. From the directory ./IS213-driver-app, open the terminal and enter `docker compose up` 
2. Access [http://localhost:1337](http://localhost:1337) in a browser to create an admin user for Konga
  ```
  Username: admin
  Email:    <your email address>
  Password: adminadmin
  ```
3. Sign in to continue
4. Connect Konga to Kong by creating a new connection
  ```
  Name: default
  Kong Admin URL: http://kong:8001
  ```
5. Go to Snapshots located on bottom right of the sidebar
6. Select _IMPORT FROM FILE_ and import ./tools/kongSnapshot.json
7. Click on _DETAILS_ for the new snapshot created which ends with Ninjatruck
8. Select _RESTORE_, tick all of the boxes, and click on _IMPORT OBJECTS_
9. Repeat step 8 until there is only 1 failed item left being under _key-auths_
10. Select _CONSUMERS_ on the side bar and select driver
11. Click on _Credentials_ and select _API KEYS_
12. Select _CREATE API KEY_ and key in: _BtqGD0VZBhHgFiIm2fbfA5zdzXmN6Coz_ and _SUBMIT_

## Prerequisites
* Docker version 20.10.13, build a224086
* Node - v16.13.0

Ensure you are running the same version by running the packages with `--version` in the terminal



<!-- USAGE EXAMPLES -->
## Usage
1. Open folder in vscode, cd “Frontend Code”, and open terminal
2. Install required dependencies 
  ```sh
	$ npm install
  ```
3. Launch NinjaTruck Application
  ```sh
	$ quasar dev
  ```
4. In browser, tap f12 to open console (as platform is only compatible for mobile)

## Scenario 1
* Driver logs in and views his dashboard
### Beyond the Lab
1. KONG is used as our API Gateway mainly for security implementation. Kong keeps the internal microservices from being directly exposed to external clients. 3 Plugins was also used to configure Kong:
* Kong’s Bot detection and rate limiting was used to prevent any bot attacks, DoS attack, and limit login attempts in case an attacker tries to brute force through the login. 
* Key-auth plugin was also used to add another layer of security by allowing only users with an api key belonging to Driver type consumer to access the microservices through kong.
2. Driver microservice is coded in Java SpringBoot. This is to highlight that the microservices are  language agnostic.
3. To handle exceptions in business logic, Error handling is implemented if username or password is incorrect when logging in. User will be notified of the incorrect username or password

## Scenario 2
* Driver views map of all his parcels for delivery


## Scenario 3
* Driver completes a delivery of a parcel and marks it as either completed or failed
### Beyond the Lab
1. Used Kafka as our message broker between Update Parcel Status and SMS microservice. Kafka is designed for holding and distributing large volumes of messages. Considering how there are hundreds of thousands of parcels delivered daily, kafka would be a good choice to handle the large amount of messages.
2. Kafka uses their own custom kafka protocol.
3. SMS microservice is built with Node.js. This is to highlight that the microservices are language agnostic.
4. To handle exceptions in business logic, Error handling is implemented if delivery has not been fulfilled. 




<!-- ROADMAP -->
## Roadmap

- [] Feature 1
- [] Feature 2
- [] Feature 3
    - [] Nested Feature

See the [open issues](https://github.com/github_username/repo_name/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Greg G Tan Jun Kai]()
* [Hazel Ma Ruiqi]()
* [Ian Chia Chern Yi]()
* [Juan Sebastian]()
* [Quinn Cheong Shi Han]()

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
