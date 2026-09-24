prot, port, pack_size, encrypt =  input().split()

port = int(port)
pack_size = int(pack_size)


def main():
    if ( port == 80 or port == 8080):
        if (encrypt == "YES"):
            return "YES"
        else:
            return "ALLOW SECURE"
    elif ( port == 443 or port == 8443):
        if (encrypt == "NO"):
            return "REJECT"
        elif (pack_size > 500): 
            return "QUARANTINE LARGE"
        else:
            return "ALLOW SECURE"
    elif (port == 53 or port == 123):
        if (prot == "UDP" and pack_size <= 64):
            return "ALLOW SYSTEM"
        else:
            return "BLOCK SUSPICIOUS"
    else:
        if (port < 1024):
            return "BLOCK PRIVILEGED"
        else:
            return "ALLOW CUSTOM"



print(main())

input()