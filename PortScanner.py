import nmap

nmap_path = r"C:\Program Files (x86)\Nmap\nmap.exe"  # Replace with the actual path to nmap.exe.

nm = nmap.PortScanner(nmap_search_path=[nmap_path])

target = "45.33.32.156" # Replace with IP Address you would like to scan. Make sure you have permission to scan the IP Address.
options = "-sV -sC"

nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))
            