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

from patrowl.apis.dashboard import PatrowlApi
import json
import pytest

api = PatrowlApi(
    url='http://localhost:8005',
    auth_token='dd222d58fb5e72242d2cacd3f358c86bf84f1dcb'
)

@pytest.mark.run('first')
def test_first():
    # Vulns
    # List all vulns
    print(api.get_vulns())

    new_vuln = api.create_vuln(
        # arsenal_id=0,
        asset_id=1,
        severity=1,  # Low
        cvss_vector="AV:A/AC:H/PR:L/UI:R/S:C/C:H/I:H/A:H",
        title="title test",
        description="description test",
        solution_headline="solution_headline test",
        solution="solution test",
        solution_priority="urgent",
        solution_effort="medium",
        is_quickwin=True,
        comments=""
    )
    print(new_vuln)

    # Get vuln
    vuln = api.get_vuln(
        vuln_id=json.loads(new_vuln)['id']
    )
    print(vuln)

    # Delete the vuln
    deleted_vuln = api.delete_vuln(
        vuln_id=json.loads(new_vuln)['id']
    )
    print(deleted_vuln)
