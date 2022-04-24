from django.db.models.lookups import Transform
class myFunc(Transform):
    lookup_name='sin'
    function='sin'
    def as_sql(self,qn,connection):
        lhs, params = qn.compile(self.lhs)
        return "%s(%s)" % (self.function, lhs), params