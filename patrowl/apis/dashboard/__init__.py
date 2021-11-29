#!/usr/bin/env -S python3 -OO
# coding:utf8

# Copyright (c) 2021, Patrowl and contributors
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

    def __init__(
            self, url, auth_token, proxies={}, ssl_verify=False, timeout=10):
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
    def action(self, url, method='GET', data=None, params={}):
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
    def get_assets(self, team_id=None, page=1, limit=10):
        """
        Get all assets.

        :param team_id: Team ID
        :param page: Page number of results (Opt.)
        :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
        :rtype: json
        """
        url_params = f'?format=json&page={page}&limit={limit}'
        if team_id is not None and str(team_id).isnumeric():
            url_params += '&team='+team_id

        try:
            r = self.rs.get(self.url+"/api/auth/assets/{}".format(url_params))
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to list assets: {}".format(e))

    # Vulns
    def get_vulns(self, team_id=None, page=1, limit=10):
        """
        Get all vulns.

        :param team_id: Team ID
        :param page: Page number of results (Opt.)
        :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
        :rtype: json
        """
        url_params = f'?format=json&page={page}&limit={limit}'
        if team_id is not None and str(team_id).isnumeric():
            url_params += '&team='+team_id

        try:
            r = self.rs.get(self.url+"/api/auth/vulns/{}".format(url_params))
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to list vulns: {}".format(e))

    # Tickets
    def get_tickets(self, team_id=None, page=1, limit=10):
        """
        Get all tickets.

        :param team_id: Team ID
        :param page: Page number of results (Opt.)
        :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
        :rtype: json
        """
        url_params = f'?format=json&page={page}&limit={limit}'
        if team_id is not None and str(team_id).isnumeric():
            url_params += '&team='+team_id

        try:
            r = self.rs.get(self.url+"/api/auth/tickets/{}".format(url_params))
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to list tickets: {}".format(e))

    def get_ticket(self, ticket_id):
        """
        Get ticket details.

        :param ticket_id: Ticket ID
        :rtype: json
        """
        try:
            r = self.rs.get(self.url+f"/api/auth/tickets/{ticket_id}/?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to retrieve ticket: {}".format(e))

    # Retests
    def get_retests(self, team_id=None, page=1, limit=10):
        """
        Get all retests.

        :param team_id: Team ID
        :param page: Page number of results (Opt.)
        :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
        :rtype: json
        """
        url_params = f'?format=json&page={page}&limit={limit}'
        if team_id is not None and str(team_id).isnumeric():
            url_params += '&team='+team_id

        try:
            r = self.rs.get(self.url+"/api/auth/retests/{}".format(url_params))
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to list retests: {}".format(e))

    def get_retest(self, retest_id):
        """
        Get retest details.

        :param retest_id: Retest ID
        :rtype: json
        """
        try:
            r = self.rs.get(self.url+f"/api/auth/retests/{retest_id}/?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to retrieve retest: {}".format(e))

    def cancel_retest(self, retest_id):
        """
        Cancel a retest.

        :param retest_id: Retest ID
        :rtype: json
        """
        try:
            r = self.rs.get(self.url+f"/api/auth/retests/{retest_id}/cancel?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to cancel retest: {}".format(e))

    def refresh_retest(self, retest_id):
        """
        Refresh a retest.

        :param retest_id: Retest ID
        :rtype: json
        """
        try:
            r = self.rs.get(self.url+f"/api/auth/retests/{retest_id}/refresh?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to refresh retest: {}".format(e))

    def sync_retests(self):
        """
        Sync all retests from Arsenal.

        :rtype: json
        """
        try:
            r = self.rs.get(self.url+"/api/auth/retests/sync?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to sync retests: {}".format(e))

    # Feeds
    def get_feeds(self, team_id=None, page=1, limit=10):
        """
        Get all feeds.

        :param team_id: Team ID
        :param page: Page number of results (Opt.)
        :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
        :rtype: json
        """
        url_params = f'?format=json&page={page}&limit={limit}'
        if team_id is not None and str(team_id).isnumeric():
            url_params += '&team='+team_id

        try:
            r = self.rs.get(self.url+"/api/auth/feeds/{}".format(url_params))
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to list feeds: {}".format(e))

    def get_overview_stats(self):
        """Return global stats."""
        stats = {}
        score = {}
        vulns = {}
        feeds = {}

        try:
            r = self.rs.get(self.url+"/api/auth/overview/widgets/stats")
            stats = r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to get ovw/stats: {}".format(e))

        try:
            r = self.rs.get(self.url+"/api/auth/overview/widgets/score")
            score = r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to get ovw/score: {}".format(e))

        try:
            r = self.rs.get(self.url+"/api/auth/overview/widgets/vulns")
            vulns = r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to get ovw/vulns: {}".format(e))

        try:
            r = self.rs.get(self.url+"/api/auth/overview/widgets/feeds")
            feeds = r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to get ovw/feeds: {}".format(e))

        return {
            'stats': stats,
            'score': score,
            'vulns': vulns,
            'feeds': feeds,
        }

    # Users
    def get_users(self, page=1, limit=10):
        """
        Get all users.

        :param page: Page number of results (Opt.)
        :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
        :rtype: json
        """
        url_params = f'?format=json&page={page}&limit={limit}'

        try:
            r = self.rs.get(self.url+"/api/auth/users/{}".format(url_params))
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to list users: {}".format(e))

    def get_user(self, user_id):
        """
        Get user details.

        :param user_id: User ID
        :rtype: json
        """
        try:
            r = self.rs.get(self.url+f"/api/auth/users/{user_id}/?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to retrieve user: {}".format(e))

    def get_user_totp(self, user_id):
        """
        Get user TOTP.

        :param user_id: User ID
        :rtype: json
        """
        try:
            r = self.rs.get(self.url+f"/api/auth/users/{user_id}/totp?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to retrieve user TOTP: {}".format(e))

    # Organizations
    def get_orgs(self, page=1, limit=10):
        """
        Get all organizations.

        :param page: Page number of results (Opt.)
        :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
        :rtype: json
        """
        url_params = f'?format=json&page={page}&limit={limit}'

        try:
            r = self.rs.get(self.url+"/api/auth/orgs/{}".format(url_params))
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to list orgs: {}".format(e))

    def get_org(self, org_id):
        """
        Get organization details.

        :param org_id: Organization ID
        :rtype: json
        """
        try:
            r = self.rs.get(self.url+f"/api/auth/orgs/{org_id}/?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to retrieve org: {}".format(e))

    def get_org_users(self, org_id):
        """
        Get organization users.

        :param org_id: Organization ID
        :rtype: json
        """
        try:
            r = self.rs.get(self.url+f"/api/auth/orgs/{org_id}/users/?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to retrieve org users: {}".format(e))

    def get_org_not_users(self, org_id):
        """
        Get users not in orgnization.

        :param org_id: Organization ID
        :rtype: json
        """
        try:
            r = self.rs.get(self.url+f"/api/auth/orgs/{org_id}/not-users/?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to retrieve org not users: {}".format(e))

    def get_org_settings(self, org_id):
        """
        Get users settings.

        :param org_id: Organization ID
        :rtype: json
        """
        try:
            r = self.rs.get(self.url+f"/api/auth/orgs/{org_id}/settings/?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to retrieve org settings: {}".format(e))

    def get_org_settings_reset(self, org_id):
        """
        Reset users settings.

        :param org_id: Organization ID
        :rtype: json
        """
        try:
            r = self.rs.get(self.url+f"/api/auth/orgs/{org_id}/settings/reset?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to reset org settings: {}".format(e))

    def get_org_setting(self, org_id, setting_id):
        """
        Get users settings.

        :param org_id: Organization ID
        :param setting_id: Setting ID
        :rtype: json
        """
        try:
            r = self.rs.get(self.url+f"/api/auth/orgs/{org_id}/settings/{setting_id}/?format=json")
            return r.text
        except requests.exceptions.RequestException as e:
            raise PatrowlException("Unable to retrieve org setting: {}".format(e))
