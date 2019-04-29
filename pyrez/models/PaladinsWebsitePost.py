from .BaseAPIResponse import BaseAPIResponse
class PaladinsWebsitePost(BaseAPIResponse):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.content = kwargs.get("content", None) if kwargs is not None else None
        self.featuredImage = kwargs.get("featured_image", None) if kwargs is not None else None
        self.postAuthor = kwargs.get("author", None) if kwargs is not None else None
        self.postCategories = kwargs.get("real_categories", None) if kwargs is not None else None
        self.postId = kwargs.get("id", 0) if kwargs is not None else 0
        self.postTimestamp = kwargs.get("timestamp", None) if kwargs is not None else None
        self.postTitle = kwargs.get("title", None) if kwargs is not None else None
        self.slug = kwargs.get("slug", None) if kwargs is not None else None
