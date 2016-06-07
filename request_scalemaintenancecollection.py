#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logforce_settings as settings
from logforce_request import LogforceRequest

def main():

  #Base url is given here
  request = LogforceRequest(base_url=settings.URLS['development'],
                            client_version=settings.CLIENT_VERSION )

  request.authenticate(username=settings.USERNAME, 
                       password=settings.PASSWORD)

  #Service url is concatenated with base url to form whole url address
  service_url = '/server/services/48112/scale/maintenance?serialNumber=Hih123&_=1463473132888'

  json = request.get(service_url).pretty_response()

  print(json)

if __name__ == '__main__':
  main()