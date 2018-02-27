pytest_plugins = ['errbot.backends.test']

extra_plugin_dir = ['plugins']

def test_no_sir(testbot):
    testbot.assertCommand('Can I work on this sir?', 
            'keep it casual :wink:')
    testbot.assertCommand('Sir, what is a PR?', 
            'keep it casual :wink:')
    testbot.assertCommand('Thanks for the input sir meet',
            'keep it casual :wink:')
