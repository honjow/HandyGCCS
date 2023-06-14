#!/bin/bash
set -e
echo "Installing HandyGCCS..."
sudo pacman -Sy --noconfirm --needed < pkg_depends.list
< pip_depends.list xargs python3 -m pip install
echo "Enabling controller functionality. NEXT users will need to configure the Home button in steam."
sudo cp -Rv usr/* /usr
sudo udevadm control -R
sudo systemctl enable handycon && sudo systemctl start handycon
echo "Installation complete. You should now have additional controller functionality."
exit 0
