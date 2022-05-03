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


def delete_org(self, org_id: int):
    """
    Delete organisation.

    ** Administration Only **

    :param id: Organization id
    """
    try:
        r = self.rs.delete(f"{self.url}/api/auth/orgs/{str(org_id)}/")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to delete org: {}".format(e))


def create_org(self, name: str, slug: str, is_active: bool):
    """
    Create new organisation.

    ** Administration Only **

    :param name: Organization name
    :param slug: Organization slug
    :param is_active: boolean
    """
    data = {
        'name': name,
        'slug': slug,
        'is_active': is_active
    }
    try:
        r = self.rs.post(self.url+"/api/auth/orgs/?format=json", json=data)
        return r.json()
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to add org: {}".format(e))


def get_orgs(self, page: int = 1, limit: int = 10):
    """
    Get all organizations.

    ** Administration Only **

    :param page: Page number of results (Opt.)
    :type page: int
    :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
    :type limit: int
    :rtype: json
    """
    url_params = f'?format=json&page={str(page)}&limit={str(limit)}'

    try:
        r = self.rs.get(self.url+"/api/auth/orgs/{}".format(url_params))
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to list orgs: {}".format(e))


def get_org(self, org_id: int):
    """
    Get organization details.

    :param org_id: Organization ID
    :type org_id: int
    :rtype: json
    """
    try:
        r = self.rs.get(self.url+f"/api/auth/orgs/{str(org_id)}/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to retrieve org: {}".format(e))


def get_org_users(self, org_id: int):
    """
    Get organization users.

    :param org_id: Organization ID
    :type org_id: int
    :rtype: json
    """
    try:
        r = self.rs.get(self.url+f"/api/auth/orgs/{str(org_id)}/users/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to retrieve org users: {}".format(e))


def get_org_not_users(self, org_id: int):
    """
    Get users not in orgnization.

    :param org_id: Organization ID
    :type org_id: int
    :rtype: json
    """
    try:
        r = self.rs.get(
            self.url+f"/api/auth/orgs/{str(org_id)}/not-users/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to retrieve org nusers: {}".format(e))


def get_org_settings(self, org_id: int):
    """
    Get users settings.

    :param org_id: Organization ID
    :type org_id: int
    :rtype: json
    """
    try:
        r = self.rs.get(
            self.url+f"/api/auth/orgs/{str(org_id)}/settings/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to retrieve org settings: {}".format(e))


def get_org_settings_reset(self, org_id: int):
    """
    Reset users settings.

    :param org_id: Organization ID
    :type org_id: int
    :rtype: json
    """
    try:
        r = self.rs.get(
            self.url+f"/api/auth/orgs/{str(org_id)}/settings/reset?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to reset org settings: {}".format(e))


def get_org_setting(self, org_id: int, setting_id: int):
    """
    Get users settings.

    :param org_id: Organization ID
    :type org_id: int
    :param setting_id: Setting ID
    :type setting_id: int
    :rtype: json
    """
    try:
        r = self.rs.get(self.url+f"/api/auth/orgs/{str(org_id)}/settings/{str(setting_id)}/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to retrieve org setting: {}".format(e))
