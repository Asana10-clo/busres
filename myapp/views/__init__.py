from .index import index
from .checkout import checkout, webhook
from .others import (
    stationloc,
    contact,
    blog,
    blog_post
)

__all__ = [
    index,
    checkout,
    webhook,
    stationloc,
    contact,
    blog,
    blog_post,
    # seat,
    # mastercard,
]