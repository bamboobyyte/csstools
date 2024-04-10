from flask import Blueprint, request, render_template
import ipaddress

sncalc = Blueprint('sncalc', __name__)

@sncalc.route('/subnetcalc', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        cidr = request.form['cidr']  # Assuming there's an input field named 'cidr' in the HTML form
        try:
            network = ipaddress.ip_network(cidr, strict=False)  # strict=False to allow non-canonical CIDRs
            network_id = network.network_address
            subnet_mask = network.netmask
            first_usable_ip = network.network_address + 1 if network.num_addresses > 2 else network.network_address
            last_usable_ip = network.broadcast_address - 1 if network.num_addresses > 2 else network.broadcast_address
            broadcast_ip = network.broadcast_address

            return render_template('sncalc.html', cidr=cidr, network_id=network_id, subnet_mask=subnet_mask,
                                   first_usable_ip=first_usable_ip, last_usable_ip=last_usable_ip, broadcast_ip=broadcast_ip)
        except ValueError:
            error_message = "Invalid CIDR notation"
            return render_template('sncalc.html', error=error_message)
    return render_template('sncalc.html')
