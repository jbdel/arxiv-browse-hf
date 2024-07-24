def test_html_fail_graceful(dbclient, mocker):
    """Test arxiv-browse graceful handling of latexml db down.

    https://arxiv-org.atlassian.net/browse/ARXIVCE-2433"""
    from pg8000.exceptions import  InterfaceError
    fn = mocker.patch('browse.services.database._inside_get_latexml_publish_dt')
    fn.side_effect = InterfaceError('network error')

    rt = dbclient.get('/abs/0906.2112')
    assert rt.status_code == 200
