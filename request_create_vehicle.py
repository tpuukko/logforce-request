#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logforce_settings as settings
from logforce_request import LogforceRequest
from vehicle_data import vehicle_data

def main():
  request = LogforceRequest(base_url=settings.URLS['development'],
                            client_version=settings.CLIENT_VERSION)

  transport_company_id = vehicle_data.get('transportCompany')
  request.post(url="/server/services/%s/vehicle" % transport_company_id,
               data=vehicle_data)

if __name__ == '__main__':
  main()

