+----------------------------+
|eln_tracker		     |
|author: Lee Tianli	     |
+----------------------------+

=======================================================================
*DEVELOPER NOTES*******************************************************
=======================================================================




--- To do ---


--- developer notes ---

-> file only updates the rows containing 'Ki boolean' and 'Mature boolean', it does not retain any information from the 'rec:...' columns




--- packages required ---

1. numpy
2. openpyxl
3. pandas
4. telegram


=======================================================================
*VERSION NOTES*********************************************************
=======================================================================

v0.2.1

=> telegram message sender was made into an API, a main function is called, adding a layer of abstraction

v0.1.1

=> '*' is added to all stocks within the ELN for mature and KO events

v0.1.0

=> date formatting is included

=> elnrecords made to only carry over previous 'KI boolean' and 'Mature boolean'

=> elnrec_clearer.py and wrapper ../RUN_ELNREC_CLEARER.command is written to enable clearing of elnrecords. So that one can run a fresh run of eln_tracker.__main__

   -> might want to make eln_clearer a generic file in the future


v0.0.0

=> there is a stubborn bug, wb.remove(wb[sheet]) is unable to remove the 'Stock' sheet

=> files draws all old exisiting entries from previous eln record, not allowing for changes in the various factors or original prices.

   -> quick and dirty solution is to delete the current ELN sheet

   -> but this means that the next time you run eln_tracker, it will notify as new, since the previous booleans are all False (0)

=> RUN.command file is created

=> crontab is configured in cronjobs.rasp
