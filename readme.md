So there are some import statements to start out with.
I think those are from the zeromq-pyre that we had to download. I don't know what they do.
So the first is " from pyre import Pyre" which brings in a code repository or library.
Then there is "from pyre import zhelper" which is a specific portion of the initial code library.
Next is all straight import statement functions" import zmq, import uuid, import json" I have no idea on what these do, but they seem to be more broad than the previous couple of statements.
Well either that or they could be drawing from those statements, but I think they are more general.

Next is def get_peer_node(username): 
This defines the function of get_peer_node, turning it into a function.
This statement has 1 parameter to it, where "n" is defined as the variable for Pyre(username) which is a function, although I don't know what that does.
It has a couple of comments, although I am unsure if they help govern the actions of the Pyre(username). 
After that there is n.start() which is another function that starts something I assume it activates something. 
Then there is return n which returns the variable to what it was input as.
So nodes are places where things are stored, so I think that this must be about saving usernames that aren't your own.

def join_group(node, group)
So def turns join_group into a function.
this one has two parameters. 
There is also a notification function below it with print(f"Joined group: {group}"). Which I know notifies the user that they have joined the group, I am unsure if it would notify others once the program is run.
This may be about saving what group has been joined.

def chat_task(ctx, pipe, n, group)
so this defines chat_task which turns it into a function.
So this definition has four parameters. 
"n" was defined as the variable for pyre(username). I would guess this has some function related to the use of a username.
I don't know about what ctx or pipe does, but I think those are functions?
I really don't know about those.

def get_channel(node, group)
So get_channel is now a function.
It has two parameters. 
I think node has something to do with memory, or recalling previous information.
I don't know if group has been defined yet, but in our context I suspect it is about the text group that you join.