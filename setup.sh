apt-get update && apt-get install -y nmap build-essential isc-dhcp-server
echo "dwc2" >> /etc/modules
echo "libcomposite" >> /etc/modules
echo "dtoverlay=dwc2" >> /boot/config.txt
wget https://raw.githubusercontent.com/pelya/android-keyboard-gadget/master/hid-gadget-test/jni/hid-gadget-test.c
gcc -o /usr/bin/hid-keyboard hid-gadget-test.c
git clone https://github.com/byt3bl33d3r/duckhunter.git
cp config/dhcpd.conf /etc/dhcp/dhcpd.conf
cp config/interfaces /etc/network/interfaces
sed -i -e 's/^exit 0/\/root\/flexiduck\/boot.sh\nexit 0/g' /etc/rc.local
