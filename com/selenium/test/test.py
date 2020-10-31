import logging
# 定义写入文件 a 表示为追加模式写入文件，encoding表示编码格式
logFile = logging.FileHandler('logTest.txt', 'a', encoding='utf-8')
# 设置log日志格式
fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s-%(message)s')
logFile.setFormatter(fmt)
# 定义日志级别
LoggerMany = logging.Logger('logTest', level=logging.DEBUG)
LoggerMany.addHandler(logFile)
# 写入内容到logging日志
LoggerMany.critical('info')
# 输出日志信息
LoggerMany.info("开始：输出Logging日志")
LoggerMany.debug("这里显示的是debug级别的日志信息")
LoggerMany.warning("这里显示的是warning级别的日志信息")
LoggerMany.info("结束：输出Logging日志")