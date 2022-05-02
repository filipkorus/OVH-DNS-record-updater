import ovh
from credentials import OVH_ENDPOINT, OVH_APP_KEY, OVH_APP_SECRET, OVH_CONSUMER_KEY
import requests as re

class DNS:
   def __init__(self) -> None:
      self.client = ovh.Client(
         endpoint = OVH_ENDPOINT,
         application_key = OVH_APP_KEY,
         application_secret = OVH_APP_SECRET,
         consumer_key = OVH_CONSUMER_KEY
      )

   def update_record(self, zone_name: str, new_ip: str, record_id: int):
      self.client.put(f'/domain/zone/{zone_name}/record/{record_id}', target=new_ip)
      return self

   def get_record_IDs(self, zone_name: str, field_type: str = 'A') -> list:
      return self.client.get(f'/domain/zone/{zone_name}/record', fieldType=field_type)

   def get_record_by_ID(self, zone_name: str, record_id: int) -> list:
      return self.client.get(f'/domain/zone/{zone_name}/record/{record_id}')

   def refresh_zone(self, zone_name: str):
      self.client.post(f'/domain/zone/{zone_name}/refresh')
      return self

   def get_server_IP(self) -> str:
      return re.get('https://api.myip.com').json()['ip']
