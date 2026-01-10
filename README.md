# INSTALLATION EXAMDNS

## install to root

- clone (or unzip) this repository as `root` into `/root`
- ln examdns/bin bin

## System DNS: System -> Settings -> General

- DNS Servers: Leer lassen oder machen
- check: Allow DNS server list to be overridden by DHCP/PPP on WAN
- check: Do not use the local DNS service as a nameserver for this system

## Unbound forward only: Services -> Unbound DNS -> Query Forwarding

- check: Use System Nameservers

## Unbound log queryies: Services -> Unbound DNS -> Advanced

- check: log Queries
- check: log Replies
- check: tag Queries and Replies

## Bundle alls DNS Traffic to unbound: Firewall -> NAT -> Port Forward

- redirect all DNS Traffic that targets "not this firewall":53 to 127.0.0.1:53

## DOH add Alias: Firewall -> Aliases -> Add

- Type: URL Table (IPs)
- Content Box: <https://raw.githubusercontent.com/crypt0rr/public-doh-servers/main/ipv4.list>

## DOH drop 443: Firewall -> Rules -> LAN

- reject 443 to the DOH alias

## NMAP CRON

- create /usr/local/opnsense/scripts/custom/nmap_cron.sh
- create /usr/local/opnsense/service/conf/actions.d/actions_nmap.conf
- run `service configd restart`
- create the cronjob with the gui

## host overrides

- router
- sense
- tplink

## UPLOADTHING runs under service user

- create 33.2/32 as Proxy ARP
- add firewall/nat port-forward from 33.2:80 to localhost:8000

## LOGIN: System -> Admin -> Settings

- enable ssh / root login
- enable sudo nopass
- enable serial console

## Optional: usb eth festschreiben

- /usr/local/sbin/usb_nic_rename.sh (chmod +x)
- /usr/local/etc/devd/usb_persist.conf

## ALIASES for .profile

- `alias ub='unbound-control -c /var/unbound/unbound.conf`
- `alias ut='tail -F /var/log/resolver/latest.log'`

## bash als login shell für root
