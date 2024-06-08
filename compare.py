def main():
    a = "hugh.ns.cloudflare.com"
    b = "roxy.ns.cloudflare.com"
    with open(f'data/{a}-list.txt', 'r') as f:
        a_domains = f.read().splitlines()
    with open(f'data/{b}-list.txt', 'r') as f:
        b_domains = f.read().splitlines()

    # domains in both
    common_domains = sorted(set(a_domains) & set(b_domains))

    with open(f'reports/common-domains-{a}-{b}.txt', 'w') as f:
        for domain in common_domains:
            f.write(f'{domain}\n')


main()