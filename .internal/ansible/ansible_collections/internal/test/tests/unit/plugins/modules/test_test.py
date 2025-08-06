# Copyright (c) 2020 Felix Fontein <felix@fontein.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import contextlib
import json

import pytest
from ansible.module_utils import basic
from ansible.module_utils.common.text.converters import to_bytes
from ansible_collections.internal.test.plugins.modules import test

try:
    from unittest import mock
except ImportError:
    import mock


@contextlib.contextmanager
def set_module_args(args):
    """
    Context manager that sets module arguments for AnsibleModule
    """
    if '_ansible_remote_tmp' not in args:
        args['_ansible_remote_tmp'] = '/tmp'
    if '_ansible_keep_remote_files' not in args:
        args['_ansible_keep_remote_files'] = False

    try:
        from ansible.module_utils.testing import patch_module_args
    except ImportError:
        # Before data tagging support was merged, this was the way to go:
        from ansible.module_utils import basic
        serialized_args = to_bytes(json.dumps({'ANSIBLE_MODULE_ARGS': args}))
        with mock.patch.object(basic, '_ANSIBLE_ARGS', serialized_args):
            yield
    else:
        # With data tagging support, we have a new helper for this:
        with patch_module_args(args):
            yield


class AnsibleExitJson(Exception):
    def __init__(self, kwargs):
        self.kwargs = kwargs


def exit_json(*args, **kwargs):
    if 'changed' not in kwargs:
        kwargs['changed'] = False
    raise AnsibleExitJson(kwargs)


def test_test():
    with set_module_args({'test': 'foo'}):
        with mock.patch.multiple(basic.AnsibleModule, exit_json=exit_json):
            with pytest.raises(AnsibleExitJson) as e:
                test.main()
    assert 'test' in e.value.kwargs
    assert e.value.kwargs['test'] == 'foo'
