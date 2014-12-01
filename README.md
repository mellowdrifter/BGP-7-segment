BGP-7-segment
=============

Pull BGP table size and then display values on two 7 segment display banks

There are three separate parts to this app. First a script that runs on my bird bgp daemon box running ipv4 and ipv6 BGP. This script runs once every 5 minutes and creates an XML file.

The second application pulls that information and then programs a Raspberry PI to display the table size correctly.

The third part is the actual PCB board that drives the 7 segment displays
