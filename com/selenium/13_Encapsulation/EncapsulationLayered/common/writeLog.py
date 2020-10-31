import logging
import os

class WriteLogs(object):
    def dirname(self, filename, filepath='data'):
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), filepath, filename)

    def log(self, log_content):
        '''定义log日志级别'''
        # 定义文件
        logFile = logging.FileHandler(self.dirname('logData.txt'), 'a', encoding='utf-8')
        # log格式
        fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
        logFile.setFormatter(fmt)
        # 定义日志
        logger1 = logging.Logger('logTest', level=logging.DEBUG)
        logger1.addHandler(logFile)
        logger1.info(log_content)
        logFile.close()