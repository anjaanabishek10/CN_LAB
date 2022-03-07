include <wifi_lte/wifi_lte_rtable.h>
struct r_hist_entry *elm, *elm2;
int num_later = 1;
elm = STAILQ_FIRST(&r_hist_);
while (elm != NULL && num_later <= num_dup_acks_)
{
num_later;
elm = STAILQ_NEXT(elm, linfo_);
}
if (elm != NULL)
{
elm = findDataPacketInRecvHistory(STAILQ_NEXT(elm,linfo_));
if (elm != NULL)
{
elm2 = STAILQ_NEXT(elm, linfo_);
while(elm2 != NULL)
{
if (elm2->seq_num_ < seq_num && elm2->t_recv_ < time)
{
STAILQ_REMOVE(&r_hist_,elm2,r_hist_entry,linfo_);
delete elm2;
}
else 
elm = elm2;
elm2 = STAILQ_NEXT(elm, linfo_);
}
}
}
}
void DCCPTFRCAgent::removeAcksRecvHistory()
{
struct r_hist_entry *elm1 = STAILQ_FIRST(&r_hist_);
struct r_hist_entry *elm2;
int num_later = 1;
while (elm1 != NULL && num_later <= num_dup_acks_)
{
num_later;
elm1 = STAILQ_NEXT(elm1, linfo_);
}
if(elm1 == NULL)
return;
elm2 = STAILQ_NEXT(elm1, linfo_);
while(elm2 != NULL)
{
if (elm2->type_ == DCCP_ACK)
{
STAILQ_REMOVE(&r_hist_,elm2,r_hist_entry,linfo_);
delete elm2;
}
else
{
elm1 = elm2;
}
elm2 = STAILQ_NEXT(elm1, linfo_);
}
}
inline r_hist_entry *DCCPTFRCAgent::findDataPacketInRecvHistory(r_hist_entry *start)
{
while(start != NULL && start->type_ == DCCP_ACK)
start = STAILQ_NEXT(start,linfo_);
return start;
}