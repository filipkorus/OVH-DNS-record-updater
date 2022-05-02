from datetime import datetime
from mailer import mail
import dns

def get_timestamp() -> str:
   return datetime.now().strftime('%Y-%m-%d %H:%M')

if __name__ == '__main__':

   mail_to = 'me@email.com'
   ZONES = [
      {'name': 'example.com','ignore_subdomains': ['blog', 'custom_subdomain']}
   ]

   for zone in ZONES:
      dns = dns.DNS()
      
      IP = dns.get_server_IP()
      old_ip = ''
      updated_records = []
      ids = dns.get_record_IDs(zone['name'], 'A')
      for record_id in ids:
         record = dns.get_record_by_ID(zone['name'], record_id)
         if record['subDomain'] not in zone['ignore_subdomains'] and record['target'] != IP:
            dns.update_record(zone['name'], IP, record_id)
            updated_records.append(f'{record["subDomain"]}.{record["zone"]}')
            old_ip = record['target']
      
      if old_ip != '':
         dns.refresh_zone(zone['name'])

         modified_records_list = ''
         for record in updated_records:
            modified_records_list += f'<li>{record[1:] if record[0] == "." else record}</li>'

         mail(
            '"ip-updater" <noreply@example.com>',
            mail_to,
            f'IP Updated at {get_timestamp()}',
            f"""\
            <!DOCTYPE html>
            <html>
               <body>
                  <h4>DNS records has been modified at {get_timestamp()}.</h4>
                  <p>Target IP was changed from <b>{old_ip}</b> to <b>{IP}</b>.</p>
                  <p>Modified entries:</p>
                  <ul>{modified_records_list}</ul>
               </body>
            </html>
            """
         )
