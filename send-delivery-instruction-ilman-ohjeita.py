#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logforce_settings as settings

from logforce_request import read_request
from logforce_request import IntegrationRequest

def main():
  tilaus_ilman_ohjeita = read_request('..', 'logforce-6900-automaattinen-jako', 'delivery-instruction-ilman-ohjeita.xml')    
  request = IntegrationRequest(base_url=settings.URLS['development'])
  request.post(service_url="/api/message_in", data=tilaus_ilman_ohjeita)
  print( request.response_report() )

if __name__ == '__main__':
  main()