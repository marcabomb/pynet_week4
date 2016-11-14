#!/usr/bin/env python
import pexpect
from getpass import getpass
import sys

def main():
    ip_addr = '184.105.247.71'
    username = 'pyclass'
    password = getpass()
    port = '22'
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    #ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('ssword:')
    ssh_conn.sendline(password)
    ssh_conn.expect('#')
    ssh_conn.sendline('config t')
    ssh_conn.expect('#')
    ssh_conn.sendline('logging buffered 19999')
    print ssh_conn.before
    print ssh_conn.after
    ssh_conn.expect('#')
    ssh_conn.sendline('end')
    ssh_conn.expect('#')
    print ssh_conn.before
    print ssh_conn.after
    ssh_conn.sendline('show run | i logging')
    ssh_conn.expect('#')
    print ssh_conn.before
    print ssh_conn.after
if __name__ == '__main__':
    main()
