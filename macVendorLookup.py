#Library for retrieving files
from urllib.request import urlretrieve

#Update OUI list
def update():
    url = "https://standards-oui.ieee.org/oui/oui.txt"
    filename = "ouiOrig.txt"
    #Download file
    urlretrieve(url, filename)
    #Clean up retrieved file from unneeded lines
    with open("ouiOrig.txt", "r", encoding="utf-8") as input:
        with open("ouiFiltered.txt", "w", encoding="utf-8") as output:
            # iterate all lines from file
            for line in input:
                # if text matches then keep it
                if "(base 16)" in line.strip("\n"):
                    output.write(line)

#Filter out spaces and all symbols like : and -
def filteredMac(mac):
    filteredMac = "".join(c for c in mac if c.isalnum())
    return filteredMac

def findMac(mac):
    with open("ouiFiltered.txt", "r", encoding="utf-8") as input:
        for line in input:
            if mac in line.strip("\n"):
                print(mac + " - " + line[22:])

#"update" to update the list, "filter" to filter the list out
def menu():
    print("Simple Mac Vendor lookup by lvl3graf\n")
    q1 = input("Enter MAC address or update to refresh OUI list: ")
    print("\n")
    if q1 == "update":
        update()
    else:
        findMac(filteredMac(q1[:6]))

menu()
