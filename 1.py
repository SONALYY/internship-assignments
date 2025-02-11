import re

def is_valid_ipv4(ip):
   
    pattern = r"^(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$"
    
    
    match = re.match(pattern, ip)
    if not match:
        return False
    
   
    parts = ip.split('.')
    for part in parts:
        if part != str(int(part)):
            return False
    
    return True


print(is_valid_ipv4("222.111.111.111"))  
print(is_valid_ipv4("5555..555"))        
print(is_valid_ipv4("0.0.0.255"))        
print(is_valid_ipv4("0.0.0.0255"))       