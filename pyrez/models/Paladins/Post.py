from pyrez.models import APIResponseBase
from pyrez.enumerations import Language
class Post(APIResponseBase):# class PaladinsWebsitePost
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content = kwargs.get("content", '') or ''
        self.featuredImage = kwargs.get("featured_image", '') or ''
        self.postAuthor = kwargs.get("author", '') or ''
        self.postCategories = kwargs.get("real_categories", '') or ''
        self.postId = kwargs.get("id", 0) or 0
        self.postTimestamp = kwargs.get("timestamp", '') or ''
        self.postTitle = kwargs.get("title", '') or ''
        self.slug = kwargs.get("slug", '') or ''

    def getUrl(self, language=Language.English):
        if self.slug is not None:
            c = {2:'de_DE', 3: 'fr_FR', 5: 'zh_CN', 7: 'es_ES', 9: 'es_LA', 10: 'pt_BR', 11: 'ru_RU', 12: 'pl_PL', 13: 'tr_TR'}.get(int(language), 'en_US')
            return 'https://paladins.com/news/{}?lng={}'.format(self.slug, c)
