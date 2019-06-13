from pyrez.models import APIResponseBase
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
