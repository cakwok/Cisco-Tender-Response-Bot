Introduction
------------

TenderBot 1.0 - Casca Kwok

The bot is built in an aim to automate TCP/IP networking tendor response process, to enhance efficiency
from searching tendor parameters, just by input network equipment model into a list to save hours of effort!

TenderBot 1.0 supports information returned by .html format

Setup
----------------
Edit inventory at the inventory list.  eg, To add a new inventory, append the model to the list.

```
inventory = ["Cisco 9400 C9400-SUP-1XL-Y", "Cisco Catalyst 9600 Series Supervisor Engine 1", "Cisco 9800-80",
             "Cisco Nexus 9500", "Cisco NCS 5500"]
```
to
```
inventory = ["Cisco 9400 C9400-SUP-1XL-Y", "Cisco Catalyst 9600 Series Supervisor Engine 1", "Cisco 9800-80",
             "Cisco Nexus 9500", "Cisco NCS 5500", "Cisco IE4000"]
```
Modify tendor parameter.  eg, edit this line from "temperature" to "mtbf"

```
SearchString = self.model.replace(" ", "+") + "+temperature"  to

SearchString = self.model.replace(" ", "+") + "+mtbf"
```
