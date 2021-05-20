from datetime import datetime

# for mac & linux use the path /etc/hosts
path_to_hosts = r'C:\Windows\System32\drivers\etc\hosts'  # for windows


class BlockDomains:
    def __init__(self):
        self.domains_to_block = ['www.instagram.com', 'instagram.com']
        self.end_time = datetime(2021, 5, 20, 5)
        self.redirect = '127.0.0.1'

    def block_sites(self):
        if datetime.now() < self.end_time:
            print('Blocking domains')

            with open(path_to_hosts, 'r+') as f:
                hosts_text = f.read()
                for domain in self.domains_to_block:
                    if domain not in hosts_text:
                        f.write(f'{self.redirect} {domain} \n')
        else:
            print('Unblocking domains')

            with open(path_to_hosts, 'r+') as f:
                lines = f.readlines()
                f.seek(0)

                for line in lines:
                    if not any(domain in line for domain in self.domains_to_block):
                        f.write(line)
                f.truncate()


if __name__ == '__main__':
    blocksites = BlockDomains()
    blocksites.block_sites()
