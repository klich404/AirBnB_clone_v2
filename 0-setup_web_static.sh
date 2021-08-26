#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static. It must

#install nginx not installed
sudo apt-get -y update
sudo apt-get -y install nginx

#create a lot of folders
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

#create a fake HTML
sudo chmod 777 /data/web_static/releases/test/index.html
sudo echo "Fake content" |sudo tee /data/web_static/releases/test/index.html

#create a simbolic link to data/web_static/releases/test/
sudo ln -sf data/web_static/releases/test/ /data/web_static/current

#ownership permitions
sudo chown -R ubuntu:ubuntu /data/

#update nginx configuration
sudo echo 'Holberton School' |sudo tee /var/www/html/index.nginx-debian.html
sudo echo "Ceci n'est pas une page" |sudo tee /usr/share/nginx/html/custom_404.html
sudo sed -i "/listen 80 default_server/a \\\terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t\t}" /etc/nginx/sites-available/default
sudo sed -i "/listen 80 default_server/a \\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default
sudo sed -i "/:80 default_server/ a \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}" /etc/nginx/sites-available/default

#restart nginx
sudo service nginx restart
