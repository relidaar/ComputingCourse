"""
Template for testing suite for Stopwatch
"""

try:
    import poc_simpletest
except ImportError:
    from PrinciplesOfComputing.libs import poc_simpletest

def run_suite(func):
    suite = poc_simpletest.TestSuite()
    values = {
        0: '0:00.0',
        11: '0:01.1',
        206: '0:20.6',
        321: '0:32.1',
        476: '0:47.6',
        511: '0:51.1',
        613: '1:01.3',
        798: '1:19.8',
        834: '1:23.4',
        999: '1:39.9',
    }

    for index, (key, value) in enumerate(values.items()):
        suite.run_test(func(key), value, 'Test #%d: %d' % (index, key))

    suite.report_results()