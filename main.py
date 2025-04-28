from Draft import DriftData
from SpatialFiltering import GeographicF
from StayPoint import StayPoint
from easydict import EasyDict as edict

if __name__ == "__main__":

    '''
        城市：
        数据集:
    '''

    dataset = ''
    area = ''

    geo_config = edict({
        'Area_path': f"E:\GISData\XXXX\{area}.shp",  # 城市矢量文件路径
        'input_folder': f"G:\{area}\{dataset}", # 输入数据路径
        'dataset': dataset,
        'output_folder': f"G:\处理\{area}\区域筛选\{dataset}"
    })  
    draft_config = edict({
        'db_path': f'D:\data_draft_{area}.db', 
        'input_folder': f"G:\处理\{area}\区域筛选\{dataset}",
        'output_folder': f'G:\处理\{area}\漂移点清洗\{dataset}',
        'batch_size': 100000 #  不能设置太大，sqlite一次搜索的数据有限
    })
    stay_config = edict({
        'input_folder': f'G:\处理\{area}\漂移点清洗\{dataset}',
        'output_folder': f'G:\处理\{area}\停留点\{dataset}',   # 最终结果路径
        'sql': False,  #  内存不够时，使用数据库进行缓冲
        'db_path': f'D:\data_stay_{area}.db', 
        'batch_size': 100000 #  不能设置太大，sqlite一次搜索的数据有限
    })
    # 区域筛选
    print("-"*10 + "区域筛选"+"-"*20)
    GeographicF(geo_config).process()
    # 漂移点清洗
    print("-"*10 + "漂移点清洗"+"-"*20)
    DriftData(draft_config).process()
    # 停留点识别
    print("-"*10 + "停留点识别"+"-"*20)
    StayPoint(stay_config).process() 
    # 内存不足时，停留点识别时使用下面这个
    # StayPoint(stay_config).process_sql()
    
    
