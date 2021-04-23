# Cloud Computing with AWS
## What is cloud computing?
Cloud computing is the delivery of computing services over the Internet. Examples of these services include servers, storage, databases, networking, software, ect.

## What are the benefits of cloud computing?
- Reduced IT costs
- Scalability
- Flexibility of work practices
- Access to automatic updates

## What is AWS?
Amazon Web Services (AWS) is a secure cloud services platform, offering access to server useage, database storage, content delivery, and other functionality.

## What are the advantages of AWS?
- Ease of use
- Diverse array of tools
- Unlimited server capacity
- Reliable encryption and security
- Flexibility and affordability

## Who in the industry is using AWS?
AWS is used by large companies for it's range of benefits, including:
- Netflix
- Twitch
- LinkedIn
- Facebook
- BBC

## Types of computing
- Public Cloud
  - Online, easily accessible
- Private Cloud / On prem (on the premises)
  - Offline, secure
- Hybrid (cloud and on premises)
  - Mix between public and private
  - Used in sectors such as banking for security

## Scaling
- Autoscaling (automatically changes based on demand)
- Scale up, improve existing resources/servers
- Scale out, buy more resources/servers

## Making AWS server
### Naming convention
Organisation, name, task (eg. Eng84 Jordan app)
### Security
- Security group works as firewall on instance level of machine
- Set specific IP to be able to access
- Keys can be required in addition to an accepted IP
### Architecture
#### Monolithic architecture
Traditional unified model all in one place. User interface and data access code are combined into a single program from a single platform. Self-contained and independent.
#### Microservices
Arranged an application as a collection of loosely coupled services. Fine-grained and lightweight protocols.

## Cloud computing
### Create an AWS server
#### Create VPC & Internet Gateway
- Create VPC named `eng84_jordan_vpc`
- IPv4 CIDR block `X.X.Y.Z/16`
	- `X.X` refers to the VPC
	- `Y` is the subnet
	- `Z` is the specific device
	- `/16` means look at only the first 16 bits (of 32), so ONLY the VPC
- Create Internet Gateway
- `eng84_jordan_gateway`
- Attach Internet Gateway to VPC
- Create root table for VPC

#### Create subnet
- Create subnets with names `eng84_jordan_app` and `eng84_jordan_db`
- IPv4 CIDR block `X.X.Y.Z/24`
	- Same as above meanings
	- `Y` must be different for each subnet
	- `/24` as we want the first 24 bits to inclue subnet
- Auto-assign IP `enable` for public subnet
- Add subnet connections to VPC root table

#### Create EC2 instance
- `Launch instance` to create the instance
- Choose desired virtual machine `Ubuntu 16.04`
- `t2 micro` instance type
- Select desired VPC and subnet
- Add tag for name of subnet
- Security groups name `eng84_jordan_use_sg`
	- Inbound rule with `Type: `SSH`, Source `My IP` to SSH into machine
	- Inbound rule with `Type: HTTP | Source 0.0.0.0/0` if public for internet access
- Confirm details and `launch`
- Choose key value pair for access

### Project deployment
#### Automation
- `scp -i ~/.ssh/DevOpsStudent.pem -r app/ ubuntu@ip:~/app/` while in app folder of project
- `scp -i ~/.ssh/DevOpsStudent.pem -r app/ ubuntu@ip:~/environment` in environment to copy automation

#### Open virtual machine and run app
- `ssh -i "DevOpsStudent.pem" ubuntu@ip` to run VM
- Convert dos2unix
	- `wget "http://ftp.de.debian.org/debian/pool/main/d/dos2unix/dos2unix_6.0.4-1_amd64.deb"` download dos2unix
	- `sudo dpkg -i dos2unix_6.0.4-1_amd64.deb` install dos2unix
	- `dos2unix db_provision.sh` convert dos file to unix
- `sudo nano provision.sh` to open
	- `sudo echo "server {
    listen 80;

    server_name _;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade \$http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host \$host;
        proxy_cache_bypass \$http_upgrade;
    }
}" | sudo tee /etc/nginx/sites-available/default`
- `sudo ./provision.sh` to run automation
- `npm install` to correctly install npm
- `nodejs app.js` to run the app on the cloud

#### Work with database
- Add inbound rules for database to accept all from the public IP
- Need to SSH into private instance using public instance as a proxy
- `ssh -i ~/.ssh/DevOpsStudent.pem -o ProxyCommand="ssh -i ~/.ssh/DevOpsStudent.pem -W %h:%p ubuntu@app_ip" ubuntu@private_ip`
- Add temp rules to access the database to setup
	- Inbound rule for security group `Type: HTTP | Source: 0.0.0.0/0`
- `sudo echo "export DB_HOST=mongodb://private_ip:27017/posts" >> ~/.bashrc`
- `source ~/.bashrc`
- `nodejs seed.js` in seeds to run seed
- 