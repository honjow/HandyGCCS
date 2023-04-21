cp -Rv usr/* /usr
udevadm control -R
systemctl daemon-reload
systemctl restart handycon