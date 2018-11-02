# Copyright 2014 Facebook, Inc.

# You are hereby granted a non-exclusive, worldwide, royalty-free license to
# use, copy, modify, and distribute this software in source code or binary
# form for use in connection with the web services and APIs provided by
# Facebook.

# As with any software that integrates with the Facebook platform, your use
# of this software is subject to the Facebook Developer Principles and
# Policies [http://developers.facebook.com/policy/]. This copyright notice
# shall be included in all copies or substantial portions of the software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from facebook_business.adobjects.abstractobject import AbstractObject
from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject
from facebook_business.adobjects.objectparser import ObjectParser
from facebook_business.api import FacebookRequest
from facebook_business.typechecker import TypeChecker

"""
This class is auto-generated.

For any issues or feature requests related to this class, please let us know on
github and we'll fix in our codegen framework. We'll not be able to accept
pull request for this class.
"""

class AdCreativeVideoData(
    AbstractCrudObject,
):

    def __init__(self, fbid=None, parent_id=None, api=None):
        self._isAdCreativeVideoData = True
        super(AdCreativeVideoData, self).__init__(fbid, parent_id, api)

    class Field(AbstractObject.Field):
        additional_image_index = 'additional_image_index'
        branded_content_shared_to_sponsor_status = 'branded_content_shared_to_sponsor_status'
        branded_content_sponsor_page_id = 'branded_content_sponsor_page_id'
        branded_content_sponsor_relationship = 'branded_content_sponsor_relationship'
        call_to_action = 'call_to_action'
        collection_thumbnails = 'collection_thumbnails'
        custom_overlay_spec = 'custom_overlay_spec'
        description = 'description'
        image_hash = 'image_hash'
        image_url = 'image_url'
        link_description = 'link_description'
        message = 'message'
        offer_id = 'offer_id'
        page_welcome_message = 'page_welcome_message'
        post_click_configuration = 'post_click_configuration'
        retailer_item_ids = 'retailer_item_ids'
        targeting = 'targeting'
        title = 'title'
        video_id = 'video_id'
        id = 'id'

    _field_types = {
        'additional_image_index': 'int',
        'branded_content_shared_to_sponsor_status': 'string',
        'branded_content_sponsor_page_id': 'string',
        'branded_content_sponsor_relationship': 'string',
        'call_to_action': 'AdCreativeLinkDataCallToAction',
        'collection_thumbnails': 'list<AdCreativeCollectionThumbnailInfo>',
        'custom_overlay_spec': 'list<AdCreativeVideoDataCustomOverlaySpec>',
        'description': 'string',
        'image_hash': 'string',
        'image_url': 'string',
        'link_description': 'string',
        'message': 'string',
        'offer_id': 'string',
        'page_welcome_message': 'string',
        'post_click_configuration': 'AdCreativePostClickConfiguration',
        'retailer_item_ids': 'list<string>',
        'targeting': 'Targeting',
        'title': 'string',
        'video_id': 'string',
        'id': 'string',
    }
    @classmethod
    def _get_field_enum_info(cls):
        field_enum_info = {}
        return field_enum_info

