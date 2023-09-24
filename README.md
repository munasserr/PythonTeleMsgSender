# PythonTeleMsgSender

PythonTeleMsgSender is a Python script that simplifies the process of sending messages to multiple users or groups on Telegram. It's a handy tool for broadcasting messages, making announcements, or conducting outreach campaigns.

## Features

- Easy setup and usage.
- Send messages to multiple users or groups simultaneously.
- Customize messages to fit your needs.
- Efficient and effective message distribution.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- pip3 installed.

## Getting Started

Before you can use PythonTeleMsgSender, you'll need to obtain the required Telegram API credentials. Follow these steps to get started:

1. **Create a Telegram Account:**

   If you don't already have a Telegram account, you'll need to [sign up for one](https://telegram.org/).

2. **Create a Telegram Application:**

   - Go to [https://my.telegram.org/apps](https://my.telegram.org/apps) and log in with your Telegram account.

   - Click on the "Create Application" button.

   - Fill out the form with the following details:
     - **App Title:** Choose a name for your application (e.g., "PythonTeleMsgSender").
     - **Short Name:** Provide a short name (must be unique).
     - **Platform:** Choose "Other."

   - Click on the "Create Application" button to create your Telegram application.

3. **Obtain API ID and Hash:**
   
   - After creating the application, you'll be taken to a page with your application's details.

   ![Screenshot 2023-09-24 141626](https://github.com/munasserr/PythonTeleMsgSender/assets/107954461/4f503bd0-9d3d-444e-90a2-bb58abcf9308)

   - Note down the **App API ID** and **App API Hash**. You'll need these credentials to configure PythonTeleMsgSender.


### Clone the repository

```sh
git clone https://github.com/munasserr/PythonTeleMsgSender.git
```

### Navigate to the project directory
```sh
cd PythonTeleMsgSender
```
### Install the required dependencies
```sh
pip install -r requirements.txt
```
### Run the script
```sh
python PythonTeleMsgSender.py
```

## Usage

#### After running the script you will get this result

![Screenshot 2023-09-24 aa150451](https://github.com/munasserr/PythonTeleMsgSender/assets/107954461/4b046998-5827-4863-9bdc-a6bb28738ba8)

1. **Enter API ID and API Hash Key you get before starting**

   If you don't already have them ,Please go back to the Getting Started section.

2. **Enter The Phone Number With Country Code**

   Enter the phone number associated with your telegram account.

3. **Enter The OTP That Has Been Sent To Your Number**

   You will get a message with an otp number , Please provide it so you can log in to start broadcasting your messages.
   
3. **Enter Your Custom Message**

   Enter your specified message , It can be anything [Announcements ,Advertising ,etc..].


5. **Get And Provide Your User ID To Start Sending Messages**

   After you signed in , now you need to get your user id to continue.
   
   ##### How To Get It :
   - Open Telegram From Your Browser
   - Go To Your Own Chat
   - Via Url You Will Find It As Specfied In The Picture
     
     ![Screenshot 2023-09-24 152007](https://github.com/munasserr/PythonTeleMsgSender/assets/107954461/b274bed3-8d43-447b-ad33-fba1318ccce9)

6. **Get And Provide The Targted Group ID**
   
   The same way we got the user id , we're gonna open the group chat and then copy the group id via url.

8. **It's Show Time**
   
   Now it's show time , just wait till the specfied group members scraped and the custom message you entered is sent to all that group members.
   
## Contributing

 ### Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
   - Fork the project.
   - Create your feature branch: git checkout -b feature/new-feature.
   - Commit your changes: git commit -m 'Add new feature'.
   - Push to the branch: git push origin feature/new-feature.
   - Submit a pull request.

## License

Distributed under the [MIT License](LICENSE). See LICENSE for more information.

## Contact

If you have any questions or suggestions, feel free to [contact me on LinkedIn](https://www.linkedin.com/in/munasser/).


