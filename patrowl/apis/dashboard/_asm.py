#!/usr/bin/env -S python3 -OO
# coding:utf8

# Copyright (c) 2022, Patrowl and contributors
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.  Redistributions in binary
# form must reproduce the above copyright notice, this list of conditions and
# the following disclaimer in the documentation and/or other materials provided
# with the distribution
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import requests
from patrowl.exceptions import PatrowlException

# ASM // IPAddress


def get_ipaddresses(self, team_id=None):
    """
    Get IPAddress objects.

    :param team_id: Team ID
    :rtype: json
    """
    url = self.url + '/api/auth/asm/ip-address/'
    if team_id is not None and str(team_id).isnumeric():
        url += f'?team={team_id}'
    try:
        return self.rs.get(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to retrieve IP address: {}".format(e))


def get_ipaddress(self, id):
    """
    Get IPAddress object by id.

    :param id: IPAddress ID
    :rtype: json
    """
    url = self.url + f'/api/auth/asm/ip-address/{id}/'
    try:
        return self.rs.get(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException(
            "Unable to retrieve IP address by id: {}".format(e))


def get_ipaddress_by_value(self, value):
    """
    Get IPAddress object by value.

    :param value: IPAddress address
    :rtype: json
    """
    url = self.url + f'/api/auth/asm/ip-address/q/{value}/'
    try:
        return self.rs.get(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException(
            "Unable to retrieve IP address by value: {}".format(e))


def add_ipaddress(self, asset, address, type="ipv4", is_up=True, ping_ok=True):
    """
    Add a new IPAddress.

    :param asset: Asset ID
    :param address: IPAddress address
    :param type: 'ipv4' or 'ipv6'
    :param is_up: boolean
    :param ping_ok: boolean
    """
    url = self.url + '/api/auth/asm/ip-address/'
    data = {
        "asset_id": asset,
        "address": address,
        "type": type,
        "is_up": is_up,
        "ping_ok": ping_ok
    }

    try:
        return self.rs.post(url, json=data)
    except requests.exceptions.RequestException as e:
        raise PatrowlException(
            "Unable to create a new IPAddress: {}".format(e))


def delete_ipaddress(self, id):
    """
    Delete an IPAddress.

    :id: IPAddress ID
    """
    url = self.url + f'/api/auth/asm/ip-address/{id}/'
    try:
        return self.rs.delete(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to delete ip address: {}".format(e))

# ASM // Domain


def get_domains(self, team_id=None):
    """
    Get Domain objects.

    :param team_id: Team ID
    :rtype: json
    """
    url = self.url + '/api/auth/asm/domain/'
    if team_id is not None and str(team_id).isnumeric():
        url += f'?team={team_id}'

    try:
        return self.rs.get(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException(
            "Unable to retrieve Domain objects: {}".format(e))


def get_domain(self, id):
    """
    Get Domain object by id.

    :param id: Domain ID
    :rtype: json
    """
    url = self.url + f'/api/auth/asm/domain/{id}/'
    try:
        return self.rs.get(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to retrieve domain by id: {}".format(e))


def get_domain_by_value(self, value):
    """
    Get Domain object by value.

    :param value: Domain value
    :rtype: json
    """
    url = self.url + f'/api/auth/asm/domain/q/{value}/'
    try:
        return self.rs.get(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException(
            "Unable to retrieve domain by value: {}".format(e))


def add_domain(self, asset, name, parent_domain=None, is_registered=True):
    """
    Add a new Domain.

    :param asset: Asset ID
    :param name: Domain address
    :param parent_domain: Domain id
    :param is_registered: boolean
    """
    url = self.url + '/api/auth/asm/domain/'
    data = {
        "asset_id": asset,
        "name": name,
        "parent_domain": parent_domain,
        "is_registered": is_registered
    }
    try:
        return self.rs.post(url, json=data)
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to create a new Domain: {}".format(e))


def delete_domain(self, id):
    """
    Delete a Domain.

    :id: Domain ID
    """

    url = self.url + f'/api/auth/asm/domain/{id}/'
    try:
        return self.rs.delete(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to delete Domain: {}".format(e))


# ASM // Port


def get_ports(self, team_id=None):
    """
    Get Port objects.

    :param team_id: Team ID
    :rtype: json
    """
    url = self.url + '/api/auth/asm/port/'
    if team_id is not None and str(team_id).isnumeric():
        url += f'?team={team_id}'
    try:
        return self.rs.get(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to retrieve Port objects: {}".format(e))


def get_port(self, id):
    """
    Get Port object by id.

    :param id: Port ID
    :rtype: json
    """
    url = self.url + f'/api/auth/asm/port/{id}/'
    try:
        return self.rs.get(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to retrieve port by id: {}".format(e))


# def add_port(self, asset, name, parent_domain=None, is_registered=True):
#     """
#     Add a new Port.
#
#     :param asset: Asset ID
#     """
#     url = self.url+ '/api/auth/asm/port/'
#     data = {
#         "asset_id": asset,
#     }
#     return self.rs.get(
#         self.rs.post,
#         url,
#         'Unable to create a new Port',
#         payload=json.dumps(data)
#     )


def delete_port(self, id):
    """
    Delete a Port.

    :id: Port ID
    """
    url = self.url + f'/api/auth/asm/port/{id}/'
    try:
        return self.rs.delete(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to delete Port: {}".format(e))


# ASM // WebServer


def get_webservers(self, team_id=None):
    """
    Get WebServer objects.

    :param team_id: Team ID
    :rtype: json
    """
    url = self.url + '/api/auth/asm/web/'
    if team_id is not None and str(team_id).isnumeric():
        url += f'?team={team_id}'
    try:
        return self.rs.get(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException(
            "Unable to retrieve WebServer objects: {}".format(e))


def get_webserver(self, id):
    """
    Get WebServer object by id.

    :param id: WebServer ID
    :rtype: json
    """
    url = self.url + f'/api/auth/asm/web/{id}/'
    try:
        return self.rs.get(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException(
            "Unable to retrieve web server by id: {}".format(e))


# def add_webserver(self, asset, name, parent_domain=None, is_registered=True):
#     """
#     Add a new WebServer.
#
#     :param asset: Asset ID
#     """
#     url = self.url+ '/api/auth/asm/web/'
#     data = {
#         "asset_id": asset,
#     }
#     return self.rs.get(
#         self.rs.post,
#         url,
#         'Unable to create a new WebServer',
#         payload=json.dumps(data)
#     )


def delete_webserver(self, id):
    """
    Delete a WebServer.

    :id: WebServer ID
    """
    url = self.url + f'/api/auth/asm/web/{id}/'
    try:
        return self.rs.delete(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to delete WebServer: {}".format(e))


# ASM // Certificate


def get_certificates(self, team_id=None):
    """
    Get Certificate objects.

    :param team_id: Team ID
    :rtype: json
    """
    url = self.url + '/api/auth/asm/cert/'
    if team_id is not None and str(team_id).isnumeric():
        url += f'?team={team_id}'
    try:
        return self.rs.get(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException(
            "Unable to retrieve Certificate objects: {}".format(e))


def get_certificate(self, id):
    """
    Get Certificate object by id.

    :param id: Certificate ID
    :rtype: json
    """
    url = self.url + f'/api/auth/asm/cert/{id}/'
    try:
        return self.rs.get(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException(
            "Unable to retrieve certificate by id: {}".format(e))

# def add_certificate(self, asset, name, parent_domain=None, is_registered=True):
#     """
#     Add a new Certificate.
#
#     :param asset: Asset ID
#     """
#     url = self.url+ '/api/auth/asm/cert/'
#     data = {
#         "asset_id": asset,
#     }
#     return self.rs.get(
#         self.rs.post,
#         url,
#         'Unable to create a new certificate',
#         payload=json.dumps(data)
#     )


def delete_certificate(self, id):
    """
    Delete a Certificate.

    :id: Certificate ID
    """
    url = self.url + f'/api/auth/asm/cert/{id}/'
    try:
        return self.rs.delete(url)
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to delete Certificate: {}".format(e))
