# This file will be used to search for books, insert new ones
# delete the ones that the user want to get rid off
# and find the availability of a certain title
# it is used by the GUI
# the user has no direct contact with it
# last modified 12/12/2019 by Student ID: B915247
import database
from datetime import datetime
import time

# the lists that will hold the databases information in order to make it
# more organized and easier for the functions to access them

bid = []
title_list = []
author_list = []
pdate_list = []
mid_list = []


def reload():
    data = (database.accessor_of_data("database.txt"))
    # sorts the data retrieved from the database.txt file
    # it breaks it down to lists that comprise all the data of each individual book
    # it breaks the string into smaller elements

    for i in range(0, len(data)):
        now_list = str(data[i]).split("|")
        if len(now_list) > 1:
            print(now_list)
            bid.append(now_list[0])
            title_list.append(now_list[1])
            author_list.append(now_list[2])
            pdate_list.append(now_list[3])
            mid_list.append(now_list[4].strip("\n"))



def search(title):
    # the function that searches the database for copies of a certain title
    # it takes the title_list which is provided by the database file and checks if it is the same with the title we have
    # provided it with, if it is it takes the index and adds it in the list_of_copies and returns it back

    database.resetdata()
    reload()
    list_of_copies = []
    title_search = str(title)
    m = False
    for i in range(len(title_list)):
        if str(title_list[i]).lower().strip(" ") == str(title_search).lower().strip(" "):
            # the search parameter for checking the title needed
            list_of_copies.append(i)
            # the list of copies
            m = True
    if m:
        return list_of_copies
    else:
        return list_of_copies.append(-1)


def presenter():
    # presents the contents of the database
    # it outputs a string how the data looks like in the database that is then printed in the GUI
    # an algorithm that is in charge of removing any duplicates in the list generated is used to ensure that no
    # duplicates are going to be presented
    reload()
    books = " ID | Title | Author | Purchase Date | Member ID"
    book1 = []
    for i in range(0, len(bid)):
        value = ("%s | %s | %s | %s | %s" % (bid[i], title_list[i], author_list[i], pdate_list[i], mid_list[i]))
        book1.append(value)
        # a list of strings that keeps the data of all the books in the database
    # this set of nested loops ensures duplicates do not exist
    m = 0
    while m < len(book1):
        n = m + 1
        while n < len(book1):
            if book1[m] == book1[n]:
                del book1[n]
            else:
                n += 1
        m += 1

    for i in range(len(book1)):
        books = books + '\n' + book1[i]
    database.resetdata()
    return books


def certain_position_presenter(list_copies):
    # it is used to present the results of the search function
    # it outputs a string how the data looks like in the database that is then printed in the GUI
    # an algorithm that is in charge of removing any duplicates in the list generated is used to ensure that no
    # duplicates are going to be presented
    reload()
    list_of_books = " ID | Title | Author | Purchase Date | Member ID"
    list_of_books1 = []
    if int(list_copies[0]) == -1:
        print("Nothing found")
    else:
        for i in range(len(list_copies)):
            value1 = ("%s | %s | %s | %s | %s" % (
                bid[list_copies[i]], title_list[list_copies[i]], author_list[list_copies[i]],
                pdate_list[list_copies[i]],
                mid_list[list_copies[i]]))
            list_of_books1.append(value1)
    # a list of strings that keeps the data of the copies of a title
    # this set of nested loops ensures duplicates do not exist
    f = 0
    while f < len(list_of_books1):
        x = f + 1
        while x < len(list_of_books1):
            if list_of_books1[f] == list_of_books1[x]:
                del list_of_books1[x]
            else:
                x += 1
        f += 1

    for i in range(len(list_of_books1)):
        list_of_books = list_of_books + '\n' + list_of_books1[i]
    return list_of_books


def availability(title):
    # checks if a book is available, it uses the search function to get a list of all copies of a book
    # then it goes through the list and tries to find how many copies of a book are there and which are available
    # it outputs true if a copy is true
    database.resetdata()
    reload()
    x = False
    position = search(title)
    if position is None:
        return False
    try:
        if len(position):
            for i in range(len(position)):
                if int(mid_list[position[i]]) == 0:
                    # checking if a book is available
                    x = True
                    break
                else:
                    x = False
        return x
    except ValueError:
        print("The book was not found")
    database.resetdata()


def book_deletion(title):
    # this function will be used to delete all the copies of a book as well as the times it has been loaned
    # we use search to find all the copies of the book that are in the library
    # an intermediary step is used to avoid a mistaken deletion
    # this part is in charge of deleting the copies of a title
    # we use a loop to delete all the titles that exist in the database
    # the same is done in the loans
    reload()
    copies = search(title)
    if copies is not None:
        certain_position_presenter(copies)
        logfile = database.accessor_of_data("logfile.txt")
        for j in range(len(copies)):
            databaseline = "%s|%s|%s|%s|%s" % (
                bid[copies[j]], title_list[copies[j]], author_list[copies[j]], pdate_list[copies[j]],
                mid_list[copies[j]])
            # it produces the strings of the database which are to be deleted
            print(databaseline)
            database.data_terminator(databaseline, "database.txt")
            # it deletes this lines from the database
            for i in range(len(logfile)):
                now = logfile[i]
                now2 = now.split("|")
                if str(now2[0]).strip(" ") == str(bid[copies[j]]).strip(" "):
                    linetoremove = "%s|%s|%s|%s" % (now2[0], now2[1], now2[2], now2[3])
                    # it produces the strings of the logfile which are to be deleted
                    database.data_terminator(linetoremove, "logfile.txt")
                    # it deletes this lines from the logfile
    else:
        print("Book not found")
    database.resetdata()


def book_insertor(book):
    # the function is used to insert new books in the database file
    # we take the three aspects that comprise the book; title, author and purchase date
    # then we use the database modifier to add the new book

    reload()
    today = time.time()
    timestamp = datetime.fromtimestamp(today).strftime('%d-%m-%Y')
    # it uses the current date as a purchase day, as it is that day that the book is finally
    # used by the library
    book_id = new_id()
    # produces a new id for the book
    pt1 = '  %s | ' % book_id
    new_book = pt1 + str(book) + ' | ' + str(timestamp) + ' | 0 \n'
    database.database_modifier("database.txt", new_book)
    database.resetdata()


def complete_search(titles):
    # it brings all components to makes searching possible
    m = search(titles)
    if m == -1 or m is None:
        # checks if search was successful
        print("Book not Found")
        database.resetdata()
    else:
        return certain_position_presenter(m)


def new_id():
    # the function is used to create new book ids for new books
    # it scans all the ids the larger one and then increments and gives the new id
    reload()
    temp = 0
    for i in range(1, len(bid)):
        if temp < int(bid[i]):
            temp = int(bid[i])

    temp = temp + 1
    return temp


def check_search():
    # checks that the voyager1 function works
    print(complete_search("The Art of War"))


if __name__ == "__main__":
    print(check_search(), " test")
    print(presenter())
