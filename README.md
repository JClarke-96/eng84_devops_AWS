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
- `Launch instance` to create the instance
- Choose desired virtual machine `Ubuntu 16.04`
- `t2 micro` instance type
- Select desired subnet `devops student`
- Auto-assign IP `enable`
- Add tag as name of machine `Key: Name`, `Value: eng84_jordan_use`
- Security groups name `eng84_jordan_use_sg`
- `Type: `SSH`, Source `My IP`
- Confirm details and `launch`
- Choose key value pair for access

### Project deployment
- `scp -i ~/.ssh/DevOpsStudent.pem -r app/ ubuntu@ip:~/app/` while in app folder of project
- `scp -i ~/.ssh/DevOpsStudent.pem -r app/ ubuntu@ip:~/provision.sh` in environment to copy automation
- `sudo ./provision.sh` to run automation
- `npm install` to correctly install npm
- `nodejs app.js` to run the app on the cloud