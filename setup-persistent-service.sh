#!/bin/bash -
sudo cp discord_invite_bot.service /etc/systemd/system/
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable discord_invite_bot.service
sudo systemctl start discord_invite_bot.service
