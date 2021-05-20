import time
interface_list = []
ip_add_list = []
subnet_mask_list = []

timestr = time.strftime("%Y%m%d-%H%M%S")
new_file_name = str(timestr)
extension = ".txt"
filename = new_file_name + extension
file = open(filename, "w")
with open(filename, "w") as f:

    int_number = input("How many interfaces do you want to configure?")
    start = 0
    start_print = 0

    for start in range(0, int(int_number)):
        interface = [str(input("What's the interface? "))]
        interface_list.append(interface)
        ip_add = [str(input("What's the IP-address? "))]
        ip_add_list.append(ip_add)
        subnet_mask = [str(input("What's the subnet mask? "))]
        subnet_mask_list.append(subnet_mask)

    run_ssh = int(input("Do you want to configure SSH and passwords (1/2) "))

    if run_ssh == 1:
        hostname = input("What do you want to call the router? ")
        domain_name = input("What's the domain? ")
        password = input("What password do you want on SSH lines? ")
        username = input("What username do you use? ")
        conpassword = input("What console password? ")

    elif run_ssh != 1:
        f.write("enable \n")
        f.write("configure terminal\n")

        for start_print in range(0, int(int_number)):
            f.write(f"interface " + str(*interface_list[int(start_print)]) + "\n")
            f.write("ip add " + str(*ip_add_list[int(start_print)]) + " " + str(*subnet_mask_list[int(start_print)]))
            f.write("\nno shut\n")
            f.write("exit\n")

    if run_ssh == 1:
        f.write("enable \n")
        f.write("configure terminal \n")
        for start_print in range(0, int(int_number)):
            f.write(f"interface " + str(*interface_list[int(start_print)]) + "\n")
            f.write("ip add " + str(*ip_add_list[int(start_print)]) + " " + str(*subnet_mask_list[int(start_print)]))
            f.write("\nno shut \n")
            f.write("exit \n")
        f.write(f"""
host {hostname}
ip domain-name {domain_name}
crypto key generate rsa 
1024
line vty 0 4
transport input ssh
login local 
password {password}
exit
line console 0
logging synchronous
exit
username {username} password {conpassword}
enable secret {conpassword}
service password-encryption
""")
