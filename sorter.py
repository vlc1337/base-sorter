with open("links.txt", 'r') as link_file:
    links = link_file.read().splitlines()

with open("baza.txt", "r") as baza_file:
    for line in baza_file:
        url, login, password = line.strip().split(":")
        for link in links:
            if link in url:
                with open(f"{link}.txt", "a") as output_file:
                    output_file.write(f'{login}:{password}\n')