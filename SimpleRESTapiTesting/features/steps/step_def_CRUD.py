#!/usr/bin/python
# -*- coding: utf-8 -*-

from behave import given, when, then, step
import requests
from SimpleRESTapiTesting.features.steps.keys import *

global_general_variables = {}
http_request_header = {}
http_request_body = {}
http_request_url_query_param = {}


@given(u'Set basic web application url is "{basic_app_url}"')
def step_impl(context, basic_app_url):
    global_general_variables['basic_application_URL'] = basic_app_url


@given(u'Set basic user details as "{particular}" and "{value}" below')
def step_impl(context, particular, value):
    for row in context.table:
        temp_value = row['value']
        global_general_variables[row['particular']] = temp_value
        if 'empty' in temp_value:
            global_general_variables[row['particular']] = ''


@when(u'Set HEADER param request content type as "{header_content_type}"')
def step_impl(context, header_content_type):
    http_request_header['content-type'] = header_content_type


@when(u'Set HEADER param response accept type as "{header_accept_type}"')
def step_impl(context, header_accept_type):
    http_request_header['Accept'] = header_accept_type


@given(u'Set GET api endpoint as "{get_api_endpoint}"')
def step_impl(context, get_api_endpoint):
    global_general_variables['GET_api_endpoint'] = get_api_endpoint


@given(u'Set POST api endpoint as "{post_api_endpoint}"')
def step_impl(context, post_api_endpoint):
    global_general_variables['POST_api_endpoint'] = post_api_endpoint


@given(u'Updating user Details')
def step_impl(context):
    print('Updating User Details')


@when(u'Set PUT api endpoint as "{put_api_endpoint}"')
def step_impl(context, put_api_endpoint):
    global_general_variables['PUT_api_endpoint'] = put_api_endpoint


@when(u'Set DELETE api endpoint as "{delete_api_endpoint}"')
def step_impl(context, delete_api_endpoint):
    global_general_variables['DELETE_api_endpoint'] = delete_api_endpoint


@when(u'Set Query param as "{query_param}"')
def step_impl(context, query_param):
    if 'empty' in query_param:
        http_request_url_query_param.clear()
    else:
        http_request_url_query_param.clear()
        http_request_url_query_param['page'] = int(query_param)


@when(u'Raise "{http_request_type}" HTTP request')
def step_impl(context, http_request_type):
    url_temp = global_general_variables['basic_application_URL']
    if 'GET' == http_request_type:
        url_temp += global_general_variables['GET_api_endpoint']
        http_request_body.clear()
        global_general_variables['response_full'] = requests.get(url_temp,
                                                                 headers=http_request_header,
                                                                 params=http_request_url_query_param,
                                                                 data=http_request_body)
    elif 'POST' == http_request_type:
        url_temp += global_general_variables['POST_api_endpoint']
        http_request_url_query_param.clear()
        if (url_temp == 'https://reqres.in/api/register'):
            global_general_variables['response_full'] = requests.post(url_temp,
                                                                      headers=http_request_header,
                                                                      params=http_request_url_query_param,
                                                                      data=http_request_body['RegistrationDetails'])
        else:
            global_general_variables['response_full'] = requests.post(url_temp,
                                                                      headers=http_request_header,
                                                                      params=http_request_url_query_param,
                                                                      data=http_request_body['LoginDetails'])

    elif 'PUT' == http_request_type:
        url_temp += global_general_variables['PUT_api_endpoint']
        http_request_url_query_param.clear()
        global_general_variables['response_full'] = requests.put(url_temp,
                                                                 headers=http_request_header,
                                                                 params=http_request_url_query_param,
                                                                 data=http_request_body['UpdateUserDetails'])
    elif 'DELETE' == http_request_type:
        url_temp += global_general_variables['DELETE_api_endpoint']
        http_request_body.clear()
        global_general_variables['response_full'] = requests.delete(url_temp,
                                                                    headers=http_request_header,
                                                                    params=http_request_url_query_param,
                                                                    data=http_request_body)


@then(u'Valid HTTP response should be received')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, 'Null response received'


@then(u'Response http code should be {expected_response_code:d}')
def step_impl(context, expected_response_code):
    global_general_variables['expected_response_code'] = expected_response_code
    actual_response_code = global_general_variables['response_full'].status_code
    if str(actual_response_code) not in str(expected_response_code):
        print(str(global_general_variables['response_full'].json()))
        assert False, '***ERROR: Following unexpected error response code received: ' + str(actual_response_code)


@then(u'Response HEADER content type should be "{expected_response_content_type}"')
def step_impl(context, expected_response_content_type):
    global_general_variables['expected_response_content_type'] = expected_response_content_type
    actual_response_content_type = global_general_variables['response_full'].headers['Content-Type']
    if expected_response_content_type not in actual_response_content_type:
        assert False, '***ERROR: Following unexpected error response content type received: ' + actual_response_content_type


@then(u'Response BODY should not be null or empty')
def step_impl(context):
    if None in global_general_variables['response_full']:
        assert False, '***ERROR:  Null or none response body received'


@when(u'Set BODY form param using basic user details')
def step_impl(context):
    http_request_body['RegistrationDetails'] = RegistrationDetails
    http_request_body['LoginDetails'] = LoginDetails
    http_request_body['UpdateUserDetails'] = UpdateUserDetails


@then(u'Response BODY parsing for "{body_parsing_for}" should be successful')
def step_impl(context, body_parsing_for):
    current_json = global_general_variables.get('response_full').json()
    if 'POST__register' == body_parsing_for:
        print(current_json['token'])
    elif 'POST__login' == body_parsing_for:
        print(current_json['token'])
    elif 'PUT__updateUser' == body_parsing_for:
        print('Update Name : ' + current_json['name'])
        print('Update Job : ' + current_json['job'])
        print('Updated Details : ' + current_json['updatedAt'])
    elif 'GET__UsersList' == body_parsing_for:
        print('page : ' + str(current_json['page']))
        print('per page : ' + str(current_json['per_page']))
        print('total : ' + str(current_json['total']))
        print('total_pages : ' + str(current_json['total_pages']))
