#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logforce_settings as settings
from logforce_request import LogforceRequest

data = {
  "transportcompany":"/services/transportcompany?updatedSince=1455195048000&includeRemoved=true",
  "forestcompany":"/services/48112/forestcompany?updatedSince=1439804384000&includeRemoved=true",
  "assortment":"/services/assortments?updatedSince=1440151423000&includeRemoved=true",
  "assortmentgroup":"/services/assortmentgroups?updatedSince=1402403441000&includeRemoved=true",
  "assortmentclass":"/services/assortmentclasses?updatedSince=1350048337000&includeRemoved=true",
  "railcartype":"/services/railcartypes?",
  "vehicle":"/services/48112/vehicle?updatedSince=1455520714000&includeRemoved=true",
  "deliveryorder":"/services/48112/deliveryorder?updatedSince=1455278790000&includeRemoved=true",
  "deliverydestination":"/services/48112/alldeliverydestinations?updatedSince=1455522623000&includeRemoved=true",
  "deliveryload":"/services/48112/deliveryload?updatedSince=1455278790000&includeRemoved=true",
  "storagelocation":"/services/48112/storagelocation?updatedSince=1452847465000&includeRemoved=true",
  "storage":"/services/48112/storage?updatedSince=1452851945000&includeRemoved=true",
  "storagereservation":"/services/48112/storagereservation?updatedSince=1449731193000&includeRemoved=true",
  "deliveryexecution":"/services/48112/deliveryexecution/vehicle/2874122?updatedSince=1454425202000&includeRemoved=true",
  "train":"/services/48112/train/2874122?","railcar":"/services/48112/railcar/2874122?",
  "stack":"/services/48112/railcarstack/2874122?",
  "crane":"/services/48112/crane?updatedSince=1453970583000&includeRemoved=true",
  "user":"/services/48112/user?updatedSince=1455273179000&includeRemoved=true",
  "standardmessagetype":"/services/storagestandardmessagetypes?",
  "usermessageuser":"/services/48112/messages/user/2869301?from=1451599200000&to=1455573599999&",
  "usermessagevehicle":"/services/48112/messages/vehicle/2874122?from=1451599200000&to=1455573599999&"
}

def main():

  #Base url is given here
  request = LogforceRequest(base_url=settings.URLS['development'],
                            client_version=settings.CLIENT_VERSION )

  #Authentication is required to make request to Logforce server.
  #Authentication cookies are stored in request._authentication_request
  #those cookies are passed to every service request.
  response = request.authenticate(username=settings.USERNAME, 
                                  password=settings.PASSWORD)

  #Service url is concatenated with base url to form whole url address
  service_url = '/server/services/package'
  
  #Response JSON can be printed out like this, the last response object
  #is stored in request._reqeuest variable.
  json = request.post(service_url, data=data).pretty_response()

  print(json)

if __name__ == '__main__':
  main()