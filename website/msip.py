import os
import json
import ipaddress
from flask import Blueprint, request, render_template

msip = Blueprint('msip', __name__)

# Path to the service_tags directory
service_tags_dir = os.path.join(os.path.dirname(__file__), 'service_tags')

# Dynamically load the service tag data from JSON files
service_tags = {}
for file_name in os.listdir(service_tags_dir):
    if file_name.endswith('.json'):
        file_path = os.path.join(service_tags_dir, file_name)
        with open(file_path) as f:
            service_tags[file_name] = json.load(f)["values"]

def is_valid_ip(ip_address):
    try:
        ipaddress.ip_address(ip_address)
        return True
    except ValueError:
        return False

def find_ip_in_service_tags(ip_address):
    if not is_valid_ip(ip_address):
        return [{'ip': ip_address, 'error': 'Invalid IP address'}]
    
    results = []
    for file_name, services in service_tags.items():
        found = False
        for service in services:
            for prefix in service["properties"]["addressPrefixes"]:
                if ipaddress.ip_address(ip_address) in ipaddress.ip_network(prefix):
                    results.append({
                        'ip': ip_address,
                        'name': service['name'],
                        'file': file_name
                    })
                    found = True
                    break
            if found:
                break
        if not found:
            results.append({'ip': ip_address, 'name': 'Not found', 'file': file_name})
    return results

@msip.route('/isthismsip', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        ips_text = request.form['ips']
        ips = ips_text.strip().splitlines()
        all_results = []
        for ip in ips:
            results = find_ip_in_service_tags(ip)
            all_results.extend(results)
        return render_template('msip.html', results=all_results)
    return render_template('msip.html')
