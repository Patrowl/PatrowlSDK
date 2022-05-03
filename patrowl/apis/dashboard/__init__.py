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


class PatrowlApi:
    """Python API for Patrowl."""

    def __init__(self, url: str, auth_token: str, proxies: dict = {}, ssl_verify: bool = False, timeout: int = 10):
        """
        Initialize a PatrowlApi object.

        :param url: Patrowl base URL
        :param auth_token: The API key
        :param proxies: The HTTP/HTTPS proxy endpoints
        :param ssl_verify: SSL/TLS certificate verification
        :param timeout: Request timeout (in sec)
        """
        self.url = url
        self.auth_token = auth_token
        self.timeout = timeout
        self.rs = requests.Session()
        self.rs.headers.update({
            'Authorization': 'Token {}'.format(auth_token),
            'Content-Type': 'application/json'
        })
        self.rs.proxies = proxies
        self.rs.verify = ssl_verify
        self.rs.timeout = timeout

    # Generic command
    def action(self, url: str, method: str = 'GET', data: dict = None, params: dict = {}):
        """
        Call a generic action.

        :param url: API endpoint
        :param method: HTTP method ('GET', 'POST', 'DELETE', 'PUT', 'PATCH')
        :param data: HTTP data
        :rtype: json
        """
        if method.upper() not in ['GET', 'POST', 'DELETE', 'PUT', 'PATCH']:
            raise PatrowlException("Bad method: {}".format(method))

        try:
            r = requests.Request(
                method=method.upper(),
                url=self.url+url,
                data=data,
                params=params,
                headers={
                    'Authorization': 'Token {}'.format(self.auth_token),
                    'Content-Type': 'application/json'
                }
            )
            pr = r.prepare()
            return self.rs.send(pr).json()
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to retrieve vuln: {}".format(e))

    # Assets
    from ._assets import get_assets, get_asset, sync_assets
    from ._assets import create_asset, update_asset, delete_asset

    # Vulns
    from ._vulns import get_vulns, get_vuln, create_vuln, delete_vuln

    # Pentests
    from ._pentests import get_pentests, get_pentest
    from ._pentests import create_pentest, delete_pentest
    from ._pentests import get_pentest_assets, get_pentest_vulns

    # Tickets
    from ._tickets import get_tickets, get_ticket

    # Retests
    from ._retests import get_retests, get_retest, cancel_retest
    from ._retests import refresh_retest, sync_retests

    # Feeds
    from ._feeds import get_feeds

    # Users
    from ._users import get_users, get_user, get_user_totp

    # Organizations
    from ._orgs import get_orgs, get_org, add_org, delete_org
    from ._orgs import get_org_users, get_org_not_users
    from ._orgs import get_org_settings, get_org_setting
    from ._orgs import get_org_settings_reset

    # Stats
    def get_overview_stats(self, org_id: int):
        """Return global stats."""
        stats = {}
        score = {}
        vulns = {}
        feeds = {}

        try:
            r = self.rs.get(self.url+"/api/auth/overview/" + str(org_id) + "/widgets/stats")
            stats = r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to get ovw/stats: {}".format(e))

        try:
            r = self.rs.get(self.url+"/api/auth/overview/" + str(org_id) + "/widgets/score")
            score = r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to get ovw/score: {}".format(e))

        try:
            r = self.rs.get(self.url+"/api/auth/overview/" + str(org_id) + "/widgets/vulns")
            vulns = r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to get ovw/vulns: {}".format(e))

        try:
            r = self.rs.get(self.url+"/api/auth/overview/" + str(org_id) + "/widgets/feeds")
            feeds = r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to get ovw/feeds: {}".format(e))

        return {
            'stats': stats,
            'score': score,
            'vulns': vulns,
            'feeds': feeds,
        }
