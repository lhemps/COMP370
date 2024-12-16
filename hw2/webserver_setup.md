How To Set Up Webserver:

1. Sign in to AWS and go to Lightsail
2. Create an instance:
    - instance location closest to where your data is stored will be fastest
    - Select platform -> Linux/Unix
    - Select blueprint -> OS only (I used Debian 12.6)
    - Change SSH key pair -> upload new -> select id_rsa public key
    - Select network type -> dual-stack
    - Select a size -> I went with the best of the free for 90 days (2GB ram, 60GB storage, 3TB transfer)
    -Identify your instance -> I changed it to COMP370
3. Get on VM and install Apache
    - used ssh through PuTTY
    - sudo apt install apache2
    - cd /var/www/html
    - sudo vim comp370_hw2.txt -> put whatever you want there

*Note: I can see my txt file by going to 3.96.150.225/comp370_hw2.txt but not on port 8008, I don't have time to figure that out lol