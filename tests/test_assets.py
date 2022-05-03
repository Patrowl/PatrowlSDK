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
import os


api = PatrowlApi(
    url=os.environ['URL'],
    auth_token=os.environ['TOKEN']
)


@pytest.mark.run('first')
def test_first():
    # Assets
    # List all assets
    print(api.get_assets())
    print(api.get_assets(1))

    # Sync all assets
    r = json.loads(api.sync_assets(2))
    print(r['status'])
    assert r['status'] == "enqueued"

    # Create an asset
    new_asset = api.create_asset(
        value="coucou.com",
        criticality=1,  # Low
        type="domain",
        is_active=True,
        description="description test",
        exposure="external",
        is_monitored=True
    )
    print(new_asset)

    # Get asset
    asset = api.get_asset(
        asset_id=json.loads(new_asset)['id']
    )
    print(asset)

    # Update the asset
    updated_asset = api.update_asset(
        asset_id=json.loads(new_asset)['id'],
        kwargs={'exposure': 'internal'}
    )
    print(updated_asset)

    # Delete the asset
    deleted_asset = api.delete_asset(
        asset_id=json.loads(updated_asset)['id']
    )
    print(deleted_asset)
