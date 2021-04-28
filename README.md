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

### AWS info
#### VPC
Virtual Private Cloud used to control a virtual network. Enables you to launch AWS resources in an isolated virtual network, such as EC2 instances.

#### Security Group
Security group acts as a virtual firewall for an EC2 instance to control incoming and outgoing traffic.

#### Subnet
A subnet is a logical subdivision of an IP network, a single subnet can have multiple ED2 instances.

#### Route Tables
Contains a set of rules called routes which are used to determine where network traffic from a subnet or gateway is directed.

#### Internet Gateway
Provide a target in VPC route tables for internet-routable traffic and perform network address translation (NAT) for instances that have a public IPv4 address

#### NACL
A Network ACL controls traffic to or from a subnet according to inbound and outbound rules. Additional (stateless) network level security.

#### Bastion instance
Used to access a private instance that is not connected to the Internet directly.

## Cloud computing
![alt text](https://trello-attachments.s3.amazonaws.com/603d18a548d66563a0707ac8/6080098145f54271d3cbcb46/0dd0819e753e8824916432f875838049/AWS_deployment_networking_security.png)
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

#### Create security groups
- Security group name `eng84_jordan_public_sg`
	- Inbound rule with `Type: "SSH", Source "My IP"` to SSH into machine
	- Inbound rule with `Type: HTTP | Source 0.0.0.0/0` if public for internet access

#### Create public NACL rules
- Inbound
	- 100 allows inbound HTTP 80 traffic from any IPv4
	- 110 allows inbound SSH 22 traffic from network over internet
	- 120 allows inbound return traffic from hosts on internet that respond to requests from subnet - TCP 1024-65535
- Outbound
	- 100 allow outbound HTTP port 80
	- 110 CIDR block allow 27017 for outbound Mongo DB server, destination subnet IP
	- 120 allow short lived ports between 1024-65535

#### Create private NACL rules
- Inbound
	- 100 allow port 27017 from public security group
	- 110 allow SSH from IP
- Outbound
	- Allow all outbound

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
- Select security group
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
- `sudo nano provision.sh` to open<br>
```sudo echo "server {<br>
	listen 80;<br>
	<br>
	server_name _;<br>
	<br>
	location / {<br>
		proxy_pass http://localhost:3000;<br>
        proxy_http_version 1.1;<br>
        proxy_set_header Upgrade \$http_upgrade;<br>
        proxy_set_header Connection 'upgrade';<br>
        proxy_set_header Host \$host;<br>
        proxy_cache_bypass \$http_upgrade;<br>
    }<br>
}" | sudo tee /etc/nginx/sites-available/default```
- `sudo ./provision.sh` to run automation
- `npm install` to correctly install npm
- `nodejs app.js` to run the app on the cloud

#### Work with database
- Add inbound rules for database to accept all from the public IP/App security group
- Need to SSH into private instance using public instance as a proxy
- `ssh -i ~/.ssh/DevOpsStudent.pem -o ProxyCommand="ssh -i ~/.ssh/DevOpsStudent.pem -W %h:%p ubuntu@app_ip" ubuntu@private_ip`
- Add temp rules to access the database to setup
	- Inbound rule for security group `Type: HTTP | Source: 0.0.0.0/0`
- `sudo echo "export DB_HOST=mongodb://private_ip:27017/posts" >> ~/.bashrc`
- `source ~/.bashrc`
- `nodejs seed.js` in seeds to run seed
