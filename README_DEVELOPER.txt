+----------------------------+
|pkg: invest_scripts	     |
|env: invest_scripts	     |
|author: Lee Tianli	     |
+----------------------------+

=======================================================================
*DEVELOPER NOTES*******************************************************
=======================================================================


--- To do ---

=> run update pip for papa

=> write sginvestors api for target price. Official implementation of this would require a new spreadsheet; and possibly renaming of the good old 'Stocks' spreadsheet to something like SGyahoofinance_API


--- future improvements ---

=> file sender: look into SSH tunneling to see if this option does not require setting a static IP address for the raspberry pi


=======================================================================
*PREREQUISITES*********************************************************
=======================================================================

=>mac only:

1. homebrew, brew install coreutils

	-> for realpath

2. google chrome browser, v78

3. Cron and terminal are enabled for 'Settings>Security and Privacy>Full Disk Access'


=>rasp only:

1. google chrome browser, v74


=>All platforms:

1. virtualenv; via pip3


=>User end:

1. telegram bot activated



======================================================================
*VERSION NOTES********************************************************
======================================================================


v1.3.0

=> mac patch for eln_tracker

   -> installation of python telegram api package

=> raspberry patch for eln_tracker

   -> installation of python telegram api package

   -> crontab configuration

=> update pip is to be run

=> requirements are frozen

=> RUN_ELN_TRACKER.command is operational

=> RUN_ELNREC_CLEARER.command is operational; wrapper for elntracker/elnrec_clearer.py


v1.2.0

=> seperated crontabs for papa's mac and raspberry, mainly to accomodate differences in file sending and receiving, cronjobs.all indicates all platform cronjobs in chronological order.

=> no patch is created, crontabs were updated manually

=> python package versions were saved in requirements.txt


v1.1.0

=> created virtual environment in ~/virtual_environments/invest_scripts

v1.0.0

=> migrating from conda to virtualenv

	-> conda removed manually from pa's laptop

	-> setting up virtualenv; folder is created in ~/virtual_environments/invest_scriptsinvest_scripts


v0.0.1


=> '. /opt/anaconda3/etc/profile.d/conda.sh' is added to bash_profile to enable conda command in bash scripts

=> turns out crontab has been failing on macbook (found through raspberry pi) because the cronjob has '%' character that has not been escaped.

	-> proper syntax would include $(date +"\%Y-\%m-\%d")



v0.0.0

=> supports >= v0.1.0 datastore_updater; with RUN file that saves cronlogs

=> created conda env: invest_scripts

=> crontab added RUN_DATASTORE_UPDATER.command
