# HTTP server using python socket library
Capable of processing one request and responding with the requested file or 404 error

## Usage
Run the server simply by
```bash
python server.py
``` 
and the client by
```
python client.py localhost 8000 <file_name>
```

### Note
This code is for Computer Networks course homework. The homework question is available below:
<br /><br /><br /> 


Specifically, your Web server will (i)
create a connection socket when contacted by a client; (ii) receive the
HTTP request from this connection; (iii) parse the request to determine the specific
file being requested;(iv) get the requested file from the server’s file system; (v)
create an HTTP response message consisting of the requested file preceded by
header lines; and (vi) send the response over the TCP connection to the requesting
client. 