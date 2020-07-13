# environment-setup: Linux-Ubuntu

## python setup

### Installing pip for Python 3
Update the package index:
<code>$ sudo apt update</code> 

Install pip for Python 3:
<code>$ sudo apt install python3-pip </code>

Check instalation:
<code>$ pip3 --version</code>

## Generation and adding the ssh key
Check if there is any key ssh key:
`$ ls ~/.ssh`

Adding a new rsa key in the ssh directory: 
`$ ssh-keygen -t rsa -b 4096 -C "moraru.mihai@hotmail.com"`

Show the new public ssh key:
`$ cat ~/.ssh/id_rsa.pub`

Add the key to GitHub

## Installing docker and docker compose
### Setup the repository
Update the apt package index and install packages to allow apt to use a repository over HTTPS:
```bash
$ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```
Add Docker’s official GPG key:
```bash
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
Verify that you now have the key with the fingerprint `9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88`, by searching for the last 8 characters of the fingerprint.
```bash
$ sudo apt-key fingerprint 0EBFCD88
```
Use the following command to set up the stable repository. To add the nightly or test repository, add the word nightly or test (or both) after the word stable in the commands below. 
```bash
$ sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```
## Install Docker Engine

```bash
 $ sudo apt-get update
 $ sudo apt-get install docker-ce docker-ce-cli containerd.io
```
Verify that Docker Engine is installed correctly by running the hello-world image.
```bash
$ sudo docker run hello-world
```
## Install Compose
Run this command to download the current stable release of Docker Compose:
```bash
$ sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
Apply executable permissions to the binary:
```bash
sudo chmod +x /usr/local/bin/docker-compose
```
Test the installation.
```bash
$ docker-compose --version
```


## asmple_subtitle1
### Sample_subtitle2
Explination:
<code>add code</code>
`add code`

