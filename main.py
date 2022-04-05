# from ansible import playbook as p
import json
from turtle import RawTurtle
import ansible
from flask import Flask, render_template, request
import ansible_runner

from switch import Switch, Interface, Cisco3750G

from jinja2 import Template

tm = Template("Hello {{ name }}")
msg = tm.render(name='steve')

print(msg)

def run_playbook(playbook_path: str, ansible_vars: dict):
    runner = ansible_runner.run_async(playbook=playbook_path, extravars=ansible_vars)
    # print(runner)
    return runner


PLAYBOOK_ROOT = '/home/pi/IT&C 529 - Advanced Networking Final Project/playbooks/'

def main():
    app = Flask(__name__)
    playbooks_dir = './playbooks'

    @app.route('/')
    def home():
        return render_template('default.html')

    @app.route('/ping/<host>', methods=['GET'])
    def ping_host(host):
        run = run_playbook(PLAYBOOK_ROOT + 'cisco_change_vlan.yml', {'host_list': f'{host}'})
        print(run[0])
        print(run[1])
        return render_template('interfaces.html')


    @app.route('/vlan/<host>', methods=['GET'])
    def add_vlan(host):
        vlan = request.args.get('vlan')
        run = run_playbook(PLAYBOOK_ROOT + 'cisco_ping.yml', {'host_list': f'{host}', 'vlan': f'{vlan}'})
        return render_template('interfaces.html')
    //?
    @app.route('/vlan/<host>', methods=['GET'])
    def add_vlan_to_interface(host):
        vlan = request.args.get('vlan')
        interface = request.args.get('interface')
        run = run_playbook(PLAYBOOK_ROOT + 'cisco_interface_vlan.yml', {'host_list': f'{host}', 'vlan': f'{vlan}', 'interface': f'{interface}'})
        return render_template('interfaces.html')

    @app.route('/<host>', methods=['GET'])
    def get_host(host):
        # TODO: fill in getting actual host interfaces later

        physical_interfaces = [
            {'number': 1, 'name': 'gigabitEthernet1/0/1', 'column': 1},
            {'number': 2, 'name': 'gigabitEthernet1/0/2', 'column': 2},
            {'number': 3, 'name': 'gigabitEthernet1/0/3', 'column': 1},
            {'number': 4, 'name': 'gigabitEthernet1/0/4', 'column': 2},
        ]

        vlan_interfaces = [
            {'number': 1, 'vlan': 10},
            {'number': 2, 'vlan': 20},
            {'number': 3, 'vlan': 30},
            {'number': 4, 'vlan': 40},
        ]
        return render_template('interfaces.html', physical_interfaces=physical_interfaces)
        
    @app.route('/<host>/<interface>', methods=['GET'])
    def get_host_interface(host, interface):
        pass

    @app.route('/css/flexbox.css')
    def get_flexbox():
        return render_template('flexbox.css')

    @app.route('/csstest')
    def test_css():
        things = [i for i in range(1, 25)]
        print(things)
        return render_template('flexbox.html', things=things)


    app.run()
    


if __name__ == '__main__':
    main()
