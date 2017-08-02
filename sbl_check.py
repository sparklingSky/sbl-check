import subprocess
from collections import defaultdict
from ip_validator import ip_validator
__author__ = 'sparklingSky, koi8'


blacklists = ['aspews.ext.sorbs.net',
              'b.barracudacentral.org',
              'l1.bbfh.ext.sorbs.net',
              'l2.bbfh.ext.sorbs.net',
              'l3.bbfh.ext.sorbs.net',
              'l4.bbfh.ext.sorbs.net',
              'cbl.abuseat.org',
              'dnsbl.inps.de',
              'cidr.bl.mcafee.com',
              'dnsbl.proxybl.org',
              'dnsbl.sorbs.net',
              'problems.dnsbl.sorbs.net',
              'proxies.dnsbl.sorbs.net',
              'relays.dnsbl.sorbs.net',
              'safe.dnsbl.sorbs.net',
              'dul.dnsbl.sorbs.net',
              'rhsbl.sorbs.net',
              'badconf.rhsbl.sorbs.net',
              'nomail.rhsbl.sorbs.net',
              'zombie.dnsbl.sorbs.net',
              'block.dnsbl.sorbs.net',
              'escalations.dnsbl.sorbs.net',
              'http.dnsbl.sorbs.net',
              'misc.dnsbl.sorbs.net',
              'smtp.dnsbl.sorbs.net',
              'socks.dnsbl.sorbs.net',
              'spam.dnsbl.sorbs.net',
              'recent.spam.dnsbl.sorbs.net',
              'new.spam.dnsbl.sorbs.net',
              'old.spam.dnsbl.sorbs.net',
              'web.dnsbl.sorbs.net',
              'bl.spamcop.net',
              'pbl.spamhaus.org',
              'sbl.spamhaus.org',
              'sbl-xbl.spamhaus.org',
              'xbl.spamhaus.org',
              'zen.spamhaus.org',
              'multi.surbl.org',
              'dnsbl-0.uceprotect.net',
              'dnsbl-1.uceprotect.net',
              'dnsbl-2.uceprotect.net',
              'dnsbl-3.uceprotect.net',
              'blacklist.woody.ch',
              'db.wpbl.info',
              'bl.blocklist.de',
              'dnswl.inps.de']


def sbl_checking(ip_list):
    """
    :param ip_list: string of IP addresses or subnet(s)
    :return: defaultdict of blacklisted IP addresses with reference to spam blacklists
    """
    result = defaultdict(list)
    ip_list = ip_validator(ip_list)
    if ip_list is 1:
        raise ValueError("Input data is not a valid string of IP addresses/subnets")
    for ip in ip_list:
        first, second, third, fourth = str(ip).split('.')
        ipR = str(fourth) + '.' + str(third) + '.' + str(second) + '.' + str(first)
        for blacklist in blacklists:
            command = "/usr/bin/dig +short " + ipR + '.' + blacklist
            try:
                returned = subprocess.check_output(command, shell=True)
                returned = returned.decode("utf-8")
            except:
                result[str(ip)].append('error while checking ' + blacklist)
            if returned != '':
                result[str(ip)].append(blacklist)

    return result


def write_to_file(result):
    my_file = open("output_sbl.log", "w")
    my_file.close()
    my_file = open("output_sbl.log", "a")
    if not result:
        my_file.write("No blacklisted IP addresses")
    else:
        for ip, bls in result.items():
            for bl in bls:
                my_file.write(ip + " " + bl + "\n")

    my_file.close()


def sbl_check(ip_list):
    write_to_file(sbl_checking(ip_list))
    print("\n")
    print("Completed. See the result in file output_sbl.log")


# ips = "1.2.3.0/28, 4.5.6.20"
# sbl_check(ips)
