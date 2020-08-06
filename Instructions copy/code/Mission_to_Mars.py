import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup
import requests
import os
import time

def init_browser();
        if os.name=="nt":
                executable_path = {'executable_path': './chromedriver.exe'}
        else:
                executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
        return Browser('chrome', **executable_path, headless=False)

def scrape_news();
        browser = init_browser()
        news_data = {}
        news_url = 'https://mars.nasa.gov/news/'
        response = requests.get(news_url)

        soup = BeautifulSoup(response.text, 'html.parser')

        results = soup.find_all('div','content_title')
        news_title = results[0].getText()
        results_p = soup.find('div', class_='rollover_description_inner')
        news_p= results_p.getText()
        news_data ["title"] = news_title
        news_data ["paragraph"] = news_p
        browser.quit()
        return news_data

def scrape_mars();
        browser = init_browser()
        mars_data = {}
        mars_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(mars_url)

        button = browser.find_by_id('full_image')
        button.first.click()

        browser.is_text_present('more info', wait_time=2)
        button_2 = browser.click_link_by_partial_text('more info')

        soup_2 = BeautifulSoup(browser.html, 'html.parser')
        full_img = soup_2.find('figure', class_='lede')

        h1 = full_img.find('a')
        href = h1['href']

        img_url = 'https://www.jpl.nasa.gov/' + href

        mars_data ["img_url"] = img_url
        browser.quit()
        return mars_data

def scrape_twitter();
        browser = init_browser()
        twitter_data = {}
        twitter_url = 'ttps://twitter.com/marswxreport?lang=en'
        browser.visit(twitter_url)

        soup_3 = BeautifulSoup(browser.html, 'html.parser')
        weather = soup_3.find('p', class_ ='tweet-text', text = True).text
        twitter_data ["twitter_url"] = twitter_url
        browser.quit()
        return twitter_data

def scrape_facts();
        browser = init_browser()
        facts_data = {}
        facts_url = "https://space-facts.com/mars/"
        mars = pd.read_html(facts_url)

        mars_df = mars[0]
        mars_df.columns = ['Description', 'Value']
        mars_df.set_index('Description', inplace = True)

        html = mars_df.to_html()
        facts_data ["facts_url"] = facts_url
        browser.quit()
        return facts_data

def scrape_hemi();
        browser = init_browser()
        hemi_data = {}
        hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemi_url)

        soup_2 = BeautifulSoup(browser.html, 'html.parser')
        detail_box = soup_2.find('div', class_='collapsible results')
        img_details = detail_box.find_all('div', class_='item')
        title = detail_box.find('h3').text

        h2 = detail_box.find('a')
        href = h2['href']

        image_url_2 = 'https://astrogeology.usgs.gov/' + href

        hemisphere = []

        for individual in img_details:
                img_dict = {}
                
                title = individual.find('h3').text
                
                img_href = individual.find('a')['href']
                img_url_3 = 'https://astrogeology.usgs.gov/' + img_href
                browser.visit(img_url_3)
                full = BeautifulSoup(browser.html, 'html.parser')
                full_detail = full.find('img', class_='wide-image')['src']
                
                full_img_url = 'https://astrogeology.usgs.gov/' + full_detail
        
                hemisphere.append({"title": title, "img_url": full_img_url})
                
                browser.back()
        hemi_data ["hemi_url"] = hemi_url
        browser.quit()
        return hemi_data