# this file will be used in order to checkout books, it is used by the GUI
# the user has no direct contact with it
# last modified 12/12/2019 by Student ID: B915247

import database
from datetime import datetime
import time

# the files that we will need to built the checkout function
linerep = ""
oldline = ""


# the functions that we will need to use

def checkout(bookidm, memberid):
    m = False
    # the function takes the book's and the member's ID
    # the database module is used to organize the data and make finding the id and status of the book easier
    # the function keeps a list of all book IDs, it is used to check if the book is correct
    # checks that the member's ID is correct, by how long it is and if it is only digits
    # if the member's id and the book' ID are correct, the function proceeds to delete
    # it modifies both the log and the database file
    # it then resets the values in the database.py file and shuts down
    # the variable m is used in order to inform the GUI if the loan of the book was successful
    # or unsuccessful

    database.resetdata()  # used to ensure that data is up to date
    initset = database.book_id_giver()
    false_bid = True
    id = memberid
    linerep = ''
    st = database.member_id()
    if len(str(id)) == 4 and str(id).isdigit():
        id = int(memberid)
        # the id of the member
        for i in range(len(initset)):
            if str(initset[i]).strip(" ") == str(bookidm).strip(" "):
                # checking that the id is the same
                if int(st[i]) == 0:
                    today = time.time()
                    timestamp = datetime.fromtimestamp(today).strftime('%d-%m-%Y %H:%M')
                    # the timestamp used to indicate the date and time the book was loaned
                    msg = " %s | %s | %s | 0\n" % (bookidm, id, timestamp)
                    if i < len(st):
                        linerep = "%s|%s|%s|%s| %s\n" % (
                            database.bookid[i], database.titles[i], database.authors[i], database.pdate[i], id)
                    if i == (len(st) - 1):
                        linerep = "%s|%s|%s|%s| %s\n" % (
                            database.bookid[i], database.titles[i], database.authors[i], database.pdate[i], id)
                    # the replacing line
                    oldline = "%s|%s|%s|%s| 0" % (
                        database.bookid[i], database.titles[i], database.authors[i], database.pdate[i])
                    # the line to be replaced
                    database.database_modifier("logfile.txt", msg)
                    database.database_overwrite("database.txt", oldline, linerep)

                    false_bid = False
                    m = True
                    break
                elif not (int(st[i]) == 0) and i == len(initset):
                    print("Book already in use")
    else:
        print("Invalid Member ID")
    if false_bid:
        print("False Book ID")
    database.resetdata()
    return m


def check_checkout():
    # checks that the checkout function works properly
    m = checkout(9, 1234)
    print(m, "True= success, False= failure")
    print(linerep, " Replacement line")
    print(oldline, "the line to be replaced")


if __name__ == "__main__":
    check_checkout()
