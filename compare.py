def main():
    with open('hal.ns.cloudflare.com-list.txt', 'r') as f:
        tegan_domains = f.read().splitlines()
    with open('amy.ns.cloudflare.com-list.txt', 'r') as f:
        greg_domains = f.read().splitlines()

    # domains in both
    common_domains = sorted(set(tegan_domains) & set(greg_domains))

    with open('common-domains.txt', 'w') as f:
        for domain in common_domains:
            f.write(f'{domain}\n')


main()