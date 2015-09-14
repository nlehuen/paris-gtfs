===================
Paris GTFS Data Set
===================

**Good news everyone!** This project is no longer needed. See `the official RATP GTFS files <http://data.ratp.fr/explore/dataset/offre-transport-de-la-ratp-format-gtfs/?tab=metas>`_.

This project aims to provide an open source data set for Paris public transport.

Done
====

Métro line 1

To do
=====

Everything else.

Note that for the moment we plan to use frequencies.txt instead of precise trip informations in trips.txt and stop_times.txt.

About stations, stops and transfers
===================================

In order to account for transfer times, metro stations with transfers are splitted into multiple stops per line, and transfers.txt is used to write a transfer time between two stops within the same station. We should have different transfer times depending on the transfer direction, hence requiring one stop per station, line and direction, but for the time being we'll keep it this way.

Each stop within a metro station with transfer had an id like this : <station id>/<route id>. For example, the Métro line 1 stop at Nation had the id nation/M1.
