from webserver import keep_alive
import requests

channelID =1000445903863304307
headers = {
    "authorization":
    "4ofSoP8baBkES8KjSIECGgTkXto"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
