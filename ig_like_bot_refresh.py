from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
import json

if __name__ == '__main__':
    ## 輸入刷新次數
    scroll_time = int(input("請輸入刷新次數："))
    post_count = 0
    driver = webdriver.Edge()
    driver.get('https://www.instagram.com/')
    driver.delete_all_cookies
    
    ## 輸入cookie登入
    sleep(3)
    with open('cookies.json', 'r') as f:
        cookies_list = json.load(f)
        for cookie in cookies_list:
            driver.add_cookie(cookie)
    driver.refresh()

    ## 成功登入後，跳出「是否開啟通知」，點「稍後再說」
    laterbutton = driver.find_element(By.CLASS_NAME, "_a9--._a9_1")
    laterbutton.click()

    sleep(10) #wait for page load


    ## find post (picture), use ActionChain to perform double click
    while(scroll_time!=0):      
        post_list = driver.find_elements(By.CLASS_NAME, "xp7jhwk")
        # print(post_list)
        if(len(post_list)!=0):                   
            for post in post_list:
                try:
                    ## scroll to post, movie mouse onto the post, then double click
                    actions = ActionChains(driver)
                    actions.pause(2).move_to_element(post).pause(1).click(post).perform()
                    # print("liked post", post)
                    post_count += 1
                except exceptions.WebDriverException as e:
                    print(e.msg)
        scroll_time -= 1
        if(scroll_time==0):
            break
        else:
            driver.refresh()
        sleep(10) # wait for page load
        
    print("total liked posts:, ", post_count)
    driver.quit()

