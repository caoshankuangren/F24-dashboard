import lark_oapi as lark
from lark_oapi.api.bitable.v1 import *
import json
import pandas as pd


def download_sup_sheet(app_token,table_id,file_path):
    # 创建client
    client = lark.Client.builder() \
        .app_id("cli_a46fd0e390b8900d") \
        .app_secret("ueiQHthqI8znv0nnvvSzIbcty53Htudp") \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ListAppTableRecordRequest = ListAppTableRecordRequest.builder() \
        .app_token(app_token) \
        .table_id(table_id) \
        .page_size(500) \
        .build()

    # 发起请求
    response: ListAppTableRecordResponse = client.bitable.v1.app_table_record.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.bitable.v1.app_table_record.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    return_data = (json.loads(lark.JSON.marshal(response.data, indent=4)))['items']

    return_data_list = [item['fields'] for item in return_data]
    df = pd.DataFrame(return_data_list)

    for column in df.columns:
        # 检查列名是否包含'时间'或'日期'
        if '时间' in column or '日期' in column:
            # 转换该列为datetime格式
            df[column] = pd.to_datetime(df[column], unit='ms').dt.date

    df.to_excel(file_path)