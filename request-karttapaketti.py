#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logforce_settings as settings
from logforce_request import LogforceRequest

def main():

  #Base url is given here
  request = LogforceRequest(base_url=settings.URLS['development'],
                            client_version=settings.CLIENT_VERSION )

  #Authentication is required to make request to Logforce server.
  #Authentication cookies are stored in request._authentication_request
  #those cookies are passed to every service request.
  response = request.authenticate(username='Kouluttaja1@logforce.com', 
                                  password='Logf2014')

  #Service url is concatenated with base url to form whole url address
  service_url = '/server/services/1006/maps/vehicle/2916746?_=1460107399102'
  
  #Response JSON can be printed out like this, the last response object
  #is stored in request._reqeuest variable.
  json = request.get(service_url).pretty_response()

  print(json)

if __name__ == '__main__':
  main()