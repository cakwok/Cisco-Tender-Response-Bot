Introduction
------------

TenderBot 1.0 - Casca Kwok

As part of network presales engineers daily life, during tender response days, we are used to spend  hours to dig out tendor parameters, responding physical dimensions/MTBF/ambience temperature/product weight, because there seems no automation tools and yet, each time the targeted equipment model/parameters required,  are not surprisingly in different combinations.  Thus, leveraging the hardwork before may not be good template for the next. Might be it's more straight forward if just google it again.  Might be if there's a tool to automate the web searching, life could be easier.

Therefore, TenderBot 1.0 was built.  It also helped me to build a dataset from sketch for vendor MTBF parameters with much more ease.

TenderBot 1.0 supports information returned by .html format (pdf is not supported).

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
