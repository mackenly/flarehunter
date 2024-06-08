import sys
import json
import requests

def get_api_key():
    try:
        with open('.config', 'r') as f:
            return f.readline().strip()
    except FileNotFoundError:
        print('Please create a .config file with your API_KEY in it.')
        sys.exit(1)


def get_balance(API_KEY):
    url = f'https://api.viewdns.info/account/?action=balance&apikey={API_KEY}&output=json'
    response = requests.get(url)
    data = json.loads(response.text)
    balance = 0;
    if 'prepaid' in data['response']:
        balance += int(data['response']['prepaid']['balance'])
    if 'monthly' in data['response']:
        balance += int(data['response']['monthly']['limit'])
        balance -= int(data['response']['monthly']['usage'])
    if 'trial' in data['response']:
        balance += int(data['response']['trial']['limit'])
        balance -= int(data['response']['trial']['usage'])
    return balance


def get_nameserver_domains(API_KEY, nameserver, page=1):
    url = f'https://api.viewdns.info/reversens/?ns={nameserver}&apikey={API_KEY}&output=json&page={page}'
    response = requests.get(url)
    print(f'GET {nameserver} #{page} {response.status_code}')
    data = json.loads(response.text)
    try:
        count = int(data['response']['domain_count'])
    except KeyError:
        if 'No domains found with that nameserver.<br><br>' in data['response']['error']:
            print(f'Error: {data["response"]}')
            return [], 0
        print(f'Error: {data["response"]}')
    total_pages = int(data['response']['total_pages'])
    current_page = int(data['response']['current_page'])
    domains = data['response']['domains']

    if current_page < total_pages and count > 0:
        domains.extend(get_nameserver_domains(API_KEY, nameserver, page+1)[0])

    return domains, count


def main():
    API_KEY = get_api_key()
    print(f'API_KEY: {API_KEY}')
    balance = get_balance(API_KEY)
    print(f'Balance: {balance}')

    nameserver = 'shaz.ns.cloudflare.com'
    domains, count = get_nameserver_domains(API_KEY, nameserver)
    if count == 0:
        print('No domains found.')
        return
    print(f'Nameserver: {nameserver}')
    print(f'Count: {count}')

    # write to file
    with open(f'data/{nameserver}-list.txt', 'w') as f:
        f.write(f'Nameserver: {nameserver}\n')
        f.write(f'Count: {count}\n')
        f.write(f'Domains:\n')
        for domain in domains:
            f.write(f'{domain['domain']}\n')


if __name__ == '__main__':
    main()
