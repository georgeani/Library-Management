# this file is the GUI that the user uses to interact with the program
# last modified 12/12/2019 by Student ID: B915247

from tkinter import *
import sys
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# the libraries and module that need to be imported
# in order to make the GUI function properly

window = Tk()
window.title("Library Logistics System")
window.geometry("2000x2000")
window.configure(background="black")
search_mes = Label(window, text="Please input the title of the book you are looking for", fg="white", bg="black")
return_mes = Label(window, text="Please input the ID of the book you want to return", fg="white", bg="black")
delete_mes = Label(window, text="Please input the tittle of the book you want to delete", fg="white", bg="black")
add_mes = Label(window, text="Please input the required information to add a new book", fg="white", bg="black")
co_mes = Label(window, text="Please input the book and student id", fg="white", bg="black")
co_member = Label(window, text="User ID:", fg="white", bg="black")
co_book = Label(window, text="Book ID:", fg="white", bg="black")
availability_mes = Label(window, text="Please write the title of the book you want to check", fg="white", bg="black")


# the initial step of the GUI declaring it includes the
# messages that come up after a button has been activated
# it also includes the title of the window and it's size
# every function also hides the button
# that are associated with different functions


def search():
    # this function is activated when the search button is clicked
    # this function shows up the search box, the button and a message explaining what to do
    search_mes.place(relx=0.05, rely=0.23, anchor=NW)
    searchbox.place(relx=0.05, rely=0.26, anchor=NW, height=25, width=150)
    initialize_search.place(relx=0.15, rely=0.26, anchor=NW, height=25, width=50)
    # closes all the widgets not associated with this function
    deletebox.place_forget()
    initialize_del.place_forget()
    initialize_add.place_forget()
    co_mid.place_forget()
    co_bid.place_forget()
    return_entry.place_forget()
    initialize_return.place_forget()
    return_mes.place_forget()
    delete_mes.place_forget()
    add_mes.place_forget()
    co_book.place_forget()
    co_member.place_forget()
    search_result.place_forget()
    availability_mes.place_forget()
    availability_entry.place_forget()
    initialize_st.place_forget()
    stres.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    datef.place_forget()
    date.place_forget()
    initialize_add.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    initialize_add.place_forget()
    confirm_del.place_forget()
    co_mes.place_forget()
    present_books.place_forget()
    return_final_mes.place_forget()
    checkout_final_mes.place_forget()


def search_pt2():
    import booksearch
    # this function is activated by the initialize_search
    # button and does the search, if the title is true it outputs
    # the results, otherwise it does nothing
    input1 = searchbox.get()
    data = booksearch.complete_search(input1)
    print(data)
    if data is not None:
        search_result.config(text=data)
        search_result.place(relx=0.5, rely=0.2, anchor=CENTER)


def killer():
    # kills the entire program, activated by the quit button
    quit()
    window.quit()


def deletion():
    # it is in charge of showing the deletion entry
    # box and the the message explaining what to do as well as the
    # button to submit the title
    delete_mes.place(relx=0.05, rely=0.35, anchor=NW)
    deletebox.place(relx=0.05, rely=0.38, anchor=NW, height=25, width=150)
    initialize_del.place(relx=0.15, rely=0.38, anchor=NW, height=25, width=50)
    # closes all the widgets not associated with this function
    searchbox.place_forget()
    initialize_search.place_forget()
    initialize_add.place_forget()
    co_mid.place_forget()
    co_bid.place_forget()
    initialize_co.place_forget()
    return_entry.place_forget()
    initialize_return.place_forget()
    search_mes.place_forget()
    return_mes.place_forget()
    add_mes.place_forget()
    co_member.place_forget()
    co_book.place_forget()
    search_result.place_forget()
    availability_mes.place_forget()
    availability_entry.place_forget()
    initialize_st.place_forget()
    stres.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    datef.place_forget()
    date.place_forget()
    initialize_add.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    initialize_add.place_forget()
    co_mes.place_forget()
    present_books.place_forget()
    return_final_mes.place_forget()
    checkout_final_mes.place_forget()


def deletionpt2():
    import booksearch
    # it is in charge in testing if the title name submitted is correct
    # if it is it shows an entry message and asks if the deletion should proceed
    titledel = deletebox.get()
    if titledel != '' and booksearch.complete_search(titledel) is not None:
        # testing that the input is correct
        inputm = "Is this the book you are looking for?"
        message.config(text=inputm + '\n' + booksearch.complete_search(titledel))
        transfer.config(text=titledel)
        message.place(relx=0.5, rely=0.2, anchor=CENTER)
        confirm_del.place(relx=0.4, rely=0.3, anchor=CENTER)
        no_button.place(relx=0.6, rely=0.3, anchor=CENTER)


def deletionpt3():
    import booksearch
    # it executes the deletion and closes all boxes and search boxes
    mes = transfer.cget("text")
    booksearch.book_deletion(str(mes))
    print(mes)
    kill_all_hiden()


def addition():
    # it is in charge of showing the addition entry box
    # and the the message explaining what to do as well as the
    # button to submit the title
    add_mes.place(relx=0.05, rely=0.5, anchor=NW)
    authorf.place(relx=0.02, rely=0.54, anchor=NW)
    author.place(relx=0.05, rely=0.54, anchor=NW, height=25, width=100)
    titlef.place(relx=0.02, rely=0.58, anchor=NW)
    title.place(relx=0.05, rely=0.58, anchor=NW, height=25, width=100)
    initialize_add.place(relx=0.05, rely=0.64, anchor=NW, height=25, width=50)
    # closes all the widgets not associated with this function
    searchbox.place_forget()
    initialize_search.place_forget()
    deletebox.place_forget()
    initialize_del.place_forget()
    co_mid.place_forget()
    co_bid.place_forget()
    initialize_co.place_forget()
    return_entry.place_forget()
    initialize_return.place_forget()
    search_mes.place_forget()
    return_mes.place_forget()
    delete_mes.place_forget()
    co_member.place_forget()
    co_book.place_forget()
    search_result.place_forget()
    availability_mes.place_forget()
    availability_entry.place_forget()
    initialize_st.place_forget()
    stres.place_forget()
    confirm_del.place_forget()
    co_mes.place_forget()
    present_books.place_forget()
    return_final_mes.place_forget()
    checkout_final_mes.place_forget()


def additionpt2():
    # it checks if the input is valide, the boxes were not empty.
    # If it is, it reads the input and produces a
    # warning message regarding if the addition should go ahead
    authorin = author.get()
    titlein = title.get()
    if authorin != '' and titlein != '':
        n = "%s | %s " % (titlein, authorin)
        m = "%s by %s " % (titlein, authorin)
        inputm = "Is this the book you are looking for"
        transfer.config(text=n)
        message.config(text=inputm + '\n' + m)
        message.place(relx=0.5, rely=0.2, anchor=CENTER)
        confirm_add.place(relx=0.4, rely=0.3, anchor=CENTER)
        no_button.place(relx=0.6, rely=0.3, anchor=CENTER)


def additionpt3():
    import booksearch
    # it executes the book addition
    mes = transfer.cget("text")
    booksearch.book_insertor(mes)
    print(mes)
    kill_all_hiden()


def checkout():
    # it is in charge of showing the checkout entry boxes
    # and the the message explaining what to do as well as the
    # button to submit the book and member's id
    co_mes.place(relx=0.94, rely=0.43, anchor=E)
    co_member.place(relx=0.84, rely=0.46, anchor=E)
    co_mid.place(relx=0.88, rely=0.46, anchor=E, height=25, width=50)
    co_book.place(relx=0.84, rely=0.5, anchor=E)
    co_bid.place(relx=0.88, rely=0.5, anchor=E, height=25, width=50)
    initialize_co.place(relx=0.95, rely=0.5, anchor=E, height=25, width=100)
    # closes all the widgets not associated with this function
    initialize_add.place_forget()
    searchbox.place_forget()
    initialize_search.place_forget()
    deletebox.place_forget()
    initialize_del.place_forget()
    return_entry.place_forget()
    initialize_return.place_forget()
    search_mes.place_forget()
    return_mes.place_forget()
    delete_mes.place_forget()
    add_mes.place_forget()
    search_result.place_forget()
    availability_mes.place_forget()
    availability_entry.place_forget()
    initialize_st.place_forget()
    stres.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    datef.place_forget()
    date.place_forget()
    initialize_add.place_forget()
    confirm_del.place_forget()
    present_books.place_forget()
    return_final_mes.place_forget()


def checkoutpt2():
    import bookcheckout
    # it makes sure that input is correct and then loans the book
    # if the loan is successful it outputs a message confirming that
    # if not it does the exact same thing
    # if the input is incorrect it does nothing
    mid = co_mid.get()
    bid = co_bid.get()

    if mid != '' and bid != '' and len(mid) == 4 and str(mid).isdigit() and str(bid).isdigit():
        x = bookcheckout.checkout(int(bid), int(mid))
        if x:
            checkout_final_mes.config(text="The book was successfully loaned")
        else:
            checkout_final_mes.config(text="The book is loaned")
        checkout_final_mes.place(relx=0.5, rely=0.2, anchor=CENTER)


def return_book():
    # it is in charge of showing the return entry box and the the message
    # explaining what to do as well as the
    # button to submit the book's id
    return_mes.place(relx=0.98, rely=0.61, anchor=E)
    return_entry.place(relx=0.885, rely=0.65, anchor=E, height=25, width=50)
    initialize_return.place(relx=0.8945, rely=0.7, anchor=E, height=25, width=70)
    # this part closes all the widgets not associated with return_book()
    searchbox.place_forget()
    initialize_search.place_forget()
    deletebox.place_forget()
    initialize_del.place_forget()
    initialize_add.place_forget()
    co_mid.place_forget()
    co_bid.place_forget()
    initialize_co.place_forget()
    search_mes.place_forget()
    delete_mes.place_forget()
    add_mes.place_forget()
    co_member.place_forget()
    co_book.place_forget()
    search_result.place_forget()
    availability_mes.place_forget()
    availability_entry.place_forget()
    initialize_st.place_forget()
    stres.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    datef.place_forget()
    date.place_forget()
    initialize_add.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    initialize_add.place_forget()
    confirm_del.place_forget()
    co_mes.place_forget()
    present_books.place_forget()
    checkout_final_mes.place_forget()


def return_bookpt2():
    import bookreturn
    # it makes sure that input is correct and then returns the book
    # if the return is successful it outputs a message confirming that
    # if not it does the exact same thing
    m = return_entry.get()

    if m != '' and str(m).isdigit():
        m = bookreturn.return_books(str(m))
        if m:
            return_final_mes.config(text="The book was successfully returned")
        else:
            return_final_mes.config(text="The book was not loaned")
        return_final_mes.place(relx=0.5, rely=0.2, anchor=CENTER)


def popular():
    import booklist
    # it produces a graph that shows the top 10 most popular books
    # in order to close the graph the small quit button needs to be pressed
    # prepares the canvas and places it
    fig = booklist.plotter()
    pop = FigureCanvasTkAgg(fig, master=window)
    pop.draw()
    pop.get_tk_widget().place(relx=0.5, rely=0.5, anchor=CENTER, height=500, width=920)

    def quitgraph():
        pop.get_tk_widget().place_forget()
        quit_graph.place_forget()

    quit_graph = Button(window, text="quit", command=quitgraph)
    quit_graph.place(relx=0.05, rely=0.78, anchor=NW, height=25, width=100)
    # closes all the widgets not associated with this function
    booklist.reformattor()
    searchbox.place_forget()
    initialize_search.place_forget()
    deletebox.place_forget()
    initialize_del.place_forget()
    initialize_add.place_forget()
    co_mid.place_forget()
    co_bid.place_forget()
    initialize_co.place_forget()
    return_entry.place_forget()
    initialize_return.place_forget()
    search_mes.place_forget()
    return_mes.place_forget()
    delete_mes.place_forget()
    add_mes.place_forget()
    co_member.place_forget()
    co_book.place_forget()
    search_result.place_forget()
    availability_mes.place_forget()
    availability_entry.place_forget()
    initialize_st.place_forget()
    stres.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    datef.place_forget()
    date.place_forget()
    initialize_add.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    initialize_add.place_forget()
    confirm_del.place_forget()
    co_mes.place_forget()
    present_books.place_forget()
    return_final_mes.place_forget()
    checkout_final_mes.place_forget()


def show_books():
    import booksearch
    # it shows all the books that the library has
    present_books.config(text=booksearch.presenter())
    present_books.place(relx=0.5, rely=0.5, anchor=CENTER)
    # closes all the widgets not associated with this function
    # your code
    searchbox.place_forget()
    initialize_search.place_forget()
    deletebox.place_forget()
    initialize_del.place_forget()
    initialize_add.place_forget()
    co_mid.place_forget()
    co_bid.place_forget()
    initialize_co.place_forget()
    return_entry.place_forget()
    initialize_return.place_forget()
    search_mes.place_forget()
    return_mes.place_forget()
    delete_mes.place_forget()
    add_mes.place_forget()
    co_book.place_forget()
    co_member.place_forget()
    search_result.place_forget()
    availability_mes.place_forget()
    availability_entry.place_forget()
    initialize_st.place_forget()
    stres.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    datef.place_forget()
    date.place_forget()
    initialize_add.place_forget()
    confirm_del.place_forget()
    co_mes.place_forget()
    return_final_mes.place_forget()
    checkout_final_mes.place_forget()


def availability():
    # it is in charge of showing the availability entry box and the
    # the message explaining what to do as well as the
    # button to submit the book's title
    availability_mes.place(relx=0.98, rely=0.23, anchor=E)
    initialize_st.place(relx=0.9, rely=0.3, anchor=E, height=25, width=100)
    availability_entry.place(relx=0.9, rely=0.26, anchor=E, height=25, width=100)
    # closes all the widgets not associated with this function
    searchbox.place_forget()
    initialize_search.place_forget()
    deletebox.place_forget()
    initialize_del.place_forget()
    initialize_add.place_forget()
    co_mid.place_forget()
    co_bid.place_forget()
    initialize_co.place_forget()
    return_entry.place_forget()
    initialize_return.place_forget()
    search_mes.place_forget()
    return_mes.place_forget()
    delete_mes.place_forget()
    add_mes.place_forget()
    co_member.place_forget()
    co_book.place_forget()
    search_result.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    datef.place_forget()
    date.place_forget()
    initialize_add.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    initialize_add.place_forget()
    confirm_del.place_forget()
    co_mes.place_forget()
    present_books.place_forget()
    return_final_mes.place_forget()
    checkout_final_mes.place_forget()


def availabilitypt2():
    import booksearch
    # it is in charge of checking if the input is correct if it exists and the field is not empty
    # then it outputs a message that declares if the book is available or not
    input1 = availability_entry.get()
    data = booksearch.availability(input1)
    if data and input1 != '':
        stres.config(text='The book "%s" is available' % input1)
        stres.place(relx=0.5, rely=0.2, anchor=CENTER)
    elif data is False and input1 != '':
        stres.config(text='The book "%s" is unavailable' % input1)
        stres.place(relx=0.5, rely=0.2, anchor=CENTER)


def kill_all_hiden():
    # it is charge of killing all the hidden widgets
    searchbox.place_forget()
    initialize_search.place_forget()
    deletebox.place_forget()
    initialize_del.place_forget()
    initialize_add.place_forget()
    co_mid.place_forget()
    co_bid.place_forget()
    initialize_co.place_forget()
    return_entry.place_forget()
    initialize_return.place_forget()
    search_mes.place_forget()
    return_mes.place_forget()
    delete_mes.place_forget()
    add_mes.place_forget()
    co_book.place_forget()
    co_member.place_forget()
    search_result.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    datef.place_forget()
    date.place_forget()
    initialize_add.place_forget()
    availability_mes.place_forget()
    initialize_st.place_forget()
    availability_entry.place_forget()
    stres.place_forget()
    add_mes.place_forget()
    authorf.place_forget()
    author.place_forget()
    titlef.place_forget()
    title.place_forget()
    initialize_add.place_forget()
    message.place_forget()
    confirm_add.place_forget()
    no_button.place_forget()
    confirm_del.place_forget()
    co_mes.place_forget()
    present_books.place_forget()
    return_final_mes.place_forget()
    checkout_final_mes.place_forget()


def restart_the_program():
    # it restarts the entire program, used to make sure that all systems behave accordingly
    python = sys.executable
    os.execl(python, python, * sys.argv)


# the entry buttons and fields of all the functions as well as the buttons that activate them
no_button = Button(window, text="Cancel", highlightcolor="Black", fg="Black", command=kill_all_hiden)
transfer = Label(window)  # used in order to transfer values from one function to another

title = Label(window, text="Welcome to the Library management system", font=("Helvetica", 16), fg="white", bg="black")
title.place(relx=0.5, rely=0.05, anchor=CENTER)

search = Button(window, text="Search a title", highlightcolor="Black", fg="Black", command=search)
search.place(relx=0.05, rely=0.2, anchor=NW, height=25, width=100)

availabilityb = Button(window, text="Availability", highlightcolor="Black", command=availability)
availabilityb.place(relx=0.90, rely=0.2, anchor=E, height=25, width=100)

quitter = Button(window, text="Quit", command=killer)
quitter.place(relx=0.05, rely=0.05, anchor=NW, height=25, width=100)

deleteb = Button(window, text="Delete a title", command=deletion)
deleteb.place(relx=0.05, rely=0.32, anchor=NW, height=25, width=100)
confirm_del = Button(window, text="Confirm", command=deletionpt3)

importb = Button(window, text="Add a book", command=addition)
importb.place(relx=0.05, rely=0.46, anchor=NW, height=25, width=100)

checkoutb = Button(window, text="Check Out", command=checkout)
checkoutb.place(relx=0.90, rely=0.4, anchor=E, height=25, width=100)

returnb = Button(window, text="Return a Book", command=return_book)
returnb.place(relx=0.9, rely=0.57, anchor=E, height=25, width=100)

popularb = Button(window, text="Popularity ratings", command=popular)
popularb.place(relx=0.05, rely=0.75, anchor=NW, height=25, width=100)

bookb = Button(window, text="See all books", command=show_books)
bookb.place(relx=0.90, rely=0.75, anchor=E, height=25, width=100)
present_books = Label(window, font=18, fg="white", bg="black")

searchbox = Entry(window)
initialize_search = Button(window, text="Search", highlightcolor="Black", fg="Black", command=search_pt2)
search_result = Label(window, font=16, fg="white", bg='black')

initialize_del = Button(window, text="Delete", highlightcolor="Black", fg="Black", command=deletionpt2)
deletebox = Entry(window)

initialize_add = Button(window, text="Add", highlightcolor="Black", fg="Black", command=additionpt2)
author = Entry(window)
authorf = Label(window, text="Author:", fg="white", bg='black')
title = Entry(window)
titlef = Label(window, text="Title:", fg="white", bg='black')
date = Entry(window)
datef = Label(window, text="Date:", fg="white", bg='black')
confirm_add = Button(window, text="Yes", highlightcolor="Black", fg="Black", command=additionpt3)
message = Label(window, font=16, fg="Black", bg="black")

initialize_co = Button(window, text="Check-Out", highlightcolor="Black", fg="Black", command=checkoutpt2)
co_mid = Entry(window)
co_bid = Entry(window)
checkout_final_mes = Label(window, font=16, fg="white", bg='black')

initialize_return = Button(window, text="Return", highlightcolor="Black", fg="Black", command=return_bookpt2)
return_entry = Entry(window)
return_final_mes = Label(window, font=16, fg="white", bg='black')

initialize_st = Button(window, text="Check", highlightcolor="Black", fg="Black", command=availabilitypt2)
stres = Label(window, font=16, fg="white", bg="black")
availability_entry = Entry(window)

restart = Button(window, text="Restart", highlightcolor="Black", fg="Black", command=restart_the_program)
restart.place(relx=0.83, rely=0.05, anchor=NW, height=25, width=100)

window.mainloop()
