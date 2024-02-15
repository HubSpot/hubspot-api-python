# coding: utf-8

"""
    Authors

    Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from hubspot.cms.blogs.authors.configuration import Configuration


class BlogAuthor(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "website": "str",
        "display_name": "str",
        "created": "datetime",
        "facebook": "str",
        "full_name": "str",
        "bio": "str",
        "language": "str",
        "linkedin": "str",
        "avatar": "str",
        "translated_from_id": "int",
        "twitter": "str",
        "deleted_at": "datetime",
        "name": "str",
        "id": "str",
        "updated": "datetime",
        "email": "str",
        "slug": "str",
    }

    attribute_map = {
        "website": "website",
        "display_name": "displayName",
        "created": "created",
        "facebook": "facebook",
        "full_name": "fullName",
        "bio": "bio",
        "language": "language",
        "linkedin": "linkedin",
        "avatar": "avatar",
        "translated_from_id": "translatedFromId",
        "twitter": "twitter",
        "deleted_at": "deletedAt",
        "name": "name",
        "id": "id",
        "updated": "updated",
        "email": "email",
        "slug": "slug",
    }

    def __init__(
        self,
        website=None,
        display_name=None,
        created=None,
        facebook=None,
        full_name=None,
        bio=None,
        language=None,
        linkedin=None,
        avatar=None,
        translated_from_id=None,
        twitter=None,
        deleted_at=None,
        name=None,
        id=None,
        updated=None,
        email=None,
        slug=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """BlogAuthor - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._website = None
        self._display_name = None
        self._created = None
        self._facebook = None
        self._full_name = None
        self._bio = None
        self._language = None
        self._linkedin = None
        self._avatar = None
        self._translated_from_id = None
        self._twitter = None
        self._deleted_at = None
        self._name = None
        self._id = None
        self._updated = None
        self._email = None
        self._slug = None
        self.discriminator = None

        self.website = website
        self.display_name = display_name
        self.created = created
        self.facebook = facebook
        self.full_name = full_name
        self.bio = bio
        self.language = language
        self.linkedin = linkedin
        self.avatar = avatar
        self.translated_from_id = translated_from_id
        self.twitter = twitter
        self.deleted_at = deleted_at
        self.name = name
        self.id = id
        self.updated = updated
        self.email = email
        self.slug = slug

    @property
    def website(self):
        """Gets the website of this BlogAuthor.  # noqa: E501

        URL to the website of the Blog Author.  # noqa: E501

        :return: The website of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this BlogAuthor.

        URL to the website of the Blog Author.  # noqa: E501

        :param website: The website of this BlogAuthor.  # noqa: E501
        :type website: str
        """
        if self.local_vars_configuration.client_side_validation and website is None:  # noqa: E501
            raise ValueError("Invalid value for `website`, must not be `None`")  # noqa: E501

        self._website = website

    @property
    def display_name(self):
        """Gets the display_name of this BlogAuthor.  # noqa: E501

        The full name of the Blog Author to be displayed.  # noqa: E501

        :return: The display_name of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this BlogAuthor.

        The full name of the Blog Author to be displayed.  # noqa: E501

        :param display_name: The display_name of this BlogAuthor.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def created(self):
        """Gets the created of this BlogAuthor.  # noqa: E501


        :return: The created of this BlogAuthor.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this BlogAuthor.


        :param created: The created of this BlogAuthor.  # noqa: E501
        :type created: datetime
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def facebook(self):
        """Gets the facebook of this BlogAuthor.  # noqa: E501

        URL to the Blog Author's Facebook page.  # noqa: E501

        :return: The facebook of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """Sets the facebook of this BlogAuthor.

        URL to the Blog Author's Facebook page.  # noqa: E501

        :param facebook: The facebook of this BlogAuthor.  # noqa: E501
        :type facebook: str
        """
        if self.local_vars_configuration.client_side_validation and facebook is None:  # noqa: E501
            raise ValueError("Invalid value for `facebook`, must not be `None`")  # noqa: E501

        self._facebook = facebook

    @property
    def full_name(self):
        """Gets the full_name of this BlogAuthor.  # noqa: E501


        :return: The full_name of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this BlogAuthor.


        :param full_name: The full_name of this BlogAuthor.  # noqa: E501
        :type full_name: str
        """
        if self.local_vars_configuration.client_side_validation and full_name is None:  # noqa: E501
            raise ValueError("Invalid value for `full_name`, must not be `None`")  # noqa: E501

        self._full_name = full_name

    @property
    def bio(self):
        """Gets the bio of this BlogAuthor.  # noqa: E501

        A short biography of the blog author.  # noqa: E501

        :return: The bio of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._bio

    @bio.setter
    def bio(self, bio):
        """Sets the bio of this BlogAuthor.

        A short biography of the blog author.  # noqa: E501

        :param bio: The bio of this BlogAuthor.  # noqa: E501
        :type bio: str
        """
        if self.local_vars_configuration.client_side_validation and bio is None:  # noqa: E501
            raise ValueError("Invalid value for `bio`, must not be `None`")  # noqa: E501

        self._bio = bio

    @property
    def language(self):
        """Gets the language of this BlogAuthor.  # noqa: E501

        The explicitly defined ISO 639 language code of the blog author.  # noqa: E501

        :return: The language of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this BlogAuthor.

        The explicitly defined ISO 639 language code of the blog author.  # noqa: E501

        :param language: The language of this BlogAuthor.  # noqa: E501
        :type language: str
        """
        if self.local_vars_configuration.client_side_validation and language is None:  # noqa: E501
            raise ValueError("Invalid value for `language`, must not be `None`")  # noqa: E501
        allowed_values = [
            "af",
            "af-na",
            "af-za",
            "agq",
            "agq-cm",
            "ak",
            "ak-gh",
            "am",
            "am-et",
            "ar",
            "ar-001",
            "ar-ae",
            "ar-bh",
            "ar-dj",
            "ar-dz",
            "ar-eg",
            "ar-eh",
            "ar-er",
            "ar-il",
            "ar-iq",
            "ar-jo",
            "ar-km",
            "ar-kw",
            "ar-lb",
            "ar-ly",
            "ar-ma",
            "ar-mr",
            "ar-om",
            "ar-ps",
            "ar-qa",
            "ar-sa",
            "ar-sd",
            "ar-so",
            "ar-ss",
            "ar-sy",
            "ar-td",
            "ar-tn",
            "ar-ye",
            "as",
            "as-in",
            "asa",
            "asa-tz",
            "ast",
            "ast-es",
            "az",
            "az-az",
            "bas",
            "bas-cm",
            "be",
            "be-by",
            "bem",
            "bem-zm",
            "bez",
            "bez-tz",
            "bg",
            "bg-bg",
            "bm",
            "bm-ml",
            "bn",
            "bn-bd",
            "bn-in",
            "bo",
            "bo-cn",
            "bo-in",
            "br",
            "br-fr",
            "brx",
            "brx-in",
            "bs",
            "bs-ba",
            "ca",
            "ca-ad",
            "ca-es",
            "ca-fr",
            "ca-it",
            "ccp",
            "ccp-bd",
            "ccp-in",
            "ce",
            "ce-ru",
            "ceb",
            "ceb-ph",
            "cgg",
            "cgg-ug",
            "chr",
            "chr-us",
            "ckb",
            "ckb-iq",
            "ckb-ir",
            "cs",
            "cs-cz",
            "cu",
            "cu-ru",
            "cy",
            "cy-gb",
            "da",
            "da-dk",
            "da-gl",
            "dav",
            "dav-ke",
            "de",
            "de-at",
            "de-be",
            "de-ch",
            "de-de",
            "de-gr",
            "de-it",
            "de-li",
            "de-lu",
            "dje",
            "dje-ne",
            "doi",
            "doi-in",
            "dsb",
            "dsb-de",
            "dua",
            "dua-cm",
            "dyo",
            "dyo-sn",
            "dz",
            "dz-bt",
            "ebu",
            "ebu-ke",
            "ee",
            "ee-gh",
            "ee-tg",
            "el",
            "el-cy",
            "el-gr",
            "en",
            "en-001",
            "en-150",
            "en-ae",
            "en-ag",
            "en-ai",
            "en-as",
            "en-at",
            "en-au",
            "en-bb",
            "en-be",
            "en-bi",
            "en-bm",
            "en-bs",
            "en-bw",
            "en-bz",
            "en-ca",
            "en-cc",
            "en-ch",
            "en-ck",
            "en-cm",
            "en-cn",
            "en-cx",
            "en-cy",
            "en-de",
            "en-dg",
            "en-dk",
            "en-dm",
            "en-er",
            "en-fi",
            "en-fj",
            "en-fk",
            "en-fm",
            "en-gb",
            "en-gd",
            "en-gg",
            "en-gh",
            "en-gi",
            "en-gm",
            "en-gu",
            "en-gy",
            "en-hk",
            "en-ie",
            "en-il",
            "en-im",
            "en-in",
            "en-io",
            "en-je",
            "en-jm",
            "en-ke",
            "en-ki",
            "en-kn",
            "en-ky",
            "en-lc",
            "en-lr",
            "en-ls",
            "en-lu",
            "en-mg",
            "en-mh",
            "en-mo",
            "en-mp",
            "en-ms",
            "en-mt",
            "en-mu",
            "en-mw",
            "en-mx",
            "en-my",
            "en-na",
            "en-nf",
            "en-ng",
            "en-nl",
            "en-nr",
            "en-nu",
            "en-nz",
            "en-pg",
            "en-ph",
            "en-pk",
            "en-pn",
            "en-pr",
            "en-pw",
            "en-rw",
            "en-sb",
            "en-sc",
            "en-sd",
            "en-se",
            "en-sg",
            "en-sh",
            "en-si",
            "en-sl",
            "en-ss",
            "en-sx",
            "en-sz",
            "en-tc",
            "en-tk",
            "en-to",
            "en-tt",
            "en-tv",
            "en-tz",
            "en-ug",
            "en-um",
            "en-us",
            "en-vc",
            "en-vg",
            "en-vi",
            "en-vu",
            "en-ws",
            "en-za",
            "en-zm",
            "en-zw",
            "eo",
            "eo-001",
            "es",
            "es-419",
            "es-ar",
            "es-bo",
            "es-br",
            "es-bz",
            "es-cl",
            "es-co",
            "es-cr",
            "es-cu",
            "es-do",
            "es-ea",
            "es-ec",
            "es-es",
            "es-gq",
            "es-gt",
            "es-hn",
            "es-ic",
            "es-mx",
            "es-ni",
            "es-pa",
            "es-pe",
            "es-ph",
            "es-pr",
            "es-py",
            "es-sv",
            "es-us",
            "es-uy",
            "es-ve",
            "et",
            "et-ee",
            "eu",
            "eu-es",
            "ewo",
            "ewo-cm",
            "fa",
            "fa-af",
            "fa-ir",
            "ff",
            "ff-bf",
            "ff-cm",
            "ff-gh",
            "ff-gm",
            "ff-gn",
            "ff-gw",
            "ff-lr",
            "ff-mr",
            "ff-ne",
            "ff-ng",
            "ff-sl",
            "ff-sn",
            "fi",
            "fi-fi",
            "fil",
            "fil-ph",
            "fo",
            "fo-dk",
            "fo-fo",
            "fr",
            "fr-be",
            "fr-bf",
            "fr-bi",
            "fr-bj",
            "fr-bl",
            "fr-ca",
            "fr-cd",
            "fr-cf",
            "fr-cg",
            "fr-ch",
            "fr-ci",
            "fr-cm",
            "fr-dj",
            "fr-dz",
            "fr-fr",
            "fr-ga",
            "fr-gf",
            "fr-gn",
            "fr-gp",
            "fr-gq",
            "fr-ht",
            "fr-km",
            "fr-lu",
            "fr-ma",
            "fr-mc",
            "fr-mf",
            "fr-mg",
            "fr-ml",
            "fr-mq",
            "fr-mr",
            "fr-mu",
            "fr-nc",
            "fr-ne",
            "fr-pf",
            "fr-pm",
            "fr-re",
            "fr-rw",
            "fr-sc",
            "fr-sn",
            "fr-sy",
            "fr-td",
            "fr-tg",
            "fr-tn",
            "fr-vu",
            "fr-wf",
            "fr-yt",
            "fur",
            "fur-it",
            "fy",
            "fy-nl",
            "ga",
            "ga-gb",
            "ga-ie",
            "gd",
            "gd-gb",
            "gl",
            "gl-es",
            "gsw",
            "gsw-ch",
            "gsw-fr",
            "gsw-li",
            "gu",
            "gu-in",
            "guz",
            "guz-ke",
            "gv",
            "gv-im",
            "ha",
            "ha-gh",
            "ha-ne",
            "ha-ng",
            "haw",
            "haw-us",
            "he",
            "hi",
            "hi-in",
            "hr",
            "hr-ba",
            "hr-hr",
            "hsb",
            "hsb-de",
            "hu",
            "hu-hu",
            "hy",
            "hy-am",
            "ia",
            "ia-001",
            "id",
            "ig",
            "ig-ng",
            "ii",
            "ii-cn",
            "id-id",
            "is",
            "is-is",
            "it",
            "it-ch",
            "it-it",
            "it-sm",
            "it-va",
            "he-il",
            "ja",
            "ja-jp",
            "jgo",
            "jgo-cm",
            "yi",
            "yi-001",
            "jmc",
            "jmc-tz",
            "jv",
            "jv-id",
            "ka",
            "ka-ge",
            "kab",
            "kab-dz",
            "kam",
            "kam-ke",
            "kde",
            "kde-tz",
            "kea",
            "kea-cv",
            "khq",
            "khq-ml",
            "ki",
            "ki-ke",
            "kk",
            "kk-kz",
            "kkj",
            "kkj-cm",
            "kl",
            "kl-gl",
            "kln",
            "kln-ke",
            "km",
            "km-kh",
            "kn",
            "kn-in",
            "ko",
            "ko-kp",
            "ko-kr",
            "kok",
            "kok-in",
            "ks",
            "ks-in",
            "ksb",
            "ksb-tz",
            "ksf",
            "ksf-cm",
            "ksh",
            "ksh-de",
            "kw",
            "kw-gb",
            "ku",
            "ku-tr",
            "ky",
            "ky-kg",
            "lag",
            "lag-tz",
            "lb",
            "lb-lu",
            "lg",
            "lg-ug",
            "lkt",
            "lkt-us",
            "ln",
            "ln-ao",
            "ln-cd",
            "ln-cf",
            "ln-cg",
            "lo",
            "lo-la",
            "lrc",
            "lrc-iq",
            "lrc-ir",
            "lt",
            "lt-lt",
            "lu",
            "lu-cd",
            "luo",
            "luo-ke",
            "luy",
            "luy-ke",
            "lv",
            "lv-lv",
            "mai",
            "mai-in",
            "mas",
            "mas-ke",
            "mas-tz",
            "mer",
            "mer-ke",
            "mfe",
            "mfe-mu",
            "mg",
            "mg-mg",
            "mgh",
            "mgh-mz",
            "mgo",
            "mgo-cm",
            "mi",
            "mi-nz",
            "mk",
            "mk-mk",
            "ml",
            "ml-in",
            "mn",
            "mn-mn",
            "mni",
            "mni-in",
            "mr",
            "mr-in",
            "ms",
            "ms-bn",
            "ms-id",
            "ms-my",
            "ms-sg",
            "mt",
            "mt-mt",
            "mua",
            "mua-cm",
            "my",
            "my-mm",
            "mzn",
            "mzn-ir",
            "naq",
            "naq-na",
            "nb",
            "nb-no",
            "nb-sj",
            "nd",
            "nd-zw",
            "nds",
            "nds-de",
            "nds-nl",
            "ne",
            "ne-in",
            "ne-np",
            "nl",
            "nl-aw",
            "nl-be",
            "nl-ch",
            "nl-bq",
            "nl-cw",
            "nl-lu",
            "nl-nl",
            "nl-sr",
            "nl-sx",
            "nmg",
            "nmg-cm",
            "nn",
            "nn-no",
            "nnh",
            "nnh-cm",
            "no",
            "no-no",
            "nus",
            "nus-ss",
            "nyn",
            "nyn-ug",
            "om",
            "om-et",
            "om-ke",
            "or",
            "or-in",
            "os",
            "os-ge",
            "os-ru",
            "pa",
            "pa-in",
            "pa-pk",
            "pcm",
            "pcm-ng",
            "pl",
            "pl-pl",
            "prg",
            "prg-001",
            "ps",
            "ps-af",
            "ps-pk",
            "pt",
            "pt-ao",
            "pt-br",
            "pt-ch",
            "pt-cv",
            "pt-gq",
            "pt-gw",
            "pt-lu",
            "pt-mo",
            "pt-mz",
            "pt-pt",
            "pt-st",
            "pt-tl",
            "qu",
            "qu-bo",
            "qu-ec",
            "qu-pe",
            "rm",
            "rm-ch",
            "rn",
            "rn-bi",
            "ro",
            "ro-md",
            "ro-ro",
            "rof",
            "rof-tz",
            "ru",
            "ru-by",
            "ru-kg",
            "ru-kz",
            "ru-md",
            "ru-ru",
            "ru-ua",
            "rw",
            "rw-rw",
            "rwk",
            "rwk-tz",
            "sa",
            "sa-in",
            "sah",
            "sah-ru",
            "saq",
            "saq-ke",
            "sat",
            "sat-in",
            "sbp",
            "sbp-tz",
            "sd",
            "sd-in",
            "sd-pk",
            "se",
            "se-fi",
            "se-no",
            "se-se",
            "seh",
            "seh-mz",
            "ses",
            "ses-ml",
            "sg",
            "sg-cf",
            "shi",
            "shi-ma",
            "si",
            "si-lk",
            "sk",
            "sk-sk",
            "sl",
            "sl-si",
            "smn",
            "smn-fi",
            "sn",
            "sn-zw",
            "so",
            "so-dj",
            "so-et",
            "so-ke",
            "so-so",
            "sq",
            "sq-al",
            "sq-mk",
            "sq-xk",
            "sr",
            "sr-ba",
            "sr-cs",
            "sr-me",
            "sr-rs",
            "sr-xk",
            "su",
            "su-id",
            "sv",
            "sv-ax",
            "sv-fi",
            "sv-se",
            "sw",
            "sw-cd",
            "sw-ke",
            "sw-tz",
            "sw-ug",
            "sy",
            "ta",
            "ta-in",
            "ta-lk",
            "ta-my",
            "ta-sg",
            "te",
            "te-in",
            "teo",
            "teo-ke",
            "teo-ug",
            "tg",
            "tg-tj",
            "th",
            "th-th",
            "ti",
            "ti-er",
            "ti-et",
            "tk",
            "tk-tm",
            "tl",
            "to",
            "to-to",
            "tr",
            "tr-cy",
            "tr-tr",
            "tt",
            "tt-ru",
            "twq",
            "twq-ne",
            "tzm",
            "tzm-ma",
            "ug",
            "ug-cn",
            "uk",
            "uk-ua",
            "ur",
            "ur-in",
            "ur-pk",
            "uz",
            "uz-af",
            "uz-uz",
            "vai",
            "vai-lr",
            "vi",
            "vi-vn",
            "vo",
            "vo-001",
            "vun",
            "vun-tz",
            "wae",
            "wae-ch",
            "wo",
            "wo-sn",
            "xh",
            "xh-za",
            "xog",
            "xog-ug",
            "yav",
            "yav-cm",
            "yo",
            "yo-bj",
            "yo-ng",
            "yue",
            "yue-cn",
            "yue-hk",
            "zgh",
            "zgh-ma",
            "zh",
            "zh-cn",
            "zh-hk",
            "zh-mo",
            "zh-sg",
            "zh-tw",
            "zh-hans",
            "zh-hant",
            "zu",
            "zu-za",
        ]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and language not in allowed_values:  # noqa: E501
            raise ValueError("Invalid value for `language` ({0}), must be one of {1}".format(language, allowed_values))  # noqa: E501

        self._language = language

    @property
    def linkedin(self):
        """Gets the linkedin of this BlogAuthor.  # noqa: E501

        URL to the blog author's LinkedIn page.  # noqa: E501

        :return: The linkedin of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._linkedin

    @linkedin.setter
    def linkedin(self, linkedin):
        """Sets the linkedin of this BlogAuthor.

        URL to the blog author's LinkedIn page.  # noqa: E501

        :param linkedin: The linkedin of this BlogAuthor.  # noqa: E501
        :type linkedin: str
        """
        if self.local_vars_configuration.client_side_validation and linkedin is None:  # noqa: E501
            raise ValueError("Invalid value for `linkedin`, must not be `None`")  # noqa: E501

        self._linkedin = linkedin

    @property
    def avatar(self):
        """Gets the avatar of this BlogAuthor.  # noqa: E501

        URL to the blog author's avatar, if supplying a custom one.  # noqa: E501

        :return: The avatar of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """Sets the avatar of this BlogAuthor.

        URL to the blog author's avatar, if supplying a custom one.  # noqa: E501

        :param avatar: The avatar of this BlogAuthor.  # noqa: E501
        :type avatar: str
        """
        if self.local_vars_configuration.client_side_validation and avatar is None:  # noqa: E501
            raise ValueError("Invalid value for `avatar`, must not be `None`")  # noqa: E501

        self._avatar = avatar

    @property
    def translated_from_id(self):
        """Gets the translated_from_id of this BlogAuthor.  # noqa: E501

        ID of the primary blog author this object was translated from.  # noqa: E501

        :return: The translated_from_id of this BlogAuthor.  # noqa: E501
        :rtype: int
        """
        return self._translated_from_id

    @translated_from_id.setter
    def translated_from_id(self, translated_from_id):
        """Sets the translated_from_id of this BlogAuthor.

        ID of the primary blog author this object was translated from.  # noqa: E501

        :param translated_from_id: The translated_from_id of this BlogAuthor.  # noqa: E501
        :type translated_from_id: int
        """
        if self.local_vars_configuration.client_side_validation and translated_from_id is None:  # noqa: E501
            raise ValueError("Invalid value for `translated_from_id`, must not be `None`")  # noqa: E501

        self._translated_from_id = translated_from_id

    @property
    def twitter(self):
        """Gets the twitter of this BlogAuthor.  # noqa: E501

        URL or username of the Twitter account associated with the Blog Author. This will be normalized into the Twitter url for said user.  # noqa: E501

        :return: The twitter of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        """Sets the twitter of this BlogAuthor.

        URL or username of the Twitter account associated with the Blog Author. This will be normalized into the Twitter url for said user.  # noqa: E501

        :param twitter: The twitter of this BlogAuthor.  # noqa: E501
        :type twitter: str
        """
        if self.local_vars_configuration.client_side_validation and twitter is None:  # noqa: E501
            raise ValueError("Invalid value for `twitter`, must not be `None`")  # noqa: E501

        self._twitter = twitter

    @property
    def deleted_at(self):
        """Gets the deleted_at of this BlogAuthor.  # noqa: E501

        The timestamp (ISO8601 format) when this Blog Author was deleted.  # noqa: E501

        :return: The deleted_at of this BlogAuthor.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this BlogAuthor.

        The timestamp (ISO8601 format) when this Blog Author was deleted.  # noqa: E501

        :param deleted_at: The deleted_at of this BlogAuthor.  # noqa: E501
        :type deleted_at: datetime
        """
        if self.local_vars_configuration.client_side_validation and deleted_at is None:  # noqa: E501
            raise ValueError("Invalid value for `deleted_at`, must not be `None`")  # noqa: E501

        self._deleted_at = deleted_at

    @property
    def name(self):
        """Gets the name of this BlogAuthor.  # noqa: E501


        :return: The name of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BlogAuthor.


        :param name: The name of this BlogAuthor.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this BlogAuthor.  # noqa: E501

        The unique ID of the Blog Author.  # noqa: E501

        :return: The id of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BlogAuthor.

        The unique ID of the Blog Author.  # noqa: E501

        :param id: The id of this BlogAuthor.  # noqa: E501
        :type id: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def updated(self):
        """Gets the updated of this BlogAuthor.  # noqa: E501


        :return: The updated of this BlogAuthor.  # noqa: E501
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this BlogAuthor.


        :param updated: The updated of this BlogAuthor.  # noqa: E501
        :type updated: datetime
        """
        if self.local_vars_configuration.client_side_validation and updated is None:  # noqa: E501
            raise ValueError("Invalid value for `updated`, must not be `None`")  # noqa: E501

        self._updated = updated

    @property
    def email(self):
        """Gets the email of this BlogAuthor.  # noqa: E501

        Email address of the Blog Author.  # noqa: E501

        :return: The email of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this BlogAuthor.

        Email address of the Blog Author.  # noqa: E501

        :param email: The email of this BlogAuthor.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def slug(self):
        """Gets the slug of this BlogAuthor.  # noqa: E501


        :return: The slug of this BlogAuthor.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this BlogAuthor.


        :param slug: The slug of this BlogAuthor.  # noqa: E501
        :type slug: str
        """
        if self.local_vars_configuration.client_side_validation and slug is None:  # noqa: E501
            raise ValueError("Invalid value for `slug`, must not be `None`")  # noqa: E501

        self._slug = slug

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(lambda x: convert(x), value))
            elif isinstance(value, dict):
                result[attr] = dict(map(lambda item: (item[0], convert(item[1])), value.items()))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BlogAuthor):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlogAuthor):
            return True

        return self.to_dict() != other.to_dict()
