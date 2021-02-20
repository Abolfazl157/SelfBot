# DocString ...


import redis
import configparser
from db import r
from pyrogram import Client , errors
from pyrogram.errors import RPCError


# Read Config File
config = configparser.ConfigParser()
config.read("config.ini")
c = config["Config"]


def main():
    plugins = dict(root="plugins")
    API_ID = int(c["3750984"])
    API_HASH = c["254bb38ccc890edd096e7260a0fc8567"]

    if r.get("password") == None:
        r.set("password", c["DEFAULT_PASSWORD"])
        password = c["DEFAULT_PASSWORD"]
    else:
        password = r.get("password")

    Client(session_name="selfbot", api_id=API_ID, api_hash=API_HASH , plugins=plugins).run()
    if not r.get("autodeltime"): r.set("autodeltime", "10")


if __name__ == "__main__":
    main()


