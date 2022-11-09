from page.base_base import BasePage

class Dashboard(BasePage):
    email_label= "//*[text()='E-mail']"
    email_input='//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div/input'
    name_input='//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[2]/div/div/input'
    surname_input='//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div/input'
    phone_input='//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[4]/div/div/input'
    phone_label='//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[4]/div/label'
    phone_label_2= "//*[text()='Phone']"
    club_input='//*[@id="__next"]/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input'
    right_leg='//*[@id="menu-leg"]/div[3]/ul/li[1]'
    left_leg='//*[@id="menu-leg"]/div[3]/ul/li[2]'
    submit_button='//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[1]/span[1]'
    clear_button='//*[@id="__next"]/div[1]/main/div[2]/form/div[3]/button[2]/span[1]'


