# this file will be used in order to list books by popularity
# it is used by the GUI
# the user has no direct contact with it
# last modified 12/12/2019 by Student ID: B915247

import numpy as np
import matplotlib.pyplot as plt
import database
from matplotlib.figure import Figure

plt.rcdefaults()

# the modules imported in order to make the retrieval of data possible but also to plot the graph
plt.rcdefaults()

book_id = []
amount = []
title = []

final_amount = []
database.sort_data_to_present_database(database.accessor_of_data("database.txt"))
database_ids = database.book_id_giver()
database_titles = database.book_titles()

final_amount2 = []
final_title = []


# the lists used for sorting the data as well as importing the values from the database


def formattor():
    # the function formattor is used in order to get the list of of ids from the logfile
    # that way it is know which books are loaned and how many times they have been
    initial_database = database.accessor_of_data("logfile.txt")
    for i in range(len(initial_database)):
        if not initial_database[i] == "":
            now = str(initial_database[i]).split("|")
            book_id.append(now[0])


def concetrator():
    # the function concetrator is used in order to know how many times a certain book has been loaned
    # this is done by using the list of all the book ids from the database file and using them
    # the amount of times has actually the same index of as the list of IDs so it is easier to find them

    formattor()
    for i in range(len(database_ids)):
        x = 0
        for j in range(len(book_id)):
            if str(database_ids[i]).strip(" ") == str(book_id[j]).strip(" "):
                x = x + 1
        amount.append(x)


def test_the_formatting():
    # it tests whether the formatting system works
    formattor()
    print(book_id)


def rearrangor():
    # the rearrangor function is used in order to take the book IDs and find the titles
    # it is also used in order to find books with the same title and add the amount of times loaned together,
    # as they are different copies
    # it is also in charge to remove duplicate titles and amounts

    concetrator()
    # this loop checks if different copies exist, if they do it presents them together, else individually
    try:
        for i in range(len(database_titles)):
            for j in range(len(database_titles)):
                if i != j:
                    if database_titles[i] == database_titles[j] and database_ids[i] != database_ids[j]:
                        title.append(database_titles[i])
                        final_amount.append(int(amount[i] + amount[j]))
                    if database_ids[i] == database_ids[j]:
                        title.append(database_titles[i])
                        final_amount.append(int(amount[i]))

    except ValueError:
        print("End of loop")

    # gets rid of the duplicate values
    g = 0
    while g < len(title):
        r = g + 1
        while r < len(title):
            if title[g] == title[r]:
                del title[r]
                del final_amount[r]
            else:
                r += 1
        g += 1


def sorter():
    # the sorter function is in charge of sorting the list of titles in ascending order regarding the amount of times
    # the title has been loaned

    for i in range(len(final_amount)):
        for j in range(len(final_amount)):
            if final_amount[i] > final_amount[j]:
                m = final_amount[i]
                n = title[i]
                final_amount[i] = final_amount[j]
                final_amount[j] = m
                title[i] = title[j]
                title[j] = n

    if len(final_amount) > 9:
        m = len(final_amount) - 10
        del final_amount[len(final_amount) - m:]
        del title[len(title) - m:]


def plotter():
    # the plotter function is in charge of using the matplotlib in order to make a bar graph from the data collected
    # by the database.txt and logfile.txt
    rearrangor()
    sorter()
    objects = title
    y_pos = np.arange(len(objects))

    plt.bar(y_pos, final_amount, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.tick_params(axis='x', which='major', labelsize=10, labelrotation=40)
    plt.ylabel('Usage')
    plt.title('Books by popularity')
    # setting up the figure that will be used in the menu.py
    fig = Figure(figsize=(3, 3), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_title("Books by popularity")
    ax.set_xlabel('Usage')
    ax.set_yticks(range(len(title)))
    ax.set_yticklabels(title)
    ax.autoscale(tight=title)
    ax.tick_params(axis='y', labelsize=6)
    ax.barh(y_pos, final_amount, align='center', alpha=0.5)
    # returning the figure
    return fig


def testplotter():
    # tests that the plotting capability works properly
    plotter()


def reformattor():
    # reformat the list in order to be ready for next time
    formattor()
    database.resetdata()


if __name__ == "__main__":
    print("testing the formatting")
    test_the_formatting()
    print("the plotter needs to be tested by the GUI")
