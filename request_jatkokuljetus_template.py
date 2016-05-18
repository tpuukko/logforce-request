#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import Template

import logforce_settings as settings

from logforce_request import read_request
from logforce_request import IntegrationRequest

def main():

  values = {
    "DeliveryInstructionNumber":"TP2016-03-09",
    "DeliveryInstructionReference":"000000000000000101",
    "DeliveryInstructionDate_Year":"2016",
    "DeliveryInstructionDate_Month":"3",
    "DeliveryInstructionDate_Day": "9",

    #ShipmentRequestedDate
    "SRD_DateTimeFrom_Date_Year":"2016",
    "SRD_DateTimeFrom_Date_Month":"3",
    "SRD_DateTimeFrom_Date_Day":"9",

    "SRD_DateTimeTo_Date_Year":"2016",
    "SRD_DateTimeTo_Date_Month":"3",
    "SRD_DateTimeTo_Date_Day":"30",

    #ActualArrivalDate
    "AAD_DateTimeFrom_Date_Year":"2016",
    "AAD_DateTimeFrom_Date_Month":"3",
    "AAD_DateTimeFrom_Date_Day":"9",

    "AAD_DateTimeTo_Date_Year":"2016",
    "AAD_DateTimeTo_Date_Month":"3",
    "AAD_DateTimeTo_Date_Day":"30",

    #LoadingDate
    "LD_DateTimeFrom_Date_Year":"2016",
    "LD_DateTimeFrom_Date_Month":"3",
    "LD_DateTimeFrom_Date_Day":"9",

    "LD_DateTimeTo_Date_Year":"2016",
    "LD_DateTimeTo_Date_Month":"3",
    "LD_DateTimeTo_Date_Day":"30",

    #EstimatedTimeOfArrival
    "ETA_DateTime_Date_Year":"2016",
    "ETA_DateTime_Date_Month":"3",
    "ETA_DateTime_Date_Day":"30",        
  }
  
  jatkotilaus = read_request('..', 'xml' ,'template-jatkokuljetustilaus-24-vaunua-kut-mg-autokuljetus.xml')

  template = Template(jatkotilaus)
  jatkotilaus_string = template.substitute( values )  
  z

  request = IntegrationRequest(base_url=settings.URLS['test'])
  request.post(service_url="/api/message_in", data=jatkotilaus_string)
  print( request.response_report() )

if __name__ == '__main__':
  main()