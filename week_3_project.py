import lab_chat as lc


def initialize_chat():
    #get user
    user = get_username()
    #get group
    group = get_group()
    # get peer node
    node = lc.get_peer_node(user)
    #return channel
    return lc.get_channel(node,group)

def get_username():
    #ask for desired username
    username = input("enter your username")
    #remove whitespace forward and trailing white space
    username = username.strip().upper()
    return username
# print(get_username())

def get_group():
    return input('enter group name').strip().upper()
# print(get_group())

def get_message():
    return input('enter message').strip()
# print(get_message())

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

start_chat()