from fastapi_filter.contrib.sqlalchemy import Filter

from pydantic import Field, ConfigDict

from .models import AnnouncementModel, AnnouncementOrientation, AnnouncementGender


class AnnouncementFilter(Filter):
    orientation__in: list[AnnouncementOrientation] | None = Field(default=None, alias='orientation')
    gender__in: list[AnnouncementGender] | None = Field(default=None, alias='gender')
    fandoms__in: list[str] | None  = Field(default=None, alias='fandoms')
    tags__in: list[str] | None = Field(default=None, alias='tags')
    nsfw_fetishes__in: list[str] | None = Field(default=None, alias='nsfw_fetishes')
    nsfw_taboo__in: list[str] | None = Field(default=None, alias='nsfw_taboo')
    is_nsfw: bool | None = Field(default=None)
    is_crossgender: bool | None = Field(default=None)

    class Constants(Filter.Constants):
        model = AnnouncementModel

    model_config = ConfigDict(
        populate_by_name=True,
    )