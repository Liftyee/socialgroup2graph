import instagram_private_api
import json
import codecs
import datetime
import functions


def main():
    uname = input("Username: ")
    pword = input("Password: ")
    log(uname, pword)
    writeCSV("username")

main()