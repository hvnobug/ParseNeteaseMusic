import re
from urllib import parse


class ShareMusic:
    share_url_match = r'^http[s]?://music.163.com/song\?id=\d+&userid=\d+'

    def __init__(self, data):
        if self.validate_url(data):
            self._url = data
            query_dict = self.parse_url()
            ids = query_dict.get('id', '')
            self._songid = ids[0] if len(ids) > 0 else ''
            userids = query_dict.get('userid', '')
            self._userid = userids[0] if len(userids) > 0 else ''
        else:
            self._songid = data

    @property
    def url(self):
        return self._url

    @property
    def songid(self):
        return self._songid

    @property
    def userid(self):
        return self._userid

    def parse_url(self):
        # url解码
        url = parse.unquote(self._url)
        # url结果
        result = parse.urlparse(url)
        # 返回url里的查询参数
        return parse.parse_qs(result.query)

    def validate_url(self, data):
        # 正则验证url
        match = re.match(self.share_url_match, data)
        return True if match else False
