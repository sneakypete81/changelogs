
def get_urls(releases, **kwargs):
    # Pypi has a old bugtracker_url which points to a separate repo which causes invalid
    # changelogs to be generated by this tool.
    ret = {'https://raw.githubusercontent.com/vertexproject/synapse/master/CHANGELOG.md'}
    return ret, set()
