
from dao.EpisodeDao import EpisodeDao
from database.schema.EpisodeSchema import EpisodeSchema
from Service.ApiService import ApiService


class EpisodeService(ApiService):

    @property
    def dao(self):
        return EpisodeDao()

    @property
    def schema(self):
        return EpisodeSchema()
