with open("links.txt", 'r') as link_file:
    links = link_file.read().splitlines()

with open("baza.txt", "r") as baza_file:
    for line in baza_file:
        parts = line.split(':')
        login, password = parts[-2], parts[-1]

        parts = parts[:-2]
        url = ':'.join(parts)

        # print(url, login, password)
        for link in links:
            if link in url:
                with open(f"{link}.txt", "a") as output_file:
                    output_file.write(f'{login}:{password}')
