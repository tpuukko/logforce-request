# -*- coding: utf-8 -*-
import logforce_settings
import psycopg2, logging

logging.basicConfig(level=logging.INFO, format=format)
log = logging.getLogger(name=__name__)

DATABASE_CONNECTION_STRING = logforce_settings.DATABASE_CONNECTION_STRING

def db_fetch_many(query='', params=None, db=DATABASE_CONNECTION_STRING):  
  """
  Fetch multiple rows from database
  @param query SQL-query as string
  @params list of query parameters, list or tuple
  @param db is connection string, default DATABASE_CONNECTION_STRING
  @return list of result tuples  
  """
  conn = psycopg2.connect(db)
  try:
    cur = conn.cursor()      
    cur.execute(query, params)
    result = cur.fetchall()
    cur.close()      
    return result
  except psycopg2.Error as e:
      log.error(e)
  finally:
    conn.close()    

def db_fetch_one(query='', params=None, db=DATABASE_CONNECTION_STRING):
  """
  Fetch single row from database
  @param query SQL-query as string
  @params list of query parameters, list or tuple
  @param db is connection string, default DATABASE_CONNECTION_STRING
  @return tuple
  """  
  conn = psycopg2.connect(db)
  try:
    cur = conn.cursor()      
    cur.execute(query, params)
    result = cur.fetchone()
    cur.close()      
    return result[0] if result != None and len(result) > 0 else None
  except psycopg2.Error as e:
    print(e)
    log.error(e)
  finally:
    conn.close()

def db_execute_query( query='', params=None, db=DATABASE_CONNECTION_STRING):
  """
  Executes query to Woodforce server database. (INSERT, UPDATE or DELETE)
  @param query SQL-query as string
  @param params query paramters as tuple or list
  @param db is connection string, default DATABASE_CONNECTION_STRING
  @return updated rows count
  """
  updated_rows = 0
  conn = psycopg2.connect(db)  
  try:
    cur = conn.cursor()      
    cur.execute(query, params)      
    conn.commit()
    updated_rows = cur.rowcount;
    cur.close()      
  except psycopg2.Error as e:
    log.error(e)
  finally:
    conn.close()
  return updated_rows


def db_table_format_result( results ):
  map(lambda x: (("|%s" * len(result))+'|' ) % result , results)
  for result in results:    
     (("|%s" * len(result))+'|' ) % result