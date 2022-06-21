# this file will be used in order to return books
# it is used by the GUI
# the user has no direct contact with it
# last modified 12/12/2019 by Student ID: B915247

import database
from datetime import datetime
import time

log = []
log_id = []
m_log = []
checkout = []
checkin = []
# the lists that will be used for the formatting and the to return the book it includes the book's id, member's id and
# the checkout date and return date


def format_logfile():
    # used to format the logfile in order to make returning the books easier it breaks the log list, all lines of the
    # log file in the book ID, member log, the Checkout data and the check in date
    # the loop is used to categorize the data

    log = database.accessor_of_data("logfile.txt")
    for i in range(len(log)):
        if not (log[i] == ""):
            now_list = str(log[i]).split("|")
            log_id.append(now_list[0])
            m_log.append(now_list[1])
            checkout.append(now_list[2])
            checkin.append(now_list[3])
            database.resetdata()


def return_books(bid):
    # the logfile is updated with the latest information
    # used to check that the book has not been return as well as if it is the same book
    # timestamp is used to indicate what time it was returned
    # modified strings are created that will replace the existing ones
    # modifying the log
    # database_overwrite is used to modify the database
    # the variable m is used in order to inform the GUI if the return of the book was successful

    format_logfile()
    m = False
    for j in range(len(log_id)):
        if (str(log_id[j]).strip(" ") == str(bid).strip(" ")) and (str(checkin[j]).strip(" ").strip("\n") == "0"):
            adjust_database(bid)
            today = time.time()
            timestamp = datetime.fromtimestamp(today).strftime('%d-%m-%Y %H:%M')
            # the timestamp used to indicate the date and time the book came back
            old_line = "%s|%s|%s| 0" % (log_id[j], m_log[j], checkout[j])
            # the old line
            new_line = "%s|%s|%s| %s\n" % (log_id[j], m_log[j], checkout[j], timestamp)
            # the new lin replacing the old
            if j == (len(log) - 1):
                new_line = "%s|%s|%s| %s\n" % (log_id[j], m_log[j], checkout[j], timestamp)
            database.database_overwrite("logfile.txt", old_line, new_line)
            # updating the logfile
            m =True
            break

        else:
            print("The book was never loaned")
    return m


def adjust_database(book):
    # the database is reset in order for the data to be up to date
    # the list of all the books ids needed in order to make the procedure faster
    # prepares the database in order for the data about the book needed to be retrieved
    # this function is in charge of making sure that the database.txt is updated

    database.resetdata()
    bid = database.bookid

    for i in range(len(bid)):
        if str(bid[i]).strip(" ") == str(book).strip(" "):
            oldline = "%s|%s|%s|%s|%s\n" % (
                database.bookid[i], database.titles[i], database.authors[i], database.pdate[i], database.mid[i])
            # the old line
            print(oldline, "original value")
            linerep = "%s|%s|%s|%s| 0\n" % (
                database.bookid[i], database.titles[i], database.authors[i], database.pdate[i])
            if i == (len(bid) - 1):
                linerep = "%s|%s|%s|%s| 0" % (
                    database.bookid[i], database.titles[i], database.authors[i], database.pdate[i])
                # the new line
                print(linerep, "aftvalue")
            database.database_overwrite("database.txt", oldline, linerep)
            # updating database.txt
            break


def check_return():
    # checks the return function
    print(return_books(5))


if __name__ == "__main__":
    print("checking the return function")
    check_return()
    print("Checking the setup")
    print(log, "before format")
    format_logfile()
    print(log)
    print(len(log))
