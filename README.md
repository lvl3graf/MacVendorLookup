A simple Python script to download and find the vendor of a given MAC address.

Usage:
 - Run script
 - Input "update" to download and refresh the list file
 - Input MAC address, script spits out all vendors it finds

How does it work?
Script strips all symbols from input, including spaces, then checks the list using the first 6 symbols of the MAC address.

Example:
PS D:\MacVendorLookup> .\macvendor.py
Simple Mac Vendor lookup by lvl3graf

Enter MAC address or update to refresh OUI list: 14:5A:FC:39:1F:ED E14


145A - Logi-D inc

145A - Apple, Inc.

145A - CLOUD NETWORK TECHNOLOGY SINGAPORE PTE. LTD.

145A - Liteon Technology Corporation

145A - Westermo Neratec AG
