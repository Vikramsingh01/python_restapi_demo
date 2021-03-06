Feature: REST API testing framework using REST Assured library and Validate HTTP response code

  Background:
    Given Set basic web application url is "https://reqres.in/"


  Scenario: New User Registration -Successful
    Given Set POST api endpoint as "api/register"
    When Set HEADER param request content type as "application/json"
    And Set HEADER param response accept type as "application/json"
    And Set BODY form param using basic user details
    And  Raise "POST" HTTP request
    Then Valid HTTP response should be received
    And Response http code should be 201
    And Response HEADER content type should be "application/json"
    And Response BODY should not be null or empty
    And Response BODY parsing for "POST__register" should be successful

  Scenario: User Login After Registration -Successful
    Given Set POST api endpoint as "api/login"
    When Set HEADER param request content type as "application/json"
    And Set HEADER param response accept type as "application/json"
    And Set BODY form param using basic user details
    And Raise "POST" HTTP request
    Then Valid HTTP response should be received
    And Response http code should be 200
    And Response HEADER content type should be "application/json"
    And Response BODY should not be null or empty
    And Response BODY parsing for "POST__login" should be successful

  Scenario: User Update -Successful
    Given Updating user Details
    When Set PUT api endpoint as "api/users/2"
    And Set HEADER param request content type as "application/json"
    And Set HEADER param response accept type as "application/json"
    And Set BODY form param using basic user details
    And Raise "PUT" HTTP request
    Then Valid HTTP response should be received
    And Response http code should be 200
    And Response HEADER content type should be "application/json"
    And Response BODY should not be null or empty
    And Response BODY parsing for "PUT__updateUser" should be successful


  Scenario: GET List of Users request example
    Given Set GET api endpoint as "api/users"
    When Set HEADER param request content type as "application/json"
    And Set HEADER param response accept type as "application/json"
    And Set Query param as " 2"
    And Raise "GET" HTTP request
    Then Valid HTTP response should be received
    And Response http code should be 200
    And Response HEADER content type should be "application/json"
    And Response BODY should not be null or empty
    And Response BODY parsing for "GET__UsersList" should be successful


    #  Scenario: DELETE request example
#    Given Perform setup for DELETE request
#    When Set DELETE api endpoint as "signout"
#    And Set HEADER param request content type as "application/json"
#    And Set HEADER param response accept type as "application/json"
#    And Set Query param as "based on user details"
#    And Raise "DELETE" HTTP request
#    Then Valid HTTP response should be received
#    And Response http code should be 200
#    And Response HEADER content type should be "application/json"
#    And Response BODY should not be null or empty
#    And Response BODY parsing for "DELETE__signout" should be successful