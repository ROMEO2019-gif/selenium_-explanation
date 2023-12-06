#import modules from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Deprecated - no longer needed
chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver"

# creates chrome options objects
chrome_options = webdriver.ChromeOptions()
# add experimental option to  keep chrome open
chrome_options.add_experimental_option("detach", True)

# initialize chrome webdiver with the specified options 

# driver = webdriver.chrome
driver = webdriver.Chrome(options=chrome_options)

#define atest function named test_eight_components
def test_eight_components():
    
    # go to url 
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    
    # obtains the tittle of the web page
    title = driver.title
    #  title of the page is retrieved
    
    # assert that title is equal to "web form"
    assert title == "Web form"
    #  assertion is "web form" title
    
    # set an implicit wait time of 0.5 seconds
    driver.implicitly_wait(0.5)
    # webdriver waits for  0.5 seconds for elements to be found
    
    # locate text box element by its name ("my-text")
    text_box = driver.find_element(by=By.NAME, value="my-text")
    #  text box element is located by its name
    
    # locate the submit button element by its css selector ("button")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
   # submit button element is located by css selector
   
   # insert "selenium" into the text box
    text_box.send_keys("Selenium")
    # the text "selenium is entered into the text box
    
    #click on submit button
    submit_button.click()
    # the submit button is clicked
    
    #find the message element by its ID attribute ("message")
    message = driver.find_element(by=By.ID, value="message")
    # message element is located by its ID attribute
    
# get the text value of the message element
    value = message.text
    # the text value of the message element is retrieved
    
    #assert that the value is equal to "Received!"
    assert value == "Received!"
# assertion passed, the value is retrieved

    # quit Chrome browser window
    driver.quit()
    
    # chrome browser window is closed
    driver.close()

# call the test function
test_eight_components()
# the entire test function executed