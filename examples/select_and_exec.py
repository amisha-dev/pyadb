#!/usr/bin/env python
#
# Very basic PyADB example
#

import sys
try:
    from pyadb import ADB
except ImportError as e:
    # should never be reached
    print("[f] Required module missing. %s" % e.args[0])
    sys.exit(-1)


def main():
    # creates the ADB object
    adb = ADB()

    # set ADB path, using a couple of popular addresses.
    try:
        adb.set_adb_path('~/android-sdk-linux/platform-tools/adb')
    except FileNotFoundError:
        adb.set_adb_path(r'C:\Android\android-sdk\platform-tools\adb.exe')

    print("Version: %s" % adb.get_version())

    print("Waiting for device...")
    adb.wait_for_device()
    err, dev = adb.get_devices()

    if len(dev) == 0:
        print("Unexpected error, may be you're a very fast guy?")
        return

    print("Selecting: %s" % dev[0])
    adb.set_target_device(dev[0])

    print("Executing 'ls' command")
    adb.shell_command('ls')

    print("Output:\n  %s" % "\n  ".join(adb.get_output()))


if __name__ == "__main__":
    main()
