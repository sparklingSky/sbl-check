import subprocess
import ipcalc
__author__ = 'koi8, sparklingSky'

# Specify networks/ips to check as python list in 'network'/'ips' variable,
# configure run at the end of file

networks = ['1.2.3.0/24', ]

ips = ['1.2.3.2',
       '1.2.3.4']

bls = ['aspews.ext.sorbs.net',
       'b.barracudacentral.org',
       'bb.barracudacentral.org',
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


def checking_network(network, my_file):
    for ip in ipcalc.Network(network):
        first, second, third, fourth = str(ip).split('.')
        ipR = str(fourth) + '.' + str(third) + '.' + str(second) + '.' + str(first)
#        print("Checking now " + str(ip))
        for bl in bls:
            command = "/usr/bin/dig +short " + ipR + '.' + bl
            try:
                returned = subprocess.check_output(command, shell=True)
            except:
                print ('error while checking ' + str(ip) + ' ' + bl)
            if returned != '':
                print (str(ip) + ' ' + bl)
                my_file.write(str(ip) + ' ' + bl + '\n')


def check_networks(networks):
    for network in networks:
        checking_network(network, my_file)


def checking_ips(ips):
    for ip in ips:
        first, second, third, fourth = str(ip).split('.')
        ipR = str(fourth) + '.' + str(third) + '.' + str(second) + '.' + str(first)
#        print("Checking now " + str(ip))
        for bl in bls:
            command = "/usr/bin/dig +short " + ipR + '.' + bl
            try:
                returned = subprocess.check_output(command, shell=True)
            except:
                print ('error while checking ' + str(ip) + ' ' + bl)
            if returned != '':
                print (str(ip) + ' ' + bl)


if __name__ == "__main__":
    my_file = open("output_sbl.log", "a", 0)

    # Uncomment or comment required checks:
    check_networks(networks)
    #checking_ips(ips)

    #closing file, do not touch
    my_file.close()

    print 'Completed. See the result in file output_sbl.log'
