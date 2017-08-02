**sbl_check.py**

This Python script is designed to check the list of IP addresses or subnet(s) through the spam blacklists (Spamhaus, CBL, SpamCop, SORBS, Barracuda, INPS.de, McAfee, WPBL, BlockList.de, etc.) and output the status of the IP address if it is 'blacklisted'.<br />
Compatible with Python 3.x.<br />
Requires dnsutils system package to be installed + [ip_validator](https://github.com/sparklingSky/ip_validator) module.

How to use:<br />
1. Specify 'ips' variable and uncomment the lines in the end of the script.<br />
2. Run the script.<br />
3. Output will be recorded to output_sbl.log<br />
