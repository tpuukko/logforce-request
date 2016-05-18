#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import Template

import logforce_settings as settings

from logforce_request import read_request
from logforce_request import IntegrationRequest

def main():

  values = {
    "DeliveryInstructionNumber":"TP2016-03-31",
    "DeliveryInstructionReference":"000000000000000103",
    "DeliveryInstructionDate_Year":"2016",
    "DeliveryInstructionDate_Month":"3",
    "DeliveryInstructionDate_Day": "31",

    #ShipmentRequestedDate
    "SRD_DateTimeFrom_Date_Year":"2016",
    "SRD_DateTimeFrom_Date_Month":"3",
    "SRD_DateTimeFrom_Date_Day":"31",

    "SRD_DateTimeTo_Date_Year":"2016",
    "SRD_DateTimeTo_Date_Month":"4",
    "SRD_DateTimeTo_Date_Day":"29",

    #ActualArrivalDate
    "AAD_DateTimeFrom_Date_Year":"2016",
    "AAD_DateTimeFrom_Date_Month":"3",
    "AAD_DateTimeFrom_Date_Day":"31",

    "AAD_DateTimeTo_Date_Year":"2016",
    "AAD_DateTimeTo_Date_Month":"4",
    "AAD_DateTimeTo_Date_Day":"29",

    #Other
    "InformationalQuantity_UOM_Percentage":"10",
    "Quantity_WoodVolume":"2000"     
  }
  
  haketilaus = read_request('..', 'xml' ,'template_haketilaus_MG.xml')
  template = Template(haketilaus)
  jatkotilaus_string = template.substitute( values )

  request = IntegrationRequest(base_url=settings.URLS['development'])
  request.post(service_url="/api/message_in", data=jatkotilaus_string)
  print( request.response_report() )

if __name__ == '__main__':
  main()