from loguru import logger
import sys

# 移除默认的日志处理器
logger.remove()

# 0 关闭debug 使用info
# 1 开启debug
debugFlag = 1

# 添加新的日志处理器，设置日志级别和格式
if debugFlag == 1:
    logger.add(sys.stdout, level="DEBUG", format="{time} {level} {message}")
else:
    logger.add(sys.stdout, level="INFO", format="{time} {level} {message}")


def log_messages():
    logger.debug("这是一条调试信息")
    logger.info("这是一条信息")
    logger.warning("这是一条警告")
    logger.error("这是一条错误信息")
    logger.critical("这是一条严重错误信息")


def debug(msg):
    logger.debug(msg)


def info(msg):
    logger.info(msg)




