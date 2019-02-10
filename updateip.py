import time
import requests
import socket

import secrets


def main():
    prev_ip = 'nothing'
    while True:
        ip = requests.get('https://ipv4.icanhazip.com').text
        print('ip is ' + ip)
        time.sleep(2)
        if prev_ip != ip:
            send_update_message(prev_ip, ip)
        prev_ip = ip


def send_update_message(old_ip, new_ip):
    hostname = socket.gethostname()
    msg = 'ip of %s has changed from %s to %s' % (hostname, old_ip, new_ip)
    print('Sending message "%s"' % msg)
    return requests.post(secrets.SLACK_WEB_HOOK, json={'text': msg})


if __name__ == '__main__':
    main()
