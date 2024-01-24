 # coding: utf-8
import time
from download_sup_sheet import download_sup_sheet
from automatic_download_everything import full_file_download_sequence
from download_F24data import process_data
from create_F24table import create_table
from high_quality_match import high_quality_match
from alumnus_match import alumnus_match 
from download_clue import process_clue
from bitable_updater import update_all_table
from get_clockin_data import get_clockin_data

'''
#下载线索
process_clue()

app_id = "cli_a4e5badd833bd00d"
app_token = "n16oQih9feqSrPRvx4y10eoImrUOLDqd"
superior_sheet_token = "YSuZs9MbahpihTtcb2hcFi5nncf"
target_sheet_token = "Fw3WsIDzlhut9UtrSKFcs1uinNh"

download_sup_sheet('FT18bZpzLaCiUJs4lOlceZIOn3g','tblRHMq6gt75pKWp','./关联上级.xlsx')

time.sleep(.5)

batch_id = 11
base_url = 'https://apply.miracleplus.com'
group_info_url = f"{base_url}/admin/contact_statistics/groups"
login_url = f"{base_url}/users/sign_in"
contacts_download = f"{base_url}/admin/contact_statistics/export"
exportation_url = f"{base_url}/evaluation/applications/"
exportation_contact_url = f"{exportation_url}"
exportation_application_url = f"{exportation_url}/exportation"
history_export_url = f"{base_url}/export_history"

full_file_download_sequence(
    batch_id, 
    base_url, 
    group_info_url,  
    login_url,
    contacts_download,
    exportation_url, 
    exportation_contact_url,
    exportation_application_url,
    history_export_url
)
time.sleep(1)

process_data(start_date ='2024-01-13')

high_quality_match()
'''
create_table()

alumnus_match()

app_token = 'NrqIbSAtoa08cdsHBOgckOwbngb'
relation_dict = {
    'tblQ0kxP02JETOXG':'./输出结果/提交明细.xlsx',
    'tblgJ4y1gh71LWJB':'./输出结果/渠道统计.xlsx',
    'tblGTNrUM55XP0pF':'./输出结果/小组统计.xlsx',
    'tblLFxcCMRHblTuu':'./输出结果/每日个人绩效.xlsx',  
    }
update_all_table(app_token,relation_dict)