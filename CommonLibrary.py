from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.Screenshot import Screenshot
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
#from datetime import datetime
import re
import os
import random
from operator import contains
from itertools import imap, repeat
import calendar
import csv
import time
import calendar
from datetime import datetime, time, date
from datetime import datetime,timedelta
from datetime import date
import time
import os
import xlrd
from random import randint
from urllib2 import Request, urlopen, URLError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 
from sys import exit
import xml.etree.ElementTree as ET
from datetime import datetime
import cx_Oracle
from selenium import webdriver

from xml.dom.minidom import parse, parseString
import xlwt
import xlsxwriter
from xlutils.copy import copy
from testrail import *
from datetime import datetime
from datetime import datetime


class CommonLibrary:

        def __init__(self):
                pass
        def get_chrome_browser_options(self,filePathToDownload):
            """ This keyword will return chrome options """
            dc = DesiredCapabilities.CHROME
            dc['loggingPrefs'] = {'browser': 'ALL'}
            dictionary= {'profile.default_content_settings.popups':'0'} 
            chrome_options = Options()
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("test-type")            
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument('--ignore-certificate-errors')
            profile = {"download.default_directory": filePathToDownload,
           "download.prompt_for_download": False,
           "download.directory_upgrade": False,
           "plugins.plugins_disabled": ["Chrome PDF Viewer"]}
            chrome_options.add_experimental_option("prefs", profile)
            chrome_options=chrome_options
            return chrome_options
        
        def click_element_using_javascript(self,locator,n=1):
                    """Returns 'True' if the element clciking by Java Script with the 'locator' in the corresponding page else returns 'False' """

                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    try:
                        elements = selenium._element_find(locator,False,True)
                        selenium._current_browser().execute_script("arguments[0].click();", elements[n-1])
                        return True
                    except Exception as exp:
                        print "not clcikable by JS, "+ str(exp)
                        return False

        def capture_page_screenshot_and_log(self, out_folder, screenshot_name=None):
            """ take a screen shot and log browser, driver and server entries """
            out_folder = out_folder or '.'
            selenium = BuiltIn().get_library_instance('Selenium2Library')
            selenium.capture_page_screenshot(filename=screenshot_name+'.png')
            status = self.capture_console_log(out_folder)
            return status
                        
        def Capture_whole_screen_and_log(self, out_folder, screenshot_name="Screenshots"):
            """ take entire window screen shot and log browser, driver and server entries """
            out_folder = out_folder or '.'
            secreenshot = BuiltIn().get_library_instance('Screenshot')
            selenium = BuiltIn().get_library_instance('Selenium2Library')
            secreenshot.take_screenshot(out_folder + os.path.sep + screenshot_name)        
            status = self.capture_console_log(out_folder)
            return status

        def capture_console_log(self,out_folder):
            selenium = BuiltIn().get_library_instance('Selenium2Library')
            browser = selenium._current_browser()
            print browser.name
           # ONLY FOR CHROME: log new browser console and driver entries if environment variable is not 'OFF'
            log_level = os.getenv('SELENIUM_LOG_LEVEL', 'OFF')
            if browser.name == 'chrome' and log_level != 'OFF':
                try:
                    with open(out_folder + os.path.sep + "browser.log", "a+") as data:
                        entries = selenium._current_browser().get_log('browser')
                        print "entries"
                        print entries
                        for entry in entries:
                            data.write(str(entry) + os.linesep)
                except:
                    print 'failed to append to browser.log file'
                try:
                    with open(out_folder + os.path.sep + "driver.log", "a+") as data:
                        entries = selenium._current_browser().get_log('driver')
                        for entry in entries:
                            data.write(str(entry) + os.linesep)
                except:
                    print 'failed to append to driver.log file'
            return True   


        def get_unique_id(self):
            """Returns Unique Value by adding Time Stamp"""
            #MYS-2512_Get_Unique_Values_Fix : Updated code to to get unique names based on timestamp with random number generation(to over come failures of test scripts run in parallel on same DB. )
            return 'sdt'+str(time.localtime().tm_year)+str(time.localtime().tm_mon)+str(time.localtime().tm_mday)+str(time.localtime().tm_hour)+str(time.localtime().tm_min)+str(time.localtime().tm_sec)+str(int(round(time.time() * 1000)))[-4:] + str(random.randint(int(0000),int(9999)))

        def get_time_stamp(self):
            """Returns the Current Date and Time
            """
            return datetime.now(est()).strftime('%a %m/%d/%Y %I:%M %p')
        def mouse_move(self, locator):
            """Moves the Mouse to the 'locator'"""
            selenium = BuiltIn().get_library_instance('Selenium2Library')
            selenium.mouse_over(locator)
        
            
        def verify_element_present(self,locator):
            """Returns 'True' if the element found with the 'locator' in the corresponding page else returns 'False'
            """
            selenium = BuiltIn().get_library_instance('Selenium2Library')
            bStatus = selenium._is_element_present(locator)
            if bStatus != True:
                    selenium.capture_page_screenshot()                    
            return bStatus

        def verify_element_visible(self,locator):
            """ Returns 'True' if the element visible with the 'locator' in the corresponding page else returns 'False' """
            selenium = BuiltIn().get_library_instance('Selenium2Library')
            #Updated code to handle stale element kind of exceptions and to return a staus value.  
            try:
                    bStatus = selenium._is_visible(locator)
            #MYS-3191:Removed specific exception statement in block,inorder to handle all kind of exceptions.
            except:
                    bStatus= False
            if bStatus !=True:
                    selenium.capture_page_screenshot()
            return bStatus
        def validate_the_sheet_in_ms_excel_file(self,filepath,sheetName):
            """Returns the True if the specified work sheets exist in the specifed MS Excel file else False"""
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            sStatus=False        
            if sheetName==None:
                return True
            else:
                for sname in snames:
                    if sname.lower()==sheetName.lower():
                        wsname=sname
                        sStatus=True
                        break
                if sStatus==False:
                    print "Error: The specified sheet: "+str(sheetName)+" doesn't exist in the specified file: "+str(filepath)
            return sStatus

        
        def get_current_date(self):
            """ Returns the current date in the format month date year"""
            cdate = datetime.now()
            return cdate.strftime("%m/%d/%Y")

        def get_future_or_past_date_from_now(self,noofdays=1):
            """Returns future(+days) / past(-days) date based on the given number of days(for past date give -ve integer for no of days)"""
            cdate = datetime.now()
            frpdate = cdate + timedelta(int(noofdays))
            frpdate = frpdate.strftime("%m/%d/%Y")
            return frpdate

        def string_should_contain(self,string,substring):
            """Returns True if The string contains substring else False' """
            ind=string.find(substring)
            if ind>=0:
                return True
            return False

        def click_on_element(self,locator,msg=''):
            selenium = BuiltIn().get_library_instance('Selenium2Library')
            #bStatus = selenium.wait_until_element_is_visible(locator,5,msg)
            self.mouse_move(locator)
            selenium.focus(locator)
            selenium.click_element(locator)
            #if bStatus != False:
             #      selenium.maximize_browser_window()
             #      time.sleep(2)
             #      self.mouse_move(locator)
             #      selenium.focus(locator)
             #      selenium.click_element(locator)
             #      return True
            #else:
             #      return False        

        def get_ms_excel_row_values_into_dictionary(self,filepath,rowNumber,sheetName=None):
            """Returns the dictionary of values given row in the MS Excel file """
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            dictVar={}
            if sheetName==None:
                sheetName=snames[0]      
            if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
                return dictVar
            worksheet=workbook.sheet_by_name(sheetName)
            noofrows=worksheet.nrows
            dictVar={}
            headersList=worksheet.row_values(int(0))
            print 'headersList'
            print headersList
            rowValues=worksheet.row_values(int(rowNumber)+1)
            for rowIndex in range(0,len(rowValues)):
                dictVar[str(headersList[rowIndex])]=str(rowValues[rowIndex])
            return dictVar

        def get_ms_excel_row_values_into_dictionary_based_on_key(self,filepath,keyName,sheetName=None):
            """Returns the dictionary of values given row in the MS Excel file """
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            dictVar={}
            if sheetName==None:
                sheetName=snames[0]      
            if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
                return dictVar
            worksheet=workbook.sheet_by_name(sheetName)
            noofrows=worksheet.nrows
            dictVar={}
            headersList=worksheet.row_values(int(0))
            for rowNo in range(1,int(noofrows)):
                rowValues=worksheet.row_values(int(rowNo))
                if str(rowValues[0])!=str(keyName):
                    continue
                for rowIndex in range(0,len(rowValues)):
                    cell_data=rowValues[rowIndex]
                    cell_data=self.get_unique_test_data(cell_data)
                
                    dictVar[str(headersList[rowIndex])]=str(cell_data)
            return dictVar

        def get_unique_test_data(self,testdata):
            """Returns the unique if data contains unique word """
            testdata=str(testdata)
            timestamp=self.get_current_date_with_time()
            testdata=testdata.replace("unique",timestamp)
            testdata=testdata.replace("Unique",timestamp)
            return testdata

        def get_current_time(self):
            """Return the Current date value"""
            return time.strftime("%H-%M-%S")

        def get_current_time_stamp(self,bStatus=True):
            """Return the Current date value"""
            ts=datetime.now()
            if bStatus==True:
                    ts=(str(ts).split(".")[0]).replace("-","").replace(":","").replace(" ","")
            else:
                    ts=(str(ts).split(" ")[1]).replace(".","").replace(":","")
                    n=randint(1,99)
                    ts=str(ts)+str(n)
            return ts

        def get_ms_excel_column_values_into_list_by_column_name(self,filePath,sheetName,columnName):
            """ It retuen the list of registration codes"""
            workbook = xlrd.open_workbook(filePath)
            columnName=str(columnName)
            worksheet = workbook.sheet_by_name(sheetName)
            noofrows = worksheet.nrows
            headersList = self.get_ms_excel_row_values_into_list(filePath,int(1),sheetName)
            colIndex = headersList.index(columnName)
            columnIndex = int(colIndex)+1
            columnValues = []
            for rowNo in range(1,int(noofrows)):
                rowValues=worksheet.row_values(int(rowNo))
                columnValues.append(rowValues[colIndex])
            return columnValues
        
                # Designed a new keyword to handle DOM exceptions.
        def wait_for_element_visible(self,locator,timeout=None,message=''):
                    """Returns 'True' if the element visible with the 'locator' in the corresponding page else returns 'False' base timeout
                    """
                    #Update to handle errors with failure message text formatting for unknown ASCII characters included in parsed message.
                    message = message.encode('ascii','ignore')
                    if(timeout == None):
                        timeout = "30s"
                    selenium = BuiltIn().get_library_instance('Selenium2Library')
                    for iCounter in range(1,3):
                        print "iCounter: "+str(iCounter)
                        try:
                            selenium.wait_until_page_contains_element(locator,timeout)
                            selenium.wait_until_element_is_visible(locator,timeout)
                            return True
                        except:
                            if(len(message)>0):
                                print "Error Message:" +str(message)
                            print "ValueError: Element locator "+str(locator) +" did not visible within "+str(timeout) +" time out"
                            print "locator: "+str(locator)
                    return False
        def get_ms_excel_multiple_row_values_into_dictionary_list_based_on_key(self,filepath,keyName,sheetName=None):
            """Returns the dictionary of values given row in the MS Excel file """
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            if sheetName==None:
                sheetName=snames[0]      
            if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
                return dictVar
            worksheet=workbook.sheet_by_name(sheetName)
            noofrows=worksheet.nrows
            listDict = {}
            size = int(0);
            headersList=worksheet.row_values(int(0))
            for rowNo in range(1,int(noofrows)):
                dictVar={}
                rowValues=worksheet.row_values(int(rowNo))                
                if str(rowValues[0])!=str(keyName):
                    continue
                size = size+1		
                for rowIndex in range(0,len(rowValues)):
                    cell_data=rowValues[rowIndex]
                    cell_data=self.get_unique_test_data(cell_data)                
                    dictVar[str(headersList[rowIndex])]=str(cell_data)
                listDict[size] = dictVar
            return listDict
        def return_If_Dictionary_Contains_Key(self, dictionaryName, respectiveKey):
            """Returns value from dictionary if it contains the given key else returns null by handling the exception"""
            if respectiveKey in dictionaryName:
               return dictionaryName[respectiveKey]
            return None
        def get_random_choice_from_list(self,numberslist):
                value = random.choice(numberslist)
                return value
        
        def get_last_day_of_current_month(self):
                i = datetime.now()
                year = i.year
                month = i.month                     
                lastday = calendar.monthrange(year,month)
                slash = "/"
                dateString = "".join((str(month),slash,str(lastday[1]),slash,str(year)))
                return dateString
        def get_current_date_without_leading_zeros(self):
                date='{dt.month}/{dt.day}/{dt.year}'.format(dt = datetime.now())
                return date
        def get_current_date_with_time(self):
            """Return the Current date with time(YYMMDD_HHMMSS)"""
            return time.strftime("%Y%m%d_%H%M%S")
        def get_current_date_format(self):
                """Return the system date with required format"""
                currentDT = datetime.now()
                i=currentDT.strftime("%m/%d/%Y")
                j=currentDT.strftime("%H:%M:%S")

                date_str = i+" "+j
                print date_str

                return date_str
        def get_browser_version_name(self):
                """Return browser version """
                browser = request.user_agent.browser
                version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
                platform = request.user_agent.platform
                uas = request.user_agent.string

                if browser and version:
                        browser = request.user_agent.browser
                        version = request.user_agent.version and int(request.user_agent.version.split('.')[0])
                        print version
                return version
        def get_browsers_name(self):
                """Return browser name"""
                driver = self.driver
                version = driver.capabilities['version']
                print version
                return version
        def connect_to_STOP_Database(self,query,dbname,username,password):
                """ connnet to the Database"""
                try:
                        connection = cx_Oracle.connect(''+str(username)+'/'+str(password)+'@'+dbname+'')
                        cursor = connection.cursor()
                        cursor.execute(query)
                        for row in cursor:
                                print (row)
                        return row
                        connection.close()
                except:
                        return None
        def connect_to_STOP_Database_to_list(self,query,dbname,username,password):
                try:
                        connection = cx_Oracle.connect(''+str(username)+'/'+str(password)+'@'+dbname+'')
                        cursor = connection.cursor()
                        cursor.execute(query)
                        
                        samplelist=[]
                        for row in cursor:
                                #print (row)
                                samplelist.append(row)
                        
                        return samplelist
                        connection.close()
                except:
                        return None
        def get_current_date_with_year(self):
                '''get current date with the year(four digit)'''
                currentDT = datetime.now()
                current_date=currentDT.strftime("%d-%m-%Y")
                print current_date
                return current_date
        def process_close(self,browsername):                
                '''kill the browser instance '''
                if browsername.lower()=='gc' or browsername.lower()=='googlechrome' or browsername.lower()=='chrome':
                        os.system("taskkill /f /im chromedriver.exe")
                if browsername.lower()=='firefox' or browsername.lower()=='ff':
                        os.system("taskkill /f /im geckodriver.exe")
                if browsername.lower()=='ie' or browsername.lower()=='internetexplorer':
                        os.system("taskkill /f /im IEDriverServer.exe")
                if browsername.lower()=='edge':
                        os.system("taskkill /f /im MicrosoftWebDriver.exe")
        def get_random_number_in_given_range(self,start,stop):
                """ Returns the random from given range"""
                return random.randint(int(start),int(stop))
        def read_data_from_output_xml_file(self,outputDirPath):
                """Return testcaselist from output.xml"""
            
                #outputDirPath='C:\\SDT\\09-Jan-2018\\RobotFramework\\CodeIntegration\\Veritracks\\Results\\02-NON-STOPapplication\\gc_201801161603'
                reportdir = str(outputDirPath)
                filepath= reportdir + '\\output.xml'
                #print filepath
                xmldoc = parse(filepath)
                #print xmldoc
                itemlist = xmldoc.getElementsByTagName('suite')
                #print itemlist
                criticaltests=[]
                noncriticaltests=[]
                tc=xmldoc.getElementsByTagName('total')[0].getElementsByTagName("stat")
                #print tc
                length = len(tc)
                #print length
                for i in range(0,len(tc)):
                    #print i
                    string=str(tc[i].toxml())
                    #print string
                    if string.find("pass")>0 and string.find("All Tests")>0:
                        ptestscount = tc[i].attributes['pass'].value
                        #print ptestscount
                    if string.find("fail")>0 and string.find("All Tests")>0:
                        ftestscount = tc[i].attributes['fail'].value
                        #print ftestscount
                ttestscount = int(ftestscount)+int(ptestscount)
                #print ttestscount
                finalList =[]
                testcaselist=[]
                testcaseresults= {}
                sample={}
                for suite in range(0,len(itemlist)-1) :
                    #print suite
                    suitename= itemlist[suite].attributes['name'].value
                    #print suitename
                    suitesource= itemlist[suite].attributes['source'].value
                    #print suitesource
                    if ('.txt' in suitesource)==False:
                        continue
                    tcs=itemlist[suite].getElementsByTagName('test')
                    #print tcs
                    for tc in range(0,len(tcs)):
                        testresult =[]
                        tcname=tcs[tc].attributes['name'].value
                        st=tcs[tc].getElementsByTagName('status')
                        tcstatus=st[len(st)-1].attributes['status'].value
                        #print tcstatus
                        #testresult.append(tcname)
                        #print testresult
                        #testresult.append(tcstatus)
                        #print testresult
                        #print tcname
                        testcaselist.append(tcname)
                        print testcaselist
                        testcaseresults ={tcname:tcstatus}
                        #testcaseresults[tcname]=[tcstatus]
                        #print testcaseresult
                        sample.update(testcaseresults)
                        #print sample
                        #print sample['Login with STOP application']
                        
                        #testcaseresults.append(testresult)
                        #print testcaseresult[tcname]
                #print testcaselist
                #print sample.keys
                return sample
                #print sample['Login with STOP application']
        def write_TC_status_into_excel(self,resultsdict,path,Sheet_name):
                """ write data into Excel"""
                rb=xlrd.open_workbook(path)
                sheet1= rb.sheet_by_name(Sheet_name)
                rowscount=sheet1.nrows
                print 'rowscount',rowscount
                print 'resultsdict',resultsdict
                wb=copy(rb)
                sheet = wb.get_sheet(Sheet_name)
                for cellval in range (rowscount-1):
                    #sheet = wb.get_sheet(0)
                    cellValue=sheet1.cell(cellval+1,2).value
                    print'cellValue', cellValue
                    dictvalue=resultsdict[cellValue]
                    print dictvalue
                    #print cellValue
                    
                    #sheet = wb.get_sheet(1)
                    #sheet.write(cellval+1,2,dictvalue.keys)
                    sheet.write(cellval+1,3,dictvalue)
                wb.save(path)
        def write_TC_names_into_excel(self,resultsdict,path,Sheet_name):
                
                rb=xlrd.open_workbook(path)
                testcase=[]
                testcase=resultsdict.keys()
                #print len(testcase)
                print testcase[1]
                #samplelist=[]
                #testcaselist=list(testcase)
                #print testcaselist[1]
               
                #print samplelist[1]
                sheet1= rb.sheet_by_name(Sheet_name)
                rowscount=sheet1.nrows
                print rowscount
                wb=copy(rb)
                for cellVal in range(rowscount-1):
                    sheet = wb.get_sheet(Sheet_name)
                    sheet.write(cellVal+1,2,testcase[cellVal])
                wb.save(path)

        #def update_tc_status_into_testrail(self,stausID,testcaseid,moduleID,comment_var):

        #def update_tc_status_into_testrail(self,stausID,testcaseid,moduleID):
        def update_TC_status_into_testrail(self,stausID,testcaseid,moduleID,comment_var):
                """update testcases status in testrail using TestRail API"""
                print stausID
                api = APIClient('https://stopllc.testrail.com/')
                #api.password = 'yq37NT/cwBVZdurV4eqV'
                api.password ='Planit@1234'
                api.user = 'gousya@sdtcorp.com'
                #case = api.send_get('get_case/1');
                #print case
                result = api.send_post(
                'add_result_for_case/'+str(moduleID)+'/'+str(testcaseid)+'',
                { 'status_id':stausID, 'comment': comment_var}
                )
         
                print(result)
        def get_id_and_status_from_excel(self,path,Sheet_name,moduleID):
                """ get data from Excel"""
                rb=xlrd.open_workbook(path)
                sheet1= rb.sheet_by_name(Sheet_name)
                rowscount=sheet1.nrows
                print rowscount
                testcasestatus={}
                testrailtcstatus={}
                for i in range(rowscount-1):
                    testrailid=sheet1.cell(i+1,1).value
                    print testrailid
                    tcstatus=sheet1.cell(i+1,3).value
                    print tcstatus
                    if tcstatus == 'PASS':
                        var = 1
                        print var
                        comment_var="Successfully Executed"
                    else:
                        var = 5
                        comment_var="Expected and actual results mismatch. Please look into the log attached to Jenkins results for more details"
                    testcaseresults ={int(testrailid):var}
                    testrailtcstatus.update(testcaseresults)

                    self.update_TC_status_into_testrail(var,testrailid,moduleID,comment_var)

                    #self.update_Tc_status_into_testrail(var,testrailid,moduleID)

                    #self.update_TC_status_into_testrail(var,testrailid,moduleID)

                print testrailtcstatus
                return testrailtcstatus
            

        def get_time_difference(self,devicetime):
                """ Return time difference between two dates"""
                a = datetime.now().replace(microsecond=0)
                print 'a',a
                b = datetime.strptime(devicetime, '%m/%d/%Y %I:%M:%S %p')
                hours_difference = abs(b - a).total_seconds() / 3600.0
                print hours_difference
                return hours_difference
        def remove_braces_from_list(self,list):
                a= str(list).strip('[]')
                print a
                return a
        def converting_tuples_to_list(self,salist):
                finallist=[]
                samplelist=[]
                length=len(salist)
                print length
                b=[list(x) for x in salist]
                for i in range (0,length-1):
                        a=b[i]
                        c=self.remove_braces_from_list(a)
                        #print c
                        finallist.append(c)
                        #print finallist
                #print 'sample',finallist[0]
                #f=[list(x) for x in finallist]
                for j in range(0,length-1):
                        d=finallist[j]
                        #print"dam", d
                        e=d.split(",")
                        f=e[1]
                        #print "eee",f
                        samplelist.append(f.strip())
                print samplelist

                return samplelist
                        
                        
                #return finallist
                        
                        #print b[1]
                #a=b[1]
                #print a[0]
                #return
        def create_new_test_run(self,suiteId,name,assignedToId):
                """ create new testrun in Testrail and returns testrun id"""
                api = APIClient('https://stopllc.testrail.com/')
                api.password = 'Planit@1234'
                api.user = 'gousya@sdtcorp.com'
                add_tes_run=api.send_post('add_run/1&is_completed=0',
                {"suite_id": suiteId,
                "name": name,
                "assignedto_id": assignedToId,
                "include_all":True,
                "case_ids":[]})
                testrun_id=add_tes_run['id']
                print "add_tes_run",testrun_id
                return testrun_id
        def validate_the_sheet_in_ms_excel_file(self,filepath,sheetName):
            """Returns the True if the specified work sheets exist in the specifed MS Excel file else False"""
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            sStatus=False        
            if sheetName==None:
                return True
            else:
                for sname in snames:
                    if sname.lower()==sheetName.lower():
                        wsname=sname
                        sStatus=True
                        break
                if sStatus==False:
                    print "Error: The specified sheet: "+str(sheetName)+" doesn't exist in the specified file: "+str(filepath)
            return sStatus


        def get_ms_excel_file_rows_count(self,filepath,sheetName=None):
            """Return The Total No Rows In MS Excel File Using The Specified File filepath"""
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            if sheetName==None:
                sheetName=snames[0]      
            if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
                return -1
            worksheet=workbook.sheet_by_name(sheetName)
            return worksheet.nrows


        def get_ms_excel_row_values_into_list(self,filepath,rowNumber,sheetName=None):
            """Returns the list of values given row in the MS Excel file """
            workbook = xlrd.open_workbook(filepath)
            snames=workbook.sheet_names()
            tempList=[]
            if sheetName==None:
                sheetName=snames[0]      
            if self.validate_the_sheet_in_ms_excel_file(filepath,sheetName)==False:
                return tempList
            worksheet=workbook.sheet_by_name(sheetName)
            noofrows=worksheet.nrows
            tempList=[]
            for rowno in range(0,noofrows):
                row=worksheet.row(rowno)
                for colno in range(0,len(row)):
                    cellval=worksheet.cell_value(rowno,colno)
                    if int(rowNumber)==int(int(rowno)+1):
                        tempList.append(cellval)
            return tempList

        
            

                
                

            
        
    
                          
                
                
                
        
       

a = CommonLibrary()
a.get_current_date()

#date=a.get_current_date()
#print date
    
#suiteId="170"
#name="name"
#assignedToId="18"
#a.create_new_test_run(suiteId,name,assignedToId)
#print a
#a.connect_to_STOP_Database
#browsername = 'Chrome'
#ab =a.get_browser_version('Chrome')
#print ab
#query = "SELECT UP.VALUE FROM TRAIN1_DAPI.USERPERMISSIONREAD UP INNER JOIN VT_MASTER_DAPI.PERMISSION P ON UP.PERMISSIONID=P.PERMISSIONID INNER JOIN VT_USER.APP_USER VUP ON UP.USERID=VUP.USER_ID WHERE VUP.USER_LOGIN='U_20180329_065952'"
#query="SELECT P.NAME,UP.VALUE FROM TRAIN1_DAPI.USERPERMISSIONREAD UP INNER JOIN VT_MASTER_DAPI.PERMISSION P ON UP.PERMISSIONID=P.PERMISSIONID INNER JOIN VT_USER.APP_USER VUP ON UP.USERID=VUP.USER_ID WHERE VUP.USER_LOGIN='U_20180329_065952'"
#dbname = 'c2dbx00_autotest'
#username='autotest'
#password='Au5oT3st'
#db=a.connect_to_STOP_Database_to_list(query,dbname,username,password)
#print db
#salist=db
#c=a.converting_tuples_to_list(salist)
#print c
#e=[[2], [2], [2], [2], [2], [2], [1], [1], [2], [1], [2], [2], [2], [2], [1], [1], [0], [1], [2], [2], [1], [2], [1], [2], [2], [2], [1], [2], [1], [2], [1], [1], [1], [2], [1], [1], [2], [1], [1], [2], [2], [1], [1], [1], [2], [2], [2], [1], [2], [1], [1], [2], [2], [1], [2], [2], [2], [2], [2], [1]]
#d=a.converting_tuples_to_list(e)
#print d

#moduleID='185'
#Sheet_name='FirstHour_edge'
#outputDirPath='C:\\Codeintegration\\Results'
#path = 'C:\\SDT\\19-03-2018\\RobotFramework\\CodeIntegration\\Automation_Scripts\\TestData\\FirstHour.xls'
#resultsdict=a.read_data_from_output_xml_file(outputDirPath)
#print resultsdict
#a.write_tc_names_into_excel(resultsdict,path)
#a.write_tc_status_into_excel(resultsdict,path,Sheet_name)
#a.api_calls()
#a.get_id_and_status_from_excel(path,Sheet_name,moduleID)
#a.update_tc_status_into_testrail()


#tclist=[u'Logon to application with Google Chrome web browser', u'Create a new Agent Profile', u'Create a new Enrollee Profile', u'Create a new Victim profile', u"Editing a Profile's picture", u'Assign Enrollee on Blutag Device', u'Unassign Enrollee from a BluTag', u'Run a Spatial Search for the Address', u'Verify Dashboard Screen', u'Verify Enrollees Screen', u'Verify Events Screen', u'Verify Zones Screen', u'Verify Analysis Screen', u'Verify Reports Screen', u'Verify Inventory Screen', u'Verify Agents Screen', u'Verify assigned device for last contact date/time']
#filename='firsthour_screenshots'
#a= copyscreenshot()
#columnvalues=a.copy_screenshots_into_excel(filename,tclist)
#print columnvalues
