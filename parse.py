from bs4 import BeautifulSoup


file_path = "./templates/home.html"
with open(file_path, 'r') as file:
    html_content = file.read()

# parce age related html
parse_label = "age"
parse_type = "input"
soup = BeautifulSoup(html_content, 'html.parser')
parced_html = soup.find(parse_type, attrs={'name': parse_label}).find_parent('div')
# parced_html = soup.find(parse_type, attrs={'name': parse_label})

print(f'\n ----- html part realted to {parse_label} -------- \n')
print(parced_html)

with open('parsed_html.txt', 'w') as file:
    file.write(str(parced_html))
