from timeless.restaurants.models import Location

"""
@todo #187:30min Move this logic from sync_location method to
 timelessis/poster/tasks, there is already done sync_tables function as
 example. Also should refactor sync_location, seems it will not work
"""


class PosterSync:

    def sync_location(poster, company):
        synced = []
        for location in company.locations:
            for poster_location in poster.locations():
                if location.id == poster_location["id"]:
                    synced.append(
                        Location(
                            id=location.id,
                            name=poster_location["name"],
                            code=poster_location["code"],
                            company_id=location.company_id,
                            country=poster_location["country"],
                            region=poster_location["region"],
                            city=poster_location["city"],
                            address=poster_location["address"],
                            longitude=poster_location["longitude"],
                            latitude=poster_location["latitude"],
                            type=poster_location["type"],
                            status=poster_location["status"],
                            comment=poster_location["comment"]
                        )
                    )
        company.locations = synced
