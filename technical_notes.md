# tech notes

## createmedium

VBoxManage createmedium disk --filename imgstick.vmdk --format VMDK --variant RawDisk --property RawDrive=/dev/zvol/img/sense

## nmap scan json output

`nmap -sn -n -PR -oX - 192.168.21.0/24 | python3 -c "import sys, json, xml.etree.ElementTree as ET; root=ET.fromstring(sys.stdin.read()); print(json.dumps([{'ip': h.find(\"./address[@addrtype='ipv4']\").get('addr'), 'mac': (h.find(\"./address[@addrtype='mac']\").get('addr') if h.find(\"./address[@addrtype='mac']\") is not None else None), 'vendor': (h.find(\"./address[@addrtype='mac']\").get('vendor') if h.find(\"./address[@addrtype='mac']\") is not None else None)} for h in root.findall('host')], indent=2))"`

## createmedium vbox

`VBoxManage createmedium disk --filename "Orbsmart_Raw.vmdk" --format VMDK --variant RawDisk --property RawDrive=/dev/zvol/rpool/orbsmart`

