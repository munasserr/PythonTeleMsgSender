"""

Credits of this script goes to MUNASSER
Github : https://github.com/munasserr
Linkedin : https://www.linkedin.com/in/munasser

Hope it's gonne be useful and help you all out <333.

"""




# importing all required libraries
import telebot
from telethon.sync import TelegramClient,errors
from telethon.tl.types import InputPeerUser, InputPeerChannel ,InputPeerChat
from telethon import TelegramClient, sync, events,types
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from tqdm import tqdm
import time
import colorama
from pyfiglet import Figlet



# This is for the developer's name printing only
# ------------------------------------------------------------------------------------------------
colorama.init()

font = "slant"  
width = 160


name = "munasser"
fig = Figlet(font=font)
output = fig.renderText(name)
output = output.rstrip('\n')
output = output.expandtabs(width)


start_color = (255, 0, 0)  # Red
end_color = (255, 165, 0)  # Orange
orange_code = '\x1b[38;2;{};{};{}m'.format(*end_color)
green_color = (0, 255, 0)  # Green RGB values
green_code = '\x1b[38;2;{};{};{}m'.format(*green_color)
reset_code = '\x1b[0m'
checkmark = '\u2713'


step = 1 / (len(output) - 1)

gradient = []
for i in range(len(output)):
    r = int(start_color[0] + (end_color[0] - start_color[0]) * (i * step))
    g = int(start_color[1] + (end_color[1] - start_color[1]) * (i * step))
    b = int(start_color[2] + (end_color[2] - start_color[2]) * (i * step))
    color = f"\033[38;2;{r};{g};{b}m"
    gradient.append(color + output[i])


print(''.join(gradient))
time.sleep(0.1)  #

# ------------------------------------------------------------------------------------------------

# ------------------------------------The Main Script----------------------------------------------


print("""
    Credits of this script goes to MUNASSER.
    Github : https://github.com/munasserr
    Linkedin : https://www.linkedin.com/in/munasser
    This script is working only on groups to scrape memebers and broadcast messages to them , Wait for more options in V2.0
      
    Please follow the Usage section on the repository [https://github.com/munasserr/PythonTeleMsgSender] for the best results.
""")


# get your api_id, api_hash
api_id = str(input('Enter your Telegram Api Id : '))
api_hash = str(input('Enter your Api Hash Key : '))


# your phone number
phone = str(input('Enter your phone number with country code [+02xxxxxxxxxxx] : '))

# creating a telegram session and assigning
# connecting and building the session
try:
    client = TelegramClient('session', api_id, api_hash)
    client.connect()

except Exception as e:
    raise Exception(f"Could not start a Telegram session [{e}], API Hash Key or Id is not valid ,Please follow the Usage section on the repository [https://github.com/munasserr/PythonTeleMsgSender]")

# logging in part
try:
    if not client.is_user_authorized():

        client.send_code_request(phone)

        # signing in the client
        client.sign_in(phone, input('Enter the login code you just received: '))

    print("You've Logged in successfully , Now You Can Start Broadcasting your messages")
except Exception:
    raise Exception("Invalid Phone Number or Login OTP ,Please follow the Usage section on the repository [https://github.com/munasserr/PythonTeleMsgSender]")

time.sleep(0.65)

# entring message
message = input("Enter Your Custom message you wanna braodcast : ")

time.sleep(0.5)
try:
    try:
        userId = int(input('Enter your User Id : '))
        user = client.get_input_entity(userId)
        access_hash = int(user.access_hash)

        user_peer = types.InputPeerUser(userId, access_hash)
        time.sleep(1)
        group_id = int(input('Enter The Targeted Group Id : '))
        members = client.get_participants(group_id, user_peer.CONSTRUCTOR_ID)
        
        # Extracting user IDs from the members
        user_ids = [member.id for member in members]

        print(f'Number Of Members Of That Group Is : {len(user_ids)}')
        time.sleep(1.5)

    except Exception as e:
        raise Exception(f"Could not extract members of that group : {e}")
        # Handle other unexpected errors

    
    
    for user_id in user_ids:
        receiver = InputPeerUser(user_id, client.get_input_entity(user_id).access_hash)
        
        try:
            # Sending message using Telegram client
            client.send_message(receiver, message, parse_mode='html')
            
            # Define a custom progress bar format with orange color
            progress_bar_format = orange_code + "{desc}: {percentage:3.0f}%|{bar}|" + reset_code

            # Iterate over the range with tqdm and print the progress bar line in orange
            for _ in tqdm(range(100), desc="Sending message to user {}".format(user_id), ncols=70, bar_format=progress_bar_format):
                time.sleep(0.002)  # Simulating some processing time

            # Print the message with the colored checkmark and orange message
            print("{} [{}{}] Message sent to user with ID {} | User #{} of {}{}".format(orange_code, green_code + checkmark, orange_code, user_id,user_ids.index(user_id)+1,len(user_ids), reset_code))

        except errors.TelegramError as te:
            # Handle Telegram-specific errors
            print(f"Telegram error while sending message to user {user_id}: {te}")
        except Exception as e:
            # Handle other unexpected errors
            print(f"An unexpected error occurred while sending message to user {user_id}: {e}")
except Exception as e:
    # Handle exceptions that occur outside the message sending loop
    raise Exception(f"An error occurred: {e}")


# disconnecting the telegram session
client.disconnect()