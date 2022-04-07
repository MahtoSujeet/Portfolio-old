from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 5992694
    API_HASH = "0db6273991952a8f57a184bd49696e76"
    # the name to display in your alive message
    ALIVE_NAME = "Sujeet"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://oqdjwspsskukmv:ff9b5698c86867f5ddd33f605308be8b243e4d4003221b47e7fce2b7c65eb048@ec2-34-230-117-165.compute-1.amazonaws.com:5432/deb12d3gt0rueo"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOLQBuxbEperF9-VZDmrOqi5eWMOfvLvUwaa7em-uq799-KG0T9mnCmFUyqwUTAyJVtfKR1vPECdMKTogS3HHOj_f91N97kcxtH0EX0O-f1qb3ll25pubzMsKmupwtJDBljrXPb_0vHRNfSrP46xbcfjCvRGp84C7Azo0oKwdR7btPqskU8FRkGu2wWBd4y7HGHcA7GUJqmfDh5LihnUMe4cNEyOVoaJc3kiqHwdT37YbLJDv5JGVy7CGWgGVSbZ9uTd_EdMH-K2UHNGXnmJfUxFosJ1SCjOTUibflkdelB8pTwysWUuYcjz8POIgfnBHJp7kUo6wvGPAJuu08ayqJYEq4gA="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "1936742408:AAFDpLHJt6VX0B8ds4pY0n5IGHMpCQQSybA"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001576544273
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
