#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logforce_settings as settings
from logforce_db import db_fetch_many

def main():
  sql = """
        SELECT tc.name,  vr.name, dovr.delivery_origin_id, dor.delivery_origin_code
        FROM vehicle_resource vr 
        RIGHT JOIN delivery_origin_vehicle_resource dovr 
        ON vr.vehicle_resource_id = dovr.vehicle_resource_id
        LEFT JOIN delivery_origin dor 
        ON dovr.delivery_origin_id = dor.delivery_origin_id
        LEFT JOIN transport_company tc 
        ON tc.transport_company_id = vr.transport_company_id
        ORDER BY vr.name ASC;
        """
        
  results = db_fetch_many(sql)  

  for result in results:
    print("|%25s|%25s|%15s|%15s|" % result)

if __name__ == '__main__':
  main()

