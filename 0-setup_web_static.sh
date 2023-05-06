#!/usr/bin/env bash
# Install Nginx if it's not already installed
if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared /data/web_static/current

# Create a fake HTML file for testing
echo "<html><body>Hello World!</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to the test release
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Set ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/listen 80 default_server;/a location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
