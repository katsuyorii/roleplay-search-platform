from fastapi_filter import FilterDepends, with_prefix
from fastapi_filter.contrib.sqlalchemy import Filter

from pydantic import Field, ConfigDict

from .models import AnnouncementModel, AnnouncementOrientation, AnnouncementGender, FandomModel, TagModel, NsfwFetishTabooModel


class FandomFilter(Filter):
    slug__in: list[str] | None  = Field(default=None, alias='fandoms')

    class Constants(Filter.Constants):
        model = FandomModel

    model_config = ConfigDict(
        populate_by_name=True,
    )


class TagFilter(Filter):
    slug__in: list[str] | None  = Field(default=None, alias='tags')

    class Constants(Filter.Constants):
        model = TagModel

    model_config = ConfigDict(
        populate_by_name=True,
    )


# НЕ РАБОТАЕТ
class NsfwFetishFilter(Filter):
    slug__in: list[str] | None  = Field(default=None, alias='nsfw_fetishes')

    class Constants(Filter.Constants):
        model = NsfwFetishTabooModel

    model_config = ConfigDict(
        populate_by_name=True,
    )


# НЕ РАБОТАЕТ
class NsfwTabooFilter(Filter):
    slug__in: list[str] | None  = Field(default=None, alias='nsfw_taboo')

    class Constants(Filter.Constants):
        model = NsfwFetishTabooModel

    model_config = ConfigDict(
        populate_by_name=True,
    )


class AnnouncementFilter(Filter):
    orientation__in: list[AnnouncementOrientation] | None = Field(default=None, alias='orientation')
    gender__in: list[AnnouncementGender] | None = Field(default=None, alias='gender')
    fandoms: FandomFilter | None = FilterDepends(with_prefix("fandoms", FandomFilter))
    tags: TagFilter | None = FilterDepends(with_prefix("tags", TagFilter))
    nsfw_fetishes: NsfwFetishFilter | None = FilterDepends(with_prefix("nsfw_fetishes", NsfwFetishFilter))
    nsfw_taboo: NsfwTabooFilter | None = FilterDepends(with_prefix("nsfw_taboo", NsfwTabooFilter))
    is_nsfw: bool | None = Field(default=None)
    is_crossgender: bool | None = Field(default=None)

    class Constants(Filter.Constants):
        model = AnnouncementModel

    model_config = ConfigDict(
        populate_by_name=True,
    )