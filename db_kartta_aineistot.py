#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logforce_settings as settings
from logforce_db import db_fetch_many
from logforce_db import db_table_format_result
from utility import humanize_bytes

def main():
  sql = """
        select mp.package_name, mpl.url, mpl.size, mpl.name from map_package_layer mpl 
        right join map_package mp on mpl.map_package_id = mp.map_package_id
        where mp.grid_version = 2 order by mp.package_name, mpl.name;
        """
        
  results = db_fetch_many(sql)  

  total_size = 0

  for result in results:            
    total_size += result[2]
    formatted = (result[0], result[3], result[1], "%.2f" % ( float(result[2]) / 2**20,) )     
    print( (("|%s" * len(result))+'|' ) % formatted )
    
  print( "Total size: %s" % (humanize_bytes(total_size)))

if __name__ == '__main__':
  main()
