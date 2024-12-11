*** Settings ***
Documentation     Login page test suite
Library           SeleniumLibrary
Resource          ../resources/locators.robot
Variables         ../feat.py

*** Variables ***
${VALID_USERNAME}    testuser
${VALID_PASSWORD}    password123

*** Test Cases ***
Verify Login Page Loads Successfully
    Open Browser    ${FEATConfig.BASE_URL}    ${FEATConfig.BROWSER}
    Maximize Browser Window
    Page Should Contain Element    ${LOGIN_USERNAME_FIELD}
    Page Should Contain Element    ${LOGIN_PASSWORD_FIELD}
    Page Should Contain Element    ${LOGIN_BUTTON}
    [Teardown]    Close Browser

Verify Successful Login
    Open Browser    ${FEATConfig.BASE_URL}    ${FEATConfig.BROWSER}
    Maximize Browser Window
    Input Text    ${LOGIN_USERNAME_FIELD}    ${VALID_USERNAME}
    Input Text    ${LOGIN_PASSWORD_FIELD}    ${VALID_PASSWORD}
    Click Element    ${LOGIN_BUTTON}
    Wait Until Page Contains Element    ${DASHBOARD_LINK}
    [Teardown]    Close Browser

*** Keywords ***
Login With Valid Credentials
    [Arguments]    ${username}    ${password}
    Input Text    ${LOGIN_USERNAME_FIELD}    ${username}
    Input Text    ${LOGIN_PASSWORD_FIELD}    ${password}
    Click Element    ${LOGIN_BUTTON} 