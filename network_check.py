import subprocess

def check_network():
    try:
        # Get the IP address of the default interface
        result = subprocess.run(['ip', 'addr'], stdout=subprocess.PIPE, text=True)
        output = result.stdout
        
        print("Network Interfaces Output:")
        print(output)  # Debugging output
        
        # Check for active Wi-Fi interface
        if "wlan0" in output and "UP" in output:
            return 'wifi'
        elif any("rmnet_data" in line and "UP" in line for line in output.splitlines()):
            return 'mobile'
        return 'none'
    except Exception as e:
        print(f"Error checking network: {e}")
        return 'none'

def prompt_override():
    response = input("You are connected to mobile data. Do you want to override the restriction on large uploads/downloads? (yes/no): ")
    return response.lower() in ['yes', 'y']

def restrict_large_transfers():
    network_type = check_network()
    
    if network_type == 'wifi':
        print("Connected to Wi-Fi. Large uploads/downloads are allowed.")
        # Proceed with large uploads/downloads
    elif network_type == 'mobile':
        print("Connected to mobile data. Large uploads/downloads are restricted.")
        if prompt_override():
            print("Override confirmed. Proceeding with large uploads/downloads.")
            # Proceed with large uploads/downloads
        else:
            print("Override denied. Large uploads/downloads are restricted.")
    else:
        print("No active network connection. Please check your connection.")

if __name__ == "__main__":
    restrict_large_transfers()