#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logforce_settings as settings
from logforce_db import db_fetch_many
from logforce_db import db_table_format_result

def humansize(nbytes):
  suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']

  if nbytes == 0: return '0 B'
  i = 0
  while nbytes >= 1024 and i < len(suffixes)-1:
      nbytes /= 1024.
      i += 1
  f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
  return '%s %s' % (f, suffixes[i])

def main():
  sql = """
        select mp.package_name, mpl.url, mpl.size from map_package_layer mpl 
        right join map_package mp on mpl.map_package_id = mp.map_package_id
        where mp.grid_version = 2 order by mp.package_name;
        """
        
  results = db_fetch_many(sql)  

  total_size = 0

  for result in results:            
    total_size += result[2]
    formatted = (result[0], result[1], humansize(result[2]))     
    print( (("|%s" * len(result))+'|' ) % formatted )
    
  print( "Total size: %s" % (humansize(total_size)))

if __name__ == '__main__':
  main()
