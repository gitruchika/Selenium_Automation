*** Settings ***
Library      SeleniumLibrary
Resource     test_data_var.robot
Resource     locator_var.robot
Resource     dummy_website_keywords.robot
Variables    session_data.py

Suite Setup       Open Browser    ${url}     ${browser}
Suite Teardown    Close Browser

*** Variables ***
#${url}          https://www.google.co.in
#${browser}      chrome

${search_data}       Facebook.com
${var1}              600
${var2}              300
${var3}              400
@{cities}            Mumbai     Bangalore     Hyderbad      Kolkata
&{DICT}              first=This value is pretty long.    second=This value is even longer. It has two sentences.



*** Test Cases ***

Launch and browser search on google
    [Tags]    Smoke    robot:skip
    search data on google        ${search_data}

Automation dummy website
     [Tags]     Sanity     robot:skip
     [Documentation]    we will automate dummy website
     go to      ${dummy_website_url}
     Select Values and Enter data      ${first_name}       ${dropdown_Value}
     Capture Page Screenshot
     sleep        10s

Condition Code Test Cases
    [Tags]     condition
    IF     ${var1} > ${var2} and ${var1} > ${var3}
           Log      ${var1} has great value
    ELSE IF    ${var2} > ${var1} and ${var2} > ${var3}
            Log      ${var2} has great value
    ELSE IF   ${var3} > ${var1} and ${var3} > ${var2}
             Log      ${var3} has great value
    END

Looping Condition Test Case
      FOR    ${i}    IN RANGE   10
            Log     ${i}
      END

      FOR     ${city}    IN    @{cities}
               Log     ${city}

      END
      Log      ${DICT}
      Log      ${DICT['second']}
      Log      ${cities[0]}

*** Keywords ***

search data on google
    [Documentation]  user will seach data on google
    [Arguments]      ${search_content}
    Input text      ${google_search_field_name}     ${search_content}
    wait until element is visible     ${google_search_button}    10s
    click element    ${google_search_button}
    sleep     5






