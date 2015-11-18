import os
from dotenv import load_dotenv
import json
import random
import string

import requests

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

options = {}
for name in [
	'USERNAME',
	'PASSWORD',
	'HOSTNAME'
]:
	options[name] = os.environ.get(name)
hostname = options['HOSTNAME'].rstrip('/') # remove trailing slash
auth = (options['USERNAME'], options['PASSWORD'])
	
# Create dataset
def create_dataset(metadata):
	r = requests.post(hostname + '/api/views.json',
		auth=auth,
		data=json.dumps(metadata)
	)
	return r.json()

# Make dataset public
def make_dataset_public(dataset_id):
	params = {
		'method': 'setPermission',
		'value': 'public.read'
	}
	r = requests.put(hostname + '/api/views/' + dataset_id, auth=auth, params=params)
	return r.status_code == 200

# Publish dataset
def publish_dataset(dataset):
	r = requests.post(hostname + '/api/views/' + dataset_id + '/publication.json', auth=auth)
	return r.status_code == 200
	
# Create a sample dataset
if __name__ == '__main__':
	# Load fields from sample file
	with open('sample_fields.json') as sample_fields_file:
		sample_fields = json.load(sample_fields_file)
	
	payload = {
		'name': 'Test ' + ''.join(random.choice(string.lowercase) for i in range(6)), # random string
		'description': 'Created via socrata-dataset-creator for testing purposes',
		'columns': sample_fields
	}
	
	# I'm probably doing try/catch incorrectly. Any suggestions? (via issue or PR)
	try:
		dataset = create_dataset(payload)
		dataset_id = dataset[u'id']
		print('Dataset created at %s/d/%s' % (hostname, dataset_id))
		
		if make_dataset_public(dataset_id):
			print('Made %s public' % dataset_id)
		else:
			print('Error making %s public' % dataset_id)
		
		if publish_dataset(dataset_id):
			print('Published %s' % dataset_id)
		else:
			print('Error publishing %s' % dataset_id)
		
	except Error as e:
		print('An error occurred: %s - %s' % (e.__class__, e))
		raise