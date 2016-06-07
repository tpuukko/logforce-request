#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import Template

import logforce_settings as settings

from logforce_request import read_request
from logforce_request import IntegrationRequest

def main():

  values = {
    "DeliveryInstructionNumber":"TP2016-06-07-A",
    "DeliveryInstructionReference":"000000000000002104",
    "DeliveryInstructionDate_Year":"2016",
    "DeliveryInstructionDate_Month":"06",
    "DeliveryInstructionDate_Day": "06",

    #ShipmentRequestedDate
    "SRD_DateTimeFrom_Date_Year":"2016",
    "SRD_DateTimeFrom_Date_Month":"06",
    "SRD_DateTimeFrom_Date_Day":"07",

    "SRD_DateTimeTo_Date_Year":"2016",
    "SRD_DateTimeTo_Date_Month":"6",
    "SRD_DateTimeTo_Date_Day":"30",

    #ActualArrivalDate
    "AAD_DateTimeFrom_Date_Year":"2016",
    "AAD_DateTimeFrom_Date_Month":"06",
    "AAD_DateTimeFrom_Date_Day":"7",

    "AAD_DateTimeTo_Date_Year":"2016",
    "AAD_DateTimeTo_Date_Month":"06",
    "AAD_DateTimeTo_Date_Day":"30",

    #LoadingDate
    "LD_DateTimeFrom_Date_Year":"2016",
    "LD_DateTimeFrom_Date_Month":"06",
    "LD_DateTimeFrom_Date_Day":"7",

    "LD_DateTimeTo_Date_Year":"2016",
    "LD_DateTimeTo_Date_Month":"06",
    "LD_DateTimeTo_Date_Day":"30",

    #EstimatedTimeOfArrival
    "ETA_DateTime_Date_Year":"2016",
    "ETA_DateTime_Date_Month":"06",
    "ETA_DateTime_Date_Day":"7",        

    #Delivery Origin, lähtöalue Default "null"
    "delivery_origin": "0000000100",

    #Kuljetusyritys
    #"ReceiverParty": "Koulutusyrittäjä",
    #"ReceiverParty_vat_identification_number": "1144911-6"
    "ReceiverParty": "Miitri kuljetus",
    "ReceiverParty_vat_identification_number": "48112"
  }
  
  jatkotilaus = read_request('..', 'xml' ,'template-jatkokuljetustilaus-24-vaunua-kut-mg-autokuljetus.xml')

  template = Template(jatkotilaus)
  jatkotilaus_string = template.substitute( values )  
  print(jatkotilaus_string)

  request = IntegrationRequest(base_url=settings.URLS['development'])
  request.post(service_url="/api/message_in", data=jatkotilaus_string)
  print( request.response_report() )

if __name__ == '__main__':
  main()