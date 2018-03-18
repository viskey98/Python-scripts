from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.hackerrank.com/')
html_source = browser.page_source
f = open('index.html','w')
f.write(html_source)
f.close()