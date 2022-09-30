from .models import Operator, Route

def search(
    from_source,
    to_dest,
    departure_date,
    return_date,
    passengers
):
    route_query = Route.objects.filter(
        fromSource=from_source,
        toDestination=to_dest
    )

    return route_query
