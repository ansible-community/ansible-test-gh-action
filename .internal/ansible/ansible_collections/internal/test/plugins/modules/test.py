#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2022 Felix Fontein <felix@fontein.de>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r'''
---
module: test
short_description: Test module
version_added: 0.1.0
author:
  - Felix Fontein (@felixfontein)
description:
  - Just a test.
notes:
  - Does not support C(check_mode).

options:
  test:
    description: Some string that is echoed back.
    required: true
    type: str
'''

EXAMPLES = r'''
- name: Does nothing
  internal.test.test:
    test: foo
'''

RETURN = r'''
test:
  description: The value of the I(test) input.
  type: str
  returned: success
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(argument_spec={'test': {'type': 'str', 'required': True}})
    module.exit_json(test=module.params['test'])


if __name__ == '__main__':
    main()
