init python:
    def DummySkip():
        if enable_skip:
            _skipping = True
            config.rollback_enabled = True
            renpy.call_in_new_context("do_skip", fast=True, confirm=True)
        else:
            _skipping = False
            config.rollback_enabled = False

label do_skip(fast=False, confirm=False):
    # Use the Skip action with parameters
    $ ui.callsinnewcontext(Skip(fast=True, confirm=True))
    return
