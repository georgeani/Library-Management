# Library Management

This was my first full Python Project. It is a library management software that uses a .txt files as a databasse. It does not utilize a SQL database at all.

## General Information

This library Management System was created to be as easy to use as possible by the end-user.
To do that, the application uses a large window, I would advise enlarging the window to cover the entire screen.
The program uses only one page where all functionality takes place in order to be simpler for the user.
Also, most of the buttons and the entry boxes for a specific functionality are hidden and activated only when the button for that specific functionality is triggered.

When you switch functionalities, the widgets specified for another function are hidden.

As for the functions, the system can perform. It can present all the library books, delete a book, add a new one,
register loans and returns of books as well as search for a specific title.
Moreover, it can produce a graph showing the 10 most popular books in the library.

Furthermore, if the user tries to search a title that does not exist or get the availability of it nothing will happen,
the system has been programmed to not react in this kind of input. If the user tries to loan a book that does not exist in the databas,
he will get a message that it is in loan andif he tries to return it, he will receive a message that the book was never loaned.
The loan and return function will return a message if the return or loan was successful or not.

Regarding the presentation, the search function presents the results at the centre of the page, the same is done for the "see books" and the "availability" function.
The search function can handle search requests if the title is like one that exists in the database,
that means that only the letter order needs to be the.

Regarding, the deletion and book insertion functions in the middle of the page there is a message asking them if they want to proceed with the removal or insertion of a new book.
Regardless of the decision, all widgets associated with these actions are hidden.
Another feature is that the deletion function also deletes every loan of that book from the logfile.txt, as such the user does not have to do it manually.
Regarding the popularity function, it produces a graph with the 10 most popular books in ascending order.
In order to close the graph, the button quit below popularity must be used. This allows the graph to update every time a new entry is made.
For the function to work properly the 'Popularity ratings' button needs to be pressed once,
then press quit and press the 'Popularity ratings' button again.

For the program to run smoothly after using the delete, add, check out and return function the restart button must be pressed.
It will automatically restart the program without the user's input.
