#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logforce_settings as settings
from logforce_db import db_fetch_many

def main():
  sql = """
        SELECT rail_car_id, car_number, sort_order FROM rail_car WHERE train_id = (
          SELECT train_id FROM delivery_order WHERE delivery_order_id = 2964952
        ) ORDER BY sort_order ASC;
        """

  sql = """
        SELECT rail_car_id, car_number, sort_order FROM rail_car 
        WHERE train_id = 701
        ORDER BY sort_order ASC;  
        """
        
  results = db_fetch_many(sql)  

  for result in results:
    print("|%3s|%10s|%3s|" % result)

if __name__ == '__main__':
  main()

