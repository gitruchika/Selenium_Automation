*** Settings ***
Resource     dummy_website_locators.robot


*** Keywords ***
Select Values and Enter data
     [Arguments]      ${first_name}     ${dropdown_value}
     click element      ${dummy_ticket_radio_button}
     input text         ${first_name_field}    ${first_name}
     Select From List By Label      ${select_passenger_dropdown}       ${dropdown_value}





