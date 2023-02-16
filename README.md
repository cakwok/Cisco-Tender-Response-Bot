Introduction
------------
As part of network presales engineers daily life, we are used to spend hours to dig out proper responses in response to tendor parameters, such as routers  physical dimensions, MTBF, ambience temperature, etc. 

In this work, a web scraper is built to seamless these parameter lookup, resultedly much faster response during tendor cycles.

This work supports information returned by .html. Pdf is not supported.

Setup
----------------
To run this script, edit the list of inventory at the following line.  In this example, "Cisco IE4000" is appended to the list.

From

```
inventory = ["Cisco 9400 C9400-SUP-1XL-Y", "Cisco Catalyst 9600 Series Supervisor Engine 1", "Cisco 9800-80",
             "Cisco Nexus 9500", "Cisco NCS 5500"]
```
to
```
inventory = ["Cisco 9400 C9400-SUP-1XL-Y", "Cisco Catalyst 9600 Series Supervisor Engine 1", "Cisco 9800-80",
             "Cisco Nexus 9500", "Cisco NCS 5500", "Cisco IE4000"]
```

Modify tendor parameter at the SearchString.  eg, edit this line from "temperature" to "mtbf"

```
SearchString = self.model.replace(" ", "+") + "+temperature"  to

SearchString = self.model.replace(" ", "+") + "+mtbf"
```
