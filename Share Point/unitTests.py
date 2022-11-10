# Author: Samuel Liu
# Package: spScrape, Share Point Scraper
# References: spApplicantInfo.py, spScrape.py, Paste.py
# Description: testing file made to test individual scraping methods on edge cases
# of resumes that might break the system.
# 
# There is a test_doc.txt that you can use to dump resume text into 
# for single case testing

from spApplicantInfo import *
import os
import time
import pyautogui
import spacy
from Paste import *
import en_core_web_lg

def nameScrape_test():
    #open the test doc first
    path = 'test_doc.txt'
    path = os.path.realpath(path)
    #os.startfile(path)

    #read the file into the test rig
    try:
        with open('test_doc.txt', 'r') as f:
            text = f.read()
    except:
        text = 'ERROR'
    
    #call the scraper
    names = name_scrape(text)
    return names


def emailScrape_test():
    #open the test doc first
    path = 'test_doc.txt'
    path = os.path.realpath(path)
    
    


def main():
    nameScrape_test()
    print("Finished tests.")

if __name__ == "__main__":
    main()