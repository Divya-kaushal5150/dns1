import dns.resolver

# Set the IP address of the local DNS server and a public DNS server
local_host_ip = '127.0.0.1'  # Local DNS server (usually localhost)
real_name_server = '8.8.8.8'  # Google's Public DNS server (you can use other public DNS servers like 1.1.1.1 for Cloudflare)

# Create a list of domain names to query
domainList  = ['example.com.','safebank.com.','google.com.','nyu.edu.','legitsite.com.']

# Define a function to query the local DNS server for the IP address of a given domain name
def query_local_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [local_host_ip]  # Set to local DNS server IP
    answers = resolver.resolve(domain, question_type)  # Query the domain with the provided question_type

    ip_address = answers[0].to_text()  # Extract the IP address from the first answer
    return ip_address   

# Define a function to query a public DNS server for the IP address of a given domain name
def query_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [real_name_server]  # Set to Google's public DNS server IP
    answers = resolver.resolve(domain, question_type)  # Query the domain with the provided question_type

    ip_address = answers[0].to_text()  # Extract the IP address from the first answer
    return ip_address

# Define a function to compare the results from the local and public DNS servers for each domain name in the list
def compare_dns_servers(domainList, question_type):
    for domain_name in domainList:
        local_ip_address = query_local_dns_server(domain_name, question_type)  # Get IP from local DNS server
        public_ip_address = query_dns_server(domain_name, question_type)  # Get IP from public DNS server
        if local_ip_address != public_ip_address:  # Compare the IPs
            return False  # Return False if IPs don't match
    return True  # Return True if all IPs match

# Define a function to print the results from querying both the local and public DNS servers for each domain name in the domainList
def local_external_DNS_output(question_type):    
    print("Local DNS Server")
    for domain_name in domainList:
        ip_address = query_local_dns_server(domain_name, question_type)  # Get IP from local DNS server
        print(f"The IP address of {domain_name} is {ip_address}")  # Print the result

    print("\nPublic DNS Server")
    for domain_name in domainList:
        ip_address = query_dns_server(domain_name, question_type)  # Get IP from public DNS server
        print(f"The IP address of {domain_name} is {ip_address}")  # Print the result

# Testing function to simulate DNS query info retrieval
def exfiltrate_info(domain, question_type):
    data = query_local_dns_server(domain, question_type)  # Get IP from local DNS server
    return data  # Return the IP address retrieved

# Main execution block
if __name__ == '__main__':
    
    # Set the type of DNS query to be performed
    question_type = 'A'  # Query type 'A' for IPv4 addresses

    # Uncomment to print the results from querying both DNS servers
    local_external_DNS_output(question_type)

    # Call the function to compare the results from both DNS servers and print the result
    result = compare_dns_servers(domainList, question_type)
    print(f"Do the local and public DNS results match for all domains? {result}")
    
    # Example of using the exfiltrate_info function for a specific domain
    result = exfiltrate_info('nyu.edu.', question_type)
    print(f"Exfiltrated info for nyu.edu: {result}")
