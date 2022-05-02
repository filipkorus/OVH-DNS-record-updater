# OVH DNS record updater

## About

This script automates changing DNS records every time your ISP changes your self-hosted server's IP.

### Setting up

1. Add OVH account credentials to `credentials.py` file. You can get your API keys from [here](https://api.ovh.com/).
2. Install ovh API for Python with `pip install ovh` command.
3. Place this repo somewhere in your server, e.g. in `/opt/ip-updater` directory.
4. Run `crontab -e` command on your server to edit cron job list.
5. Add `*/1 * * * * python3 /opt/ip-updater/main.py` line to cron job file. This one will run the script every minute. Other cron schedule patterns can be easily generated at [crontab.guru](https://crontab.guru/) website.
