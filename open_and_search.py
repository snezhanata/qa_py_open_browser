from selene.support.shared import browser
from selene import be, have

browser.config.hold_browser_open = True
# browser.open('https://google.com')
# browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
# browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

browser.open('https://demoqa.com/automation-practice-form')
browser.element('[id=firstName]').should(be.blank).type('Alan')
browser.element('[id=lastName]').should(be.blank).type('Smithee')
browser.element('[id=userEmail]').type('maroulauddaugou-3210@yopmail.com')
browser.element('[id=gender-radio-2]').double_click()
browser.element('[id=userNumber]').should(be.blank).type('0987687899').press_enter()

#browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

browser.element('[class="table table-dark table-striped table-bordered table-hover"]').should(have.text('Alan Smithee' and 'maroulauddaugou-3210@yopmail.com' and 'Female' and '0987687899'))
