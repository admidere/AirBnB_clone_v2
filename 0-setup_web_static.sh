#!/usr/bin/env bash
# Install Nginx if it's not already installed
# Install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
  sudo apt-get update
  sudo apt-get install -y nginx
fi

# Create required directories
# Creates /data/web_static/releases/test/ if it doesn’t already exist
if ! [ -d /web_static/releases/test/ ]; then
	mkdir -p /data/web_static/releases/test/
fi

if ! [ -d /data/web_static/shared/ ]; then
	mkdir -p /data/web_static/shared/
fi

# Create a fake HTML file
echo "<html>
  <head>
    <title>Test Page</title>
  </head>
  <body>
    <h1>This is a test page for Nginx configuration</h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# /data/web_static/releases/test/ folder.
if [ -L /data/web_static/current ]; then
	rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Set ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "/^server {/a \\
	location /hbnb_static { \\
	alias /data/web_static/current/; \\
}" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
