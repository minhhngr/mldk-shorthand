# Jenkins

## Windows

TBD...

## Unix (MacOSX / Ubuntu / CentOS / WSL)

### Installation

#### WSL

(Brew)

- brew install jenkins-lts
- sudo nano /etc/systemd/system/jenkins.service
- Insert the following configuration
  ```text
    [Unit]
    Description=Jenkins Server
    After=network.target
    
    [Service]
    User=<username>
    ExecStart=/home/linuxbrew/.linuxbrew/bin/jenkins-lts --httpPort <port> --httpListenAddress=<http>
    Restart=always
    
    [Install]
    WantedBy=multi-user.target
  ```

- sudo systemctl daemon-reload
- sudo systemctl enable jenkins
- sudo systemctl start jenkins
