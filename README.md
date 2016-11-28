Flexiduck
=========

A [duckyscript](https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript) compatible Pi-Zero project, which utilises [nmap](https://nmap.org/) - in particular the [OS Detection](https://nmap.org/book/man-os-detection.html) features - to trigger OS-specific payloads.

## Payloads

The payloads are kept in the `payloads` directory, and are structured using the `cpe` output of `nmap`. The script `run.py` will extract the first OS match from the `nmap` scan, and iterate through the pieces of the `cpe` until a matching payload directory is found.

    cpe:/o:apple:mac_os_x:10.7

The parts that are used for iteration are everything after `cpe:/o:`, split by the `:` character. This allows you to target not only specific operating systems, but also different versions. The highest level matching directory is used, and all scripts within that directory built and executed in order. The above `cpe` subsequently matches the example payload, under the directory `payloads/apple/mac_os_x`.

## Setup

The included `setup.sh` script *should* get you ready to run out of the box. Simply clone this repo and run the `setup.sh` script. When you reboot the Pi Zero, the NIC and HID devices will be setup, an `nmap` scan fired against `1.0.0.10`, and any subsequent payloads will be triggered.

If you clone the repo to anywhere other than `/root/flexiduck`, you'll need to update the path in `boot.sh`, and `setup.sh`.

### Note

While I *believe* `setup.sh` should perform all the steps required to get this setup on a fresh Pi Zero, I have yet to test it fully. Your mileage may vary.

## Credits

- [android-keyboard-gadget](https://github.com/pelya/android-keyboard-gadget) - Lifted `hid-gadget-test` from here
- [duckhunter](https://github.com/byt3bl33d3r/duckhunter) - Used to parse `duckyscript` in to a usable bash script
- [hardpass-passwordmanager](https://github.com/girst/hardpass-passwordmanager) - Influence taken for HID setup
- [poisontap](https://github.com/samyk/poisontap) - Made me aware of the possibilities of the Pi Zero
