# Socrata Creator
Create Socrata datasets via API. Complementary to [socrata-pusher](https://github.com/timwis/socrata-pusher).

# Note: this functionality is being incorporated into [sodapy](https://github.com/xmunoz/sodapy/pull/8)
This repo only serves as a demonstration/proof of concept

## Installation
`pip install -r requirements.txt`

## Configuration
Rename `.env.sample` to `.env` and fill in the values for your Socrata instance.
At the moment this project just creates a sample dataset, defined in `main.py` using columns defined in `sample_fields.json`.

## Roadmap
A library for creating datasets in Socrata that can be paired with a database reader to facilitate replication from database to Socrata 

## Field Types
* text
* number
* calendar_date
* money
* location
* multipolygon
