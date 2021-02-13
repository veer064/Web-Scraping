%%time

### Data Dictionary

data_dict = {}
data_dict['Product Name'] = []
data_dict['MRP'] = []
data_dict['Price'] = []
data_dict['SKU'] = []
data_dict['Sub-Category'] = []

std_url = "https://intakes.in/product-category/"
#Product
for n in range(3, 4):
    #Page Number
    for i in range(1, 6):
        url = std_url+'/'+url_cat_part[n]+f'/page/{i}/'
        browser.get(url)
        time.sleep(2)
        #Item Number
        for q in range(1, 13):
            try:
                qv = browser.find_element_by_xpath(f'/html/body/div[1]/main/div/div[2]/div/div[2]/div[{q}]/div/div[2]/div[1]/div[4]/a')
                browser.execute_script("arguments[0].click();", qv)
                time.sleep(2)
                #Product Name
                prod_name = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/a/h1').text
                data_dict['Product Name'].append(prod_name)

                #MRP & Price
                try:
                    mrp = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/p/del/span').text
                    data_dict['MRP'].append(float(mrp[1:].replace(',', '')))

                    price = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/p/ins/span').text
                    data_dict['Price'].append(float(price[1:].replace(',', '')))
                except:
                    mrp = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[2]/p/span').text
                    price = mrp
                    data_dict['MRP'].append(float(mrp[1:].replace(',', '')))
                    data_dict['Price'].append(float(price[1:].replace(',', '')))

                #SKU
                try:
                    sku = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[3]/span[1]/span').text
                    data_dict['SKU'].append(sku)
                except:
                    data_dict['SKU'].append('-')

                #Category & Sub-Category
                try:
                    categories = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[3]/span[2]').text
                    data_dict['Sub-Category'].append(categories.replace(', '+prod_cats_dict[n], '').replace(prod_cats_dict[n], '').replace('Categories:', '').strip())
                except:
                    try:
                        categories = browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/div/div[2]/div/div[3]/span').text
                        data_dict['Sub-Category'].append(categories.replace(', '+prod_cats_dict[n], '').replace(prod_cats_dict[n], '').replace('Categories:', '').strip())
                    except:
                        data_dict['Sub-Category'].append('-')
            #Back to main
                webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
                time.sleep(1)
            except:
                print(url,'>>>' , q)
        webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
        time.sleep(1)
