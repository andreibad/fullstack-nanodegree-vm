# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

POSTS = [("This is the first post.", datetime.datetime.now())]

def get_posts():
  """Return all posts from the 'database', most recent first."""

  # Try to connect

  try:
      conn=psycopg2.connect("dbname=forum")
  except:
      print "I am unable to connect to the database."

  cur = conn.cursor()
  try:
      cur.execute("""SELECT content,time from posts order by time desc""")
  except:
      print "I can't SELECT "

  rows = cur.fetchall()
  conn.close()
  return rows

def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
    # Try to connect

  try:
      conn=psycopg2.connect("dbname=forum")
  except:
      print "I am unable to connect to the database."
  print "connected to the database."

  cur = conn.cursor()
  try:
      print "trying to insert " + content

      postgres_insert_query = "INSERT INTO posts (content ) VALUES (%s)"
      cur.execute(postgres_insert_query, (content,))


      conn.commit()
  except (Exception, psycopg2.Error) as error :
      if(conn):
          print("Failed to insert record into mobile table", error)
  
  conn.close()


