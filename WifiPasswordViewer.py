import subprocess
# getting all Wifi profiles
profiles = subprocess.check_output("netsh wlan show profiles",
                                   shell=True).decode()

# Extracting profile names
names = [line.split(":")[1].strip()
         for line in profiles.split("\n") if "All User Profile" in line]

# Displaying available networks (the first output)
for i, n in enumerate(names,1):
    print(f"[{i}] {n}")

# Getting User selection input
## converts user's entered number to integer, uses numbet to select the WiFI name from the list 
### (subtracting 1 for Python's 0 based indexing)
ch = int(input("\nChoose WiFi number : "))
wifi = names[ch - 1]
result = subprocess.check_output(
    f"netsh wlan show profile \"{wifi}\" key-clear",
    shell=True).decode()
print("\n" + result)
