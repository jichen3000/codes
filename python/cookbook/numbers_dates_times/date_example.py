# sudo pip install python-dateutil
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
from dateutil import parser
if __name__ == '__main__':
    from minitest import *

    with test(timedelta):
        b = timedelta(hours=4)
        b.__str__().must_equal("4:00:00")
        b.seconds.must_equal(14400)

        a = timedelta(hours=0.5, days=1)
        a.__str__().must_equal('1 day, 0:30:00')
        a.seconds.must_equal(1800)
        a.total_seconds().must_equal(88200.0)

        one = datetime(2015, 7, 1)
        one.__str__().must_equal('2015-07-01 00:00:00')

        (one + a).__str__().must_equal('2015-07-02 00:30:00')

        (one + relativedelta(months=-1)).__str__().must_equal(
                '2015-06-01 00:00:00')

        datetime.today().p()
        next_friday = datetime.today() + relativedelta(weekday=FR)
        next_friday.p()

        last_friday = datetime.today() + relativedelta(weekday=FR(-1))
        last_friday.p()
        pass


        dt = parser.parse('2018-06-04T20:48:53.945-07:00')
        now_time = datetime.now()
        now = datetime(*now_time.date())
        pre = dt + relativedelta(days=-7)
