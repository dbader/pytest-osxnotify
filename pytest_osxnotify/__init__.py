# pytest-osxnotify
# Mac OS X notification center support for py.test
# Requirements: pyobjc-core
import time

# Lazy-import pyobjc to work around a conflict with pytest-xdist
# looponfail on Python 3.3
objc = None


def pytest_addoption(parser):
    """
    Adds options to control notifications.

    """
    group = parser.getgroup('terminal reporting')
    group.addoption(
        '--osxnotify',
        dest='osxnotify',
        default=True,
        help='Enable Mac OS X notification center notifications.'
    )


def pytest_sessionstart(session):
    if session.config.option.osxnotify:
        notify('py.test', 'Running tests...')


def pytest_terminal_summary(terminalreporter):
    if not terminalreporter.config.option.osxnotify:
        return
    tr = terminalreporter
    passes = len(tr.stats.get('passed', []))
    fails = len(tr.stats.get('failed', []))
    skips = len(tr.stats.get('deselected', []))
    errors = len(tr.stats.get('error', []))
    if errors + passes + fails + skips == 0:
        msg = 'No tests ran'
    elif passes and not (fails or errors):
        msg = 'Success - %i Passed' % passes
    elif not (skips or errors):
        msg = '%s Passed %s Failed' % (passes, fails)
    else:
        msg = '%s Passed %s Failed %s Errors %s Skipped' % (
            passes, fails, errors, skips
        )
    notify('py.test', msg)


def swizzle(cls, SEL, func):
    old_IMP = getattr(cls, SEL, None)
    if old_IMP is None:
        # This will work on OS X <= 10.9
        old_IMP = cls.instanceMethodForSelector_(SEL)

    def wrapper(self, *args, **kwargs):
        return func(self, old_IMP, *args, **kwargs)

    new_IMP = objc.selector(
        wrapper,
        selector=old_IMP.selector,
        signature=old_IMP.signature
    )
    objc.classAddMethod(cls, SEL.encode(), new_IMP)


def notify(title, subtitle=None):
    """
    Display a NSUserNotification on Mac OS X >= 10.8

    """
    global objc
    if not objc:
        objc = __import__('objc')
        swizzle(
            objc.lookUpClass('NSBundle'),
            'bundleIdentifier',
            swizzled_bundleIdentifier
        )

    NSUserNotification = objc.lookUpClass('NSUserNotification')
    NSUserNotificationCenter = objc.lookUpClass('NSUserNotificationCenter')
    if not NSUserNotification or not NSUserNotificationCenter:
        print('NSUserNotifcation is not supported by your version of Mac OS X')
        return

    notification = NSUserNotification.alloc().init()
    notification.setTitle_(str(title))
    if subtitle:
        notification.setSubtitle_(str(subtitle))

    notification_center = NSUserNotificationCenter.defaultUserNotificationCenter()
    notification_center.deliverNotification_(notification)
    # Delay a bit to ensure that all notifications get displayed
    # even if py.test finishes very quickly.
    time.sleep(0.1)


def swizzled_bundleIdentifier(self, original):
    """
    Swizzle [NSBundle bundleIdentifier] to make NSUserNotifications work.

    To post NSUserNotifications OS X requires the binary to be packaged
    as an application bundle. To circumvent this restriction, we modify
    `bundleIdentifier` to return a fake bundle identifier.

    Original idea for this approach by Norio Numura:
    https://github.com/norio-nomura/usernotification

    """
    return 'com.apple.terminal'
