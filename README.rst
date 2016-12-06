=============================
python-agiletixapi
=============================

A Python interface for the Agile Ticketing API.


Installation 
-----------------

::

    pip install agiletixapi


Example
-----------------

Create a client::

    from agiletixapi import AgileSalesAPI
    

    api = AgileSalesAPI(
        base_url=AGILE_BASE_URL,
        app_key=AGILE_APP_KEY,
        user_key=AGILE_USER_KEY,
        corp_org_id=AGILE_CORP_ORG_ID
    )


Fetch events::

    from datetime import datetime, timedelta
    
    from agiletixapi.models import Event

    start_date = datetime.now()
    end_date = start_date + timedelta(days=30)

    response = api.event_list(start_date=start_date, end_date=end_date)

    if response.success:
        agile_events = [Event(n) for n in response.data]
        for event in agile_events:
            print(event.id)
            print(event.name)

