from pyrez.models import APIResponseBase
class Post(APIResponseBase):# class PaladinsWebsitePost
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content = kwargs.get("content", None) if kwargs else None
        self.featuredImage = kwargs.get("featured_image", None) if kwargs else None
        self.postAuthor = kwargs.get("author", None) if kwargs else None
        self.postCategories = kwargs.get("real_categories", None) if kwargs else None
        self.postId = kwargs.get("id", 0) if kwargs else 0
        self.postTimestamp = kwargs.get("timestamp", None) if kwargs else None
        self.postTitle = kwargs.get("title", None) if kwargs else None
        self.slug = kwargs.get("slug", None) if kwargs else None
