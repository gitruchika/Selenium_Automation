*** Settings ***
Library      SeleniumLibrary
Resource     test_data_var.robot
Resource     locator_var.robot
Variables    session_data.py



*** Variables ***
#${url}          https://www.google.co.in
#${browser}      chrome


*** Test Cases ***
Launch and browser search on google
    Open Browser    ${url}     ${browser}
    Input text      ${google_search_field_name}     ${google_search_data}
    wait until element is visible     ${google_search_button}    10s
    click element    ${google_search_button}
    sleep     5
    Close Browser


