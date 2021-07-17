'''
    selenium을 이용한 웹크롤링
    : 동적 크롤링
    : chrome 브라우저를 이용할 것이기 때문에 chromedriver를 설치했다

    1. 네이버 자동 로그인 기능
    2. 네이버 날씨 데이터 가져오기 기능
'''

from selenium import webdriver
driver = webdriver.Chrome("C:/Users/김유진/Downloads/chromedriver_win32/chromedriver.exe")

#1. 네이버 자동 로그인 기능
driver.get("https://www.naver.com")
b_log_in = driver.find_element_by_xpath("//*[@id=\"account\"]/a") #따옴표 \"
b_log_in.click()
w_id = driver.find_element_by_css_selector("#id")
w_id.click()
w_id.send_keys("yourid")
w_pw = driver.find_element_by_css_selector("#pw")
w_pw.send_keys("yourpassword")
ok = driver.find_element_by_xpath("//*[@id=\"log.login\"]")
ok.click()

#2. 네이버 날씨 데이터 가져오기 기능
driver.get("https://www.naver.com")
driver.maximize_window()
more = driver.find_element_by_css_selector("#NM_FAVORITE > div.group_nav > a")
more.click()
weather = driver.find_element_by_css_selector("#gnb > div.ly_service > div.group_service.NM_FAVORITE_ALL_LY > dl:nth-child(1) > dd:nth-child(2) > a")
weather.click()
location = driver.find_element_by_css_selector("#header > div.gnb_area > div > div.location_area > strong")
print("위치 :", location.text)
str = driver.find_element_by_css_selector("#content > div > div.card.card_today > div.today_weather > div.weather_area > p")
print(str.text)
driver.quit()