# datadog
from datadog.api.format import format_points
from datadog.api.resources import SendableAPIResource


class Distribution(SendableAPIResource):
    """A wrapper around Distribution HTTP API"""
    _resource_name = 'distribution_points'

    @classmethod
    def send(cls, distributions=None, attach_host_name=True, **distribution):
        """
        Submit a distribution metric or a list of distribution metrics to the distribution metric
        API
        :param metric: the name of the time series
        :type metric: string
        :param points: a (timestamp, [list of values]) pair or
        list of (timestamp, [list of values]) pairs
        :type points: list
        :param host: host name that produced the metric
        :type host: string
        :param tags:  list of tags associated with the metric.
        :type tags: string list
        :returns: Dictionary representing the API's JSON response
        """
        if distributions:
            # Multiple distributions are sent
            for d in distributions:
                if isinstance(d, dict):
                    d['points'] = format_points(d['points'])
            series_dict = {"series": distributions}
        else:
            # One distribution is sent
            distribution['points'] = format_points(distribution['points'])
            series_dict = {"series": [distribution]}
        return super(Distribution, cls).send(attach_host_name=attach_host_name, **series_dict)
