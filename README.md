# ansible-test-gh-action for setting up CI in Ansible Collection repositories

A composite GitHub Action encapsulating the GitHub Actions CI/CD workflows
setup necessary for testing Ansible collection repositories on GitHub.


## Usage

To use the action add the following step to your workflow file (e.g.
`.github/workflows/ansible-test.yml`)

```yaml
- name: Perform integration testing with ansible-test
  uses: ansible-community/ansible-test-gh-action@release/v1
  with:
    ansible-core-version: stable-2.11
    pre-test-cmd: echo This runs before the ansible-test invocation
    python-version: 3.9
    target-python-version: 3.9
    testing-type: integration
    test-deps: ansible.netcommon
- name: Perform sanity testing with ansible-test
  uses: ansible-community/ansible-test-gh-action@release/v1
  with:
    ansible-core-version: stable-2.11
    testing-type: sanity
- name: Perform unit testing with ansible-test
  uses: ansible-community/ansible-test-gh-action@release/v1
  with:
    ansible-core-version: stable-2.11
    pre-test-cmd: echo This runs before the ansible-test invocation
    python-version: 3.9
    target-python-version: 3.9
    testing-type: units
    test-deps: >-
      ansible.netcommon
      ansible.utils
```

> **Pro tip**: instead of using branch pointers, like `main`, pin
versions of Actions that you use to tagged versions or SHA-1 commit
identifiers. This will make your workflows more secure and better
reproducible, saving you from sudden and unpleasant surprises.


## Options


### `ansible-core-version`

`ansible-core` Git revision. See https://github.com/ansible/ansible/tags
and https://github.com/ansible/ansible/branches/all?query=stable- for
ideas **(DEFAULT: `stable-2.11`)**


### `docker-image`

A container image spawned by `ansible-test` **(OPTIONAL)**


### `pre-test-cmd`

Extra command to invoke before ansible-test **(OPTIONAL)**


### `python-version`

Controller Python version **(DEFAULT: `3.9`)**


### `target`

`ansible-test` TARGET **(OPTIONAL)**


### `target-python-version`

Target Python version **(OPTIONAL)**


### `testing-type`

`ansible-test` subcommand **(REQUIRED, Must be one of 'sanity', 'units'
or 'integration')**


### `test-deps`

Test dependencies to install along with this collection **(OPTIONAL)**
