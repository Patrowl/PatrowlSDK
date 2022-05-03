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

# Assets
ASSET_TYPES = [
    'ip',
    'ip-range',
    'ip-subnet',
    'fqdn',
    'domain',
    'url',
    'keyword'
]

ASSET_EXPOSURES = [
    'unknown', 'external', 'internal', 'restricted'
]

ASSET_CRITICALITIES = [
    1, 2, 3
]


# Vulnerability
VULNERABILITY_SEVERITY = [
    0, 1, 2, 3, 4
]

VULNERABILITY_STATUS = [
    'new', 'ack', 'assigned', 'patched', 'closed',
    'closed-benign', 'closed-fp', 'closed-duplicate', 'closed-workaround'
]

active_vulns_status = [
    'new', 'ack', 'assigned'
]

closed_vulns_status = [
    'patched', 'closed',
    'closed-benign', 'closed-fp', 'closed-duplicate', 'closed-workaround'
]

VULNERABILITY_SOLUTION_PRIORITIES = [
    'urgent', 'moderate', 'hardening'
]

VULNERABILITY_SOLUTION_EFFORTS = [
    'low', 'medium', 'high'
]
