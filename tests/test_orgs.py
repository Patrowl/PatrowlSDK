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
    """Get orgs."""
    orgs = json.loads(api.get_orgs())
    assert len(orgs['results']) >= 0


def test_org_details():
    """Get org details."""
    orgs = json.loads(api.get_orgs())
    org_id = orgs['results'][0]['id']
    assert str(org_id).isnumeric()
    org = json.loads(api.get_org(org_id))
    assert org['name'] != ""
    org_users = json.loads(api.get_org_users(org_id))
    assert len(org_users['results']) >= 0
    org_not_users = json.loads(api.get_org_not_users(org_id))
    assert len(org_not_users['results']) >= 0

# org_settings = json.loads(api.get_org_settings(org_id))
# print(org_settings)
# print(api.get_org_setting(org_id, org_settings['results'][0]['id']))


# reset
# print(api.get_org_settings_reset(org_id))
