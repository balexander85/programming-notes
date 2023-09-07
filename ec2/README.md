# Setting up React App on Ec2 instance in AWS

### 1. Install Nginx:
```
sudo yum install nginx
```
### 2. Configure Nginx:
Create a configuration file for your React app in the
```
sudo vi /etc/nginx/conf.d/react-resume-app.conf
```
Add the following configuration (make sure to adjust paths and server_name as needed):
```
server {
    listen 80;
    server_name 54.208.141.83; # Replace with your domain name or public IP address

    location / {
        proxy_pass http://localhost:3000;
	proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        #root /home/ec2-user/react-resume-app/build; # Replace with the actual path to your website files
        #index index.html; # Specify the default index file (e.g., index.html)
    }
}
```
Create a symbolic link to enable the site:
```
sudo ln -s /etc/nginx/conf.d/react-resume-app.conf /etc/nginx/sites-enabled/
```
### 3. Test Nginx configuration:
```
sudo nginx -t
```

### 4. Reload Nginx
```
sudo systemctl reload nginx
```