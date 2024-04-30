# `zynq-app`

Tool to control services on a ZYNQ SoC.

Reverse-engineered from [hexactrl-script](https://gitlab.cern.ch/hgcal-daq-sw/hexactrl-sw/-/tree/ROCv3/) based on endpoint data.

Contains 3 endpoints: `/command` (PUT), as well as `/i2c` and `/daq` (GET). The first allows the loading of firmware and rebooting of services while the second and third queries the status of services.

Run via `./venv/bin/python3 -m flask run --host 0.0.0.0 --port 8080`
