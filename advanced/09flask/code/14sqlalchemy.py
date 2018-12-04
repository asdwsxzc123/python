""" 操作mysql提示告警级别 """
# 路径
/.virtualenv/python3.5/lib/python3.5/site-packages/sqlalchemy/dialects/mysql
# 修改文件
# def get_isolation_level
    if  self.server_version_info < (5,7,20):
        cursor.execute('SELECT @@tx_isolation')
    else:
        cursor.execute('SELECT @transaction_isolation')