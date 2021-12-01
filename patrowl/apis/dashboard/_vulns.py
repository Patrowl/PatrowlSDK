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
from . import constants


def get_vulns(self, org_id=None, page=1, limit=10):
    """
    Get all vulns.

    :param org_id: Organization ID
    :param page: Page number of results (Opt.)
    :param limit: Max results per page. Default is 10, Max is 100 (Opt.)
    :rtype: json
    """
    url_params = f'?format=json&page={page}&limit={limit}'
    if org_id is not None and str(org_id).isnumeric():
        url_params += f'&org={org_id}'

    try:
        r = self.rs.get(self.url+"/api/auth/vulns/{}".format(url_params))
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to list vulns: {}".format(e))


def get_vuln(self, vuln_id):
    """
    Get vuln details.

    :param vuln_id: Vulnerability ID
    :type vuln_id: int|str
    :return: Vulnerability details
    :rtype: json
    """
    try:
        r = self.rs.get(self.url+f"/api/auth/vulns/{vuln_id}/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to retrieve vuln: {}".format(e))


def create_vuln(
        self, asset_id, severity=0, cvss_vector="", title="", description="",
        category="", solution_headline="", solution="",
        solution_priority="hardening", solution_effort="low",
        is_quickwin=False, comments=""):
    """
    Create a new vulnerability.

    :param asset_id: Asset ID
    :param severity: Severity
    :param cvss_vector: CVSSv3 vector
    :param title: Title
    :param description: Description
    :param category: Category
    :param solution_headline: Solution Headline
    :param solution: Solution details
    :param solution_priority: Solution priority
    :param solution_effort: Solution effort
    :param is_quickwin: Is quick-win ?
    :param comments: Comments
    :rtype: json
    """
    if severity not in constants.VULNERABILITY_SEVERITY:
        raise PatrowlException("Bad 'severity' parameter")
    if solution_priority not in constants.VULNERABILITY_SOLUTION_PRIORITIES:
        raise PatrowlException("Bad 'solution_priority' parameter")
    if solution_effort not in constants.VULNERABILITY_SOLUTION_EFFORTS:
        raise PatrowlException("Bad 'solution_effort' parameter")
    data = {
        'asset': asset_id,
        'severity': severity,
        'cvss_vector': cvss_vector,
        'title': title,
        'description': description,
        'category': category,
        'solution_headline': solution_headline,
        'solution': solution,
        'solution_priority': solution_priority,
        'solution_effort': solution_effort,
        'is_quickwin': is_quickwin,
        'comments': comments
    }
    try:
        r = self.rs.post(self.url+"/api/auth/vulns/?format=json", json=data)
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to create vuln: {}".format(e))


def delete_vuln(self, vuln_id):
    """
    Delete a vulnerability.

    :param vuln_id: Vuln ID
    :type vuln_id: int|str
    :rtype: json
    """
    try:
        r = self.rs.delete(self.url+f"/api/auth/vulns/{vuln_id}/?format=json")
        return r.text
    except requests.exceptions.RequestException as e:
        raise PatrowlException("Unable to delete a vuln: {}".format(e))
