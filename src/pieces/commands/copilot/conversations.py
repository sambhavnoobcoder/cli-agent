import pydoc
import pieces_os_client as pos_client
from pieces.api.config import api_client
from rich.console import Console
from rich.markdown import Markdown
from pieces.gui import show_error
from .ask_command import ws_manager

conversation_map = {}

def conversation_handler(**kwargs):
    """Handle the conversation command"""
    
    idx = kwargs.get("CONVERSATION_INDEX",None) 
    rename = kwargs.get("rename",False)
    delete = kwargs.get("delete",False)


    # Check if the conversation is not empty 
    if not ws_manager.conversation and (rename or delete) and not idx:
        show_error("Error in rename/delete","You can rename/delete an empty conversation")
        return 
    else:
        if idx:
            conversation_id = get_conversation_id(idx)  
        else:
            conversation_id = ws_manager.conversation



    # Rename the conversation
    if rename:
        conversation_api = pos_client.ConversationApi(api_client)
        if rename == True:
            con = conversation_api.conversation_specific_conversation_rename(conversation=conversation_id)
            print(f"Renamed the conversation to {con.name}")
            
        else:
            con = conversation_api.conversation_get_specific_conversation(conversation=conversation_id)
            con.name = rename
            conversation_api.conversation_update(transferables = False,conversation=con)
            print("Renamed the conversation successfully")
        return

    # Delete the conversation
    if delete:
        r = input("Are you sure you want to delete the conversation? (y/n) : ")
        if r == "y":
            pos_client.ConversationsApi(api_client).conversations_delete_specific_conversation(conversation=conversation_id)
            print("Conversation deleted successfully")
        return


    # Check if we want to create a new conversatiaon
    if kwargs.get("new",False):
        ws_manager.conversation = None
        print("New conversation created successfully")
        return
    
    
    
    # If the index is not given we get the conversation that we are using in the ask websocket.
    if not idx:
        if ws_manager.conversation:
            get_conversation_messages(conversation_id = ws_manager.conversation)
        else:
            # Show error if no conversation in the ask show error
            show_error("The conversation is empty","Please enter a conversation index, or use the ask command to ask a question.")
    else:
        get_conversation_messages(idx)


def get_conversations(**kwargs):
    """This function is used to print all conversation avaiable"""
    global conversation_map
    api_instance = pos_client.ConversationsApi(api_client)
    api_response = api_instance.conversations_snapshot()

    # Sort the dictionary by the "updated" timestamp
    sorted_conversations = sorted(api_response.iterable, key=lambda x: x.updated.value, reverse=True)
    
    conversation_map = {idx: conversation.id for idx,conversation in enumerate(sorted_conversations,start=1)}

    readable = sorted_conversations[0].updated.readable
    output = f"            {readable}\n"
    for idx,conversation in enumerate(sorted_conversations,1):
        if conversation.updated.readable != readable: # if new date print it to group them
            readable = conversation.updated.readable
            output += f"___________________________________________\n\n            {readable}\n"
        
        if not conversation.name:
            conversation.name = "New conversation"

        conversation_str = f"{idx}. {conversation.name} \n"
        # Check if we are using this conversation
        if ws_manager.conversation == conversation.id:
            output += f"\033[92m  * {conversation_str} \033[0m"
        else:
            output += conversation_str
    
    # print the pager
    pydoc.pager(output)



def get_conversation_messages(idx:int=None,conversation_id=None):
    """Print a conversation messages. you need to pass the index of the conversation or the conversation id"""

    conversation_api = pos_client.ConversationApi(api_client)
    message_api = pos_client.ConversationMessageApi(api_client)
    
    if not conversation_id:
        conversation_id = get_conversation_id(idx)

    conversation:pos_client.Conversation = conversation_api.conversation_get_specific_conversation(conversation=conversation_id)

    ws_manager.conversation = conversation.id # change the conversation that the ask is using
    
    
    console = Console()
    for key,val in conversation.messages.indices.items():
        if val == -1: # message is deleted
            continue
        message = message_api.message_specific_message_snapshot(message=key)
        console.print(message.role+"\n", justify = "center", style="bold italic") # make the role bold and italic 
        if message.fragment.string:
            md = Markdown(message.fragment.string.raw)
            console.print(md)
        
        console.print("_",justify="right",style="u") # print a Line filling the page width
        


def get_conversation_id(idx):
    global conversation_map
    if not conversation_map:
        conversations_api = pos_client.ConversationsApi(api_client)
        api_response = conversations_api.conversations_snapshot()
        # Sort the dictionary by the "updated" timestamp
        sorted_conversations = sorted(api_response.iterable, key=lambda x: x.updated.value, reverse=True)

        conversation_map = {idx: conversation.id for idx,conversation in enumerate(sorted_conversations,start=1)}

    return conversation_map[idx]

