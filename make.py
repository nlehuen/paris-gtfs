import transitfeed
from itertools import groupby, combinations

def InsertTransferData(schedule):
    """ Check transfers between stops from the same stations """
    
    transfers = dict(((t.from_stop_id,t.to_stop_id),True) for t in schedule.GetTransferList())
    
    def EnsureTransfer(stop1, stop2):
        if not transfers.get((stop1.stop_id,stop2.stop_id)):
            print 'Missing %s => %s'%(stop1.stop_id, stop2.stop_id)
            transfer = transitfeed.Transfer(
                schedule=schedule,
                from_stop_id=stop1.stop_id,
                to_stop_id=stop2.stop_id,
                transfer_type=2,
                min_transfer_time=300)
    
    ps = lambda stop : stop.parent_station    
    stations = (stop for stop in schedule.GetStopList() if ps(stop))
    stations = sorted(stations,key = ps)
    for parent, stops in groupby(stations, ps):
        for stop1, stop2 in combinations(stops,2):
            EnsureTransfer(stop1,stop2)
            EnsureTransfer(stop2,stop1)

if __name__ == "__main__":
    loader = transitfeed.Loader(feed_path="data")
    schedule = loader.Load()

    InsertTransferData(schedule)
    
    schedule.WriteGoogleTransitFeed("paris-gtfs.zip")