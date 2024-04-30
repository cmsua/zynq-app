# `zynq-app`

Tool to control services and power on a ZYNQ SoC via an HTTP server.

Reverse-engineered from [hexactrl-script](https://gitlab.cern.ch/hgcal-daq-sw/hexactrl-sw/-/tree/ROCv3/) based on endpoint data.

Contains 3 endpoints: `/command` (PUT), as well as `/i2c` and `/daq` (GET). The first allows the loading of firmware and rebooting of services while the second and third queries the status of services.

Install by running the following commands as `daq`:

```bash
# Clone repository
cd ~ && git clone https://github.com/cmsua/zynq-app.git
cd zynq-app

# Install Service
sudo cp zynq-app.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable zynq-app

# Start Service
sudo systemctl start zynq-app
```
