#!/bin/bash

err()
{
  echo "${0##*/}: $*" >&2
  exit 1
}

main()
{
  set -e

  local topdir
  topdir=$(dirname "$0") || err "could not determine topdir"
  topdir=$(cd "$topdir" && pwd) || err "could not determine topdir"

  local docker_args=(
    run
    --rm
    -v "$topdir:/rpmbuild"
    -w /rpmbuild
    amazonlinux:2023
  )

  local rpmbuild_args=(
    --define "_topdir /rpmbuild"
    -ba
    "$@"
    SPECS/confd.spec
    )
  local rpmbuild_command="rpmbuild $(printf '%q ' "${rpmbuild_args[@]}")"

  set -x
  mkdir -p "$topdir/SOURCES"
  exec docker "${docker_args[@]}" sh -xc "dnf install -y rpm-build && exec $rpmbuild_command"
}

main "$@"

# vim:set sw=2 ts=2 et:
