import os

from selene import browser, have, by, command


def test_practice_form():
    browser.open("/automation-practice-form")
    browser.element('.main-header').should(have.text("Practice Form"))
    browser.element('#fixedban').execute_script('element.remove()')
    browser.element('footer').execute_script('element.remove()')
    # browser.element('#fixedban').perform(command.js.scroll_into_view)

    browser.element("#firstName").type('Imechko')
    browser.element("#lastName").type('Familyitze')
    browser.element("#userEmail").type('username@gmail.com')
    browser.element('#gender-radio-1').double_click()
    browser.element("#userNumber").type('0987654321')
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click().element(by.text("June")).click()
    browser.element(".react-datepicker__year-select").click().element(by.text("1900")).click()
    browser.element(".react-datepicker__day--012:not(.react-datepicker__day--outside-month)").click()
    browser.element('#currentAddress').perform(command.js.scroll_into_view)
    browser.element("#subjectsInput").type('Com')
    browser.element(".subjects-auto-complete__menu").element(by.text("Commerce")).click()
    browser.element("#hobbiesWrapper").element(by.text("Sports")).click()
    browser.element("#hobbiesWrapper").element(by.text("Music")).click()
    browser.element(by.css("input[type=file]")).send_keys(os.path.abspath('picture/sss.png'))
    browser.element('#currentAddress').type('Adler city')
    browser.element("#state").click().element(by.text("Rajasthan")).click()
    browser.element("#city").click().element(by.text("Jaipur")).click()
    browser.element("#submit").click()

    browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))

    browser.element('.table-responsive').all('td:nth-of-type(2)').should(
        have.texts(
            'Imechko Familyitze',
            'username@gmail.com',
            'Male',
            '0987654321',
            '12 June,1900',
            'Commerce',
            'Sports, Music',
            'sss.png',
            'Adler city',
            'Rajasthan Jaipur',
        )
    )

    browser.element("#closeLargeModal").click()