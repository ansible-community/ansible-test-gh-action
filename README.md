[![🧪 GitHub Actions CI/CD workflow tests badge]][GHA workflow runs list]
[![pre-commit.ci status badge]][pre-commit.ci results page]

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
    ansible-core-version: stable-2.14
    pre-test-cmd: echo This runs before the ansible-test invocation
    target-python-version: 3.9
    controller-python-version: auto
    testing-type: integration
    test-deps: ansible.netcommon
- name: Perform sanity testing with ansible-test
  uses: ansible-community/ansible-test-gh-action@release/v1
  with:
    ansible-core-version: stable-2.14
    testing-type: sanity
- name: Perform unit testing with ansible-test
  uses: ansible-community/ansible-test-gh-action@release/v1
  with:
    ansible-core-version: stable-2.14
    pre-test-cmd: echo This runs before the ansible-test invocation
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
ideas. The repository this refers to can be changed with the
`ansible-core-github-repository-slug` option. **(DEFAULT: `stable-2.14`)**


### `ansible-core-github-repository-slug`

The GitHub repository slug from which to check out ansible-core
**(DEFAULT: `ansible/ansible`)**


### `controller-python-version`

Controller Python version. This is only used for integration tests and
ansible-core 2.12 or later when `target-python-version` is also specified
**(DEFAULT: `auto`)**


### `collection-root`

Path to collection root relative to repository root **(DEFAULT: `.`)**


### `collection-src-directory`

A pre-checked out collection directory that's already on disk
**(OPTIONAL, substitutes getting the source from the remote Git
repository if set, also this action will not attempt to mutate
its contents)**


### `docker-image`

A container image spawned by `ansible-test` **(OPTIONAL)**


### `git-checkout-ref`

Committish to check out, unused if `collection-src-directory`
is set **(OPTIONAL)**


### `origin-python-version`

Environment Python version. The value `auto` uses the maximum Python
version supported by the given `ansible-core-version` **(DEFAULT: `auto`)**


### `pre-test-cmd`

Extra command to invoke before ansible-test **(OPTIONAL)**


### `pull-request-change-detection`

Whether to use change detection for pull requests. If set to `true`, will
use change detection to determine changed files against the target branch,
and will not upload code coverage results. If the invocation is not from a
pull request, this option is ignored. Note that this requires
`collection-src-directory` to be empty or something ending with
`ansible_collections/{namespace}/{name}`. **(DEFAULT: `false`)**


### `python-version`

**(DEPRECATED)** Use `origin-python-version` instead.


### `target`

`ansible-test` TARGET **(OPTIONAL)**


### `target-python-version`

Target Python version **(OPTIONAL)**


### `testing-type`

`ansible-test` subcommand **(REQUIRED, Must be one of 'sanity', 'units'
or 'integration')**


### `test-deps`

Test dependencies to install along with this collection **(OPTIONAL)**


## Outputs


### `ansible-playbook-executable`

Path to the auto-installed `ansible-playbook` executable


### `ansible-test-executable`

Path to the auto-installed `ansible-test` executable


### `checkout-directory`

Path to the auto-downloaded collection src directory


### `collection-fqcn`

Detected collection FQCN


### `collection-name`

Detected collection name


### `collection-namespace`

Detected collection namespace


### `origin-python-path`

The [`python-path` output value][`python-path`] of the [setup-python] action


### `origin-python-version`

The actual value of `origin-python-version` passed to the [setup-python] action


## Related community projects

Check out the [Data-Bene/ansible-test-versions-gh-action] to explore
a semi-automatic job matrix generation for testing your collections. This
project is not maintained by us but it is a rather promising way of
configuring your GitHub Actions CI/CD workflows.

[🧪 GitHub Actions CI/CD workflow tests badge]:
https://github.com/ansible-community/ansible-test-gh-action/actions/workflows/test-action.yml/badge.svg?branch=main&event=push
[GHA workflow runs list]: https://github.com/ansible-community/ansible-test-gh-action/actions/workflows/test-action.yml?query=branch%3Amain

[pre-commit.ci results page]:
https://results.pre-commit.ci/latest/github/ansible-community/ansible-test-gh-action/main
[pre-commit.ci status badge]:
https://results.pre-commit.ci/badge/github/ansible-community/ansible-test-gh-action/main.svg

[`python-path`]:
https://github.com/actions/setup-python/blob/main/docs/advanced-usage.md#python-path
[setup-python]: https://github.com/actions/setup-python/#readme

[Data-Bene/ansible-test-versions-gh-action]:
https://github.com/Data-Bene/ansible-test-versions-gh-action
