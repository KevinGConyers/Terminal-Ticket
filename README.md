# ttkt: cli ticket management

## Quickstart 

	- Install the Terminal-Ticket software by cloning the repo and running
	  ```sudo install.sh```
	- This will install the software system-wide
	- Edit the file "~/.ttktconfig.json" to add you information
	- start handling tickets!


## Documentation
Terminal ticket is a client for the jira ticketing software. It is designed to
ease the burden of having to constantly context shift between terminal sessions
and GUIs when performing IT fixes. It can be deployed onto most linux distro's
with python3 and configured for to point at a jira server. 
	```ttkt [mode] (operands)```
	### Modes:
		- list: lists all tickets
		- view <ticket-slug>: view details of a ticket
		- create: creates a new ticket
		- edit <ticket-slug>: edit information about a ticket
		- resolve <ticket-slug>: close a ticket
		- qresolve <ticket-slug> -m <message>: resolve a ticket as
		  current user with message
		
## Configuration Notes
	Currently, the software only works with Jira on http users so those
fields must be filled on in the config file. 
