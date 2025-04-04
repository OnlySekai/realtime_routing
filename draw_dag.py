from lib.utils import draw_dag_image
from segment.marketing_sub.dag.main import main
from segment.marketing_sub.dag.hdfs import active_flow
draw_dag_image(main, "marketing_sub")
draw_dag_image(active_flow, "marketing_sub")
