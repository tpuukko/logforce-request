#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logforce_settings as settings
from logforce_db import db_fetch_many
from logforce_db import db_table_format_result

def main():
  sql = """
        SELECT * FROM user_feature ORDER BY created_on DESC;
        """
        
  results = db_fetch_many(sql)  
  db_table_format_result( result )

  for result in results:    
    print( (("|%s" * len(result))+'|' ) % result )
    

if __name__ == '__main__':
  main()

