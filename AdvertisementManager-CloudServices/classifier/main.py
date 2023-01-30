import pika, sys, os
import requests
import os
import json
import psycopg2
from config import *


def send_simple_message(to_email,result,body_str):
  return requests.post(
    "https://api.mailgun.net/v3/sandboxb69e29a468544e6b8355681bc25d184c.mailgun.org/messages",
    auth=("api", "615addf4f9bf796416268ae81cebf304-8845d1b1-3ecac492"),
    data={"from": "ad manager admin <mailgun@sandboxb69e29a468544e6b8355681bc25d184c.mailgun.org>",
          "to": [to_email],
          "subject": "AD MANAGER",
          "text": f'your ad with id {body_str} has been {result.capitalize()}'})


def main():
  # reading from rabbitMQ
  connection = pika.BlockingConnection(pika.URLParameters(AMQP_URL))
  channel = connection.channel()
  channel.queue_declare(queue='ad_requests')
  conn = psycopg2.connect(db)

  def callback(ch, method, properties, body):
    body_str = str(int(body))
    image_url = bucket_url + body_str + '.png'
    # get image tags
    response = requests.get('https://api.imagga.com/v2/tags?image_url=%s' % image_url, auth=(api_key, api_secret))
    response = response.json()

    # check if vehicle is inside tags or not
    state = ''
    category = ''

    for tag in response['result']['tags']:
      if tag['tag']['en'] == 'vehicle' and tag['confidence'] > 50:
        category = response['result']['tags'][0]['tag']['en']
        state = 'ad accepted'
        break
      else:
        state = 'ad rejected'

    # write result in db
    cur = conn.cursor()
    cur.execute("UPDATE ad_manager_api_ad SET (state, category) = (%s, %s) WHERE id = %s;", (state, category, body_str))
    conn.commit()

    # send email
    cur.execute('SELECT email from ad_manager_api_ad where id = %s;', (body_str, ))
    user_email = cur.fetchall()
    cur.close()
    send_simple_message(user_email[0][0], state, body_str)
    print(body_str)
    print('----')

  channel.basic_consume(queue='', on_message_callback=callback, auto_ack=True)
  print(' [*] Waiting for messages. To exit press CTRL+C')
  channel.start_consuming()
  conn.close()


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Interrupted')
    try:
      sys.exit(0)
    except SystemExit:
      os._exit(0)
