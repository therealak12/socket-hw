# UDP ping
The client measures RTT using python time library. If responding takes
more than 1 seconds, the package is assumed to be lost.

## Usage
Run the server simply by
```bash
python udp_ping_server.py
``` 
and the client by
```
python udp_ping_client.py
```

### Note
This code is for Computer Networks course homework. The homework question is available below:
<br /><br /><br /> 


Your ping program is to send 10 ping messages to the target server over UDP. For
each message, your client is to determine and print the RTT when the
corresponding pong message is returned. Because UDP is an unreliable protocol, a
packet sent by the client or server may be lost. For this reason, the client cannot
wait indefinitely for a reply to a ping message. You should have the client wait up
to one second for a reply from the server; if no reply is received, the client should
assume that the packet was lost and print a message accordingly.
On the other hand, write the server so that it randomly replies the client. This will
imitate the UDP packet loss.