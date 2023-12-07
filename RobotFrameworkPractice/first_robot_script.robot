*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
Launch and browser search on google
    Open Browser    https://www.google.co.in      chrome
    Input text      name=q      Robotframework
    wait until element is visible     name=btnK    10s
    click element    name=btnK
    sleep     5
    Close Browser


