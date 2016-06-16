**sbl_check.py**

This Python script is designed to check IP addresses within the specified subnet through the spam blacklists (Spamhaus, CBL, SpamCop, SORBS, Barracuda, INPS.de, McAfee, WPBL, BlockList.de, etc.) and output the status of the IP address if it is 'blacklisted'.<br />
Compatible with Python 2.x.<br />
Requires dnsutils system package and ipcalc Python module to be installed.

How to use:<br />
1. Specify 'networks'/'ips' variable.<br />
2. Configure run at the end of file (follow the comments).<br />
3. Run the script.<br />
4. Output will be recorded to output_sbl.log<br />
