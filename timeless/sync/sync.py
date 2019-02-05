"""
    Syncs Poster with database.
    @todo #66:30min Implement synchronization between Poster and Databse for
     Locations. Data coming from Poster has priority upon data stored in our
     database. After implementing this, remove @unittest.skip annotation from
     test_sync_location in test_sync.py. Do not forget to create cron script and
     put int into scripts folder to make this sync periodic.
    @todo #24:30min Implement synchronization between Poster and Database for
     Tables. Data coming from Poster has priority upon data stored in our
     database. Do not forget to create cron script and
     put int into scripts folder to make this sync periodic.
"""
class PosterSync():

    def sync_location(self, poster, company):
        raise Exception("sync_location not implemented yet")
