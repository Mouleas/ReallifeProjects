# ReallifeProjects

## Digital signature
- A digital signature is a mathematical scheme for verifying the authenticity of digital messages or documents. A valid digital signature, where the prerequisites are satisfied, gives a recipient very strong reason to believe that the message was created by a known sender (authentication), and that the message was not altered in transit integrity.
##### Uses
Digital Signature Certificate is used for the following purposes.

- Income tax return filling.
- GST registration.
- GST return filling.
- All type of Company registration (LLP, LTD, PVT LTD, OPC etc.)
- Annual compliance filling of all type of company.
- All other transactions in the MCA portal.
- Import-export transaction in DGFT portal.
- Trademark registration and logo registration.
- Patent registration or application.
- IRCTC vendor transaction.
- Employee provident fund transaction.
- Mgnrega contractor use.
- Government organisation transaction.
- Panchayat office transaction.
- eTender and eAuction transaction.

Digital signature uses are increasing day by day. There are many other websites where digital signature is used for all transaction. It is practically imposible to list all websites. He have listed some major sites only.
#### Pictorial representation
![3-56](https://user-images.githubusercontent.com/74062509/115358984-d6e25900-a1db-11eb-8832-339e0bb6f871.png)



## Image To Text

- It is a program which is used to convert a pdf to a text format

#### Advantages
-  There is no need in manual operation 
-  It automatically reconizes the text and print in the screen

#### Libraries required
```Python
pip install pytesseract
pip install tkinter
pip install PIL
```




## Voice_Assistant

##### This codes is based on python 3.9

#### INSTRUCTIONS
you need to download various packages.
Here is the procedure to download all these packages
```python
//open your command prompt and type the following lines one by one
pip install SpeechRecognition
pip install pyttsx3
pip install webbrowser
pip install pyaudio
pip install datetime
pip install speedtest-cli
pip install pywhatkit
pip install wikipedia
```
#### Uses of these modules
- SpeechRecognition   ==> this makes our program to listen
- pyttsx3 and pyaudio ==> this is used to catch our voice commands
- webbroser           ==> this directs us to web
- datetime            ==> this displays the present time
- speedtest-cli       ==> this checks our ping ,download speed and upload speed
- pywhatkit           ==> this directs your search to youtube
- wikipedia           ==> this is similar to wikipedia

#### In this program i copied the links of my most commonly used websites because i need this websites always logged in and i don't need to see any kind of log in pages when i command my program so make sure to use your program  has your soial media links otherwise it not gonna work 

## GUI Chatroom
#### Socket programming

Sockets can be thought of as endpoints in a communication channel that is bi-directional, and establishes communication between a server and one or more clients. Here, we set up a socket on each end and allow a client to interact with other clients via the server. The socket on the server side associates itself with some hardware port on the server side. Any client that has a socket associated with the same port can communicate with the server socket.

#### Multi-Threading

A thread is sub process that runs a set of commands individually of any other thread. So, every time a user connects to the server, a separate thread is created for that user and communication from server to client takes place along individual threads based on socket objects created for the sake of identity of each client.
We will require two scripts to establish this chat room. One to keep the serving running, and another that every client should run in order to connect to the server.


#### Server Side Script

The server side script will attempt to establish a socket and bind it to an IP address and port specified by the user (windows users might have to make an exception for the specified port number in their firewall settings, or can rather use a port that is already open). The script will then stay open and receive connection requests, and will append respective socket objects to a list to keep track of active connections. Every time a user connects,
a separate thread will be created for that user. In each thread, the server awaits a message, and sends that message to other users currently on the chat. If the server encounters an error while trying to receive a message from a particular thread, it will exit that thread.

#### Usage

This server can be set up on a local area network by choosing any on computer to be a server node, and using that computer’s private IP address as the server IP address.
For example, if a local area network has a set of private IP addresses assigned ranging from 192.168.1.2 to 192.168.1.100, then any computer from these 99 nodes can act as a server, and the remaining nodes may connect to the server node by using the server’s private IP address. Care must be taken to choose a port that is currently not in usage. For example, port 22 is default for ssh, and port 80 is default for HTTP protocols. So these two ports preferably, shouldnt be used or reconfigured to make them free for usage.
However, if the server is meant to be accessible beyond a local network, the public IP address would be required for usage. This would require port forwarding in cases where a node from a local network (node that isnt the router) wishes to host the server. In this case, we would require any requests that come to the public IP addresses to be re routed towards our private IP address in our local network, and would hence require port forwarding.
