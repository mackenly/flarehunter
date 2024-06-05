# flarehunter
 Hunt for Cloudflare zones on the same account using nameservers

Initial work of a tool to hunt for Cloudflare accounts using nameservers. This tool is based on the research of the following post: https://community.cloudflare.com/t/privacy-concern-regarding-cloudflares-nameserver-pairing-policy/650232

I've had mixed results. It does appear to work, but none of the Cloudflare accounts I've tested had domains I own or know about in the results from the API. If anyone knows of a better data source with friendly pricing, please let me know (or if someone wants to sponsor it, that would be cool too).

## Usage
Create a file named `.config` and put in your API key from https://viewdns.info/api/ (nothing else, just the key)

Edit the `nameserver` variable in `getter.py` to one of the nameservers of the target domain. Run it, then edit to the next nameserver and run again.

Now edit the file names in `compare.py` to the files you want to compare. Run it. Look at the results in `common-domains.txt`.

Sorry that parameters are hardcoded, unless I can get it to work I'm not going to spend time on it.