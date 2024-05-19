def extract_cookies(content):
    cookies = []
    lines = content.splitlines()
    
    current_entry = ""
    for line in lines:
        if current_entry:
            current_entry += line
        else:
            current_entry = line
        
        # Check if current_entry contains at least two colons
        if current_entry.count(':') >= 2:
            try:
                user, passwd, cookie = current_entry.split(':', 2)
                cookies.append(cookie)
                current_entry = ""
            except ValueError:
                pass  # Continue to accumulate the current_entry
    
    return cookies

def read_user_pass_cookies(input_file):
    # Read the entire content from the input file
    with open(input_file, 'r') as file:
        content = file.read()
    return content

def write_cookies_to_file(cookies, output_file):
    # Write all cookies to the output file, one per line
    with open(output_file, 'w') as file:
        for cookie in cookies:
            file.write(cookie + '\n')

# File names
input_file = "cookies.txt"
output_file = "output.txt"

# Process the input file and write the cookies to the output file
try:
    content = read_user_pass_cookies(input_file)
    cookies = extract_cookies(content)
    write_cookies_to_file(cookies, output_file)
    print(f"The extracted cookies have been written to {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")
