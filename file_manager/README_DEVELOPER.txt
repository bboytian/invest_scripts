+----------------------------+
|File manager		     |
|author: Lee Tianli	     |
+----------------------------+

========================================================================
*DEVELOPER NOTES********************************************************
========================================================================

--- To do ---



--- pre-tests ---

=> able to ssh across internet

	-> ssh -p 22 pi@<public IP>

=> able to transfer file via scp

	-> required to create a ssh key on the client, the public key generated as to be added to the authorized_keys in the server (raspberry pi). This process has to be done manually

	-> https://www.digitalocean.com/community/tutorials/how-to-set-up-ssh-keys--2

	-> dynamic IP address is created to prevent IP address from showing on the bash script: lees-theparc-router.twilightparadox.com



========================================================================
*VERSION NOTES**********************************************************
========================================================================

v1.0.2

=> correcting bug in file_sender.sh, the directory for the host was invest 
instead of invest_scripts_repo

v1.0.1

=> correcting bug that makes file_receiver.py retrieve the mostoutdate file, just a simple index change

v1.0.0

=> file_receiver.py created for reaspberry

=> configuring cronjob, and seperate cronjob.txt for raspberry and for pa's mac

v0.1.0

=> file_sender.sh created

=> created a RUN.command file

=> configured cronjob


v0.0.0

=> km-home-mac sshkey generated, and placed in tian-home-rasp3bp ~/.ssh/authorized_keys

