# Heyo
This little repo was made to show my implementation of a research paper regarding network security and steganography.

If you would like to read it, the corresponding paper is in the repo as well. You can also go to https://dl.acm.org/doi/10.1145/3339252.3341488 in order to view it.

I have attached a small diagram in order to explain the implementation.

![image](https://github.com/user-attachments/assets/498ead39-8ec7-4fa4-b050-89903c5b83aa)

In essence, two devices (sender and receiver) which are present in the same network, are able to communicate by using the network router as a 'dead drop'.

This works by sending message encoded ARP packets over the network, where the router stores their details. These details, which contain the encoded message, can then be accessed by the receiver, completing the communication line.

## Requirements
* IDE or code editor to run the scripts.
* Scapy library, in python using `pip install scapy`.
* A network analyser, such as WireShark.
* A Router, or a Virtual Router (which I used) to act as the dead drop.



