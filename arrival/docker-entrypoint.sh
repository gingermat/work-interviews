#!/bin/bash
set -e

case "$1" in
    run_server)
        exec python3 -m app
        ;;
    *)
        exec "$@"
        ;;
esac
