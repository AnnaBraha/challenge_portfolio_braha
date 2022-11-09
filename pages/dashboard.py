from page.base_base import BasePage

class Dashboard(BasePage):
    button_add_player="//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    button_change_language="//*[@id='__next']/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    button_change_language_Pol="// *[text() = 'Polski']"
    id_next="'//*[@id='__next']"
    Sign_out="//*[@id='__next']/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    Sign_out_2="//*[text()='Sign out']"
    Last_created_player="//h2/following-sibling::h6[1]"
    Main_page="//*[@id='__next']/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    Main_page_2="//*[text()='<Main_page>']"
    Menu='//*[@ id ="__next"]/div[1]/div/div/div'


