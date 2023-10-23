import socket
from  threading import Thread

from pynput.mouse import Button, Controller
from screeninfo import get_monitors
import autopy

SERVER = None
PORT = 8000
IP_ADDRESS = input("Enter your computer IP ADDR : ").strip()

# TA2: Create mouse object using Controller class


# TA2: Receive the message from the client

    # Access mouse as global
    

    # Create infinite while loop
    
        # Start try block
        
            # Receive message from client_socket

            # TA2: Check if message exits
            
                # Eval the message string toi get a dictionary
                
                # Check if data key value is 'left_click'
                
                    # Press left button using mouse object
                    
                    # Release the  left button 
                    
        # Add except block   
        
            # Pass
            


def accept_connections():
    global SERVER

    while True:
        client_socket, addr = SERVER.accept()
        print(f"Connection established with {client_socket} : {addr}")

        # TA2: Create a thread to receive the message from client
        
        


def setup():
    print("\n\t\t\t\t\t*** Welcome To Remote Mouse ***\n")

    global SERVER
    global PORT
    global IP_ADDRESS


    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(10)

    print("\t\t\t\tSERVER IS WAITING FOR INCOMING CONNECTIONS...\n")

    accept_connections()

setup()
