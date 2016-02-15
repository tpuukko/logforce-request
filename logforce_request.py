#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module gives ability to send HTTP-request to the Logforce server. Module 
contains two classes IntegrationRequest and LogforceRequest. The 
IntegrationRequest is used to send a integration side request, as the 
LogforceRequest class is used to send a service side request. The integration 
side messages are for messages coming from Metsäjärjestelmäs, and the service 
side is for all Logforce clients as Lastaussovellus, Suunnittelusovellus and 
Ajoneuvosovellus.

The service side needs a authentication before it grants access make any other 
request. Use LogforceRequest method authenticate to authenticate to the server. 
Server gives cookies that are passed to other service side request.
"""
import requests, urllib, json, os 

def read_request(*filepath):
  """
  Open a file in given path and return it content as a string
  @param {list} filepath as list, or similar read more os.path.join docs..
  @return {string} file content
  @raise FileNotFoundError, if the is no such file
  """
  with open(os.path.join(*filepath), 'r', encoding="utf-8") as jatkotilaus:
    return jatkotilaus.read()

class IntegrationRequest:
  """
  Class contains methods to make a integration side requests to Logforce Server
  @variable {request.Response} self.response is last request's response object
  """
  def __init__(self, base_url ):
    """
    @Constructor
    @param {string} base_url requests base url, use some url from URLS dictionary
    @raise {ConnectionError} if fails to connect
    @return {IntegrationRequest}    
    """    
    self._base_url = base_url
    self._headers = {
      'Accept': 'application/xml',
      'connection': 'Keep-Alive',
      'Content-Type': 'text/xml; charset=utf-8',    
      'Cache-Control': 'no-cache'
    }

  def post( self, service_url, data ):
    self.response = requests.post(self._base_url+service_url, 
                                  headers=self._headers, 
                                  data=data.encode('utf-8') )
    return self

  def response_report(self):
    params = (self.response.status_code, self.response.headers['tracking_number'])
    return "Status code: %s\nTracking number: %s\n" % params

class LogforceRequest:
  """
  Class contains methods to make a service side reqeust to Logforce server.
  @variable {request.Response} self.response contains last response object
  @variable {request.Response} self.authentication_response contains authentication request
  """  

  def __init__( self, base_url, client_version ):
    """
    @Constructor
    @param {string} base_url requests base url, use some url from URLS dictionary
    @param {string} client_version LF-Client-Version   
    @return {None} 
    """
    self._base_url = base_url
    self._client_version = client_version

    self._headers = {    
      'Accept': 'application/json',
      'connection': 'Keep-Alive',
      'LF-Client-Type': 'drive',
      'LF-Client-Version': self._client_version,
      'Content-Type': 'application/json',
    }


  def authenticate(self, username, password):
    """
    Authenticate user to logforce server
    @param {string} username
    @param {string} password
    @return {LogforceRequest}
    @raise ConnectionError if connection fails
    """  
    headers = {
      'Accept-Encoding': 'gzip, deflate',
      'Accept-Language': 'en-US,en;q=0.8',
      'X-Requested-With' : 'XMLHttpRequest',
      'LF-Client-Version': self._client_version,      
      'Connection': 'keep-alive',
      'Pragma': 'no-cache',
      'LF-Client-Type': 'web',
      'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
      'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
      'Accept': '*/*'      
    }

    data = {
      'j_username': username,
      'j_password': password,
      'j_language':'FI',
      '_spring_security_remember_me':'false'
    }

    url = self._base_url + '/server/j_spring_security_check'

    response = requests.post(url, headers=headers, 
                                  data=urllib.parse.urlencode( data ))

    #Store for internal user later
    self.authentication_response = response
    
    return self

  def get(self, url, data=None):
    """
    Makes a get request to Logforce server
    @param {String} url
    @param {dictionary} data
    @param {string} client_version, LF_CLIENT_VERSION number
    @param {request.Response} response object from authentication request
    @return {LogforceRequest}
    """
    request_url = self._base_url + url

    if data:
      request_url += urllib.parse.urlencode(data) 

    cookies = self.authentication_response.cookies
    
    self.response = requests.get(request_url, headers=self._headers, 
                                              cookies=cookies )
    return self

  def post(self, url, data=None):
    """
    Makes a POST request to Logforce server
    @param {String} url
    @param {dictionary} data
    @param {string} client_version, LF_CLIENT_VERSION number
    @param {request.Response} response object from authentication request
    @return {LogforceRequest}
    """
    self.response = requests.post(self._base_url + url, 
                                  headers=self._headers, 
                                  data=json.dumps(data), 
                                  cookies=self.authentication_response.cookies )
    return self
 
  def put(self, url, data):
    """
    Makes a PUT request to Logforce server
    @param {String} url
    @param {dictionary} data
    @param {string} client_version, LF_CLIENT_VERSION number
    @param {request.Response} response object from authentication request
    @return {LogforceRequest}
    """
    self.response = requests.put(self._base_url + url,  
                                 headers=self._headers, 
                                 data=json.dumps(data), 
                                 cookies=self.authentication_response.cookies )
    return self

  def delete(self, url):
    """
    Makes a DELETE request to Logforce server
    !Not implemented!
    """
    pass

  def pretty_response(self):
    """
    Return last response reponses jsos as prettyfied
    @return {string}
    """
    return json.dumps(json.loads(self.response.text), sort_keys=True, indent=2)
    


    

