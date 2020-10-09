+----------------------------+
|pkg: datastore_updater	     |
|author: Lee Tianli	     |
+----------------------------+

=======================================================================
*DEVELOPER NOTES*******************************************************
=======================================================================

--- To do ---

=> API depreciation catching, and notification via telegram bot

   -> catch 'MISSING' table element, and notify developer and user of the column and row

   -> will have to consider how to manage for larger set of 'MISSING'


--- package list ---

1. bs4
2. requests
3. selenium
4. numpy
5. pandas
6. openpyxl
7. xlrd; for pandas


=======================================================================
*VERSION NOTES*********************************************************
=======================================================================

v1.2.0

=> There is some cookie problem with the driver when trying to pull the
stock, infact it's coupled together with other stocks

=> the brute force but slow solution is to initialise the driver before 
every pull, thus driver initialisation is made into a function

v1.1.2

=> chromedriver v83 for mac64 is added

=> filtering webdriver str_lst for only 'chromedriver files'


v1.1.1

=> chromedriver v80 for mac64 is added

=> the __main__ now sends out an error message to the developer when
the chrome driver is outdated, it also raises a DeprecationWarning

=> driver version exception added so that it will try all versions of
drivers and finish the loop


v1.0.1

=> realpath is added to RUN.command script

=> $wd of $wd/datastore_updater is removed from python3 -m command

v1.0.0

x=> including different stock markets in datastore.xlsx

	-> format has changed, to accomodate future column adjustments, the variable 'keywordstart_ind' was introduced


v0.2.1

=> datastore.xlsx/Stocks/Beta (5Y Monthly) -> Beta (5Y monthly), API deppreciation

=> better catching of API deppreciation with 'AttributeError'

=> chromedriver is added for raspberry

	-> there is a special workaround for this under __main__.chrom_options

v0.2.0

=> __main__.py is converted into a function; datastore_updater.main

=> Stock sheet is now cleared before pasting of DataFrame into the workbook


v0.1.0

=> creating an excelwriter for pandas.DataFrame.to_excel, so that it now appends to data instead of rewriting everything

=> working complete API for sg yahoo finance, text based search for statistics



v0.0.0

=> working API for sg yahoo finance, the code specifically works with datastore.xlsx, sheet: Stock, but can be expanded in the future

=> now working with pandas dataframe, pasting is over the old sheet, without clearing the previous sheet

=> API is simply a dictionary with 3 main components, easily changed by observing the html in google chrome.

	-> note that what we see on chrome might not tally with what we get with requests, as such, a boolean to switch to chromewebdriver is available in __main__.py

