from segment.marketing_sub.dag.core_payment import DataPlus, DataPre, TopupPlus, TopupPre
from lib.utils import JoinPoint
from segment.marketing_sub.dag.trans_his import PlusGreater, PlusLess, PreGreater, PreLess
from segment.marketing_sub.operator import *

main = JoinPoint("Prepare Push", "",PreLess, PreGreater, PlusLess, PlusGreater, TopupPlus, TopupPre, DataPre, DataPlus) \
    .bind(update_push_status) \
    .bind(push_data)