import datetime as dt
import unittest
from scripts.reconcile_publication_dates import reconcile, month_cutoff

class PublicationDateReconciliationTest(unittest.TestCase):
    def test_crossings_without_aging(self):
        history={'items':[{'id':'old-id','date':'2026-01-01','title':'Old source','url':'https://example.org/1','strand':'A'}, {'id':'aging','date':'2026-01-01','title':'Aged','url':'https://example.org/2','strand':'A'}]}
        radar={'strand_a':[{'date':'2026-09-01','title':'Recent','link':'https://example.org/3','strand':'A'}]}
        corrections={'records':{'historical:id:old-id':{'fields':{'date':'2026-10-14'}}, 'link:https://example.org/3':{'fields':{'date':'2021-01-03'}}}}
        admission={'records':{'historical:id:old-id':{'decision':'keep'},'link:https://example.org/3':{'decision':'keep'}}}
        x=reconcile(radar,history,corrections,admission,{'records':{}},dt.date(2026,4,28))
        self.assertEqual(x['counts']['recent_from_earlier'],1)
        self.assertEqual(x['counts']['earlier_from_recent'],1)
        self.assertEqual(x['recent_from_earlier'][0]['original_record_key'],'historical:id:old-id')
        self.assertNotIn('historical:id:aging',x['recent_from_earlier_keys'])
        self.assertEqual(history['items'][0]['date'],'2026-01-01')
        self.assertEqual(radar['strand_a'][0]['date'],'2026-09-01')
        self.assertEqual(x,reconcile(radar,history,corrections,admission,{'records':{}},dt.date(2026,4,28)))

    def test_unknown_dates_not_moved(self):
        history={'items':[{'id':'x','date':'2026-01-01','strand':'A'}]}
        corrections={'records':{'historical:id:x':{'fields':{'date':'2026-10'}}}}
        out=reconcile({},history,corrections,{'records':{}},{'records':{}},dt.date(2026,4,28))
        self.assertEqual(out['counts']['recent_from_earlier'],0)
        self.assertEqual(out['review'][0]['reason'],'ambiguous_date')

    def test_month_end(self):
        self.assertEqual(month_cutoff(dt.date(2026,8,31)),dt.date(2026,2,28))

if __name__=='__main__':unittest.main()
