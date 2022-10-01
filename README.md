Lab 4 – Databases and Networking in Python
These are the tasks for the 4th lab. Before you start this lab remember that cheating is not
acceptable in any form.
Requirements:
1. Read the tasks carefully, try to follow a description of tasks.
2. You should use only those topics that were covered at lectures. If you use something
that we have not considered yet and cannot explain it, then your mark might be
reduced or your work can be considered as cheating.
3. Do not forget to comment your code and make a user friendly program.
4. Use .py extension to upload your file(s) to moodle.astanait.edu.kz, please upload up to
4 files only.
Tasks (static for all the coming labs, outputs must be readable and beautiful)
Please, create sensible class and variable names and follow the naming conventions. For any
output use a string formatting. e.g. f“...”, “...”.format(...), “...% ” % (...).
Use try-except to deal with errors and avoid program crush.
Try to integrate classes with asyncio (if you are not happy with asyncio, see these python
libraries: threading, multiprocessing, selectors and coroutine.future. threading will be easier and
close in meaning to asyncio, but not faster)
These links are for asyncio library, “kind of” tutorials (but not the best ones)
https://docs.python.org/3.6/library/asyncio-protocol.html#tcp-echo-client-protocol
https://docs.python.org/3.6/library/asyncio-protocol.html#tcp-echo-server-protocol
https://docs.python.org/3/library/asyncio-task.html
The task [80%]
Your task is to create a chat server that accepts several connections from chat clients. The
idea is to create a chat conference where users send broadcast messages (one-to-all, kind of
WhatsApp group). When a user sends a message the user name should appear next to the
message. You can consider that usernames are all unique. Server should save the log of all
the incoming messages in a database in case if a user asks for the log of his/her messages.
Challenge Task 20%
Give users a possibility to send private messages to each other. You can do it this way:
On client side sending message: /private to username_here message_content.
On server side check if the message is starting from /private word and search for this person in
your connections list/dictionary.
