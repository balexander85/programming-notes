# Setting up React App on EC2 Instance in AWS

Welcome to the guide on setting up a production-ready React app on an Amazon Elastic Compute Cloud (EC2) instance within Amazon Web Services (AWS). Whether you're a developer looking to deploy your React application or simply curious about hosting web applications on AWS, this step-by-step tutorial will walk you through the process.

By the end of this guide, you will have your React app up and running on an EC2 instance, accessible to users on the internet. We'll cover everything from creating your EC2 instance to configuring Nginx as a reverse proxy and using pm2 for process management.

Let's get started on your journey to deploying your React app to the cloud!

## Create an Instance in AWS Console

1. Click `Launch instances` on [AWS EC2 Console](https://us-east-1.console.aws.amazon.com/ec2/home).
2. Enter a name like `DadGumWebServer`.
3. Select Amazon Machine Image `Amazon Linux 2023 AMI`.
4. Choose Instance type `t2.micro`.
5. Select a Key pair for SSH access.
6. Configure Network Settings:
   - Create a security group.
   - Allow SSH from `My IP`.
   - Allow HTTPS and HTTP traffic from the internet.
7. Keep the default storage configuration.
8. Click `Launch instance`.

## Install Dependencies
To set up your EC2 instance for hosting a React app, you'll need to install a few dependencies. You can do this by running the following commands:
```bash
sudo yum check-update
sudo yum update
sudo yum install git nodejs npm nginx -y
```
After successfully installing these dependencies, you'll be all set to proceed with serving your React app. You have the option to use a Node.js-based web server like serve or express. Below is an example of installing serve globally if it's not already installed:
```bash
sudo npm install -g serve
```

## Install Project

> **Note**: You will not need to do this if your project is public
```bash
ssh-keygen
cat .ssh/id_rsa.pub # paste this value to git repo https://github.com/settings/ssh/new
```

#### Clone project

```bash
git clone git@github.com:balexander85/react-resume-app.git
```

#### Install Project Dependencies
```bash
# Navigate to your React app directory
cd react-resume-app/
npm ci
```

#### Build your React app
This command will generate optimized production-ready static files in the build directory of your project.
```bash
npm run build
```

#### Serve your React app
You can use a Node.js-based web server like serve or express to serve your React app. Here's an example using serve:
> First, install serve globally (if not already installed): `sudo npm install -g serve`
```bash
serve -s build -l 3000
```
You will not be able to access web app until after setting up Nginx or maybe opening port 3000 on your Ec2 instance.

## Setup Nginx
> **Note**: If you haven't already, install nginx. `sudo yum install nginx`

Create a configuration file for your React app in the
```bash
sudo vi /etc/nginx/conf.d/react-resume-app.conf
```

Add the following configuration (make sure to adjust paths and server_name as needed):
```bash
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
```bash
sudo mkdir /etc/nginx/sites-enabled/ # if sites-enabled does not exist
sudo ln -s /etc/nginx/conf.d/react-resume-app.conf /etc/nginx/sites-enabled/
```

#### Test Nginx configuration:
```bash
sudo nginx -t
```

#### Start or reload Nginx
```
sudo systemctl start nginx
sudo systemctl reload nginx
# to make sure nginx starts at boot
sudo systemctl enable nginx
```

## Setup pm2

A commonly used tool for managing Node.js processes is pm2. pm2 provides more advanced process management features, including automatic restarts on crashes and better log management. To use pm2:
> **Note**: If you haven't already, install pm2 globally. `sudo npm install pm2 -g`

```bash
# Start your React app using serve with the following command.
serve -s build -l 3000 & # The & at the end of the command runs serve in the background.
# Now, you can use pm2 to manage the serve process.
pm2 start "serve -s build -l 3000" --name "react-resume-app"
# First, you need to save your current PM2 process list, which includes your application, so that it can be restored after a reboot.
pm2 save
# Finally, restart PM2 with the saved processes
pm2 resurrect
```

Next, generate a startup script:
```bash
pm2 startup # copy sudo command
# This command will provide you with a command to run (usually sudo),
# which will create a startup script to start PM2 at boot. Run the command provided.
sudo env PATH=$PATH:/usr/bin /usr/local/lib/node_modules/pm2/bin/pm2 startup systemd -u ec2-user --hp /home/ec2-user
```
