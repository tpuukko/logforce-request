#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logforce_settings as settings

from logforce_request import read_request
from logforce_request import IntegrationRequest

def main():
  jatkotilaus = read_request('..', 'xml' ,'TOIMII_vaunutilaus_Teemu_24-vaunua.xml')    
  request = IntegrationRequest(base_url=settings.URLS['development'])
  request.post(service_url="/api/message_in", data=jatkotilaus)
  print( request.response_report() )

if __name__ == '__main__':
  main()