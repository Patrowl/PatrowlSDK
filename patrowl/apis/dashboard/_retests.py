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


def get_retests(self, org_id: int = None, page: int = 1, limit: int = 10):
    """
    Get all retests.

    :param org_id: Organization ID
    :param page: Page number of results (Opt.)
    :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
    :rtype: json
    """
    url_params = f'?format=json&page={str(page)}&limit={str(limit)}'
    if org_id is not None and str(org_id).isnumeric():
        url_params += f'&org={str(org_id)}'

    try:
        r = self.rs.get(self.url+"/api/auth/retests/{}".format(url_params))
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to list retests: {}".format(e))


def get_retest(self, retest_id: int):
    """
    Get retest details.

    :param retest_id: Retest ID
    :rtype: json
    """
    try:
        r = self.rs.get(self.url+f"/api/auth/retests/{str(retest_id)}/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to retrieve retest: {}".format(e))


def cancel_retest(self, retest_id: int):
    """
    Cancel a retest.

    :param retest_id: Retest ID
    :rtype: json
    """
    try:
        r = self.rs.get(
            self.url+f"/api/auth/retests/{str(retest_id)}/cancel?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to cancel retest: {}".format(e))


def refresh_retest(self, retest_id: int):
    """
    Refresh a retest.

    :param retest_id: Retest ID
    :rtype: json
    """
    try:
        r = self.rs.get(
            self.url+f"/api/auth/retests/{str(retest_id)}/refresh?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to refresh retest: {}".format(e))


def sync_retests(self):
    """
    Sync all retests from Arsenal.

    ** Administration Only **

    :rtype: json
    """
    try:
        r = self.rs.get(self.url+"/api/auth/retests/sync?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to sync retests: {}".format(e))
